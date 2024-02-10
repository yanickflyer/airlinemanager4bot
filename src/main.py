import launch, threading
from apscheduler.schedulers.background import BackgroundScheduler
from marketing import marketing


thread1=threading.Thread(target=launch.launch.depart_maintenance)
thread2=threading.Thread(target=launch.launch.fuel)

thread1.start()
thread2.start()

scheduler = BackgroundScheduler()
job = scheduler.add_job(marketing.eco_campaign,'cron', hours=8, minute=0, timezone="Indian/Mauritius")
scheduler.start()


while True:
    pass