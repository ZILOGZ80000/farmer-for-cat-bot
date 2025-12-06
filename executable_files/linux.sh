cd ~ 
sudo apt install -y python3
sudo apt install -y python3-pip
git clone https://github.com/ZILOGZ80000/farmer-for-cat-bot
cd farmer-for-cat-bot
pip3 install --break-system-packages selenium requests telethon
python3 main.py
# дальше все сделает скрипт 
