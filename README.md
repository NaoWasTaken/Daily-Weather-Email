# Daily Weather Email
Python Automation Project: Sends a daily email at 06:00a.m. with a report on the weather for the day

[INSTRUCTIONS FOR USE]

1. Download this code as zip
   
2. Register at openweathermap.org
   
   a. Click on your username

   b. Click on 'My API Keys'
   
   c. Copy default api key

4. In any IDE open weatheremail.py

5. create a new file 'api_key.txt'

   a. copy and paste your api key

6. Change the api_key variable to the path where you have your api_key.txt file

7. Change the location variable to your location

8. Replace sender_email variable with your email

9. Replace recipient_emial variable with the email you'd like to receive the daily email to

10. Replace smtp_username variable with the sender_email

11. Replace smtp_password variable with your email's password
    
    a. If you are using gmail do the following:
    
      i. Enable Two-Factor Authentication
    
      ii. Go to https://myaccount.google.com/u/3/apppasswords
    
      iii. Create a new App Password
    
      iv. Replace smtp_password with your App Password (including whitespaces)

12. Run the program and leave it open

    a. I leave it running in a separate desktop screen (windows_key + tab)

Notes:
Feel free to change any of the text by changing the body variable. Time the email is sent can be changed in the schedule.every().day.at("06:00").do(send_email) line.

In my example, "06:00" is the time (It uses a 24hr clock and local time)


If you would like to use Celsius isntead of Fahrenheit, find the result variable 

[result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}')]

Replace units=imperial with units=metric

Be sure to replace any 'F' found within the variables titled first, second, and third with 'C'


If you are not using gmail, replace smtp_port = 587 with your smtp port (smtp_port = XYZ) and server = smtplib.SMTP(smtp_server, 587) with your smtp port (server = smtplib.SMTP(smtp_server, XYZ))
