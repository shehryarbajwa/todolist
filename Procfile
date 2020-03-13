web: gunicorn backend.app.app:app
python3 backend.app.app:manage.py db init
python3 backend.app.app:manage.py db migrate
python3 backend.app.app:manage.py db upgrade