import json


def get_wc_data() -> list[dict]:
    data = json.load(open("worldcupdata.json", "r"))
    return data


if __name__ == '__main__':
    pass
