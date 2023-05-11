# Executando Crawler no Docker Container
Este repositório para executar o rastreador de target_url para obter dados no banco de dados no contêiner docker.

[![Suporte à versão do Python][shield-python]](#)
[![Suporte à versão do Pypi][shield-pypi]](#)
[![Suporte à versão do Docker][shield-docker]](#)


## Executando no docker:
1. Instale e execute a máquina do Docker.
2. Clone este repositório
3. Dentro do repositório:
    * verifique os existentes ou crie novos `target_url_crawler` e `data_cralwer` de acordo com seus requisitos.
       >_NOTE:_ Você pode acessar o mysql após executar o docker em: <br />`http://<docker-public ip>:8080?server=172.30.0.5`) <br />
        Para o ip público do docker, verifique: `docker-machine ip default` <br />
        No mac: `http://localhost:8080?server=172.30.0.5`
         
4. Altere o cmd `go_spider.py` conforme seu rastreador
5. Crie e execute o rastreador
    
        docker-compose up --build

>Nota:
1. Quaisquer alterações no serviço, primeiro exclua o respectivo contêiner de serviço.
2. Pode acessar o volume após executar o contêiner:

        docker exec -it <container-id/name> bash

[shield-python]: https://img.shields.io/badge/python-v3.5.0-blue.svg
[shield-docker]: https://img.shields.io/badge/Docker-v3-blue.svg
[shield-pypi]: https://img.shields.io/badge/pypi-v9.0.1-blue.svg
[shield-build]: https://img.shields.io/badge/build-passing-brightgreen.svg
