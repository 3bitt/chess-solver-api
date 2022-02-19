from abc import ABC, abstractmethod
from solver.utils import (
    normalize_position_format,
    clear_invalid_positions,
)


class Figure(ABC):
    @abstractmethod
    def __init__(self, current_field: str) -> None:
        pass

    @abstractmethod
    def list_available_moves(self) -> list[str]:
        pass

    @abstractmethod
    def validate_move(self, dest_field: str):
        pass


class FigureFactory:
    @classmethod
    def create_figure(self, figure: str, position: str) -> Figure:
        figure = {
            "king": King,
            "queen": Queen,
            "rook": Rook,
            "bishop": Bishop,
            "knight": Knight,
            "pawn": Pawn,
        }.get(figure, None)

        if figure is not None:
            obj = figure(position)
            return obj
        else:
            raise KeyError


class King(Figure):
    def __init__(self, current_field: str) -> None:
        self.position = normalize_position_format(current_field)
        self.min_range = 1
        self.max_range = 1
        self.x = self.position[0]
        self.y = self.position[1]

    def __str__(self) -> str:
        return "king"

    def validate_move(self, dest_field: str) -> bool:
        return (
            True
            if dest_field.upper() in self.list_available_moves()
            else False
        )

    def list_available_moves(self) -> list[str]:
        result = []
        for distance in range(self.min_range, self.max_range + 1):
            horizontal_moves = self.get_horizontal_move_options(distance)
            vertical_moves = self.get_vertical_move_options(distance)
            diagonal_moves = self.get_diagonal_move_options(distance)
            result += clear_invalid_positions(
                horizontal_moves + vertical_moves + diagonal_moves
            )

        return result

    def get_horizontal_move_options(self, distance: int) -> list[str]:
        to_right = chr(ord(self.x) + distance) + self.y
        to_left = chr(ord(self.x) - distance) + self.y
        return [to_right, to_left]

    def get_vertical_move_options(self, distance: int) -> list[str]:
        upwards = self.x + chr(ord(self.y) + distance)
        downwards = self.x + chr(ord(self.y) - distance)
        return [upwards, downwards]

    def get_diagonal_move_options(self, distance: int) -> list[str]:
        right_upward = chr(ord(self.x) + distance) + chr(
            ord(self.y) + distance
        )
        right_downward = chr(ord(self.x) + distance) + chr(
            ord(self.y) - distance
        )
        left_upward = chr(ord(self.x) - distance) + chr(ord(self.y) + distance)
        left_downward = chr(ord(self.x) - distance) + chr(
            ord(self.y) - distance
        )
        return [right_upward, right_downward, left_upward, left_downward]


class Queen(Figure):
    def __init__(self, current_field: str) -> None:
        self.position = normalize_position_format(current_field)
        self.min_range = 1
        self.max_range = 7
        self.x = self.position[0]
        self.y = self.position[1]

    def __str__(self) -> str:
        return "queen"

    def validate_move(self, dest_field: str):
        return (
            True
            if dest_field.upper() in self.list_available_moves()
            else False
        )

    def list_available_moves(self) -> list[str]:
        result = []
        for distance in range(self.min_range, self.max_range + 1):
            horizontal_moves = self.get_horizontal_move_options(distance)
            vertical_moves = self.get_vertical_move_options(distance)
            diagonal_moves = self.get_diagonal_move_options(distance)
            result += clear_invalid_positions(
                horizontal_moves + vertical_moves + diagonal_moves
            )
        return result

    def get_horizontal_move_options(self, distance: int) -> list[str]:
        to_right = chr(ord(self.x) + distance) + self.y
        to_left = chr(ord(self.x) - distance) + self.y
        return [to_left, to_right]

    def get_vertical_move_options(self, distance: int) -> list[str]:
        upwards = self.x + chr(ord(self.y) + distance)
        downwards = self.x + chr(ord(self.y) - distance)
        return [upwards, downwards]

    def get_diagonal_move_options(self, distance: int) -> list[str]:
        right_upward = chr(ord(self.x) + distance) + chr(
            ord(self.y) + distance
        )
        right_downward = chr(ord(self.x) + distance) + chr(
            ord(self.y) - distance
        )
        left_upward = chr(ord(self.x) - distance) + chr(ord(self.y) + distance)
        left_downward = chr(ord(self.x) - distance) + chr(
            ord(self.y) - distance
        )
        return [right_upward, right_downward, left_upward, left_downward]


class Rook(Figure):
    def __init__(self, current_field: str) -> None:
        self.position = normalize_position_format(current_field)
        self.min_range = 1
        self.max_range = 7
        self.x = self.position[0]
        self.y = self.position[1]

    def __str__(self) -> str:
        return "rook"

    def validate_move(self, dest_field: str):
        return (
            True
            if dest_field.upper() in self.list_available_moves()
            else False
        )

    def list_available_moves(self) -> list[str]:
        result = []
        for distance in range(self.min_range, self.max_range + 1):
            horizontal_moves = self.get_horizontal_move_options(distance)
            vertical_moves = self.get_vertical_move_options(distance)
            result += clear_invalid_positions(
                horizontal_moves + vertical_moves
            )
        return result

    def get_horizontal_move_options(self, distance: int) -> list[str]:
        to_right = chr(ord(self.x) + distance) + self.y
        to_left = chr(ord(self.x) - distance) + self.y
        return [to_right, to_left]

    def get_vertical_move_options(self, distance: int) -> list[str]:
        upwards = self.x + chr(ord(self.y) + distance)
        downwards = self.x + chr(ord(self.y) - distance)
        return [upwards, downwards]


class Bishop(Figure):
    def __init__(self, current_field: str) -> None:
        self.position = normalize_position_format(current_field)
        self.min_range = 1
        self.max_range = 7
        self.x = self.position[0]
        self.y = self.position[1]

    def __str__(self) -> str:
        return "bishop"

    def validate_move(self, dest_field: str):
        return (
            True
            if dest_field.upper() in self.list_available_moves()
            else False
        )

    def list_available_moves(self) -> list[str]:
        result = []
        for distance in range(self.min_range, self.max_range + 1):
            diagonal_moves = self.get_diagonal_move_options(distance)
            result += clear_invalid_positions(diagonal_moves)
        return result

    def get_diagonal_move_options(self, distance: int) -> list[str]:
        right_upward = chr(ord(self.x) + distance) + chr(
            ord(self.y) + distance
        )
        right_downward = chr(ord(self.x) + distance) + chr(
            ord(self.y) - distance
        )
        left_upward = chr(ord(self.x) - distance) + chr(ord(self.y) + distance)
        left_downward = chr(ord(self.x) - distance) + chr(
            ord(self.y) - distance
        )
        return [right_upward, right_downward, left_upward, left_downward]


class Knight(Figure):
    def __init__(self, current_field: str) -> None:
        self.position = normalize_position_format(current_field)
        self.min_range = 2
        self.max_range = 3
        self.x = self.position[0]
        self.y = self.position[1]

    def __str__(self) -> str:
        return "knight"

    def validate_move(self, dest_field: str):
        return (
            True
            if dest_field.upper() in self.list_available_moves()
            else False
        )

    def list_available_moves(self) -> list[str]:
        result = []
        for distance in range(self.min_range, self.max_range):
            horizontal_moves = self.get_horizontal_move_options(distance)
            vertical_moves = self.get_vertical_move_options(distance)
            result += clear_invalid_positions(
                horizontal_moves + vertical_moves
            )
        return result

    def get_horizontal_move_options(self, distance: int) -> list[str]:
        shifted_to_right = chr(ord(self.x) + distance)
        shifted_to_left = chr(ord(self.x) - distance)

        right_upwards = shifted_to_right + chr(ord(self.y) + 1)
        right_downwards = shifted_to_right + chr(ord(self.y) - 1)
        left_upwards = shifted_to_left + chr(ord(self.y) + 1)
        left_downwards = shifted_to_left + chr(ord(self.y) - 1)
        return [right_upwards, right_downwards, left_upwards, left_downwards]

    def get_vertical_move_options(self, distance: int) -> list[str]:
        shifted_to_up = chr(ord(self.y) + distance)
        shifted_to_down = chr(ord(self.y) - distance)

        upper_right = chr(ord(self.x) + 1) + shifted_to_up
        upper_left = chr(ord(self.x) - 1) + shifted_to_up
        downer_right = chr(ord(self.x) + 1) + shifted_to_down
        downer_left = chr(ord(self.x) - 1) + shifted_to_down
        return [upper_right, upper_left, downer_right, downer_left]


class Pawn(Figure):
    def __init__(self, current_field: str) -> None:
        self.position = normalize_position_format(current_field)
        self.max_range = 1
        self.x = self.position[0]
        self.y = self.position[1]

    def __str__(self) -> str:
        return "pawn"

    def validate_move(self, dest_field: str):
        return (
            True
            if dest_field.upper() in self.list_available_moves()
            else False
        )

    def list_available_moves(self) -> list[str]:
        return self.get_vertical_move_options(self.max_range)

    def get_vertical_move_options(self, distance: int) -> list[str]:
        upwards = self.x + chr(ord(self.y) + distance)
        valid_positions = clear_invalid_positions([upwards])
        return valid_positions
