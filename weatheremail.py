import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

api_key = open('C:\\Users\\avibo\\Desktop\\Weather\\api_key.txt', 'r').read()

while True:
    location = 'Rosedale'

    result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}')
    if result.json()['cod'] == '404':
        print('Invalid location')
        continue
    break

description = result.json()['weather'][0]['description']
temperature = round(result.json()['main']['temp'])
feels_like = round(result.json()['main']['feels_like'])
high = round(result.json()['main']['temp_max'])
low = round(result.json()['main']['temp_min'])

first = f'The weather in {location[0].capitalize()}{location[1:]} is {temperature}°F with a {description}.'
second = f'It feels like {feels_like}°F.'
third = f"Today's high is {high}°F, and the low is {low}°F."


def send_email():

    sender_email = "dailyweatherservicenao@gmail.com"
    receiver_email = "aviboyd04@gmail.com"
    subject = "Daily Weather"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    body = "Daily Weather Report:\n\n" + first + '\n' + second + '\n' + third
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "dailyweatherservicenao@gmail.com"
    smtp_password = "hsoi loko qhfa molq"

    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
   
    server.login(smtp_username, smtp_password)
  
    server.sendmail(sender_email, receiver_email, msg.as_string())
  
    server.quit()

schedule.every().day.at("06:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)