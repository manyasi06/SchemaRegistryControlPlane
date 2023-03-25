makemigaration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

build_dev:
	docker build --tag schema-registry-control-plane:1.0.0