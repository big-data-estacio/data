# Alpine for WSL with Docker
## What you'll get
* Docker & Docker Compose (obviously).
* Non-root user supplied through `build args`.
* Non-root user is a member of **admin** and **docker** groups, as well as **sudoers**.
* While running this image with WSL, non-root user is used by default.
* Docker daemon starts automatically on non-root user login.
* Zscaler certificates. In case you're on corporate Windows machine, with Zscaler client running in the background.

## Prerequisites
To build this image you'll need Docker, of course. No specific requirements regarding version as far as I know. Unless you want to use **BuildKit** for building, then it's 18.09 or higher.  
To run the image WSL2 is required. Type `wsl --status` and check "Default Version".

## Build WSL distro
### Using Docker Build
> source: https://medium.com/nerd-for-tech/create-your-own-wsl-distro-using-docker-226e8c9dbffe
```
docker build --build-arg USER=myuser --build-arg PASS=PassW0rd --tag alpine-docker-wsl .
docker run --name alpine-docker-wsl alpine-docker-wsl
docker export --output alpine-docker-wsl.tar.gz alpine-docker-wsl
```
### Using BuildKit
```
DOCKER_BUILDKIT=1 docker build --build-arg USER=myuser --build-arg PASS=PassW0rd --output type=tar,dest=alpine-docker-wsl.tar.gz .
```

## Run WSL distro
```
wsl --import alpine-docker-wsl .\alpine-docker-wsl .\alpine-docker-wsl.tar.gz
wsl --distribution alpine-docker-wsl
```
