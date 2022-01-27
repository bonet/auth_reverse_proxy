## Docker Quickstart using `docker-compose` for local development
1. ```cd auth```
1. ```COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build auth-dev``` (to build flask-dev container for the first time)
2. ```docker-compose up reverse-proxy-dev``` (if auth-dev container is already built, then run it)
3. ```docker-compose up oauth2-token-db-dev``` ('auth_dev' database will be created if haven't created yet)
4. ```docker exec -it auth-dev pip install -r requirements.txt``` to install python modules - ONLY if need to update container
5. ```docker exec -it auth-dev flask db upgrade``` to migrate / upgrade database


++ AUTH ++
docker-compose up oauth2-token-db-dev

COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build auth-dev
docker-compose up auth-dev
docker exec -it auth-dev flask db upgrade
0.0.0.0

++ API ++
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build products-api-dev
docker-compose up products-api-dev
0.0.0.0:2001

COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build orders-api-dev
docker-compose up orders-api-dev
0.0.0.0:2002


++ PROXY SERVER ++
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build products-reverse-proxy-dev
docker-compose up products-reverse-proxy-dev
0.0.0.0:1001

COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build orders-reverse-proxy-dev
docker-compose up orders-reverse-proxy-dev
0.0.0.0:1002


docker exec -it products-api-dev bash

docker exec -it oauth2-token-db-dev psql -U some_user -d auth_dev
