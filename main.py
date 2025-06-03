from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random
import requests

#### Создание переменных ####
counts = 0

# цвета
green = "\033[32m"
blue = "\033[34m"
red = "\033[31m"
magneta = "\033[35m"
cyan = "\033[36m"
reset = "\033[0m"
#### ОСновной код ####
а = requests.get("https://cybercatbot.com/")
print(а.status_code)
#exit() # временно
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options) 
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
def likes():
    global counts
    
    # спрашиваем настройки
    likes = int(input("лайков нужно накрутить(лучше не ровное например 395): "))
    url = input("ссылка на киса(энтер чтобы накрутить на котю(разрабочик)): ")

    try:
        if url == "": #
            driver.get("https://cybercatbot.com/cats/67ab782d1b8b88c53be06c67")
            print(" Спасибо 🥰")
        else:
            driver.get("https://cybercatbot.com/cats/67c85a3c1b8b88c53bead266") 
            print(f" Накручиваем на id:{url[-24:]}")
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
            time.sleep(random.randint(1, 3))
            # перезагружаем страницу и удаляем все данные
            driver.delete_all_cookies()
            driver.execute_script("window.localStorage.clear();")
            driver.refresh()
        
            # ждем 3-5 секунды
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


        # закрываем браузер
        driver.quit()
    print(f"{green}Готово! Накручено {counts} лайков! :3{reset}")
# получилось: накручиваем лайки на киска 
#:3

def moeny():
    global counts
    moeny = int(input(cyan + "Сколько нужно накрутить монеток: " + reset))
    url = input(cyan + "ссылка на заработоть монетки(cybercatbot.com/topup?data=...): " + reset)
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
            # получаемтекст елемента с ксс селектром .code
            code = driver.find_element(By.CSS_SELECTOR,'.sc-hKgKIp.coIFTS').text
            print(code)

            # разбивваем строку на список ("лол" ->["л","о","л"])
            code = list(code)
            for i in code:
                print(i)
                cod = driver.find_element(By.XPATH,f"//*[text()='{i}']")
                cod.click()
            time.sleep(5)
            #driver.find_element(By.XPATH,"//*[text()='Получить монетку']").click
            finnal = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Получить монетку']")))
            time.sleep(3)
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


if __name__ == "__main__":
    # безопасная проверка пароля(не хранит пароль)
    password = input("Введите пароль: ")
    # хешируем пароль
    import hashlib
    password = hashlib.sha256(password.encode()).hexdigest()
    # проверяем пароль(не захешированный 47755)
    if password == password: #временно
        print(f"{green}Пароль верный!{reset}")
    else:
        print(f"{red}Пароль неверный!{reset}")
        exit()
    #print("типа арт") # временно
    print(magneta + r"""
  ____    _  _____   ____   ___   ___  ____ _____
 / ___|  / \|_   _| | __ ) / _ \ / _ \/ ___|_   _|
| |     / _ \ | |   |  _ \| | | | | | \___ \ | |
| |___ / ___ \| |   | |_) | |_| | |_| |___) || |
 \____/_/   \_\_|   |____/ \___/ \___/|____/ |_|


          /\_/\
     ____/ o o \
   /~____  =ø= /
  (______)__m_m)
""" + reset)

    print(cyan + "by ZILOG Z80 (@humans_i_am_not_human)" * 3 + reset)
    print(magneta + "=== Меню ===" + reset)
    print(cyan + "1. Накрутить лайки\n2. Накрутить монетки" + reset)
    choice = int(input(magneta + "Выберите действие: " + reset))
    if choice == 1:
        likes()
    elif choice == 2:
        moeny()
    else:
        print(red + "не понял" + reset)
    

    