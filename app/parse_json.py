import json
from typing import List


def open_json(path: str):
    with open(f"{path}", "r") as file_json:
        data = json.load(file_json)

    return data, type(data)


def parse_data_from_json(params: List[str]):
    #TODO
    pass


def main():
    path = "../data/json/CPU.json"
    res = open_json(path)
    print(res)


if __name__ == "__main__":
    main()
