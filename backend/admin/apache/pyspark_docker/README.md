# Pyspark docker environment

If you simply want to test a single node spark cluster, just run `docker run -it wlongxiang/pyspark-2.4.4 pyspark`, this will bring you yo spark-shell.

Or you can also create a muti-worker cluster with a simple compose file, the example will mount the `data` and `code` local dir to the cluster worker and master such that you can easily change your code and data locally and test it within docker cluster.

 - Checkout the master branch
 - Run ``docker-compose up`` to spin up 2 workers and 1 master (or you can also set COMPOSE_FILE env to a diff. compose file)
 - Go to http://localhost:8080 to see the spark master UI
 - Run `docker exec -it pyspark_docker_master_1 bash` to shell into the spark container
 - word count: `spark-submit /code/wordcount.py /data/logs.txt`

Supported spark versions: 2.4.4.

Some examples to test out, see `code` directory.


## How to publish a new image (manually)

- first you do `docker login` with your credentials to docker-hub
- then `docker build -t wlongxiang/pyspark-2.4.4:<version_tag> .`, this command will build your email with name pyspark and tag with 2.4.4
- verify your image is built successfully by `docker images`
- finally `docker push wlongxiang/pyspark-2.4.4:<version_tag>`, in the end this will be available in your docker repo
- now, everything should be able to run your image or use it in the docker-compose file, such as `docker run -it pyspark-2.4.4:<version_tag> bash`
