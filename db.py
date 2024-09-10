import json

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