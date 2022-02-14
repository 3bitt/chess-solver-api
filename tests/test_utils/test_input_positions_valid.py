import pytest
from solver.utils import input_positions_valid


@pytest.mark.parametrize(
    "positions, expected_validity",
    [
        (["a7", "b8", "a1", "h8", "a8", "f5"], True),
        ([" a7"], True),
        (["a7 "], True),
        (["7f", "8c", "1e", "8g", "a8", "f5"], True),
        (["a7", "b8", "a15", "h8", "a8", "i5"], False),
        (["I5"], False),
        ([""], False),
        (["  "], False),
        (["@$%"], False),
        (["a 7"], False),
        (["11"], False),
        (["aa"], False),
        (["0a"], False),
        (["p2"], False),
    ],
)
def test_input_positions_valid(positions: list[str], expected_validity: bool):
    position_valid = input_positions_valid(positions)
    assert position_valid == expected_validity
