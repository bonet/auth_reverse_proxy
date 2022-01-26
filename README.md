## Docker Quickstart using `docker-compose` for local development
1. ```cd auth```
1. ```COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build auth-dev``` (to build flask-dev container for the first time)
2. ```docker-compose up auth-dev``` (if flask-dev container is already built, then run it)
3. ```docker-compose up oauth2-token-db-dev``` ('onlineniaga_dev' database will be created if haven't created yet)
4. ```docker exec -it auth-dev pip install -r requirements/dev.txt``` to install python modules - ONLY if need to update container
5. ```docker exec -it auth-dev flask db upgrade``` to migrate / upgrade database
