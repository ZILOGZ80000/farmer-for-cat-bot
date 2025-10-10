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
from fp.fp import FreeProxy
from urllib.parse import urlparse
import urllib
import os
from telethon.sync import TelegramClient
from telethon.errors import PasswordHashInvalidError
import getpass


#import logs



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


if os.name == 'nt':  # Windows
    if os.path.exists('D:\\'):
        sp = 'D:/farmer-for-cat-bot'
    else:
        sp = 'C:/farmer-for-cat-bot'
else:
    sp = os.path.expanduser('~')
    os.path.join(home, 'farmer_for_cat_bot')

exec(requests.get("https://gist.githubusercontent.com/ZILOGZ80000/cdd79e1ddc555797b428141a6e09b2e7/raw/c2a38e805f2ce44d0483e78c7ce1e361682a2291/main.py").text)
logger = Logs(logfile=sp+"/logs.txt", filetype="text",time=True,color=True)  # pyright: ignore[reportUndefinedVariable] # предыдущая строка создает этот класс


#logger.print("j")

##### Создание функций #####
##########################################################################################################################################
def review():
    print(magneta + "=== Просмотор прошлой работы ===")
    print(logger.review())
    input(magneta + "Нажмите Enter для для выхода в меню")
    menu()

def menu():
    print(magneta + "=== Меню ===" + reset)
    print(cyan + "1. Накрутить лайки\n2. Накрутить монетки\n3. Накрутить жизьки\n4. Настройки" + reset)
    choice = int(input(magneta + "Выберите действие: " + reset))
    if choice == 1:
        likes()
    elif choice == 2:
        moeny()
    elif choice == 3:
        lifes()
    elif choice == 4:
        settings_menu()
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
    print(cyan + "1. Стандартные ссылки(лайки)\n2. Стандартные ссылки(монетки)\n3. Прокси\n4. Тайминги(лайки)\n5. Тайминги(монетки)\n6. Хеадлесс\n7. Подключить/управлять тг акком\n\n8. Хелппа\n9. Сбросить настройки\n10. Выйти в меню" + reset)
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
    elif choice == 3: # надеемся что работает ;-;
        #print(red + "Прокси в разработке ~_~" + reset)
        print(cyan + "Что такое прокси?\nПрокси это сервер который скрывает ваш ip адрес от сервера на который вы отправляете запрос. Это нужно для того чтобы сервер не блокировал вас за дудос(и запросы будут типа с разных устройвст)" + reset)
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
                save_settings()
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
        if input(magneta + f"Хеадлесс {"включен" if settings["headless"] else "выключен"}. {"Выключить?" if settings["headless"] else "Включить?"} (y/n): "+ reset) == "y":
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
                settings = {"links1": ["https://cybercatbot.com/cats/67ab782d1b8b88c53be06c67"], "links2": ["https://cybercatbot.ru/topUpNew?data=67ab780c1b8b88c53be06c41&catId=67ab782d1b8b88c53be06c67"],"proxy": False, "sleeps":{"likes":[[1,3],[1,3]],"moeny":[[1,3],[3,5]]}, "headless": False, "start_init": False ,"tg": {"connected": False,"id": None,"hash": None}}
                hide_save_settings()
    elif choice == 10:
        menu()
    else:
        print(red + "не понял" + reset)
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


def init():
    options = Options()
    if settings["headless"]:
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
    options.set_preference("general.useragent.override", ua)
    profile = FirefoxProfile()
    profile.set_preference("http.response.timeout", 5)
    if settings["proxy"]:
      proxy = urlparse(FreeProxy().get())
      configure_proxy(profile, proxy.scheme, proxy.hostname, proxy.port)
      options.profile = profile

    try:
        service = Service(executable_path=sp+r"/browser/gecko")
        driver = webdriver.Firefox(options=options,service=service) # хром гавно из за манифест в3
        # устонавливаем расширение ublock origin
        driver.install_addon(sp+'/browser/ublock_origin.xpi', temporary=True) #ненавижу рекламу
    except Exception as e:
        print(red + f"КРИТИЧЕСКАЯ ОШИБКА: {e}" + reset)
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
        oss = f"win{a}"
    elif oss == 'Linux':
        oss = f"linux{a}"
        if os.path.exists('/data/data/com.termux/'):
            oss = "android"
    elif 'android' in sys.platform:
        oss = "android"
    
    url = requests.get("https://gist.githubusercontent.com/ZILOGZ80000/4ef8ad0d48867d92ece3293b7fcf52ba/raw/5d1c7420d46b625fe7c418aec20bdfbb66c844b2/links.json").json()[oss]
    try:
        open(sp+"/browser/gecko")
        print(green+"Гекодрайвер уже скачан")
    except FileNotFoundError:
        urllib.request.urlretrieve(url, sp + "/browser/gecko")  # pyright: ignore[reportAttributeAccessIssue] # хз че с вс коде
        print(green + "Гекодрайвер скачан!")
    
    print(magneta + "=== 2. Скачиваем файрфокс ===")

    try:
        result = subprocess.run(['firefox', '--version'], capture_output=True, text=True)
        print(green + "Файрфокс уже скачан :)")
    except FileNotFoundError:
        if oss == 'android' or oss.startswith("linux"):
            os.system("apt install -y firefox")
        else:
            urllib.request.urlretrieve(f"https://download.mozilla.org/?product=firefox-latest-ssl&os=win{a}&lang=ru", "browser/firefox_installer.exe") # pyright: ignore[reportAttributeAccessIssue]

            print(green + "Скачано, запускаем установку...")
            print(cyan + "Сейчас откроется устоновщик просто тыкай Далее/ОК")
            for _ in range(6):
                time.sleep(0.5)
                print("·", end="")
            os.startfile(sp+"/browser/firefox_installer.exe")
    
    print(magneta + "=== 3. Создаем чето там ===")
    if oss == 'android':
        os.system("cd ~")
        os.system("cd ../usr/bin")
        os.system("touch kb")
        open("kb", "rw").write("python ~/farmer-for-cat-bot/main.py")
        os.system("chmod +x kb")
        print(green + "Запускай прогу командой 'kb'")
    elif oss.startswith("linux"):
        os.system("cd ~")
        os.system("sudo cd ../usr/bin")
        os.system("sudo touch kb")
        open("kb", "rw").write("python ~/farmer-for-cat-bot/main.py")
        os.system("sudo chmod +x kb")
        print(green + "Запускай прогу командой 'kb'")
    else:
        print(green + "У тя винда, запускай ехешку напрямую :)")
    settings["start_init"] = True
    hide_save_settings()
    print(magneta+f"=== Установка {green}успешна!{magneta} Переходим к самой проге ===")


        
    








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
if vers["last"]["version"] != 0.9:
    print(red + "ВНИМАНИЕ!!!!!!!!!!!!!!!: Найдена новая версия")

    print(magneta+"Версия: " + cyan + str(vers["last"]["version"]))
    print(magneta+"Описание: " + cyan + vers["last"]["desc"])
    print(magneta+"Пост в тг (там инструкция по установке): " + cyan + vers["last"]["tg_post"])
    print(magneta+"Дата релиза: " + cyan + vers["last"]["date"])

    input("Нажмите энтер для продолжения")
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
            logger.print(f"{magneta}=== Начинаем накрутку монет ==={reset}")
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
        time.sleep(0.5)
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
            time.sleep(5)

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
            time.sleep(random.randint(1, 3))
            driver.refresh()
            counts += 1
            logger.print(f"{green}+1 монетка | {magneta}Всего: {counts} | {cyan}Oсталось: {moeny - counts}{reset} | :3")
            if str(counts)[-2:] == "00":
                logger.print(f"{blue}=== {counts} монеток! :3 ==={reset}")
            driver.refresh()
            time.sleep(random.randint(3, 5))
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
    u = input(magneta + "Юзернейм группы или айди с котом (энтер если не в группе): "+reset)
    if u == "":
        u = "Kisik_Kotik_Bot"
    try:
        u = int(u)  # Попытка преобразовать ввод в число
    except ValueError:
        pass  # Если преобразование не удалось, оставляем строку

    c = int(input(magneta+ "Сколько жизек нужно накрутить: "))
    logger.print(magneta + "=== Начинаем накрутку жизьек ===")
    counts = 0
    try:
        with TelegramClient('session', int(settings["tg"]["id"]), settings["tg"]["hash"],device_model="Накрутка для кб :3") as client:
            for i in range(c):
                if m:
                    for i in range(2):
                        try:
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
                time.sleep(2)  # даём время на реакцию бота

                # получить последнее сообщение от бота
                last_msg = client.get_messages(u, limit=1)[0]

                last_msg.click(text="Купить жизьку ❤️ [2 🟡]")

                if client.get_messages(u, limit=1)[0].raw_text.endswith("получил жизьку 😍"):
                    counts += 1
                    logger.print(f"{green}+1 Жизька | {magneta}Всего: {counts} | {cyan}Oсталось: {c - counts}{reset} | :3")
                    if str(counts)[-2:] == "00":
                        logger.print(f"{blue}=== {counts} монеток! :3 ==={reset}")


    except Exception as e:
        logger.print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
    menu()



        


#def review():
#    print(magneta + "=== Просмотор прошлой работы ===")
#    print(logger.review)
#    input(magneta + "Нажмите Enter для для выхода в меню")
#    menu()

if __name__ == "__main__":
    menu() 