from snake.md import HorizontalRule


def test_horizontal_rule():
    hr = HorizontalRule()
    assert str(hr) == "---"
