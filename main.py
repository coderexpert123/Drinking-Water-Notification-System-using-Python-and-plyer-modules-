import time
from  plyer import  notification
if __name__=="__main__":
    while True:

        notification.notify(
            title="Plese drink water ",
            message="Water makes up 60-75% of human body weight. A loss of just 4% of total body water leads to dehydration, and a loss of 15% can be fatal. Likewise, a person could survive a month without food but wouldn’t survive 3 days without water.",
            timeout=10

        )
        time.sleep(60)


