import requests
from bs4 import BeautifulSoup

TOKEN = "8629166658:AAHJ5zwlogOwwtIJwJp7exguEdiAeuSP8Kg"
CHAT_ID = "871400825"
URL = "https://pl.el-ed.ru/clan/5298/homeworks"

def send_message(text):
    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")
text = soup.get_text()

if "Просмотреть" in text:
    send_message("📘 Новая работа! Есть 'Просмотреть'")
else:
    print("Пока нет новых работ")
