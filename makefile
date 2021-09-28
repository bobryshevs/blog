build:
	docker-compose build

up: build
	docker-compose up  --remove-orphans -d

tests: up
	docker exec -it backend python -m pytest

down:
	docker-compose down 