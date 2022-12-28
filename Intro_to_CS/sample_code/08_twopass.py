"""Sample code for 08_1_Twopass.md"""
from typing import List, Tuple
from numbers import Number

# First example: Normalizing exam scores
# (in a really terrible way that I would never actually use)

scores = [
    ("Albert", 30),
    ("Bertal", 24),
    ("Cheri", 32),
    ("Dolores", 22),
    ("Ethan", 20)
]


def normalize_scores(scores: List[Tuple[str, Number]]) -> List[Tuple[str, float]]:
    """Normalized scores are fraction of average"""
    total = 0
    count = 0
    for student, score in scores:
        count += 1
        total += score
    mean = total / count
    result = []
    for student, score in scores:
        normalized = score / mean
        result.append((student, normalized))
    return result


def bad_normalize(scores: List[Tuple[str, Number]]) -> List[Tuple[str, float]]:
    """Looks cute, but this algorithm is quadratic in length of list!"""
    result = []
    count = len(scores)
    for student, score in scores:
        total = sum([score for name, score in scores])
        mean = total / count
        normalized = score / mean
        result.append((student, normalized))
    return result


def show_scores(scores: List[Tuple[str, Number]]):
    """Print scores list as Markdown format table"""
    print("|Name   |Score  |")
    print("|-------|-------|")
    for student, score in scores:
        print(f"|{student}|{score:02.2f}|")


show_scores(scores)
normalized = bad_normalize(scores)
show_scores(normalized)
print()
normalized = normalize_scores(scores)
print()
show_scores(normalized)

# Second example:
#    Apply "m of n" style numbering for
#    each fruit in the fruit bowl

fruit_bowl = ["banana", "orange", "banana", "kiwi", "banana", "orange"]


def itemize_fruits(bowl: List[str]):
    """Print the fruits as
    banana 1 of 3
    orange 1 of 2
    etc
    """
    # Pass 1
    full_counts = {}  # We'll keep summary information here
    for fruit in bowl:
        # Ensure there is an entry for the fruit
        if fruit not in full_counts:
            full_counts[fruit] = 0
        full_counts[fruit] += 1
    # Pass 2
    cur_counts = {}
    for fruit in bowl:
        # Ensure this is an entry for the fruit
        if fruit not in cur_counts:
            cur_counts[fruit] = 0
        cur_counts[fruit] += 1
        # Now we have both pieces of information
        print(f"{fruit} {cur_counts[fruit]} of {full_counts[fruit]}")


print()
itemize_fruits(fruit_bowl)
