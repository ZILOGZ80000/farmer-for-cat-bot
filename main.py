from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import random
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

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

# спрашиваем настройки
likes = int(input("лайков нужно накрутить(лучше не ровное например 395): "))
url = input("ссылка на киса(энтер чтобы накрутить на котю(разрабочик)): ")
if url == "":
    driver.get("https://cybercatbot.com/cats/67ab782d1b8b88c53be06c67")
    print(" Спасибо 🥰")
else:
    driver.get(url)
    print(f" Накручиваем на id:{url[-24:]}")

for i in range(likes):
    # нажимаем Лайк
    like_btn = driver.find_element(By.XPATH, '//*[text()="Лайк"]')
    like_btn.click()
    counts += 1
    print(f"{green}+1 лайк | {magneta}Всего: {counts} | {cyan}Осталось: {likes - counts}{reset} | :3") #не работает. причина: хз(наверно не правильно расставлены цвет/ресет
    #бляу я тупой правильно будет так: 
    # если накрутили число заканчивающееся на 00 (например 500,1000,100 и тд)
    if str(counts)[-2:] == 00:
        print(f"{blue}=== {counts} лайков! :3 ==={reset}")
    # ждем 1-3 секунды
    time.sleep(random.randint(1, 3))
    # ждем 1-3 секунды
    time.sleep(random.randint(1, 3))
    # перезагружаем страницу и удаляем все данные
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.refresh()
    # ждем 3-5 секунды
    time.sleep(random.randint(3, 5))


# получилось: накручиваем лайки на киска 
#:3

