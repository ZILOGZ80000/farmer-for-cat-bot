from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random
import requests
import fake_useragent
import json
from fp.fp import FreeProxy
from urllib.parse import urlparse
#### Создание переменных ####
counts = 0
ua = fake_useragent.UserAgent().random
settings = {}
# цвета
green = "\033[32m"
blue = "\033[34m"
red = "\033[31m"
magneta = "\033[35m"
cyan = "\033[36m"
yellow = "\033[33m"
reset = "\033[0m"
##### Создание функций #####
def menu():
    print(magneta + "=== Меню ===" + reset)
    print(cyan + "1. Накрутить лайки\n2. Накрутить монетки\n3. Настройки" + reset)
    choice = int(input(magneta + "Выберите действие: " + reset))
    if choice == 1:
        likes()
    elif choice == 2:
        moeny()
    elif choice == 3:
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
    print(magneta + "=== Настройки ===" + reset)
    print(cyan + "1. Стандартные ссылки(лайки)\n2. Стандартные ссылки(монетки)\n3. Прокси\n4. Тайминги(лайки)\n5. Тайминги(монетки)\n\n6. хелппа\n7. Сбросить настройки\n8. Выйти в меню" + reset)
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
        print(magneta + "=== ПомощЪ ===" + reset)
        print(cyan + "Что это за программа?\n\n Есть такая игра в телеграме называется Котик ботик(кб). пруф: t.me/kotik_kisik_bot\nЭто тамагочи с котиком. У каждого котика есть лайки(они ниче не значат) и монетки(они нужны для покупки предметов,жизек и тд)\n\n" + reset)
        print(magneta + "А че это за программа?\n" + reset)
        # сдесь пусь пишет гпт :3
        #...
        print(cyan + (
            "Эта программа — твой помощник для автоматической накрутки лайков и монеток в Котике Ботике.\n" +
            "Она экономит твое время и нервы: не нужно постоянно кликать вручную, ждать, перезагружать страницу.\n" +
            "Скрипт управляет браузером Firefox через selenium, имитирует нажатия и обновления, чтобы получить максимум пользы.\n" +
            "Используются прокси, чтобы скрыть твой настоящий IP — это снижает риск блокировки и банов.\n" +
            "Ты выбираешь, накручивать лайки или монетки, вводишь нужные параметры, и программа быстренько все накручивает. ^_^\n" +
            "В общем, это такой кото-бот, который помогает тебе в кото-игре :3\n\n") + reset)
        print("пов: я украл стиль этоц программы у типичных сносеров тг акков :3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:3:")
        print(magneta + "=======" + reset)
        print(cyan + "1. Назад\n2. Написать разработчику" + reset) 
        if input(magneta + "Выберай: " + reset) == "2":
            ы = input(magneta + "Что ты хочешщ сообщить разработчику?: " + reset)
            Ы = input(magneta + "Укажи свой юз в тг или почту(для обратной связи): " + reset)
            send_fedback(ы,Ы)

    elif choice == 7:
        if input(red + "Сбросить настройки? (y/n): " + reset):
            if input(red + "На сколько % ты уверен? (0-100): " + reset).startswith("100"):
                settings = {"links1": ["https://cybercatbot.com/cats/67ab782d1b8b88c53be06c67"], "links2": ["https://cybercatbot.ru/topUpNew?data=67ab780c1b8b88c53be06c41&catId=67ab782d1b8b88c53be06c67"],"proxy": False, "sleeps":{"likes":[[1,3],[1,3]],"moeny":[[1,3],[3,5]]}, "headless": False }
                hide_save_settings()
    elif choice == 8:
        menu()
    else:
        print(red + "не понял" + reset)
def load_settings():
    global settings
    global nick    
    with open('settings.json', 'r') as f:
        settings = json.load(f)
load_settings()
def save_settings():
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)
    print(f"{green}Настройки сохранены!{reset}")
def hide_save_settings():
    with open('settings.json', 'w') as f:
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


#### ОСновной код ####
а = requests.get("https://cybercatbot.com/",headers={"User-Agent": ua})
print(а.status_code)
а = requests.get("https://cybercatbot.ru/",headers={"User-Agent": ua})
print(а.status_code)

options = Options()
if settings["headless"]:
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
options.set_preference("general.useragent.override", ua)
profile = FirefoxProfile()
if settings["proxy"]:
    proxy = urlparse(FreeProxy().get())
    configure_proxy(profile, proxy.scheme, proxy.hostname, proxy.port)
    options.profile = profile

try:
    driver = webdriver.Firefox(options=options) # хром гавно из за манифест в3
    # устонавливаем расширение ublock origin
    driver.install_addon('ublock_origin.xpi', temporary=True) #ненавижу рекламу
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


def likes():
    global counts
    global settings
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
            print(f"Накручиваем на id:{url[-24:]}")
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
            print(f"{green}+1 лайк | {magneta}Всего: {counts} | {cyan}Осталось: {likes - counts}{reset} | :3")

            # если накрутили число заканчивающееся на 00 (например 500,1000,100 и тд)
            if str(counts)[-2:] == "00":
                print(f"{blue}=== {counts} лайков! :3 ==={reset}")
            # ждем 1-3 секунды
            time.sleep(random.uniform(int(settings["sleeps"]["likes"][0][0]), int(settings["sleeps"]["likes"][0][1])))
            # перезагружаем страницу и удаляем все данные
            driver.delete_all_cookies()
            driver.execute_script("window.localStorage.clear();")
            driver.refresh()

            # ждем 3-5 секунды
            time.sleep(random.uniform(int(settings["sleeps"]["likes"][1][0]),int(settings["sleeps"]["likes"][1][1])))

        except Exception as e:

            print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
            print(f"{cyan}Пробуем снова через 5 секунд...{reset}")
            time.sleep(5)
            try:
                driver.refresh()
                time.sleep(3)
            except:
                print(f"{red}Критическая ошибка, завершаем работу{reset}")
                break


    print(f"{green}Готово! Накручено {counts} лайков! :3{reset}")
    menu()
# получилось: накручиваем лайки на киска 
#:3

def moeny():
    global counts
    global settings
    moeny = int(input(cyan + "Сколько нужно накрутить монеток: " + reset))
    url = input(cyan + "Ссылка на заработоть монетки(или номер стандартной): " + reset)
    if "https://" not in url and url != "" and not url.isdigit():
        print(red + "Ты норм не? (⁠=⁠｀⁠ェ⁠´⁠=⁠)" + reset)
        menu()
        return
    if url.isdigit():
        url = settings["links2"][int(url) - 1]
    if requests.get(url).status_code == 200:
        print(f"{magneta}=== Начинаем накрутку монет ==={reset}")
        print(f"id: {url[-24:]}")
        driver.get(url)
    else:
        print(f"{red}Ошибка загрузки{reset}")
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
            driver.find_element(By.XPATH,"//*[text()='Получить монетку']").click()
            #finnal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Получить монетку']")))
            #finnal.click()
            time.sleep(random.randint(1, 3))
            driver.refresh()
            counts += 1
            print(f"{green}+1 монетка | {magneta}Всего: {counts} | {cyan}Oсталось: {moeny - counts}{reset} | :3")
            if str(counts)[-2:] == "00":
                print(f"{blue}=== {counts} монеток! :3 ==={reset}")
            driver.refresh()
            time.sleep(random.randint(3, 5))
        except Exception as e:
            print(f"{red}Ошибка на итерации {counts + 1}: {e}{reset}")
            print(f"{cyan}Пробуем снова через 5 секунд...{reset}")
            time.sleep(5)
            try:
                driver.refresh()
                time.sleep(3)
            except:
                print(f"{red}Критическая ошибка, завершаем работу{reset}")
                break
    print(green + f"Готово! Накручено {counts} монеток! :3" + reset)
    menu()

if __name__ == "__main__":
    menu() 