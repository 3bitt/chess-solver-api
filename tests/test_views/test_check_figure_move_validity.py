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
            '{"move":"valid","figure":"king","error":null,"currentField":"D2","destField":"D3"}',
            200,
        ),
        (
            "bishop",
            "c3",
            "A5",
            '{"move":"valid","figure":"bishop","error":null,"currentField":"C3","destField":"A5"}',
            200,
        ),
        (
            "bishop",
            "c3",
            "g2",
            '{"move":"invalid","figure":"bishop","error":"Current move is'
            ' not permitted.","currentField":"C3","destField":"G2"}',
            200,
        ),
        (
            "rook",
            "h7",
            "7d",
            '{"move":"invalid","figure":"rook","error":"Current move is not'
            ' permitted.","currentField":"H7","destField":"7D"}',
            200,
        ),
        (
            "rook",
            "h7",
            "3a",
            '{"move":"invalid","figure":"rook","error":"Current move is not'
            ' permitted.","currentField":"H7","destField":"3A"}',
            200,
        ),
        (
            "rooks",
            "h7",
            "3a",
            '{"move":"","figure":"rooks","error":"Figure not'
            ' found.","currentField":"h7","destField":"3a"}',
            404,
        ),
        (
            "rook",
            "h77",
            "3a",
            '{"move":"","figure":"rook","error":"Field does not'
            ' exist.","currentField":"h77","destField":"3a"}',
            409,
        ),
        (
            "queen",
            "h7",
            "aa",
            '{"move":"","figure":"queen","error":"Field does not'
            ' exist.","currentField":"h7","destField":"aa"}',
            409,
        ),
        (
            "queen",
            "h7",
            "h4",
            '{"move":"valid","figure":"queen","error":null,"currentField":"H7","destField":"H4"}',
            200,
        ),
    ],
)
def test_check_figure_move_validity(
    figure: str,
    position: str,
    destination: str,
    expected_response: str,
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
    expected_data = json.loads(expected_response)
    assert response.data == expected_data
    assert response.status_code == response_code
