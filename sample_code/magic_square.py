"""Simple recursive solution of magic square"""
from typing import List

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)  # Print information messages


class Tile:
    """Just a wrapper for an int;
    allows aliasing for tiles accessible
    in different orientations
    """

    def __init__(self):
        self.val = 0

    def set(self, val: int):
        self.val = val

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return f"Tile({self.val})"


class Square:
    """A magic 3x3 square
    with search for solutions with a given target sum"""

    def __init__(self):
        """Initially the most trivial magic square"""
        self.tiles = [[Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile()],
                      [Tile(), Tile(), Tile()]]
        # Group by rows, columns, diagonals
        self.groups = []
        for row in self.tiles:
            self.groups.append(row)
        for col_i in range(len(self.tiles[0])):
            self.groups.append([row[col_i] for row in self.tiles])
        diag = []
        for i in range(len(self.tiles)):
            diag.append(self.tiles[i][i])
        self.groups.append(diag)
        diag = []
        for i in range(len(self.tiles)):
            diag.append(self.tiles[i][len(self.tiles) - i - 1])
        self.groups.append(diag)

    def __str__(self):
        return "/".join([",".join([str(tile) for tile in row])
                         for row in self.tiles])

    # For this simple puzzle, it would be easier and more
    # efficient to have an "undo" operation for restoration,
    # but we want to illustrate the save/restore approach
    #
    def save(self) -> List[List[int]]:
        return [[tile.val for tile in row] for row in self.tiles]

    def restore(self, values: List[List[int]]):
        for row_i in range(len(self.tiles)):
            for col_i in range(len(self.tiles[0])):
                self.tiles[row_i][col_i].set(values[row_i][col_i])

    # Cut off search early if any row, column, or diagonal
    # sum exceeds the target

    def group_sum(self, group: List[Tile]) -> int:
        """Sum of values in this group of tiles"""
        return sum([tile.val for tile in group])

    def all_filled(self, group: List[Tile]) -> bool:
        """All of the elements of this group have been
        filled with non-zero integers
        """
        for tile in group:
            if tile.val == 0:
                return False
        return True

    def can_continue(self, target_sum: int) -> bool:
        """Is it possible that this board state can be
        continued to a solution with zero or more
        placements of a positive value, or should we
        declare it a dead end?
        """
        for group in self.groups:
            sum_so_far = self.group_sum(group)
            if self.all_filled(group):
                if sum_so_far != target_sum:
                    log.info(f"Complete row sums to wrong value: {group}")
                    return False
            elif sum_so_far > target_sum:
                # It can only get larger
                log.info(f"Incomplete row already too big: {group}")
                return False
        return True

    def is_complete(self):
        """Are all the positions filled?"""
        for row in self.tiles:
            for tile in row:
                if tile.val == 0:
                    return False
        return True

    def make_magic(self, target: int, values: List[int]) -> bool:
        """Mutator: Completes the magic square with
        target sum in all groups and returns True
        if possible; False means unable to complete, and square
        is unchanged.
        We assume that if all tiles have been placed successfully,
        the sum must have been reached.
        """
        # Base case:  Hopeless position, give up
        if not self.can_continue(target):
            return False
        # Base case:  No more tiles to place
        if len(values) == 0:
            return self.is_complete()

        # Recursive case: Place one tile somewhere.
        # We'll try at each position currently
        # holding a zero.
        val = values[0]
        remaining = values[1:]
        saved = self.save()
        log.info(f"Current viable state {saved}")

        for row in self.tiles:
            for tile in row:
                if tile.val == 0:
                    # Attempt to place the tile here
                    tile.set(val)
                    log.info(f"Attempting placement of {val}")
                    if self.make_magic(target, remaining):
                        return True
                    # Didn't work; restore and try another
                    self.restore(saved)
        # I tried placing it everywhere, and none
        # of them worked.  Sigh.
        return False


if __name__ == "__main__":
    square = Square()
    square.make_magic(15, [9, 8, 7, 6, 5, 4, 3, 2, 1])
