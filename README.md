# Pipeline Setup

Prefect deployment using docker-compose and kubernetes (minikube)

Usage of a prefect worker and prefect server.

Local package and image builds will be used.

Guide created on WSL2 Ubuntu 22.04.4 LTS

## Installation of packages

Poetry is used in this repository.

Note: Poetry is a bit annoying to use on Windows

Dependencies can also be checked and installation/building part can be done differently.

Usage of [poetry](https://python-poetry.org/docs/#installing-with-pipx)

```bash | powershell
poetry shell
poetry install
```

## Usage without deployments

To debug any flow, debug_local_main.py can be used.

To debug with prefect setup:
Open two shells and run each command on a seperate shell.

```bash
python debug_prefect_main.py
prefect server start
```

## Deployments

### Docker compose

Install docker compose and run the following command

```
poetry build
docker compose up
```

After that you can reach the prefect frontend from localhost:4200

The [config](docker-compose.yml) can be edited to include a network to eliminate
the need to use the internal docker ip.

### Kubernetes (minikube)

Install [minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download), and follow the steps

```bash | powershell
poetry build
minikube start

# This command can be used to use minikubes docker daemon directly.
# It modifies environment variables
eval $(minikube -p minikube docker-env)

# Or the following commands can be used to transfer images from host to minikube after they are built on host
# minikube image load prefect-server:latest
# minikube image load prefect-worker:latest

docker build -t prefect-server -f prefect_server/Dockerfile .
docker build -t prefect-worker -f prefect_worker/Dockerfile .

kubectl apply -f kubernetes/prefect-server.yml
kubectl apply -f kubernetes/prefect-server.yml
kubectl apply -f kubernetes/prefect-worker.yml

# After these steps you deployments should be working inside minikube
# To forward the service to localhost

minikube service prefect-service
```