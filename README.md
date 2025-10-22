### <center>⬇⬇⬇ русская версия чуть чуть ниже ⬇⬇⬇

# === English ===
# farmer-for-cat-bot 

![Version 1.0](https://gist.githubusercontent.com/ZILOGZ80000/4ef8ad0d48867d92ece3293b7fcf52ba/raw/f18967f338fccb9873e6eba6c686bd4f84316c51/version.svg) <!-- Original badge host may not work properly -->

# === English ===

## Description  
A Python tool for automated farming of hearts, likes, and in-game coins for [Cat Bot](t.me/Kisik_Kotik_Bot).  
Uses Selenium with Firefox to simulate human-like interactions.

## Features  
⦁ **Like Farming:** Automates likes for cats via specified links.  
⦁ **Coin Mining:** Plays mini-games to accumulate coins.  
⦁ **Heart Cheating:** Manages Telegram accounts to interact with the bot. 
⦁ **Items Cheating:** Manages Telegram accounts to interact with the bot.  
⦁ **Settings Persistence:** Stores default links and parameters in `settings.json`.  
⦁ **Proxy Support:** Uses free proxies for anonymity and bypassing limits.  
⦁ **Humanized Timing:** Randomized delays to avoid detection.  
⦁ **Headless Mode:** Runs browser in background (no GUI).  
⦁ **AdBlock Integration:** Auto-installs uBlock Origin.  
⦁ **Update Notifications:** Checks `vers.json` for new versions.

## Requirements  
⦁ Python 3.x  
⦁ Firefox & Geckodriver (auto-installed during setup)  

## Installation

### Android  

1. **Install Termux:**  
   Download the full version [here](https://f-droid.org/repo/com.termux_1002.apk) (*DO NOT use Google Play*).  

2. **Run Installer:**  
   Paste this command in Termux:  
   ```bash
   curl https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/main/executable_files/termux.sh | bash
   ```  
   The script will install Python, dependencies, Firefox/Geckodriver, and run initial setup.  
   Launch anytime with: `kb`

### Linux  
Run this command in a terminal:  
```bash
curl https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/main/executable_files/linux.sh | bash
```  
Launch after installation with: `kb`

### Windows  
1. Download the executable:  
   [windows.exe](https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/main/executable_files/windows.exe)  
2. Double-click to run (place it on Desktop for convenience).

## Support/Suggest an Idea

Write to t.me/humansiamnothuman (<span style="color:red">I might not notice or reply for a million years<span style="color:white">),  
but it’s better to report bugs in GitHub issues, and for everything else — in discussions.





# === Русский ===
# Накрутка для котика ботика 

![Version 1.0](https://gist.githubusercontent.com/ZILOGZ80000/4ef8ad0d48867d92ece3293b7fcf52ba/raw/f18967f338fccb9873e6eba6c686bd4f84316c51/version.svg) <!-- хз почему у меня не работает оригинальный сайт  -->

## Описание
Небольшой Python-инструмент для автоматической накрутки жизек,лайков и внутриигровых "монеток" для котов в [котике ботике](t.me/Kisik_Kotik_Bot)
Использует Selenium для автоматизации действий в браузере Firefox.

## Возможности
⦁   **Накрутка лайков:** Автоматически ставит лайки котам по указанной ссылке.

⦁   **Накрутка монеток:** Проходит мини-игры для заработка монеток.

⦁   **Накрутка жизек:** Управляет телеграм акаунтом и пишет боту 

⦁   **Накрутка предметов:** Управляет телеграм акаунтом и пишет боту 

⦁   **Сохранение настроек:** Сохраняет стандартные ссылки и параметры в `settings.json`.

⦁   **Прокси-серверы:** Поддержка бесплатных прокси для анонимности и обхода ограничений.

⦁   **Настраиваемые тайминги:** Рандомные задержки для имитации человеческого поведения.

⦁   **Режим Headless:** Возможность запускать браузер в фоновом режиме.

⦁   **Блокировка рекламы:** Автоматическая установка uBlock Origin.

⦁   **Обновления:** Уведомляет об обновлениях  из файла vers.json


## Требования
⦁   Python 3.x

⦁   Firefox и Geckodriver (Устанавливаются авотматически)

## Установка
### Android

0.  **Установите termux:**

    **Termux** - это эмулятор линукс терминала который нужен для запуска пайтон кода. [Нажмите для загрузки](https://f-droid.org/repo/com.termux_1002.apk)
    
    **Внимание!** Ни в коем случае не скачивайте из Google play/Get apps или подобных магазинов! Там **урезанная версия** которая не может установить пайтон!

1.  **Запустите установщик:**
    
    Скопируйте и запустите эту команду в Termux:
    
    ``` Bash
    curl https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/refs/heads/main/executable_files/termux.sh | bash
    ```
    Запустится установщик питона, библиотек, далее начнется первоначальная инициализация (функция start_init() в main.py), установится файрфокс и гекодрайвер, и вы попадете в меню. Далее запускайте командой kb

## Linux

1.  **Запустите установщик:**
    
    Установка почти такая же как и на андроид но команда немного другая:
    
    ``` Bash
    curl https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/refs/heads/main/executable_files/linux.sh | bash
    ```
    После установки также запускайте командой kb

## Windows 

1. **Скачайте и запустите exe файл:** 

    Скачайте [этот файл](https://raw.githubusercontent.com/ZILOGZ80000/farmer-for-cat-bot/refs/heads/main/executable_files/windows.exe) 
    
    Для удобства можно перенести на рабочий стол

    Запустите :)

## Поддержка/предложить идею

Пиши в t.me/humans_i_am_not_human (<span style="color:red">Могу не заметить или ответить через 1000000 лет<span style="color:white">)
но лучше для багов в [Github issues](https://github.com/ZILOGZ80000/farmer-for-cat-bot/issues), а для остального в [discussions](https://github.com/ZILOGZ80000/farmer-for-cat-bot/discussions)


<!--
### Вариант 1:

1.  **Клонируйте репозиторий:**
    ```
    git clone https://github.com/ZILOGZ80000/farmer-for-cat-bot.git
    cd farmer-for-cat-bot
    ```

2. **Установите зависимости**: bash pip install selenium requests free-proxy

## Запуск Запустите основной скрипт:

python main.py

После запуска появится интерактивное меню в консоли, где вы сможете выбрать действие (накрутка лайков, монеток, жизек или настройка параметров).

### Вариант 2(только если есть github аккаунт):

1. На [странице проекта](https://github.com/ZILOGZ80000/farmer-for-cat-bot) нажимаем Code
2. Переключаемся на вкладку Codespaces
3. Тыкаем Create codespace on main
4. Ждем загрузку
5. Нажимаем ▶-->
