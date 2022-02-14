from django.urls import path

from solver.views import CheckFigureMoveValidity, GetPossibleFigureMoves


urlpatterns = [
    path(
        "<str:chess_figure>/<str:current_field>/",
        GetPossibleFigureMoves.as_view(),
    ),
    path(
        "<str:chess_figure>/<str:current_field>/<str:dest_field>/",
        CheckFigureMoveValidity.as_view(),
    ),
]
