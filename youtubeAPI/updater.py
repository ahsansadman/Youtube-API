from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import fetch_data


def start():
    """
    start scheduler to call fetch data function to update the database every minute interval 
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_data, 'interval', seconds=60)
    scheduler.start()