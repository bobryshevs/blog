ENV=local
include ./secrets/$(ENV)/.env

use_secrets:
	cp ./secrets/$(ENV)/.env ./.

build: use_secrets
	docker-compose build

up: build
	docker-compose up  --remove-orphans -d

tests: up
	docker exec -it ${APP_NAME} pytest ./tests/

unit: up
	docker exec -it ${APP_NAME} pytest ./tests/unit

integration: up
	docker exec -it ${APP_NAME} pytest ./tests/integration

ipython: up
	docker exec -it ${APP_NAME} ipython

down:
	docker-compose down --remove-orphans