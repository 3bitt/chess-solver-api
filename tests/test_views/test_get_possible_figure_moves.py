import json
import pytest
from rest_framework.test import APIRequestFactory
from solver.views import GetPossibleFigureMoves


@pytest.mark.parametrize(
    "figure, position, expected_response, response_code",
    [
        (
            "king",
            "d2",
            {
                "availableMoves": [
                    "E2",
                    "C2",
                    "D3",
                    "D1",
                    "E3",
                    "E1",
                    "C3",
                    "C1",
                ],
                "error": "null",
                "figure": "king",
                "currentField": "D2",
            },
            200,
        ),
        (
            "bishop",
            "e5",
            {
                "availableMoves": [
                    "F6",
                    "F4",
                    "D6",
                    "D4",
                    "G7",
                    "G3",
                    "C7",
                    "C3",
                    "H8",
                    "H2",
                    "B8",
                    "B2",
                    "A1",
                ],
                "error": "null",
                "figure": "bishop",
                "currentField": "E5",
            },
            200,
        ),
        (
            "knight",
            "h7",
            {
                "availableMoves": ["F8", "F6", "G5"],
                "error": "null",
                "figure": "knight",
                "currentField": "H7",
            },
            200,
        ),
        (
            "rook",
            "f8",
            {
                "availableMoves": [
                    "G8",
                    "E8",
                    "F7",
                    "H8",
                    "D8",
                    "F6",
                    "C8",
                    "F5",
                    "B8",
                    "F4",
                    "A8",
                    "F3",
                    "F2",
                    "F1",
                ],
                "error": "null",
                "figure": "rook",
                "currentField": "F8",
            },
            200,
        ),
        (
            "queen",
            "a2",
            {
                "availableMoves": [
                    "B2",
                    "A3",
                    "A1",
                    "B3",
                    "B1",
                    "C2",
                    "A4",
                    "C4",
                    "D2",
                    "A5",
                    "D5",
                    "E2",
                    "A6",
                    "E6",
                    "F2",
                    "A7",
                    "F7",
                    "G2",
                    "A8",
                    "G8",
                    "H2",
                ],
                "error": "null",
                "figure": "queen",
                "currentField": "A2",
            },
            200,
        ),
    ],
)
def test_get_possible_figure_moves_should_pass(
    figure: str, position: str, expected_response: dict, response_code: int
):
    factory = APIRequestFactory()
    request = factory.get(f"/{figure}/{position}/", format="json")
    view = GetPossibleFigureMoves().as_view()
    response = view(request, chess_figure=figure, current_field=position)
    response.render()
    response.data = json.loads(response.content.decode("utf-8"))
    assert response.data == expected_response
    assert response.status_code == response_code


@pytest.mark.parametrize(
    "figure, position, expected_response, response_code",
    [
        (
            "knight",
            "hh7",
            {
                "availableMoves": [],
                "error": "Field does not exist.",
                "figure": "knight",
                "currentField": "HH7",
            },
            409,
        ),
        (
            "knight",
            "7",
            {
                "availableMoves": [],
                "error": "Field does not exist.",
                "figure": "knight",
                "currentField": "7",
            },
            409,
        ),
        (
            "kingkong",
            "a4",
            {
                "availableMoves": [],
                "error": "Figure not found.",
                "figure": "kingkong",
                "currentField": "A4",
            },
            404,
        ),
    ],
)
def test_get_possible_figure_moves_should_fail(
    figure: str, position: str, expected_response: str, response_code: int
):
    factory = APIRequestFactory()
    request = factory.get(f"/{figure}/{position}/", format="json")
    view = GetPossibleFigureMoves().as_view()
    response = view(request, chess_figure=figure, current_field=position)
    response.render()
    response.data = json.loads(response.content.decode("utf-8"))
    assert response.data == expected_response
    assert response.status_code == response_code
