# Ambiente de encaixe Pyspark

Se você simplesmente deseja testar um cluster de spark de nó único, basta executar `docker run -it wlongxiang/pyspark-2.4.4 pyspark`, isso trará seu shell de spark.

Ou você também pode criar um cluster muti-worker com um arquivo de composição simples, o exemplo montará os diretórios locais `data` e `code` para o cluster worker e master de forma que você possa alterar facilmente seu código e dados localmente e testá-los dentro do cluster do docker.

 - Check-out do branch master
 - Execute ``docker-compose up`` para ativar 2 workers e 1 master (ou você também pode definir COMPOSE_FILE env para um arquivo diff. compose)
 - Acesse http://localhost:8080 para ver a interface do usuário do Spark Master
 - Execute `docker exec -it pyspark_docker_master_1 bash` para shell no contêiner de spark
 - contagem de palavras: `spark-submit /code/wordcount.py /data/logs.txt`

Versões do spark suportadas: 2.4.4.

Alguns exemplos para testar, veja o diretório `code`.


## Como publicar uma nova imagem (manualmente)

- primeiro você faz `docker login` com suas credenciais para docker-hub
- então `docker build -t wlongxiang/pyspark-2.4.4:<version_tag> .`, este comando irá construir seu e-mail com o nome pyspark e marcar com 2.4.4
- verifique se sua imagem foi criada com sucesso por `docker images`
- finalmente `docker push wlongxiang/pyspark-2.4.4:<version_tag>`, no final isso estará disponível em seu repositório docker
- agora, tudo deve ser capaz de executar sua imagem ou usá-la no arquivo docker-compose, como `docker run -it pyspark-2.4.4:<version_tag> bash`