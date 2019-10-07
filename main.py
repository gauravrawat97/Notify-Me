from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler


def my_job():
    cmd = "python cronjob.py"
    os.system(cmd)

scheduler = BackgroundScheduler()
scheduler.add_job(my_job, 'interval', hours=1)
scheduler.start()
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
try:
    while True:
            time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()