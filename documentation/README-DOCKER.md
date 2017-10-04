# Running Docker

## Table of Contents

* [Installing Docker](#installing-docker)
* [Helpful Commands](#helpful-commands)
    1. [Build Container](#build-the-container)
    1. [Run Container](#run-the-container)
    1. [Check Container Status](#check-status-of-containers)
    1. [Kill Containers](#kill-all-running-containers)
    1. [Print Logs](#print-logs-for-api-container)
* [Docker Documentation](#docker-documentation)

## Installing Docker

Before you can utilize the Docker commands, [Docker](https://www.docker.com/) must be installed locally on your machine.

## Helpful Commands

### Build the container

```bash
docker-compose build
```

### Run the container

```bash
docker-compose up -d
```

### Check status of containers

```bash
docker-compose ps (checks status of containers)
```

### Kill all running api containers

```bash
docker-compose kill (kills all running containers)
```

### Print logs for api container

* useful for debugging

```bash
docker-compose logs api
```

## Docker Documentation

[Official Docker documentation](https://docs.docker.com/)