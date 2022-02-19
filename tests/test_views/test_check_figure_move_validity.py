import json
import pytest
from rest_framework.test import APIRequestFactory

from solver.views import CheckFigureMoveValidity


@pytest.mark.parametrize(
    "figure, position, destination, expected_response, response_code",
    [
        (
            "king",
            "d2",
            "d3",
            {
                "move": "valid",
                "figure": "king",
                "error": "null",
                "currentField": "D2",
                "destField": "D3",
            },
            200,
        ),
        (
            "bishop",
            "c3",
            "A5",
            {
                "move": "valid",
                "figure": "bishop",
                "error": "null",
                "currentField": "C3",
                "destField": "A5",
            },
            200,
        ),
        (
            "queen",
            "h7",
            "h4",
            {
                "move": "valid",
                "figure": "queen",
                "error": "null",
                "currentField": "H7",
                "destField": "H4",
            },
            200,
        ),
    ],
)
def test_check_figure_move_validity_should_pass(
    figure: str,
    position: str,
    destination: str,
    expected_response: dict,
    response_code: int,
):
    factory = APIRequestFactory()
    request = factory.get(f"/{figure}/{position}/{destination}", format="json")
    view = CheckFigureMoveValidity().as_view()
    response = view(
        request,
        chess_figure=figure,
        current_field=position,
        dest_field=destination,
    )
    response.render()
    response.data = json.loads(response.content.decode("utf-8"))
    assert response.data == expected_response
    assert response.status_code == response_code


@pytest.mark.parametrize(
    "figure, position, destination, expected_response, response_code",
    [
        (
            "rooks",
            "h7",
            "3a",
            {
                "move": "invalid",
                "figure": "rooks",
                "error": "Figure not found.",
                "currentField": "H7",
                "destField": "3A",
            },
            404,
        ),
        (
            "rook",
            "h77",
            "3a",
            {
                "move": "invalid",
                "figure": "rook",
                "error": "Field does not exist.",
                "currentField": "H77",
                "destField": "3A",
            },
            409,
        ),
        (
            "queen",
            "h7",
            "aa",
            {
                "move": "invalid",
                "figure": "queen",
                "error": "Field does not exist.",
                "currentField": "H7",
                "destField": "AA",
            },
            409,
        ),
        (
            "bishop",
            "c3",
            "g2",
            {
                "move": "invalid",
                "figure": "bishop",
                "error": "Current move is not permitted.",
                "currentField": "C3",
                "destField": "G2",
            },
            409,
        ),
        (
            "rook",
            "h7",
            "7d",
            {
                "move": "invalid",
                "figure": "rook",
                "error": "Current move is not permitted.",
                "currentField": "H7",
                "destField": "7D",
            },
            409,
        ),
        (
            "rook",
            "h7",
            "3a",
            {
                "move": "invalid",
                "figure": "rook",
                "error": "Current move is not permitted.",
                "currentField": "H7",
                "destField": "3A",
            },
            409,
        ),
    ],
)
def test_check_figure_move_validity_should_fail(
    figure: str,
    position: str,
    destination: str,
    expected_response: dict,
    response_code: int,
):
    factory = APIRequestFactory()
    request = factory.get(f"/{figure}/{position}/{destination}", format="json")
    view = CheckFigureMoveValidity().as_view()

    response = view(
        request,
        chess_figure=figure,
        current_field=position,
        dest_field=destination,
    )
    response.render()
    response.data = json.loads(response.content.decode("utf-8"))
    assert response.data == expected_response
    assert response.status_code == response_code
