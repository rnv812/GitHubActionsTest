from utils import roll_the_dice


def test_roll_the_dice():
    for _ in range(1, 100):
        assert roll_the_dice() in range(1, 7)
