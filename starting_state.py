import json

from pydantic import BaseModel


class Winner(BaseModel):
    country: str
    year: int
    competition: str


def get_world_cup_data() -> list[Winner]:
    data = json.load(open("worldcupdata.json", "r"))
    winners = [Winner(**w) for w in data]
    winners.sort(key=lambda w: w.year)
    return winners


if __name__ == '__main__':
    data = get_world_cup_data()
