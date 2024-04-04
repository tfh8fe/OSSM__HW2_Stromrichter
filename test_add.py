from add import add


def test_add():
    assert add(2, 3) == 5
    assert add(20, 15) == 35
    assert add(300, 3) == 303