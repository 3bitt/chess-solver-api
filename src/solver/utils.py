import re


def input_positions_valid(positions: list[str]) -> bool:
    pattern = r"^([A-H]{1}[1-8]{1}|[1-8]{1}[A-H]{1}){1}$"
    for position in positions:
        position = position.strip()
        if not bool(re.match(pattern, position, re.IGNORECASE)):
            return False
    return True


def normalize_position_format(position: str) -> str:
    if position[0].isdigit():
        formatted = position[1] + position[0]
        return formatted
    return position


def clear_invalid_positions(positions: list[str]) -> list[str]:
    valid_positions = []
    for position in positions:
        try:
            x = ord(position[0])
            y = ord(position[1])
        except IndexError:
            continue
        if field_exists_on_board(x, y):
            valid_positions.append(position.upper())
    return valid_positions


def field_exists_on_board(x: int, y: int) -> bool:
    return True if (96 < x < 105) and (48 < y < 57) else False
