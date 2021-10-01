build:
	docker-compose build

up: build
	docker-compose up  --remove-orphans -d

tests: up
	docker exec -it backend pytest

down:
	docker-compose down --remove-orphans
