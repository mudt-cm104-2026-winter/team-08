BOOKS_PER_LEVEL = 25

LEVELS = [
    {"name": "Beginner reader", "shelf": "wooden"},
    {"name": "Silver reader", "shelf": "silver"},
    {"name": "Gold reader", "shelf": "gold"},
    {"name": "Master reader", "shelf": "diamond"},
]
MAX_REBIRTHS = len(LEVELS) - 1

THEMES = {
    "wooden": "Wooden",
    "silver": "Silver",
    "gold": "Gold",
    "diamond": "Diamond",
    "christmas": "Christmas",
    "dog-treats": "Dog treats",
}
FREE_THEMES = ["wooden", "christmas", "dog-treats"]

ACHIEVEMENTS = [
    (1, "First book"),
    (5, "Bookworm"),
    (10, "Double digits"),
    (15, "Page turner"),
    (20, "Shelf filler"),
    (25, "Ready for a new shelf"),
]


def level(rebirths):
    """The level a reader has after this many rebirths."""
    return LEVELS[min(rebirths, MAX_REBIRTHS)]


def books_for_next_rebirth(rebirths):
    """Finished books needed for the next rebirth: 25, then 50, then 75."""
    return BOOKS_PER_LEVEL * (rebirths + 1)


def can_rebirth(finished, rebirths):
    """True if the reader has enough finished books and is not yet a master."""
    return rebirths < MAX_REBIRTHS and finished >= books_for_next_rebirth(rebirths)


def unlocked_themes(rebirths):
    """The free looks, plus one metal shelf for every rebirth."""
    earned = [LEVELS[number]["shelf"] for number in range(1, rebirths + 1)]
    return FREE_THEMES + earned


def achievements(finished):
    """All achievements, each marked as earned or not."""
    return [
        {"books": books, "name": name, "earned": finished >= books}
        for books, name in ACHIEVEMENTS
    ]
