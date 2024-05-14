# This is a sample Python script.
import requests
from datetime import datetime
import time
import smtplib
MY_EMAIL="b21cs086@mace.ac.in"
MY_PASSWORD="B21CS086"
MY_LAT=51.507351
MY_LONG=-0.127758


def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    is_latitude = float(data["iss_position"]["latitude"])
    is_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= is_latitude <= MY_LAT + 5 and MY_LONG - 5 <= is_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {"lat": MY_LAT,
                  "lng": MY_LONG,
                  "formatted": 0,
                  }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour()
    print(time_now.hour)
    if time_now>=sunset and time_now<=sunrise:
        return True


while True:
    time.sleep(60)
    if iss_is_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="subject:LOOK UP \n\n THE ISS IS ABOVE ")



