import json
from rich import print

from flask import Flask, request
from random import randint

app = Flask(__name__)

def get_wc_data() -> list[dict]:
    data = json.load(open("worldcupdata.json", "r"))
    return data


def show_wc_data(wc_data: list[dict]):
    def format_competition(competition: str):
        return "Fifa Women's World Cup" if competition == "women" else "Fifa Men's World Cup"

    for winner in wc_data:
        print(f"[blue]{winner['country']}[/blue] won {format_competition(winner['competition'])} in {winner['year']}")


def get_womens_winners_by_country(country_name: str, wc_data: list[dict]) -> list[dict]:
    filtered_data: list[dict] = []
    for winner in wc_data:
        if winner["competition"] == "women" and winner['country'] == country_name:
            filtered_data.append(winner)
    return filtered_data


@app.route("/men")
def get_mens_winners_by_country() -> list[dict]:
    wc_data = get_wc_data()
    country_name = request.args.get('country_name')
    return [winner for winner in wc_data if winner["competition"] == "men" and winner["country"] == country_name]


if __name__ == '__main__':
    data = get_wc_data()
    germany_womens_wins = get_womens_winners_by_country("Germany", data)
    show_wc_data(germany_womens_wins)


"""
IMPORTANT
To run as a rest service execute 'flask run' from the terminal.
"""

