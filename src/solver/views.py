from __future__ import annotations
from http import HTTPStatus
from rest_framework.views import APIView
from rest_framework.response import Response

from solver.utils import input_positions_valid
from .models import FigureFactory


class GetPossibleFigureMoves(APIView):
    def get(self, request, chess_figure: str, current_field: str) -> Response:
        response = {
            "availableMoves": [],
            "error": None,
            "figure": chess_figure,
            "currentField": current_field,
        }
        if not input_positions_valid([current_field]):
            response["error"] = "Field does not exist."
            return Response(response, status=HTTPStatus.CONFLICT)
        try:
            figure = FigureFactory.create_figure(chess_figure, current_field)
        except (KeyError, TypeError):
            response["error"] = "Figure not found."
            return Response(data=response, status=HTTPStatus.NOT_FOUND)
        response["figure"] = str(figure)
        response["currentField"] = current_field.upper()
        response["availableMoves"] = figure.list_available_moves()
        return Response(data=response, status=HTTPStatus.OK)


class CheckFigureMoveValidity(APIView):
    def get(
        self, request, chess_figure: str, current_field: str, dest_field: str
    ) -> Response:
        response = {
            "move": "",
            "figure": chess_figure,
            "error": None,
            "currentField": current_field,
            "destField": dest_field,
        }
        if not input_positions_valid([current_field, dest_field]):
            response["error"] = "Field does not exist."
            return Response(response, status=HTTPStatus.CONFLICT)
        try:
            figure = FigureFactory.create_figure(chess_figure, current_field)
        except (KeyError, TypeError):
            response["error"] = "Figure not found."
            return Response(data=response, status=HTTPStatus.NOT_FOUND)
        response["figure"] = str(figure)
        response["currentField"] = current_field.upper()
        response["destField"] = dest_field.upper()

        move_valid = figure.validate_move(dest_field)
        if move_valid:
            response["move"] = "valid"
        else:
            response["move"] = "invalid"
            response["error"] = "Current move is not permitted."
        return Response(data=response, status=HTTPStatus.OK)
