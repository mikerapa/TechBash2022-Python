import json


def get_wc_data() -> list[dict]:
    data = json.load(open("worldcupdata.json", "r"))
    return data


def show_list(winners: list[dict]):
    for winner in winners:
        print(f"{winner['country']} \t {winner['competition']} - {winner['year']}")


def get_womens_winners_by_country(country_name: str) -> list[dict]:
    data: list[dict] = get_wc_data()
    return [cup for cup in data if cup['country'] == country_name and cup['competition'] == "women"]


def get_mens_winners_by_country(country_name: str) -> list[dict]:
    data: list[dict] = get_wc_data()
    return [cup for cup in data if cup['country'] == country_name and cup['competition'] == "men"]


if __name__ == '__main__':
    winners = get_womens_winners_by_country("Germany")
    show_list(winners)
    mens_winners = get_mens_winners_by_country("Brazil")
    show_list(mens_winners)
