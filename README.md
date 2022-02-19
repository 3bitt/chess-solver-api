# Chess Solver

## Setup instructions
1. Clone repo

2. Create virtual environment with **Python 3.9** with your favourite tool

3. Activate virtualenv and install dependencies

	`pip install -r requirements.txt`

4. Create file with name `.env` in project root and define your variables, for example:
	```
	SECRET_KEY="an#1b7k5i)=$t1@ke9429s@01n51=*iel(iyy*bazil@pc4gt&2exm"
	DEBUG=1
	```

5. Run server

	`python src/manage.py runserver`

6. Have fun ;)

 **To run tests use `pytest src` command**

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

