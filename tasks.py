from celery import Celery
import time

celery = Celery('tasks',
                broker='redis://redis:6379',
                backend='redis://redis:6379')

@celery.task()
def do_task():

    """
    some long task here please
    """

    time.sleep(10)

    msg = "task done"

    return msg