import json
from random import randint

from flask import Flask, request
from pydantic import BaseModel
from rich import print

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World"


@app.route("/nums")
def get_nums():
    limit: int = request.args.get('limit', default=10, type=int)
    return [randint(0, 10) for _ in range(limit)]


"""
IMPORTANT
Make sure this file is named app.py
Run in terminal by calling 'flask run'
"""


class Winner(BaseModel):
    country: str
    year: int
    competition: str


def get_world_cup_data() -> list[Winner]:
    data = json.load(open("worldcupdata.json", "r"))
    winners = [Winner(**w) for w in data]
    winners.sort(key=lambda w: w.year)
    return winners


def print_world_cup_data(data: list[Winner]):
    for winner in data:
        print(f"[blue]{winner.year}[/blue] - {winner.country} ({winner.competition})")


def get_mens_winners_by_country(country_name: str) -> list[Winner]:
    filter_fn = lambda w: w.country == country_name and w.competition == 'men'
    return (list(filter(filter_fn, get_world_cup_data())))


@app.route("/men")
def get_mens_winners_by_country_json() -> json:
    country_name = request.args.get("country_name")
    filter_fn = lambda w: w.country == country_name and w.competition == 'men'
    filtered_list = list(filter(filter_fn, get_world_cup_data()))
    return [winner.dict() for winner in filtered_list]


def get_womens_winners_by_country(country_name: str) -> list[Winner]:
    return [winner
            for winner in get_world_cup_data()
            if winner.country == country_name and winner.competition == 'women']


if __name__ == '__main__':
    data = get_world_cup_data()
    print("get men's world cup winners from Germany")
    print_world_cup_data(get_mens_winners_by_country("Germany"))

    print("get womens winners from United States")
    print_world_cup_data(get_womens_winners_by_country('United States'))
