import json


def get_wc_data() -> list[dict]:
    data = json.load(open("worldcupdata.json", "r"))
    return data

def display_winners(winners : list[dict]):
    def format_competition_name(competition:str):
        return "Men's FIFA World Cup" if competition=="men" else "Women's FIFA World Cup"
    for winner in winners:
        print(f"{winner['country']} won the {format_competition_name(winner['competition'])} in {winner['year']}")


def get_womens_winners_by_country(country: str, winners:list[dict]):
    filtered_data : list[dict] = []
    for winner in winners:
        if winner['competition'] == "women" and winner['country']==country:
            filtered_data.append(winner)

    return filtered_data


if __name__ == '__main__':
    wc_data = get_wc_data()
    womens_winners = get_womens_winners_by_country("United States", wc_data)
    display_winners(womens_winners)