import colorama
from colorama import Back, Fore

from messages import error
from db import load


colorama.init()

def check_bgcolor() -> None:
    """ Проверка на изменение фона текста """
    try:
        fd = load()
        if fd["settings"]["bgcolor"] == "GREEN":
            print(Back.GREEN)
        elif fd["settings"]["bgcolor"] == "RED":
            print(Back.RED)
        elif fd["settings"]["bgcolor"] == "BLUE":
            print(Back.BLUE)
        elif fd["settings"]["bgcolor"] == "YELLOW":
            print(Back.YELLOW)
        elif fd["settings"]["bgcolor"] == "PURPLE":
            print(Back.MAGENTA)
        elif fd["settings"]["bgcolor"] == "WHITE":
            print(Back.WHITE)
        elif fd["settings"]["bgcolor"] == "BLACK":
            print(Back.BLACK)
        else:
            print(Back.BLACK)
    except Exception as e:
        error(f"Возникла внутренняя ошибка: {e}")

def check_color():
    """ Проверка на изменение цвета текста """
    try:
        fd = load()
        if fd["settings"]["color"] == "GREEN":
            print(Fore.GREEN)
        elif fd["settings"]["color"] == "RED":
            print(Fore.RED)
        elif fd["settings"]["color"] == "BLUE":
            print(Fore.BLUE)
        elif fd["settings"]["color"] == "YELLOW":
            print(Fore.YELLOW)
        elif fd["settings"]["color"] == "PURPLE":
            print(Fore.MAGENTA)
        elif fd["settings"]["color"] == "WHITE":
            print(Fore.WHITE)
        elif fd["settings"]["color"] == "BLACK":
            print(Fore.BLACK)
        else:
            print(Fore.WHITE)
    except Exception as e:
        error(f"Возникла внутренняя ошибка: {e}")