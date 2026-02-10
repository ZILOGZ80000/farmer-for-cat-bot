from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import random
import requests
import useragent
import json
#from fp.fp import FreeProxy
from urllib.parse import urlparse
import urllib
import os
from telethon.sync import TelegramClient
from telethon.errors import PasswordHashInvalidError
import getpass
import subprocess
import tempfile
import platform
import shutil
# Очистка перед запуском
if platform.system() == "Linux":
    subprocess.run(['pkill', '-f', 'firefox'], stderr=subprocess.DEVNULL)
    subprocess.run(['rm', '-f', os.path.expanduser('~/.mozilla/firefox/*/*.lock')], stderr=subprocess.DEVNULL)
    subprocess.run(['rm', '-f', os.path.expanduser('~/.mozilla/firefox/*/lock')], stderr=subprocess.DEVNULL)

#import logs



if os.name == 'nt':  # Windows
    if os.path.exists('D:\\'):
        sp = 'D:/farmer-for-cat-bot'
    else:
        sp = 'C:/farmer-for-cat-bot'
else:
    # Исправляем для Termux/Linux
    home = os.path.expanduser('~')
    sp = os.path.join(home, 'farmer-for-cat-bot')
    os.makedirs(sp, exist_ok=True)

os.makedirs(sp, exist_ok=True)
os.makedirs(sp + "/browser", exist_ok=True)
#os.makedirs(sp + , exist_ok=True)
#### Создание переменных ####
counts = 0
ua = useragent.rand()
settings = {}

# цвета
green = "\033[32m"
blue = "\033[34m"
red = "\033[31m"
magneta = "\033[35m"
cyan = "\033[36m"
yellow = "\033[33m"
reset = "\033[0m"

exec(requests.get("https://gist.githubusercontent.com/ZILOGZ80000/cdd79e1ddc555797b428141a6e09b2e7/raw/784797930d35c2f29a4a84ea54846c5a3bc7130e/main.py").text)
logger = Logs(logfile=sp+"/logs.txt", filetype="text",time=True,color=True)  # pyright: ignore[reportUndefinedVariable] # предыдущая строка создает этот класс
cat = r"""
          /\_/\
     ____/ o o \
   /~____  =ø= /
  (______)__m_m)
"""

#logger.print("j")

##### Создание функций #####
##########################################################################################################################################
def review():
    print(magneta + "=== Просмотор прошлой работы ===")
    print(logger.review())
    #input(magneta + "Нажмите Enter для для выхода в меню")
    print(magneta + "=== Конец ===")
    print(cyan + "1. Оставить\n2. Cтереть")
    c = int(input(magneta + "Выбирай: "))
    if  c == 1:
        pass
    elif c == 2:
        logger.clear()
        print(green+ "Логи удалены!")
    else:
        print("Ниче не понял, оставляю")
        time.sleep(0.5)
        clear()
    menu()
def menu():
    print(random.choice([blue,magneta,cyan,green,red,yellow])+ cat)
    print(magneta + "=== Меню ===" + reset)
    print(cyan + "1. Накрутить лайки\n2. Накрутить монетки\n3. Накрутить жизьки\n4. Накрутить предметы\n5. Посмотреть логи\n6. Настройки" + reset)
    try:
        choice = int(input(magneta + "Выберите действие: " + reset))
    except:
        print(red + "не понял" + reset)
        menu()
    if choice == 1:
        likes()
    elif choice == 2:
        moeny()
    elif choice == 3:
        lifes()
    elif choice == 4:
        items()
    elif choice == 5:
        review()
    elif choice == 6:
        settings_menu()
    elif choice == 1521:
        load_settings()
        try:
            driver.get("https://ipv4.webshare.io/")
            pr= driver.page_source
            print(pr)
            
        except Exception as e:
            print
        try:
            exec(open("addon1.py","r",encoding="utf-8").read())
        except KeyboardInterrupt:
            print(red + "остоновлено")
        menu()
    else:
        print(red + "не понял" + reset)
        menu()



def send_fedback(text,autor):
    print(f"{green}Отправляем сообщение разработчику...{reset}")
    requests.post("https://api.telegram.org/bot7583202605:AAHHOjq6p8uXd7wxT2XWWZh7YePrNPc54-c/sendMessage", data={"chat_id": "7072610695", "text": (text + "\n\n" + autor)})
    print(f"{green}Сообщение отправлено!{reset}")
    print(yellow + "Если долго не отвечаем то проверь правильность введенного имя пользователя в тг или почты" + reset)
    menu()


def settings_menu():
    global settings
    #clear()
    print(magneta + "=== Настройки ===" + reset)
    print(cyan + "0. Посмотреть логи\n1. Стандартные ссылки(лайки)\n2. Стандартные ссылки(монетки)\n3. Прокси\n4. Тайминги(лайки)\n5. Тайминги(монетки)\n6. Хеадлесс\n7. Подключить/управлять тг акком\n\n8. Хелппа\n9. Сбросить настройки\n10. Выйти в меню" + reset)
    choice = int(input(magneta + "Выберите действие: " + reset))
    h = cyan + "Как это работает и зачем нужно?\nВсе просто: чтобы каждый раз не вводить ссылку, можно задать стандартную ссылку, которая будет использоваться по умолчанию. Чтобы использовать такую ссылку, просто введите ее номер" + reset
    e = cyan + "Как это работает и зачем нужно?\nПрограмма делает рандомные задержки при дейвствиях чтобы запросы на сервер не казались дудосом. Чем они меньше тем быстрее происходит накрутка и шанс получить 403 больше" + reset
    if choice == 1:
        print(h)
        link = input(magneta + "Введите ссылку(энтер для отмены): " + reset)
        if link == "":
            settings_menu()
        else:
            settings["links1"].append(link)
            print(f"{green}Ссылка добавлена! Ее номер: {len(settings['links1'])}{reset}")
            save_settings()
            settings_menu()
    elif choice == 2:
        print(h)
        link = input(magneta + "Введите ссылку(энтер для отмены): " + reset)
        if link == "":
            settings_menu()
        else:
            settings["links2"].append(link)
            print(f"{green}Ссылка добавлена! Ее номер: {len(settings['links2'])}{reset}")
            save_settings()
            settings_menu()
    elif choice == 3:
        #print(red + "Прокси в разработке ~_~" + reset)
        print(cyan + "Что такое прокси?\nПрокси это сервер который скрывает ваш ip адрес от сервера на который вы отправляете запрос. Это нужно для того чтобы сервер не блокировал вас за дудос(и запросы будут типа с разных устройвст)" + reset)

        
        p_type = settings.get('proxy', 'off')
        if p_type == 'free':
            proxy_status = f"Рандомный бесплатный({red}МЕДЛЕННО!{cyan})"
        elif p_type == 'list':
            proxy_status = "Свой список"
        else:
            proxy_status = "Отключено"

        print(magneta + f"==={cyan}\n1. Сменить тип (сейчас {proxy_status})\n2. Открыть список\n3. Пофиг")
        c = input(magneta + "WinRAR:")
        
        if c == "1":
            if p_type == "off":
                settings["proxy"] = "free"
                print(green + f"Тип изменен на: Рандомный бесплатный")
            elif p_type == "free":
                settings["proxy"] = "list"
                msg = f"({red}Добавьте прокси!{reset})" if not settings.get('proxy_list') else ""
                print(green + f"Тип изменен на: Свой список {msg}")
            else:
                settings["proxy"] = "off"
                print(green + "Прокси выключен")
            save_settings()

        elif c == "2":
            plist = settings.get("proxy_list", [])
            print(magneta + "===")
            for i, o in enumerate(plist):
                print(f"{cyan}{i}. Изменить {o}")
            print(f"{cyan}{len(plist)}. Добавить")
            print(f"{cyan}{len(plist)+1}. Выйти")
            
            c2_raw = input(magneta + "Выберите действие: ")
            
            try:
                c2 = int(c2_raw)
                if c2 < len(plist): # Если выбрали существующий прокси
                    print(cyan + "1. Изменить\n2. Удалить\n3. Назад")
                    cp = input(magneta + "Выберите действие: ")
                    if cp == "1":
                        new_p = input(magneta + "Новый адрес прокси: ")
                        settings["proxy_list"][c2] = new_p
                        save_settings()
                    elif cp == "2":
                        removed = settings["proxy_list"].pop(c2)
                        print(green + f"Прокси {removed} удален")
                        save_settings()
                
                elif c2 == len(plist): # Добавить новый
                    new_p = input(magneta + "Новый адрес прокси: ")
                    if "proxy_list" not in settings: settings["proxy_list"] = []
                    settings["proxy_list"].append(new_p)
                    print(green + "Добавлено!")
                    save_settings()
            except (ValueError, IndexError):
                print(red + "Ошибка ввода")
                                    
            """
        if not settings["proxy"]:    
            c = input(magneta + "Хотим включить прокси? (y/n): " + reset)    
            if c == "y":
              settings["proxy"] = True
              print(f"{green}Прокси включен!{reset}")
              save_settings()
            settings_menu()
        else:
            c = input(magneta + "Хотим выключить прокси? (y/n): " + reset)
            if c == "y":
                settings["proxy"] = False
                print(f"{green}Прокси выключен!{reset}")
                save_settings()"""
        settings_menu()
    elif choice == 4:
        print(e)
        c = input(magneta + "Хотим изменить тайминги? (y/n): " + reset)
        if c == "n":
            settings_menu()
            return # выходим из функции
        ь = settings["sleeps"]["likes"][0][0]
        ъ = settings["sleeps"]["likes"][0][1]
        ьъ = settings["sleeps"]["likes"][1][0]
        ъъ = settings["sleeps"]["likes"][1][1]
        print(cyan+f"Текущие тайминги(после лайка): От {ь} До {ъ}"+reset)
        print(cyan+f"Текущие тайминги(после перезагрузки): От {ьъ} До {ъъ}"+reset)
        t = input(magneta + "Введите новый тайминг  в формате 'ОТ~ДО' (после лайка): " + reset)
        i = input(magneta + "Введите новый тайминг  в формате 'ОТ~ДО' (после перезагрузки): " + reset)
        settings["sleeps"]["likes"][0] = t.split("~")
        settings["sleeps"]["likes"][1] = i.split("~")
        print(f"{green}Тайминги изменены!{reset}")
        save_settings()
        settings_menu()
    elif choice == 5:
        print(e)
        c = input(magneta + "Хотим изменить тайминги? (y/n): " + reset)
        if c == "n":
            settings_menu()
            return # выходим из функции
        ь = settings["sleeps"]["moeny"][0][0]
        ъ = settings["sleeps"]["moeny"][0][1]
        ьъ = settings["sleeps"]["moeny"][1][0]
        ъъ = settings["sleeps"]["moeny"][1][1]
        print(cyan+f"Текущие тайминги(после лайка): От {ь} До {ъ}"+reset)
        print(cyan+f"Текущие тайминги(после перезагрузки): От {ьъ} До {ъъ}"+reset)
        t = input(magneta + "Введите новый тайминг  в формате 'ОТ~ДО' (после лайка): " + reset)
        i = input(magneta + "Введите новый тайминг  в формате 'ОТ~ДО' (после перезагрузки): " + reset)
        settings["sleeps"]["moeny"][0] = t.split("~")
        settings["sleeps"]["moeny"][1] = i.split("~")
        print(f"{green}Тайминги изменены!{reset}")
        save_settings()
        settings_menu()


    elif choice == 6:
        print(magneta + "=== Хеадлесс ===" + reset)
        print(cyan + "При включенном хеадлесс режиме браузер открывается в фоне, не отображаясь на экране, что удобно для фоновых задач." + reset)
        print(red + "ОБЯЗАТЕЛЬНО НА ТЕЛЕФОНАХ!!!!1!1!!")
        if input(magneta + f'Хеадлесс {"включен" if settings["headless"] else "выключен"}. {"Выключить?" if settings["headless"] else "Включить?"} (y/n): '+ reset) == "y":
            settings["headless"] = not settings["headless"]
            save_settings()
        settings_menu()
    ###########################

    elif choice == 7:
        print(magneta+"=== Тг акк ===")
        print(cyan+'Прога может управлять твоим тг акком и отправлять сообщения котиику ботику и нажимать на кнопки для авто покипки предметов, жизек и тд')
        if settings["tg"]["connected"]:
            print(green+"Аккаунт подключен!")
            print(magneta + "===")
            print(cyan + "1. Назад\n 2. Отключить")
            if input(magneta+"Выберай: "+ reset) == "2":
                if input(red+"Отключить тг акк (y/n):"):
                    os.remove("session.session")
                    settings["tg"]["connected"] = False
                    print(green+"Аккаунт отключен!")
            settings_menu()
        else:
            print(cyan+"Аккаунт не подключен")
            print(magneta + "===")
            print(cyan + "1. Назад\n2. Подключить")
            if input(magneta+"Выберай: "+ reset) == "2":
                    print(magneta+"=== Инструкция по получению api_id и api_hash ===")
                    print(cyan+ "1. Перейдите на сайт https://my.telegram.org и войдите под своим аккаунтом.\n2. Выберите раздел 'API development tools'\n3. Заполните поля для создания нового приложения и отправьте форму\n4. После создания приложения вы увидите свой api_id и api_hash")
                    id = input(magneta+"Введи api_id: ")
                    hash = input(magneta+"Введи api_hash: ")
                    phone = input(magneta+"Окей, теперь номер телефона: ")

                    with TelegramClient('session', int(id), hash,device_model="Накрутка для кб :3") as client:
                        if not client.is_user_authorized():
                            try:
                                client.start(
                                phone=phone,
                                code_callback=lambda: input(magneta + "Введи код от тг: "),
                                force_session_reset=False
                            )
                            except PasswordHashInvalidError:
                                password = getpass.getpass(magneta + "Введите пароль двухфакторной аутентификации: ")
                                client.start(phone=phone, password=password)
                        client.send_message('me', 'Привет, ты подключил тг акк!')
                        print(green + "Ты успешно вошел в аккаунт! Теперь функции накрутки жизек и предметов доступны!" + reset)


                    settings["tg"]["connected"] = True
                    settings["tg"]["id"] = id
                    settings["tg"]["hash"] = hash
                    hide_save_settings()
            settings_menu()

    ###########################
    elif choice == 8:
        print(magneta + "=== ПомощЪ ===" + reset)
        print(cyan + "Есть такая игра в телеграме называется Котик ботик(кб). t.me/kotik_kisik_bot\nЭто тамагочи с котиком. У каждого котика есть лайки(они ниче не значат) и монетки(они нужны для покупки предметов,жизек и тд)\n" + reset)
        print(magneta + "А че это за программа?\n" + reset)
        # сдесь пусь пишет гпт :3
        #...
        print(cyan + (
            "Эта программа — твой помощник для автоматической накрутки жизек, лайков и монеток в Котике Ботике.\n" +
            "Она экономит твое время и нервы: не нужно постоянно кликать вручную, ждать, перезагружать страницу.\n" +
            "Скрипт управляет браузером Firefox через selenium, имитирует нажатия и обновления, чтобы получить максимум пользы.\n" +
            f"Используются прокси, чтобы скрыть твой настоящий IP — это снижает риск блокировки (ну и 403).\n" +
            "Ты выбираешь, накручивать лайки или монетки, вводишь нужные параметры, и программа быстренько все накручивает. ^_^\n" +
            "В общем, это такой кото-бот, который помогает тебе в кото-игре :3\n") + reset)
        #print(": я украл стиль этот программы у типичных сносеров тг акков :3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:") #да ну его 
        print(magneta + "=======" + reset)
        print(cyan + "1. Назад\n2. Написать разработчику" + reset) 
        if input(magneta + "Выберай: " + reset) == "2":
            ы = input(magneta + "Что ты хочешщ сообщить разработчику?: " + reset)
            Ы = input(magneta + "Укажи свой юз в тг или почту(для обратной связи): " + reset)
            send_fedback(ы,Ы)

    elif choice == 9:
        if input(red + "Сбросить настройки? (y/n): " + reset):
            if input(red + "На сколько % ты уверен? (0-100): " + reset).startswith("100"):
                settings = {"links1": ["https://cybercatbot.com/cats/67ab782d1b8b88c53be06c67"], "links2": ["https://cybercatbot.ru/topUpNew?data=67ab780c1b8b88c53be06c41&catId=67ab782d1b8b88c53be06c67"],"proxy": False, "sleeps":{"likes":[[1,3],[1,3]],"moeny":[[1,3],[3,5]]}, "headless": False, "start_init": False ,"tg": {"connected": False,"id": None,"hash": None},"custom_ffp": False}
                hide_save_settings()
    elif choice == 10:
        menu()
    else:
        print(red + "не понял" + reset)


try:
    with open(sp+'/settings.json', 'r') as f:
        settings = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    default_settings = {
        "links1": ["https://cybercatbot.com/cats/67ab782d1b8b88c53be06c67"],
        "links2": ["https://cybercatbot.ru/topUpNew?data=67ab780c1b8b88c53be06c41&catId=67ab782d1b8b88c53be06c67"],
        "proxy": False,
        "sleeps": {
            "likes": [[1, 3], [1, 3]],
            "moeny": [[1, 3], [3, 5]]
        },
        "headless": False,
        "start_init": False,
        "tg": {
            "connected": False,
            "id": None,
            "hash": None
        },
        "custom_ffp": False
    }
    with open(sp + "/settings.json", "w", encoding="utf-8") as f:
        json.dump(default_settings, f, indent=4)


try:
    with open(sp+'/items.json', 'r') as f:
        settings = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    default_items = {
  "Для дома": [
    {"name":"Кустик в горшке", "price":3},
    {"name":"Когтеточка", "price":4},
    {"name":"Столик", "price":2},
    {"name":"Коврик", "price":2},
    {"name":"Лежанка", "price":1},
    {"name":"Фикус", "price":2},
    {"name":"Велосипед", "price":2},
    {"name":"Лестница на чердак", "price":2}
  ],
  "Цветы": [
    {"name":"Роза 🌹", "price":1},
    {"name":"Гортензия 💙", "price":1},
    {"name":"Ромашка 🤍", "price":1},
    {"name":"Подсолнух 🌻", "price":1}
  ],
  "Другое": [
    {"name":"Резиновая уточка 🐤", "price":2},
    {"name":"Кольцо соника", "price":1},
    {"name":"Белый шарик", "price":2}
  ],
  "Для сада":[
    {"name":"Зеленое дерево","price":2},
    {"name":"Розовое дерево","price":2}
  ],
  "Зд принтер": [
    {"name": "Жёлтый картридж", "price": 2},
    {"name": "Красный картридж", "price": 2},
    {"name": "3д принтер", "price": 2},
    {"name": "Зелёный картридж", "price": 2},
    {"name": "Синий картридж", "price": 2},
    {"name": "Фиолетовый картридж", "price": 2},
    {"name": "Табличка забор", "price": 2}
  ],
  "Мяу Технолоджис":[
    {"name": "Cхема телевизора", "price": 2},
    {"name": "Cхема пульта", "price": 2}
  ]
}
    with open(sp + "/items.json", "w", encoding="utf-8") as f:
        json.dump(default_items, f, indent=4)


def load_settings():
    global settings
    global nick    
    with open(sp+'/settings.json', 'r') as f:
        settings = json.load(f)
load_settings()
def save_settings():
    with open(sp+'/settings.json', 'w') as f:
        json.dump(settings, f, indent=4)
    print(f"{green}Настройки сохранены!{reset}")
def hide_save_settings():
    with open(sp+'/settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def configure_proxy(profile, proxy_type, address, port):
    profile.set_preference("network.proxy.type", 1)
    if proxy_type == "http":
        profile.set_preference("network.proxy.http", address)
        profile.set_preference("network.proxy.http_port", port)
    elif proxy_type == "https":
        profile.set_preference("network.proxy.ssl", address)
        profile.set_preference("network.proxy.ssl_port", port)
    elif proxy_type == "socks5":
        profile.set_preference("network.proxy.socks", address)
        profile.set_preference("network.proxy.socks_port", port)
        profile.set_preference("network.proxy.socks_version", 5)
        profile.set_preference("network.proxy.socks_remote_dns", True)
    else:
        raise ValueError("Неизвестный тип прокси")

    profile.update_preferences()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def gffp():
    import shutil
    # 1. Попробуем стандартные Program Files
    for pf in (os.environ.get('PROGRAMFILES'), os.environ.get('PROGRAMFILES(X86)')):
        if not pf:
            continue
        path = os.path.join(pf, r'Mozilla Firefox\firefox.exe')
        if os.path.isfile(path):
            ffp = path

    # 2. Попробуем PATH + App Paths
    path = shutil.which('firefox') or shutil.which('firefox.exe')
    if path:
        ffp =  path
    return ffp

def init():
    options = Options()
    import platform
    import shutil
    profile = FirefoxProfile()
    if platform.system() == "Linux":
            # Критически важные настройки для Linux
            profile.set_preference("browser.startup.homepage", "about:blank")
            profile.set_preference("startup.homepage_welcome_url", "about:blank")
            profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    
            # Отключаем все, что может мешать
            profile.set_preference("dom.push.enabled", False)
            profile.set_preference("geo.enabled", False)
            profile.set_preference("browser.tabs.remote.autostart", False)
            profile.set_preference("browser.tabs.remote.autostart.2", False)

            options.add_argument('-no-remote')
            options.add_argument('-new-instance')
            options.add_argument("--allow-hosts")
            options.add_argument("--allow-root")
    if settings["headless"]:
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
    options.set_preference("general.useragent.override", ua)
    profile.set_preference("http.response.timeout", 5)

    if settings["proxy"] == "free":
        proxy = requests.get("https://lol.alwaysdata.net/fp").text #либа не рработает в термуксе без 2 гигобайтных зависимостей, поэтому я поставил либибу на серв и все норм (возващает строку типа http://4.149.153.123:3128)
        proxy = urlparse(proxy)
        configure_proxy(profile, proxy.scheme, proxy.hostname, proxy.port)
    elif settings["proxy"] == "list":
        proxy = random.choice(settings.get("proxy_list", [""]))
        os.environ['http_proxy'] = proxy
        os.environ['https_proxy'] = proxy
        proxy = urlparse(proxy)
        configure_proxy(profile, proxy.scheme, proxy.hostname, proxy.port)
    else:
        pass # хз
    ffp = gffp()
    print(ffp)
    load_settings()
    try:
        if not settings["custom_ffp"]:
            options.binary_location = ffp
        #сторовский файрфокс оно находит само
    except:
        load_settings()
        settings["custom_ffp"] = True
        hide_save_settings()
    options.profile = profile


    try:
        service = Service(
        executable_path=sp+r"/browser/gecko",
        log_path=sp+'/geckodriver.log',  # Сохраняем логи драйвера
        service_args=['--log', 'debug']   # Включаем debug режим
    )
    
        # Добавим настройки для логирования Firefox
        options.set_preference("browser.dom.window.dump.enabled", True)
        options.set_preference("devtools.console.stdout.content", True)
        options.set_preference("devtools.console.stdout.chrome", True)
    
        # Сохраним логи браузера в файл
        options.set_preference("browser.console.loglevel", "all")
        driver = webdriver.Firefox(options=options,service=service) # хром гавно из за манифест в3
        # устонавливаем расширение ublock origin
        driver.install_addon(sp+'/browser/ublock_origin.xpi', temporary=True) #ненавижу рекламу
    except Exception as e:
        print(red + f"КРИТИЧЕСКАЯ ОШИБКА: {e}" + reset)
        if settings["custom_ffp"]:
            if input(magneta+"Возможно фвйрфокс поставлен через майкрософт сторе и чтото там. Короче если да напишете 'Y'").upper() == "Y":
                settings["custom_ffp"] = True
                hide_save_settings()
        else:
            if input(magneta+"Возможно отключение настройки сustom_ffp поможет. короче попробуйте (напишите  'Y')").upper() == "Y":
                settings["custom_ffp"] = False
                hide_save_settings() 
                    
        if not settings["headless"]:
            print(yellow + "Headless режим включен, перезапустите программу" + reset)
            settings["headless"] = True
            hide_save_settings()
            exit()
        else:
            print(yellow + "проверьте установку Firefox и его драйвера" + reset)
            print(yellow + "Если файрфокс установлен напишите в поддержку" + reset)
            if input(magneta + "Хотите отправить сообщение разработчику? (y/n): " + reset) == "y":
                send_fedback(input(magneta + "Пожалуйста подробно опишите устройвство и среду где запускается программа: " + reset),input(magneta + "Укажи свой юз в тг или почту(для обратной связи): " + reset))
                exit()
            else:
                exit()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)
    return driver

def start_init():
    print(magneta + "=== Первоначальная инициализация ===")
    import platform
    import sys
    import subprocess


    print(cyan + "ляляля")


    print(magneta + "=== 0. Создаем папку для всяких файликов ===")


    os.makedirs(sp, exist_ok=True)
    print(green + "Папка создана по пути: " + sp)


    print(magneta + "=== 1. Скачиваем гекодрайвер ===")
    oss = platform.system()
    a = platform.architecture()[0]
    
    if oss == 'Windows':
        oss = f"win{a[:-3]}"
    elif oss == 'Linux':
        oss = f"linux{a[:-3]}"
        if os.path.exists('/data/data/com.termux/'):
            oss = "android"
    elif 'android' in sys.platform:
        oss = "android"
    
    url = requests.get("https://gist.githubusercontent.com/ZILOGZ80000/4ef8ad0d48867d92ece3293b7fcf52ba/raw/5d1c7420d46b625fe7c418aec20bdfbb66c844b2/links.json").json()[oss.replace("64bit", "64").replace("32bit", "32")]
    try:
        open(sp+"/browser/gecko")
        print(green+"Гекодрайвер уже скачан")
    except FileNotFoundError:
        urllib.request.urlretrieve(url, sp + "/browser/gecko")  # pyright: ignore[reportAttributeAccessIssue] # хз че с вс коде
        print(green + "Гекодрайвер скачан!")
    os.chmod(sp + "/browser/gecko", 0o755)
    print(magneta + "=== 2. Скачиваем файрфокс ===")

    class SillyError(Exception): pass
    try:
        result = subprocess.run([gffp(), '--version'], capture_output=True, text=True)
        if not "/" in gffp():
            raise SillyError("гыг")
        print(green + "Файрфокс уже скачан :)")
    except:# FileNotFoundError:
        if oss == 'android' or oss.startswith("linux"):
            #urllib.request.urlretrieve("http://ftp.us.debian.org/debian/pool/main/f/firefox/firefox_145.0-1_arm64.deb","/data/data/com.termux/files/home/farmer-for-cat-bot/browser/firefox.deb") #type: ignore
            os.system("apt install firefox")
        else:
            a = a.replace("64bit", "64").replace("32bit", "32")
            urllib.request.urlretrieve(f"https://download.mozilla.org/?product=firefox-latest-ssl&os=win{a}&lang=ru", sp + "/browser/firefox_installer.exe") # pyright: ignore[reportAttributeAccessIssue]


            print(green + "Скачано, запускаем установку...")
            print(cyan + "Сейчас откроется устоновщик просто тыкай Далее/ОК")
            for _ in range(6):
                time.sleep(0.5)
                print("·", end="")
            os.startfile(sp+"/browser/firefox_installer.exe")
            input(magneta + "Нажми энтер когда установишь.")
    
    print(magneta + "=== 3. Скачиваем юблок ===")
    try:
        open(sp+"/browser/ublock_origin.xpi")
        print(green+"юблок уже скачан")
    except FileNotFoundError:
        urllib.request.urlretrieve("https://www.dropbox.com/scl/fi/upa8q9bmbqch7pl6rdt2h/ublock_origin.xpi?rlkey=e2r5ln911k8604pkurjfts5j5&st=7ldx5n0j&dl=1", sp + "/browser/ublock_origin.xpi")  # pyright: ignore[reportAttributeAccessIssue] # хз че с вс коде
        print(green + "юблок скачан!")

    print(magneta + "=== 4. Создаем чето там ===")
    if oss == 'android':
        open("/data/data/com.termux/files/usr/bin/kb", "w+").write("python ~/farmer-for-cat-bot/main.py")
        os.system("chmod 775 kb")
        print(green + "Запускай прогу командой 'kb'")
    elif oss.startswith("linux"):
        bashrc = os.path.join(os.path.expanduser('~'), '.bashrc')
        with open(bashrc, 'a') as f:
            f.write(f'\nalias kb="cd {sp} && python3 main.py"\n')
        os.system("source ~/.bashrc")
        print(green + "Запускай прогу командой 'kb'")
    else:
        print(green + "У тя винда, запускай ехешку напрямую :)")
    settings["start_init"] = True
    hide_save_settings()
    load_settings()
    if not settings["start_init"]:
        settings["start_init"] = True
        save_settings()
    print(magneta+f"=== Установка {green}успешна!{magneta} Переходим к самой проге ===")


def change_proxy(driver, new_proxy_url):
    driver.proxy = {
        'http': new_proxy_url,
        'https': new_proxy_url,
        'no_proxy': 'localhost,127.0.0.1' 
    }
    logger.print(f"=== Прокси изменен на изменен на {new_proxy_url}")
        
    








##########################################################################################################################################
#### ОСновной код ####
clear()
load_settings()

if not settings["start_init"]:
    start_init()
    settings["start_init"] = False

''' 
if logger.review() != "" and logger.review() != " " and logger.review() != None:
    print(magneta + "=== Найдены старые логи ===")
    print(cyan + "1. Оставить\n2. Cтереть\n3. Просмотреть")
    c = int(input(magneta + "Выбирай: "))
    if  c == 1:
        pass
    elif c == 2:
        logger.clear()
        print(green+ "Логи удалены!")
    elif c == 3:
        review()
    else:
        print("Ниче не понял, оставляю")
        time.sleep(0.5)
        clear()
''' #фиг с ним, неработает и бесит 

print(yellow+"Проверка сайтов...")
а = requests.get("https://cybercatbot.com/",headers={"User-Agent": ua})
print(green + "200 OK" if а.status_code == 200 else red + str(а.status_code))
а = requests.get("https://cybercatbot.ru/",headers={"User-Agent": ua})
print(green + "200 OK" if а.status_code == 200 else red + str(а.status_code))
time.sleep(0.5)

print(yellow + "Запуск браузера...")
driver = init()
print(green + "Браузер запущен!")
time.sleep(0.5)

print(yellow + "Проверка обновлений...")
vers = requests.get("https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/refs/heads/main/vers.json").json()
if vers["last"]["version"] != 1.2:
    print(red + "ВНИМАНИЕ!!!!!!!!!!!!!!!: Найдена новая версия")

    print(magneta+"Версия: " + cyan + str(vers["last"]["version"]))
    print(magneta+"Описание: " + cyan + vers["last"]["desc"])
    print(magneta+"Пост в тг (там инструкция по установке): " + cyan + vers["last"]["tg_post"])
    print(magneta+"Дата релиза: " + cyan + vers["last"]["date"])

    input("Нажмите энтер для продолжения")
elif requests.get("https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/refs/heads/main/items.json").text != open(sp+"/items.json",encoding="utf-8").read():
    print(yellow + "Обновление предметов...")
    with open("items.json","w",encoding="utf-8") as f:
        f.write(requests.get("https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/refs/heads/main/items.json").text)
        f.close()
    print(green+"Предметы обновлены!")
else:
    print(green+"Обновления не найдены!")
time.sleep(1)
clear()



def likes():

    global counts
    global settings
    counts = 0 # в минус уезжает иногда
    # спрашиваем настройки
    likes = int(input("лайков нужно накрутить(лучше не ровное например 395): "))
    url = input("ссылка на киса(или номер стандартной): ")
    # проверяем ссылку на киса
    if "https://" not in url and url != "" and not url.isdigit():
        print(red + "Ты норм не? (⁠=⁠｀⁠ェ⁠´⁠=⁠)" + reset)
        menu()
        return
    try:
        # проверяем ссылку на стандартную
        if url.isdigit():
            url = settings["links1"][int(url) - 1]
            logger.print(f"{magneta}=== Начинаем накрутку лайков ==={reset}")
            logger.print(f"Накручиваем на id:{url[-24:]}")
        driver.get(url)
    except Exception as e:
        print(f"{red}Ошибка при загрузке страницы: {e}{reset}")
        driver.quit()
        exit()
    for i in range(likes):
        try:
            # нажимаем Лайк
            like_btn = driver.find_element(By.XPATH, '//*[text()="Лайк"]')
            like_btn.click()
            counts += 1
            logger.print(f"{green}+1 лайк | {magneta}Всего: {counts} | {cyan}Осталось: {likes - counts}{reset} | :3")

            # если накрутили число заканчивающееся на 00 (например 500,1000,100 и тд)
            if str(counts)[-2:] == "00":
                logger.print(f"{blue}=== {counts} лайков! :3 ==={reset}")
            # ждем 1-3 секунды
            time.sleep(random.uniform(int(settings["sleeps"]["likes"][0][0]), int(settings["sleeps"]["likes"][0][1])))
            # перезагружаем страницу и удаляем все данные
            driver.delete_all_cookies()
            driver.execute_script("window.localStorage.clear();")
            driver.refresh()

            # ждем 3-5 секунды
            time.sleep(random.uniform(int(settings["sleeps"]["likes"][1][0]),int(settings["sleeps"]["likes"][1][1])))

        except Exception as e:

            logger.print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
            logger.print(f"{cyan}Пробуем снова через 5 секунд...{reset}")
            time.sleep(5)
            try:
                driver.refresh()
                time.sleep(3)
            except:
                logger.print(f"{red}Критическая ошибка, завершаем работу{reset}")
                break


    logger.print(f"{green}Готово! Накручено {counts} лайков! :3{reset}")
    menu()
# получилось: накручиваем лайки на кисика 
#:3

def moeny():
    global counts
    global settings
    counts = 0 # в минус уезжает иногда
    moeny = int(input(cyan + "Сколько нужно накрутить монеток: " + reset))
    url = input(cyan + "Ссылка на заработоть монетки(или номер стандартной): " + reset)
    if "https://" not in url and url != "" and not url.isdigit():
        print(red + "Ты норм не? (⁠=⁠｀⁠ェ⁠´⁠=⁠)" + reset)
        menu()
        return
    if url.isdigit():
        url = settings["links2"][int(url) - 1]
    if requests.get(url).status_code == 200:
        logger.print(f"{magneta}=== Начинаем накрутку монет ==={reset}")
        logger.print(f"id: {url[-24:]}")
        driver.get(url)
        time.sleep(1)
        driver.execute_script("window.stop();")

    else:
        logger.print(f"{red}Ошибка загрузки{reset}")
        return
    for i in range(moeny):
        try:
            # нажимаем Начать
            start_btn = driver.find_element(By.XPATH,'//*[text()="Начать"]')
            start_btn.click()
            # получаемтекст елемента с ксс селектром
            code = driver.find_element(By.CSS_SELECTOR,'.sc-hKgKIp.coIFTS').text
            print(code)

            # разбивваем строку на список ("лол" ->["л","о","л"])
            code = list(code)
            for i in code:
                #cod = driver.find_element(By.XPATH,f"//*[text()='{i}']")
                if i == "😻":
                    driver.find_element(By.XPATH,"//div[text()='😻']").click()
                    print("😻 тыкаем на кота")
                else:
                    driver.find_element(By.XPATH,"//div[text()='🐭']").click()
                    print("🐭 Тыкаем на мыщку")
            time.sleep(random.uniform(int(settings["sleeps"]["moeny"][0][0]),int(settings["sleeps"]["moeny"][0][1])))
            driver.save_screenshot("lol.png")
            try:
                driver.find_element(By.XPATH,"//*[text()='Получить монетку']").click()
            except:
                buttons = driver.find_elements(By.XPATH, "//*[text()='Вернуться']")
                if buttons:
                    pass #хз, кнопка то пойвится то пропадет, оч хороший способ сломать накрутку 
                else:
                    print(red + "Кнопка 'Получить монетку'/'Вернуться' не найдена")

                    driver.refresh()
                    continue



            #finnal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Получить монетку']")))
            #finnal.click()
            time.sleep(0.5)
            driver.delete_all_cookies()
            driver.execute_script("window.localStorage.clear();")
            driver.refresh()

            counts += 1
            logger.print(f"{green}+1 монетка | {magneta}Всего: {counts} | {cyan}Oсталось: {moeny - counts}{reset} | :3")
            if str(counts)[-2:] == "00":
                logger.print(f"{blue}=== {counts} монеток! :3 ==={reset}")

        except Exception as e:
            logger.print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
            logger.print(f"{cyan}Пробуем снова через 5 секунд...{reset}")
            time.sleep(5)
            try:
                driver.refresh()
                time.sleep(3)
            except:
                logger.print(f"{red}Критическая ошибка, завершаем работу{reset}")
                break
    logger.print(green + f"Готово! Накручено {counts} монеток! :3" + reset)
    menu()















def coin():
    driver.refresh()
    # нажимаем Начать
    start_btn = driver.find_element(By.XPATH,'//*[text()="Начать"]')
    start_btn.click()
    # получаемтекст елемента с ксс селектром
    code = driver.find_element(By.CSS_SELECTOR,'.sc-hKgKIp.coIFTS').text          

    # разбивваем строку на список ("лол" ->["л","о","л"])
    code = list(code)
    for i in code:
        #cod = driver.find_element(By.XPATH,f"//*[text()='{i}']")
        if i == "😻":
            driver.find_element(By.XPATH,"//div[text()='😻']").click()
        else:
            driver.find_element(By.XPATH,"//div[text()='🐭']").click()
        time.sleep(3)

        try:
            driver.find_element(By.XPATH,"//*[text()='Получить монетку']").click()
            logger.print(green+"+1 Монетка")
        except:
            buttons = driver.find_elements(By.XPATH, "//*[text()='Вернуться']")
            logger.print(green+"+1 Монетка")
            if buttons:
                pass #хз, кнопка то пойвится то пропадет, оч хороший способ сломать накрутку 
            else:
                logger.print(red + "Кнопка 'Получить монетку'/'Вернуться' не найдена")
                driver.refresh()
                continue

def lifes():
    load_settings()
    if not settings["tg"]["connected"]:
        print(red+"Для этой функции необходимо подключить тг аккаунт. " + cyan + "4. Настройки -> 7. Подключить/управлять тг акком -> 2. Подключить")
        menu()
    print(cyan + "1. Просто накрутить жизьки\n2. Накручивать по 2 монетки а затем жизьку")
    m = input(magneta + "Выбирай: ")
    if m == "2":
        m = True
        url = input(cyan + "Ссылка на заработоть монетки(или номер стандартной): " + reset)
        if "https://" not in url and url != "" and not url.isdigit():
            print(red + "Ты норм не? (⁠=⁠｀⁠ェ⁠´⁠=⁠)" + reset)
            menu()
            return
        if url.isdigit():
            url = settings["links2"][int(url) - 1]
        if requests.get(url).status_code == 200:
            driver.get(url)
            time.sleep(0.5)
            driver.execute_script("window.stop();")
        else:
            logger.print(f"{red}Ошибка загрузки{reset}")
            return
    else:
        m = False
    u = input(magneta + "Юзернейм группы или айди с котом (энтер если не в группе): "+reset)
    if u == "":
        u = "Kisik_Kotik_Bot"
    try:
        u = int(u)  # Попытка преобразовать ввод в число
    except ValueError:
        pass  # Если преобразование не удалось, оставляем строку

    c = int(input(magneta+ "Сколько жизней нужно накрутить: "))
    logger.print(magneta + "=== Начинаем накрутку жизьек ===")
    counts = 0
    try:
        with TelegramClient('session', int(settings["tg"]["id"]), settings["tg"]["hash"],device_model="Накрутка для кб :3") as client:
            for i in range(c):
                if m:
                    for i in range(2):
                        try:
                            coin()
                            
                        except Exception as e:
                            logger.print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
                            logger.print(f"{cyan}Пробуем снова через 5 секунд...{reset}")
                            time.sleep(5)
                            try:
                                driver.refresh()
                                time.sleep(3)
                            except:
                                logger.print(f"{red}Критическая ошибка, завершаем работу{reset}")
                                break
                        
                msg = client.send_message(u, "👛")
                time.sleep(0.5)  # даём время на реакцию бота

                # получить последнее сообщение от бота
                last_msg = client.get_messages(u, limit=1)[0]

                last_msg.click(text="Купить жизьку ❤️ [2 🟡]")

                if client.get_messages(u, limit=1)[0].raw_text.endswith("получил жизьку 😍"):
                    counts += 1
                    logger.print(f"{green}+1 Жизька | {magneta}Всего: {counts} | {cyan}Oсталось: {c - counts}{reset} | :3")
                    if str(counts)[-2:] == "00":
                        logger.print(f"{blue}=== {counts} жизек! :3 ==={reset}")


    except Exception as e:
        logger.print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
    menu()


def click_wait(peer, text, client, timeout=5):
    # Получаем последнее сообщение
    msg = client.get_messages(peer, limit=1)[0]

    if msg.buttons:
        for row in msg.buttons:
            for button in row:
                #print(button.text + (" = " if button.text == text else " ≠ ") + text)
                if button.text == text:
                    button.click()
                    time.sleep(2)  # Ждём новое сообщение
                    return client.get_messages(peer, limit=1)[0]  

    logger.print(f"{red}Кнопка '{text}' не найдена{reset}")
    return None

def items():
    load_settings() 
    with open(sp+'/items.json', 'r',encoding='utf-8') as f:
        items = json.load(f)

    if not settings["tg"]["connected"]:
        print(red+"Для этой функции необходимо подключить тг аккаунт. " + cyan + "4. Настройки -> 7. Подключить/управлять тг акком -> 2. Подключить")
        menu()
    print(cyan + "1. Просто накрутить что то из магазина\n2. Накручивать по цене предмета монеток а затем предмет")
    m = input(magneta + "Выбирай: ")
    if m == "2":
        m = True
        url = input(cyan + "Ссылка на заработоть монетки(или номер стандартной): " + reset)
        if "https://" not in url and url != "" and not url.isdigit():
            print(red + "Ты норм не? (⁠=⁠｀⁠ェ⁠´⁠=⁠)" + reset)
            menu()
            return
        if url.isdigit():
            url = settings["links2"][int(url) - 1]
        if requests.get(url).status_code == 200:
            driver.get(url)
            time.sleep(0.5)
            driver.execute_script("window.stop();")
        else:
            logger.print(f"{red}Ошибка загрузки{reset}")
            return
    else:
        m = False
    u = input(magneta + "Юзернейм группы или айди с котом (энтер если не в группе): "+reset)
    if u == "":
        u = "Kisik_Kotik_Bot"
    try:
        u = int(u)  # Попытка преобразовать ввод в число
    except ValueError:
        pass  # Если преобразование не удалось, оставляем строку
    for ii, i in enumerate(items.keys()):
        print(cyan + str(ii) + ". " + str(i))
    category = int(input(magneta + "Выберите категорию: "))
    category_name = list(items.keys())[category]

    # Список предметов в выбранной категории
    category_items = items[category_name]

    # Выводим  предметы
    for idx, item in enumerate(category_items):
        print(cyan + f"{idx}. {item['name']} (Цена: {item['price']})")

    # Выбор предмета
    item_index = int(input(magneta+"Выберите: "))

    # Получаем выбранный предмет
    item = category_items[item_index]
    c = int(input(magneta+ "Сколько предметов нужно накрутить: "))
    logger.print(magneta + f'=== Начинаем накрутку "{item["name"]}" ==='+reset)
    counts = 0
    try:
        with TelegramClient('session', int(settings["tg"]["id"]), settings["tg"]["hash"],device_model="Накрутка для кб :3") as client:
            for i in range(c):
                if m:
                    for i in range(item["price"]):
                        try:
                            coin()
                            
                        except Exception as e:
                            logger.print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
                            logger.print(f"{cyan}Пробуем снова через 5 секунд...{reset}")
                            time.sleep(5)
                            try:
                                driver.refresh()
                                time.sleep(3)
                            except:
                                logger.print(f"{red}Критическая ошибка, завершаем работу{reset}")
                                break
                if not client.get_messages(u, limit=1)[0].raw_text.startswith("Это твой кошелёк, тут лежат монетки и можно что-нибудь купить или заработать"):
                    msg = client.send_message(u, "👛")
                time.sleep(1)
                msg = click_wait(u, "Предметы 🎮",client)
                print(msg.raw_text) # type: ignore
                
                msg = click_wait(u, category_name,client)
                print(msg.raw_text) # type: ignore
                msg = click_wait(u, item["name"],client)
                print(msg.raw_text) # type: ignore
                msg = click_wait(u, "Да",client)
                print(msg.raw_text) # type: ignore
                
                time.sleep(2)
                if client.get_messages(u, limit=1)[0].raw_text.startswith("Ура, мы купили"):
                    counts += 1
                    logger.print(f"{green}+1 Предмет | {magneta}Всего: {counts} | {cyan}Oсталось: {c - counts}{reset} | :3")
                    if str(counts)[-2:] == "00":
                        logger.print(f"{blue}=== {counts} предметов! :3 ==={reset}")

    except Exception as e:
        logger.print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
    logger.print(green + f"Готово! Накручено {counts} предметов! :3" + reset)
    menu()


    


        


#def review():
#    print(magneta + "=== Просмотор прошлой работы ===")
#    print(logger.review)
#    input(magneta + "Нажмите Enter для для выхода в меню")
#    menu()

if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print(red+"кхе кхе:"+e) #type: ignore
        menu() 
#os.system("pause")
