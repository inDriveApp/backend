# backend

## **Docs generator**

* Dependencias:
  * graphviz

```bash
pyreverse -o png -d docs/assets -ASmy src
```

---

## **Build**

### Fora do docker

```bash
docker network create inDrive

docker run --name nginx -d -p 8888:443 -p 80:80 -v /media/pi/kairos/nginx/conf/:/etc/nginx/conf.d/:ro -v /media/pi/kairos/certbot/www:/var/www/certbot/:ro nginx

docker run -d --network inDrive --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=inDrive -e POSTGRES_USER=inDrive -e POSTGRES_DB=inDrive postgres:13-alpine

docker run -it --network inDrive -p 8000:8000 -v /media/pi/kairos/projects/inDrive/backend/:/home/ --name python --entrypoint /bin/bash python:3.9-bullseye

docker run --rm -it -v /media/pi/kairos/projects/inDrive/frontend/:/home -p 3000:3000 ubuntu:20.04
```

### Dentro do docker

```bash
pip install --upgrade pip
pip install -r requirements.txt
./run.sh
```
