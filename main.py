import json
import datetime
import os
import sys
import random
import requests
import time
import webbrowser
import subprocess

import openai
import pyttsx3
import translate
from pyfiglet import Figlet

from messages import error, suc
from db import load, save
from utils import check_bgcolor, check_color


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
running = True
check_bgcolor()
check_color()
os.system("cls")
preview_text = Figlet(font='slant')
print(preview_text.renderText('MANAGER Lite'))
print(f"=============================================================================================\n Добро пожаловать. Список команд ---> help \n=============================================================================================")

while running:
    text = input()

    if text == "help":
        print("============ Список команд и их описание ============")
        print("ОБЩИЕ, ОСНОВНЫЕ КОММАНДЫ:")
        print(" help - данный список команд")
        print(" prog - информация о программе")
        print(" /ex - прекратить использвание комманды")
        print(" balance или bal - узнать свой баланс")
        print(" givebal - выдаёт деньги")
        print(" clear или cls - отчистить чат, введённые команды и т.п.")
        print(" color - изменить цвет текста")
        print(" bgcolor - изменить обводку текста")
        print(" exit - выход из программы")
        print("ПОЛЕЗНЫЕ КОММАНДЫ:")
        print(" info - информация о вашем ПК")
        print(" gpt - настоящий чат с ChatGPT")
        print(" wifi - выдаёт список паролей wifi, к которым было подключено устройство")
        print(" course - курс валют")
        print(" rand - создает случайный пароль")
        print(" yt - найти видео в ютубе")
        print(" sear - найти какую-либо информацию в браузере (google)")
        print(" ya - направляет на страницу Yandex")
        print(" google - направляет на страницу Google")
        print(" onen - перевести текст с русского на английский")
        print(" onru - перевести текст с английского на русский")
        print(" ip - найти информацию по ip")
        print(" time - узнать время")
        print(" voice - воспроизвести текст в речь")
        print("РАЗВЛЕЧЕНИЕ:")
        print(" kazino - игра в казино ")
        print(" or - орел или решка?")
        print(" spam - спам текстом")
        print(" try - правда или неправда")
        print("=====================================================")

    elif text == "spam":
        try:
            kol = int(input(">>> Сколько вы хотите строк спама: "))
            if kol > 0:
                text = input(">>> Введите текст: ")
                for i in range(kol):
                    print(text)
                    time.sleep(0.05)
            else:
                error("Количество строк не должно быть менее 1")
        except ValueError:
            error("Введено неверное значение")
    
    elif text == "rand":
        symbol_password = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        lenght = int(input(">>> Введите длину пароля: "))
        try:
            password = ""
            for i in range(lenght):
                password += random.choice(symbol_password)
            suc(f"Ваш пароль: {password}")
        except ValueError:
            error("Введено неверное значение")
                        
    elif text == "clear" or text == "cls":
        os.system("cls")

    elif text == "yt":
        search = input(">>> Что найти (/ex для отмены): ")
        if search == "/ex":
            suc("Отменено")
        else:
            webbrowser.open(f'https://www.youtube.com/search?q={search}&oq={search}')

    elif text == "sear":
        search = input(">>> Что найти (/ex для отмены): ")
        if search == "/ex":
            suc("Отменено")
        else:
            webbrowser.open(f'https://www.google.com/search?q={search}&oq={search}')

    elif text == "exit":
        sys.exit()

    elif text == "balance" or text == "bal":
        fd = load()
        suc(f"Ваш баланс: {fd['balance']}")
    
    elif text == "kazino":
        fd = load()
        balance = int(fd["balance"])
        numbers = '1234567890'
        try:
            stavka = int(input(">>> Ваша ставка: "))
            if stavka < 1000:
                error("Ставка не должна быть меньше 1000")
            else:
                if balance < stavka:
                    error("У вас недостаточно денег, чтобы поставить такую ставку")
                else:
                    balance -= stavka
                    def selectionText():
                        global r1, r2, r3
                        r1 = random.choice(numbers)
                        r2 = random.choice(numbers)
                        r3 = random.choice(numbers)
                        print("Идёт подбор числа: ", r1, end='')
                        print(r2, end='')
                        print(r3, end='')
                        time.sleep(0.09)
                        print('\r', end='')
                        print('\r', end='')
                        print('\r', end='')
                    for i in range(50):
                        selectionText()
                    rand_numbers = r1 + r2 + r3
                    win_numbers = ["000","111", "222", "333", "444", "555", "666", "777", "888", "999", "123", "100", "200", "300", "400", "500", "600", "700", "800", "900"]
                    if (rand_numbers in win_numbers) or (int(rand_numbers) % 5 == 0) or (r1 == r2) or (r1 == r3) or (r2 == r3):
                        stavka *= 5
                        suc(f"Поздравляем, вам выпали числа {rand_numbers}! Вы выиграли {stavka}$")
                        fd['balance'] += stavka
                    else:
                        fd['balance'] -= stavka
                        suc("Вы ничего не выиграли. Выпали числа " + rand_numbers)
                    save(fd)
        except ValueError:
            error("Введено неверное значене")

    elif text == "or":
        try:
            stavka = int(input(">>> Ваша ставка (/ex для отмены): "))
            if stavka == "/ex":
                suc("Отменено")
            else:
                fd = load()
                balance = fd['balance']
                if balance < stavka:
                    error("У вас недостаточно денег, чтобы поставить такую ставку")
                elif stavka < 10:
                    error("Ставка не должна быть меньше 10")
                else:
                    rand = input(">>> Выберете: орел (1), решка (2) (/ex для отмены): ")
                    if rand == "/ex":
                        suc("Отменено")
                    elif rand == "1" or rand == "2":
                        print("Монетка подкинута...")
                        time.sleep(2)
                        r = random.choice(["1", "2"])
                        if rand == r:
                            stavka *= 2
                            if r == "1":
                                suc(f"Выпал Орёл. Вы выиграли {stavka}")
                            else:
                                suc(f"Выпала Решкаю Вы выиграли {stavka}")
                            fd['balance'] += stavka
                        else:
                            fd['balance'] -= stavka
                            suc("Вы проиграли")
                        save(fd)
                    else:
                        error("Введено неверное значение")
        except ValueError:
            error("Введено неверное значение")

    elif text == "givebal":
        fd = load()
        try:
            amount = int(input(">>> Сумма перевода (/ex для отмены): "))
            fd["balance"] += amount
            save(fd)
            suc(f"Вам начислено {amount}$")
        except ValueError:
            error("Введено неверное значение")
    
    elif text == "onen":
        translator = translate.Translator(from_lang="ru", to_lang="en")
        text_ru = input(">>> Введите текст на русском: ")
        suc(f"Перевод: {translator.translate(text_ru)}")

    elif text == "onru":
        translator = translate.Translator(from_lang="en", to_lang="ru")
        text_en = input(">>> Введите текст на английском: ")
        suc(f"Перевод: {translator.translate(text_en)}")

    elif text == "try":
        ask_try = input(">>> Введите удтверждение: ")
        rand_try = ["ДА", "НЕТ"]
        suc(f"{random.choice(rand_try)}")

    elif text == "ya":
        webbrowser.open(f'https://ya.ru/')
        suc("Открыт Yandex")
    
    elif text == "google":
        webbrowser.open(f'https://www.google.com')
        suc("Открыт Google")

    elif text == "ip":
        def get_info_by_ip(ip='127.0.0.1'):
            try:
                response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
                data = {
                    '[IP]': response.get('query'),
                    '[Int prov]': response.get('isp'),
                    '[Org]': response.get('org'),
                    '[Country]': response.get('country'),
                    '[Region Name]': response.get('regionName'),
                    '[City]': response.get('city'),
                    '[ZIP]': response.get('zip'),
                    '[Lat]': response.get('lat'),
                    '[Lon]': response.get('lon'),
                }
                suc(f"Информация об ip-адресе ({ip}):")
                for k, v in data.items():
                    print(f' {k}: {v}')
            except requests.exceptions.ConnectionError:
                error("Проверте подключение к интернету")
        ip = input(">>> Введите ip: ")
        get_info_by_ip(ip=ip)

    elif text == "color":
        fd = load()
        colors = ["GREEN", "RED", "BLUE", "YELLOW", "PURPLE", "WHITE", "BLACK"]
        suc("Доступные цвета:")
        for col in colors:
            print(f" - {col}")
        color = input(">>> Введите цвет теста (/ex для отмены): ")
        color_up = color.upper()
        if color == "/ex":
            suc("Отменено")
        elif color_up in colors:
            fd["settings"]["color"] = color_up
            save(fd)
            check_color()
            suc(f"Цвет текста изменён на {color}")
        else:
            error("Такого цвета не существует или он не доступен")
            
    elif text == "bgcolor":
        fd = load()
        bgcolors = ["GREEN", "RED", "BLUE", "YELLOW", "PURPLE", "WHITE", "BLACK"]
        suc("Доступные цвета:")
        for col in bgcolors:
            print(f" - {col}")
        bgcolor = input(">>> Выберете цвет теста: ")
        bgcolor_up = bgcolor.upper()
        if bgcolor == "/ex":
            suc("Отменено")
        elif bgcolor_up in bgcolors:
            fd["settings"]["bgcolor"] = bgcolor_up
            save(fd)
            check_bgcolor()
            suc(f"Цвет фона текста изменён на {bgcolor}")
        else:
            error("Такого цвета не существует или он не доступен")
        
    elif text == "gpt":
        fd = load()
        openai.api_key = fd['token']
        def get_openai_response(message):
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=message,
                max_tokens=2900,
                n=1,
                stop=None,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        suc("Открыт ChatGPT. Для выхода введите /ex")
        while True:
            user_input = input(">>> Вы: ")
            if user_input.lower() == '/ex':
                suc("Отменено")
                break
            print("Генерация текста, подождите...")
            try:
                openai_response = get_openai_response(user_input)
                print(f"OpenAI:\n{openai_response}\n")
            except Exception:
                error("Что-то пошло не так. Проверьте токен")
                break
                
    elif text == "/ex":
        error("На данный момент вы не используете команду")
    
    elif text == "voice":
        voice = input(">>> Введите текст для воспроизведения (/ex для отмены): ")
        if voice == "/ex":
            suc("Отменено")
        else:
            try:
                engine.say(voice)
                engine.runAndWait()
            except Exception as e:
                error(f"Возникла внутренняя ошибка: {e}")

    elif text == "token":
        fd = load()
        new_token = input(">>> Введите токен для ChatGPT (/ex для отмены): ")
        if new_token == "/ex":
            suc("Отменено")
        else:
            fd["settings"]["token"] = new_token
            save(fd)
            suc("Токен был успешно заменён")
    
    elif text == "time":
        now = datetime.datetime.now()
        print(f"\nДата: {now.strftime('%d %m %Y')}")
        print(f"Время: {now.strftime('%H:%M:%S')}\n")
    
    elif text == "wifi":
        print("Подождите...")
        try:
            data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "Все профили пользователей" in i] 
            pass_wifi = '' 
            for i in profiles:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')
                for j in results:
                    if "Содержимое ключа" in j:
                        pass_wifi += f"{i} -- {j.split(':')[1][1:-1]}\n"
            print(pass_wifi)
        except Exception as e:
            error(f"Возникла внутренняя ошибка: {e}")

    elif text == "course":
        course = input(">>> Какую валюту отследить:\n EUR\n USD\n/ex для отмены: ")
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        if course == "/ex":
            suc("Отменено")
        elif course.upper() == "EUR":
            suc(f"Курс евро: {response['Valute']['EUR']['Value']} рублей")
        elif course.upper() == "USD":
            suc(f"Курс доллара: {response['Valute']['USD']['Value']} рублей")
        else:
            error("Неизвестная валюта")
    
    elif text == "calc":
        def calculate(expression):
            result = eval(expression)
            return result
        expression = input(">>> Введите выражение для вычисления (/ex для отмены): ")
        if expression.lower() == "/ex":
            suc("Отменено")
        try:
            result = calculate(expression)
            print(f"Результат: {result}")
        except Exception as e:
            error(f"Возникла внутренняя ошибка: {e}")

    elif text == "prog":
        print("\n========= ИНФОРМАЦИЯ =========")
        print(f"Название: Manager Lite")
        print(f"Исходник: ")