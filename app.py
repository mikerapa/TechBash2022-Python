import json
from rich import print

from flask import Flask, request
from random import randint

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World"


@app.route("/nums")
def get_nums():
    nums: list(int) = []
    nums = [randint(0, 10) for _ in range(10)]
    return nums


"""
IMPORTANT
Make sure this file is named app.py
Run in terminal by calling 'flask run'
"""


@app.route("/women")
def get_womens_world_cup_winners():
    data: list[dict] = get_wc_data()
    return [cup for cup in data if cup['competition'] == "women"]


def get_wc_data() -> list[dict]:
    data = json.load(open("worldcupdata.json", "r"))
    return data


def display_winners(winners: list[dict]):
    def format_competition_name(competition: str):
        return "Men's FIFA World Cup" if competition == "men" else "Women's FIFA World Cup"

    for winner in winners:
        print(
            f"{winner['country']} won the {format_competition_name(winner['competition'])} in [blue]{winner['year']}[/blue]")


def get_womens_winners_by_country(country: str, winners: list[dict]):
    filtered_data: list[dict] = []
    for winner in winners:
        if winner['competition'] == "women" and winner['country'] == country:
            filtered_data.append(winner)

    return filtered_data


@app.route("/men", methods=['GET'])
def get_mens_winners_by_country() -> list[dict]:
    data: list[dict] = get_wc_data()
    country_name: str = request.args.get('country_name')
    return [cup for cup in data if cup['country'] == country_name and cup['competition'] == "men"]


if __name__ == '__main__':
    wc_data = get_wc_data()
    womens_winners = get_womens_winners_by_country("United States", wc_data)
    display_winners(womens_winners)
    mens = get_mens_winners_by_country("Germany")
    display_winners(mens)
