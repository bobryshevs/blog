
blog:
	docker build -t blog .

start: blog
	docker-compose up  --remove-orphans
