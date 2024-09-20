from celery import shared_task
import time

@shared_task
def process_task(task_id):
    time.sleep(60)
    return f'Task {task_id} completed.'
