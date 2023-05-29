run format:
	black . & isort .

run dev req:
	pipenv requirements --dev > dev_requirements.txt

run migrations:
	python docker_django/manage.py makemigrations

run migrate:
	python docker_django/manage.py migrate

run venv_prod:
	python -m venv venv
	