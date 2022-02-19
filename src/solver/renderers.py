from rest_framework.renderers import JSONRenderer
from solver.exceptions import DefaultServerErrorException_500


def zero_as_none(value):
    return None if value == 0 else value


class CustomJSONRenderer(JSONRenderer):
    media_type = "application/json"
    format = "json"

    def render(
        self, data, accepted_media_type=None, renderer_context: dict = None
    ):
        response_data = self._get_distinct_response_json(renderer_context)

        response_data |= {**data}
        response = super(CustomJSONRenderer, self).render(
            response_data, accepted_media_type, renderer_context
        )
        return response

    def _get_distinct_response_json(self, renderer_context):
        context: dict = renderer_context.get("kwargs", None)
        view_name: str = renderer_context.get("view").get_view_name()

        figure: str = context.get("chess_figure", None)
        current_field: str = context.get("current_field", None)
        dest_field: str = context.get("dest_field", None)
        error: str = context.get("error", "null")

        if view_name == "Get Possible Figure Moves":
            return {
                "availableMoves": [],
                "figure": figure,
                "error": error,
                "currentField": current_field.upper(),
            }
        elif view_name == "Check Figure Move Validity":
            move: str = context.get("move", "invalid")

            return {
                "move": move,
                "figure": figure,
                "error": error,
                "currentField": current_field.upper(),
                "destField": dest_field.upper(),
            }
        else:
            raise DefaultServerErrorException_500("Internal Server Error")
