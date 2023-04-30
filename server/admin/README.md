# Running Crawler on Docker Container
This repository for running crawler from target_url to getting data in database on docker container. 

[![Python version support][shield-python]](#)
[![Pypi version support][shield-pypi]](#)
[![Docker version support][shield-docker]](#)


## Running on docker:
1. Install and run the Docker machine.
2. Clone this repository 
3. Inside the repository:
    * check existing or create new `target_url_crawler` and `data_cralwer` as per your requirements.
       >_NOTE:_ You can access mysql after running docker on: <br />`http://<docker-public ip>:8080?server=172.30.0.5`) <br />
        For docker public ip, check: `docker-machine ip default` <br />
        On mac: `http://localhost:8080?server=172.30.0.5`
         
4. Change `go_spider.py` cmd as per your crawler
5. Build and Run the Crawler
    
        docker-compose up --build

>Note: 
1. Any changes in the service, make sure you first delete respective service conatiner.
2. Can access the volume after running container:

        docker exec -it <container-id/name> bash

[shield-python]: https://img.shields.io/badge/python-v3.5.0-blue.svg
[shield-docker]: https://img.shields.io/badge/Docker-v3-blue.svg
[shield-pypi]: https://img.shields.io/badge/pypi-v9.0.1-blue.svg
[shield-build]: https://img.shields.io/badge/build-passing-brightgreen.svg
