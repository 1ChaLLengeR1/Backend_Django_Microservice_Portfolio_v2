from worker.config.celery import app


# @app.task
def fetch_user_data(user_id):
    print(f"Fetching user {user_id}")
    return {"user_id": user_id}
