services = backend mongo rabbitmq
build:
	docker-compose build

up: backend
	docker-compose up  --remove-orphans -d

tests: up
	docker exec -it backend python -m pytest

stop:
	docker stop $(services)