import pytest
from solver.utils import field_exists_on_board


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (100, 49, True),
        (100, 56, True),
        (97, 50, True),
        (104, 50, True),
        (20, 50, False),
        (96, 50, False),
        (105, 50, False),
        (100, 15, False),
        (100, 48, False),
        (100, 57, False),
    ],
)
def test_field_exists_on_board(x: int, y: int, expected_result: bool):
    expected_result = field_exists_on_board(x, y)
    assert expected_result == expected_result
