from email import charset
from django.http.multipartparser import parse_header
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


def zero_as_none(value):
    return None if value == 0 else value


class CustomJSONRenderer(JSONRenderer):
    media_type = "application/json"
    format = "json"

    def render(
        self, data, accepted_media_type=None, renderer_context: dict = None
    ):
        context: dict = renderer_context.get("kwargs", None)

        figure: str = context.get("chess_figure")
        current_field: str = context.get("current_field")
        dest_field: str = context.get("dest_field")
        response_data = {
            "figure": figure,
            "error": "null",
            "currentField": current_field.upper(),
            **(
                {"destField": dest_field.upper()}
                if dest_field is not None
                else {}
            ),
        }
        response_data |= {**data}
        response = super(CustomJSONRenderer, self).render(
            response_data, accepted_media_type, renderer_context
        )
        return response
