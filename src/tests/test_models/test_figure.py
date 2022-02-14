import pytest
from solver.models import (
    Bishop,
    Figure,
    FigureFactory,
    King,
    Knight,
    Pawn,
    Queen,
    Rook,
)


@pytest.mark.parametrize(
    "figure, position, expected_class",
    [
        ("king", "a1", King),
        ("queen", "b3", Queen),
        ("rook", "h8", Rook),
        ("bishop", "c5", Bishop),
        ("knight", "e2", Knight),
        ("pawn", "f6", Pawn),
    ],
)
def test_figure_factory(figure: str, position: str, expected_class: Figure):
    figure = FigureFactory.create_figure(figure, position)
    assert isinstance(figure, expected_class)
    assert figure.position == position


@pytest.mark.parametrize(
    "figure, position, expected_move_list",
    [
        ("king", "d2", ["C1", "D1", "E1", "E2", "C2", "C3", "D3", "E3"]),
        (
            "queen",
            "a1",
            [
                "B1",
                "A2",
                "B2",
                "C1",
                "A3",
                "C3",
                "D1",
                "A4",
                "D4",
                "E1",
                "A5",
                "E5",
                "F1",
                "A6",
                "F6",
                "G1",
                "A7",
                "G7",
                "H1",
                "A8",
                "H8",
            ],
        ),
        (
            "rook",
            "d4",
            [
                "A4",
                "B4",
                "C4",
                "E4",
                "F4",
                "G4",
                "H4",
                "D1",
                "D2",
                "D3",
                "D5",
                "D6",
                "D7",
                "D8",
            ],
        ),
        (
            "bishop",
            "c4",
            ["D5", "D3", "B5", "B3", "E6", "E2", "A6", "A2", "F7", "F1", "G8"],
        ),
        ("knight", "g7", ["E6", "E8", "H5", "F5"]),
        ("knight", "b7", ["D6", "D8", "A5", "C5"]),
        ("knight", "e5", ["G6", "G4", "C6", "C4", "D7", "F7", "D3", "F3"]),
        ("pawn", "f5", ["F6"]),
    ],
)
def test_figure_available_moves(
    figure: str, position: str, expected_move_list: list[str]
):
    figure = FigureFactory.create_figure(figure, position)
    horizontal_move_options = figure.list_available_moves()
    assert sorted(horizontal_move_options) == sorted(expected_move_list)
