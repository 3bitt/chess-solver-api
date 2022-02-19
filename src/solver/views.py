from rest_framework.views import APIView
from rest_framework.response import Response
from solver.exception_handler import (
    ConflictException_409,
    NotFoundException_404,
)
from solver.renderers import CustomJSONRenderer

from solver.utils import input_positions_valid
from .models import FigureFactory


class GetPossibleFigureMoves(APIView):
    renderer_classes = [CustomJSONRenderer]

    def get(self, request, chess_figure: str, current_field: str) -> Response:

        if not input_positions_valid([current_field]):
            raise ConflictException_409("Field does not exist.")
        try:
            figure = FigureFactory.create_figure(chess_figure, current_field)
        except (KeyError, TypeError):
            raise NotFoundException_404("Figure not found.")

        available_moves = figure.list_available_moves()
        response = {"availableMoves": available_moves}
        return Response(data=response, content_type="application/json")


class CheckFigureMoveValidity(APIView):
    renderer_classes = [CustomJSONRenderer]

    def get(
        self, request, chess_figure: str, current_field: str, dest_field: str
    ) -> Response:

        if not input_positions_valid([current_field, dest_field]):
            raise ConflictException_409("Field does not exist.")

        try:
            figure = FigureFactory.create_figure(chess_figure, current_field)
        except (KeyError, TypeError):
            raise NotFoundException_404("Figure not found.")

        move_is_valid = figure.validate_move(dest_field)
        if move_is_valid:
            response = {"move": "valid"}
        else:
            raise ConflictException_409("Current move is not permitted.")
        return Response(data=response, content_type="application/json")
