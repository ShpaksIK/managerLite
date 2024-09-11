import json
import os

from messages import error


def load():
    with open("data.json", "r", encoding="utf-8") as jf:
        fd = json.load(jf)
    return fd

def save(fd) -> bool:
    try:
        with open("data.json", "w", encoding="utf-8") as jf:
            json.dump(fd, jf, indent=4)
        return True
    except Exception as e:
        error("Произошла ошибка:", e)
        return False
    
filename = "data.json"
if not os.path.exists(filename):
    default_data = {
        "name": "",
        "balance": 100000,
        "token": "",
        "passwords": {},
        "settings": {
            "color": "WHITE",
            "bgcolor": "BLACK"
        }
    }
    save(default_data)
