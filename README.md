# heartbeat-client

This code can be seen on any of these repositories:
[GitLab](https://gitlab.com/luisnabais/heartbeat-client)
[GitHub](https://github.com/luisnabais/heartbeat-client)
[Codeberg](https://codeberg.org/luisnabais/heartbeat-client)

## Description
Python script running inside a docker container, which posts a heartbeat endpoint (which uses my [heartbeat-server](https://gitlab.com/luisnabais/heartbeat-server) project) to say it's alive.
Script can also be executed locally or any other way, as long as dependencies are met.

## Instructions
### Run container
1. Set variable values (HEARTBEAT_SERVER_HOST, HEARTBEAT_SERVER_PORT, HEARTBEAT_CLIENT_ID and HEARTBEAT_INTERVAL) in .env file or docker-compose.yml
2. Execute the command: `docker-compose up -d`

### Build container
If you don't want/need to use the pre-built container and/or want/need to build the container by yourself, execute the command:
`docker build -t heartbeat-client:latest .` (my advice is to not use latest, but a version system of your own)