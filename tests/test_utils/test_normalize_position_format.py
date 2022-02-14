import pytest
from solver.utils import normalize_position_format


@pytest.mark.parametrize(
    "position, expected_format",
    [
        ("a1", "a1"),
        ("1a", "a1"),
        ("1B", "B1"),
        ("ab", "ab"),
        ("15", "51"),
        ("95", "59"),
        ("7c", "c7"),
    ],
)
def test_normalize_position_format(position: str, expected_format: str):
    result = normalize_position_format(position)
    assert result == expected_format
