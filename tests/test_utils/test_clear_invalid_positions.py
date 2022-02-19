import pytest
from solver.utils import clear_invalid_positions


@pytest.mark.parametrize(
    "positions_to_clear, expected_positions",
    [
        (["c2", "c0", "_2", "_0", "b3", "`3", "b/", "`/"], ["C2", "B3"]),
        (["j9", "j7", "f9", "f7", "i:", "g:", "i6", "g6"], ["F7", "G6"]),
        (["!2", "@0", "_2", "_0", "23", "`3", "b/", "`/"], []),
        (["  ", "", " :", " 2", "23", "`3", "b/", "`/"], []),
        (["V2", "aa", "_2", "_0", "9E", "`3", "b/", "`/"], []),
        (["`8", "b8", "a9", "a7", "b9", "b7", "`9", "`7"], ["B8", "A7", "B7"]),
        (
            ["\\8", "f8", "a=", "a3", "f=", "f3", "\\=", "\\3"],
            ["F8", "A3", "F3"],
        ),
        (["]8", "e8", "a<", "a4", "e<", "e4", "]<", "]4"], ["E8", "A4", "E4"]),
    ],
)
def test_clear_invalid_positions(
    positions_to_clear: list[str], expected_positions: list[str]
):
    result = clear_invalid_positions(positions_to_clear)
    assert result == expected_positions
