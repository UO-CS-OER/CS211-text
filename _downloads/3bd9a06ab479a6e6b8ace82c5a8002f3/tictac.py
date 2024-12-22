"""
Tic-Tac-Toe (Noughts and Crosses)
Example for chapter 4, Aliasing on Purpose

"""
from enum import Enum
from typing import Tuple, List


class Mark(Enum):
    xmark = "X"
    omark = "O"
    unmarked = "."


""""Interpret abc|def|ghi as positions 
on the board, e.g., "e" -> (1,1)
"""
_INDEX_CODES = {
    "a": (0, 0), "b": (0, 1), "c": (0, 2),
    "d": (1, 0), "e": (1, 1), "f": (1, 2),
    "g": (2, 0), "h": (2, 1), "i": (2, 2)}


def board_index(pos: str) -> Tuple[int, int]:
    try:
        return _INDEX_CODES[pos]
    except:
        raise IndexError(f"Position '{pos}' not understood. Accepted positions are in abcdefghi")


class Tile:
    def __init__(self, name: str):
        self.name = name
        self.mark = Mark.unmarked
        self.worth = 0

    def set(self, mark: Mark):
        self.mark = mark

    def __str__(self) -> str:
        if self.mark == Mark.unmarked:
            return self.name
        return self.mark.value

    def __repr__(self) -> str:
        """Debugging representation like (eX)"""
        return f"({self.name}{self.mark.value})"


class Board:
    """Simple 3x3 Tic Tac Toe board"""

    def __init__(self):
        self.tiles = [[Tile('a'), Tile('b'), Tile('c')],
                      [Tile('d'), Tile('e'), Tile('f')],
                      [Tile('g'), Tile('h'), Tile('i')]]
        # 3-in-a-row can be horizontal, vertical, or diagonal
        self.groups = []
        # horizontal
        for row in self.tiles:
            self.groups.append(row)
        # vertical
        for col_i in range(3):
            group = []
            for row_i in range(3):
                group.append(self.tiles[row_i][col_i])
            self.groups.append(group)
        # diagonal left-to-right
        self.groups.append([self.tiles[i][i] for i in range(3)])
        # diagonal right-to-left
        self.groups.append([self.tiles[i][2 - i] for i in range(3)])

    def __getitem__(self, pos: str) -> Mark:
        """Expects position to be in abc/def/ghi
        representing positions in first, second, third
        row of board.
        """
        row, col = board_index(pos)
        return self.tiles[row][col].mark

    def __setitem__(self, pos: str, mark: Mark):
        assert isinstance(mark, Mark), "value should be a Mark object"
        row, col = board_index(pos)
        self.tiles[row][col].set(mark)

    def __str__(self) -> str:
        """Printable representation is three rows of marks"""
        lines = []
        for row in self.tiles:
            line = []
            for col in row:
                line.append(str(col))
            lines.append("".join(line))
        return "\n".join(lines)
        # Or super-compressed version:
        # return "\n".join([("".join([str(tile) for tile in row])) for row in self.tiles])

    def choose_for(self, mark: Mark) -> str:
        """Returns the most worthwhile position for
        mark to take, assuming it is the turn for
        mark and that there are open positions.
        """
        # We use the 'worth' field of the tiles to tally
        # how valuable each position is.
        for row in self.tiles:
            for col in row:
                col.worth = 0
        for group in self.groups:
            worth = calc_worth(group, mark)
            for tile in group:
                # No harm in granting worth to marked tiles
                tile.worth += worth
        # Pick open tile with max worth
        all_tiles = self.tiles[0] + self.tiles[1] + self.tiles[2]
        open_tiles = [tile for tile in all_tiles if tile.mark == Mark.unmarked]
        open_tiles.sort(key=lambda tile: tile.worth, reverse=True)
        return open_tiles[0].name

    def has_winner(self) -> bool:
        """There is some winning row or column (for either X or O)"""
        for group in self.groups:
            if is_winner(group):
                return True
        return False

    def has_open_tiles(self) -> bool:
        """There are open spaces"""
        for row in self.tiles:
            for col in row:
                if col.mark == Mark.unmarked:
                    return True
        return False


def is_winner(group: List[Tile]) -> bool:
    """True if a win for *either* X or O"""
    q, r, s = group
    return (q.mark != Mark.unmarked
            and q.mark == r.mark
            and r.mark == s.mark)


def calc_worth(group: List[Tile], mark: Mark) -> int:
    """How much is this tile worth to this player?"""
    # How many of each?
    x_count = 0
    o_count = 0
    for tile in group:
        if tile.mark == Mark.xmark:
            x_count += 1
        elif tile.mark == Mark.omark:
            o_count += 1
    # Mixed groups are worthless
    if x_count > 0 and o_count > 0:
        return 0
    # At least one is zero; now we want
    # to know whether this mover or the opponent
    count = x_count + o_count
    mine = False;
    if x_count > 0 and mark == Mark.xmark:
        mine = True
    elif o_count > 0 and mark == Mark.omark:
        mine = True
    # Empty groups have small potential value
    if count == 0:
        return 1
    # Groups with 2 can be a winner (if mine) or a block
    if count == 2:
        if mine:
            return 5000
        else:
            return 1000
    if count == 1:
        if mine:
            return 200
        else:
            return 100
    assert False, "Should never reach this point"


board = Board()


def move(board):
    # Should the game continue?
    if board.has_winner():
        print("\nI win!\n")
        print(board)
        exit(0)
    if not board.has_open_tiles():
        print("The game is a draw.  Darn!")
        exit(0)
    # User's turn
    print("""Use letter from abcdefghi as position choice""")
    print(f"Board state is\n\n{board}\n")
    move = input("Your move: ").strip()
    if len(move) == 0:
        print("Goodbye")
        exit(0)
    if move not in _INDEX_CODES:
        print(f"{move} is not a valid move position")
    elif board[move] != Mark.unmarked:
        print(f"Position {move} is not open")
    else:
        board[move] = Mark.xmark
        if board.has_winner():
            print("You beat me!")
            exit(0)
        if not board.has_open_tiles():
            print("Oh dear, a drawn game.")
            exit(0)
        # My turn
        position = board.choose_for(Mark.omark)
        print(f"You chose {move}. I choose position {position}")
        board[position] = Mark.omark


def main():
    while (True):
        try:
            move(board)
        except Exception as e:
            print(f"Busted: {e}")
            raise e


if __name__ == "__main__":
    main()
