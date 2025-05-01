from .celery import app  # <-- UWAGA, skąd importujesz app


@app.task(name='worker.worker.tasks.fetch_user_data')  # <-- NAZWA MUSI SIĘ ZGADZAĆ
def fetch_user_data(user_id):
    print(f"Fetching user: {user_id}")
    return {"user_id": user_id, "name": "John Doe"}
