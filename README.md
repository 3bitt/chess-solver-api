# Chess Solver API

## Setup instructions

| Docker  | Manual |
| ------------- | ------------- |
| <p>1. Build image <br> &emsp; `docker build -t chess-solver-api`</p> <p>2. Run container <br> &emsp; `docker run -dp 8000:8000 chess-solver-api`</p> <p>3. Access API, for example <br> &emsp; `http://localhost:8000/api/v1/king/a2/` </p> | <p>1. Clone or download repo</p> <p>2. Create virtual environment with **Python 3.9**</p> <p>3. Activate virtualenv and install dependencies <br> &emsp; `pip install -r requirements.txt`</p> <p>4. Run server <br> &emsp; `python src/manage.py runserver`</p> <p>5. Access API, for example <br> &emsp; `http://localhost:8000/api/v1/king/a2/`</p> <tr><td colspan=2>Have fun!</td></tr><tr><td colspan=2>**To run tests use `pytest` command**</td></tr>
<br/>


## Endpoints
> [GET] /api/v1/{chess_figure}/{current_field}

> [GET] /api/v1/{chess_figure}/{current_field}/{dest_field}

### Parameters
- **chess_figure**

    king **|** queen **|** rook **|** bishop **|** knight **|** pawn

- **current_field / dest_field**

	[a-h][1-8] - first character between a-h, second character between 1-8 (example: a4, h7)
<br/>

## Examples
>  **/api/v1/rook/d5/**
```json
{
    "availableMoves":["E5","C5","D6","D4","F5","B5","D7","D3","G5","A5","D8","D2","H5","D1"],
    "error":null,
    "figure":"rook",
    "currentField":"D5"
}
```
<br/>

> **/api/v1/king/a1/a2/**
```json
{
    "move":"valid",
    "figure":"king",
    "error":null,
    "currentField":"A1",
    "destField":"A2"
}
```

