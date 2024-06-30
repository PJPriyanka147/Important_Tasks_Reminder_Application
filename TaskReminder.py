#code for the reminder
from plyer import notification
from datetime import datetime, timezone, timedelta
from time import sleep

utc_dt = datetime.now(timezone.utc)
is_notification_sent = [0] * 24

def send_reminder(msg):
    notification.notify(title = "Urgent Reminder",
                 message = msg,
                 timeout = 5)
    
def schedule(date, test_hour=None, test_minute=None):
    hour = date.hour
    minute = date.minute

    #Remind for lunch time at 1 PM
    if hour == 13 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time for lunch break!!")

    #Remind for snacks at 4 PM
    if hour == 16 and is_notification_sent[hour] == 0:
        is_notification_sent[hour] = 1
        send_reminder("It's time for snack and water!!")

    #Remind for drinking water in the day time between 9.00 am to 6.00 pm
    for i in range(9, 18):
        if hour == i and hour not in [13, 16] and is_notification_sent[hour] == 0:
            is_notification_sent[hour] = 1
            send_reminder("It's time to drink water!!")

if __name__ == "__main__":
    prev_date = utc_dt.astimezone() - timedelta(days=1)
    while True:
        date = utc_dt.astimezone()
        if date.day == 1 or date.day > prev_date.day:
            is_notification_sent = [0 for x in is_notification_sent]
            prev_date = date

        current_hour = date.hour
        current_minute = date.minute

        schedule(date, test_hour=current_hour, test_minute=current_minute)
        sleep(300)

