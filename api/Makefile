active_venv:
	.\venv\Scripts\Activate

exit_venv:
	deactivate

run_dependencies:
	pip install -r requirements.txt

migration_up:
	./worker/scripts/database/migration_up.sh

run_app:
	python manage.py runserver