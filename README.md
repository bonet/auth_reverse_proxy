## API Authorization Check through Reverse Proxy

In microservice architecture, API authentication and authorization are best done
through a separate standalone server. This is for scalability purpose and to
simplify the multi-level complexities

A good solution is to build a reverse-proxy which every API requests (excluding login)
must pass before being able to connect to the API destination.

This way, each API microservice doesn't need to care about the authorization. We can
set the authorization rule on the reverse-proxy so that it can remove unwanted
requests before it reaches API servers. Reverse Proxy is designed to be very light,
thus will process each request very fast. Either it will reject the request due
to improper authorization or will forward the request to the appropriate API endpoints
if authorization goes through.

I use Python Flask as the reverse proxy server's framework, because it's a light platform,
quite robust and relatively easy to setup.

To simulate the authentication and authorisation scenario, there are 3 main directories
in the source code:
1. `/api` is where mock API server codes are located
2. `/auth` is where login and authentication-related process happens
3. `/reverse_proxy` is the frontline reverse_proxy server code base

Below is the architecture diagram:

![image info](./docs/microservice_architecture.png)

Each of the 3 directories is a Flask server running in a standalone Docker container.


## How to Setup

Use docker-compose to build and run the container. Below are the steps for each server.
(Note that I am using an older version of Docker, thus the long build command)

### 1. Auth Service
1. `docker-compose up oauth2-token-db-dev` to setup the database
2. `COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build auth-dev` to build the image
3. `docker-compose up auth-dev` to run the container
4. `docker exec -it auth-dev flask db upgrade` to build the DB schema

Address for this service is 0.0.0.0:80


### 2. API Service
There are 2 API services in the simulation. One is for Products API, the other is
for Orders API. The 2 services have internal address, we don't need to access this.
We only need to access the address of this API's related Proxy Server

##### Products API Service
1. `COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build products-api-dev`
2. `docker-compose up products-api-dev`

##### Orders API Service
1. `COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build orders-api-dev`
2. `docker-compose up orders-api-dev`



### 3. Reverse Proxy Server
This is the API endpoint for the API requests. There are 2 provy services, each for
its corresponding API.

##### Products API Reverse Proxy
1. `COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build products-reverse-proxy-dev`
2. `docker-compose up products-reverse-proxy-dev`

Address for this service is 0.0.0.0:1001

##### Orders API Reverse Proxy
1. `COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build orders-reverse-proxy-dev`
2. `docker-compose up orders-reverse-proxy-dev`

Address for this service is 0.0.0.0:1002

Documents for this architecture can be found [here](./docs)
