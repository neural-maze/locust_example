.PHONY: build up down logs clean restart

# Build and start the application
up:
	docker-compose up --build -d

# Build the application
build:
	docker-compose build

# Stop and remove containers
down:
	docker-compose down

# View logs
logs:
	docker-compose logs -f api

# Remove all containers and images
clean:
	docker-compose down --rmi all --volumes --remove-orphans

# Restart the application
restart:
	docker-compose restart api
