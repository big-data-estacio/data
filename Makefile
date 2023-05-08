IMAGE_NAME = big_data_app_estacio

# build: que constrói a imagem Docker a partir do Dockerfile.
build:
	docker build -t $(IMAGE_NAME) .

# run: que executa o contêiner a partir da imagem criada.
run:
  docker run -p 8501:8501 -e MYSQL_USER=user -e MYSQL_PASSWORD=user -e MYSQL_DATABASE=$(IMAGE_NAME) -e MYSQL_HOST=192.168.1.100 $(IMAGE_NAME)
  # docker run -p 8501:8501 -e MYSQL_USER=user -e MYSQL_PASSWORD=user -e MYSQL_DATABASE=big_data_app_estacio -e MYSQL_HOST=192.168.1.100 big_data_app_estacio

# clean: que para e remove o contêiner e a imagem Docker.
clean:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q)
	docker rmi $(IMAGE_NAME)


# Para executar qualquer um desses comandos, basta abrir um terminal na pasta do projeto e executar make <comando>, onde <comando> pode ser build, run ou clean.

# Por exemplo, para construir a imagem Docker, basta executar o comando make build. Isso irá executar o comando docker build -t pedacinho-do-ceu ., que irá construir a imagem a partir do Dockerfile.

# Caso deseje executar o contêiner, basta executar o comando make run. Isso irá executar o comando docker run -p 8501:8501 pedacinho-do-ceu, que irá executar o contêiner a partir da imagem criada.

# Caso deseje remover a imagem Docker e o contêiner, basta executar o comando make clean. Isso irá executar os comandos docker stop e docker rm para remover o contêiner e docker rmi para remover a imagem.
