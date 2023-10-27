from utils.dicts import get_val


def test_get():
    assert get_val({1: 1, 2: 2, 3: 3}, 1, "git") == 1
    assert get_val({1: 1, 2: 2, 3: 3}, 3, "random_word") == 3
    assert get_val({1: 1, 2: 2, 3: 3}, 5, "git") == "git"
    assert get_val({1: 1, 2: 2, 3: 3}, 0, "test") == "test"
    assert get_val({}, 0) == "git"