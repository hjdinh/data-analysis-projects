import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/HP-15-Inch-i7-9750H-Processor-15-dc1047nr/dp/B07SRXV9LG/ref=sr_1_18?keywords=gaming+laptop&qid=1583286109&sr=8-18"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[1] + price[3:6])

    if converted_price < 1500:
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("csjimmydinh@gmail.com","earkrjyjpxahgsgr")

    subject = "HP Omen Price Drop"
    body = "Check the price here https://www.amazon.com/HP-15-Inch-i7-9750H-Processor-15-dc1047nr/dp/B07SRXV9LG/ref=sr_1_18?keywords=gaming+laptop&qid=1583286109&sr=8-18"

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        "csjimmydinh@yahoo.com",
        "csjimmydinh@gmail.com",
        msg
    )
    print("Email has been sent")

    server.quit()

while(True):
    check_price()
    time.sleep(86400)