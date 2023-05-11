from pyspark.sql import SparkSession
from deta import Deta

# Configuração do Spark
spark = SparkSession.builder \
    .appName("MeuProjeto") \
    .master("spark://master:7077") \
    .getOrCreate()

# Configuração do Deta
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"
deta = Deta(DETA_KEY)
db = deta.Base("data")

# Criação de um DataFrame de exemplo
data = [("João", 25), ("Maria", 30), ("Pedro", 35)]
df = spark.createDataFrame(data, ["Nome", "Idade"])

# Conversão do DataFrame para uma lista de dicionários
data_dict = df.rdd.map(lambda row: row.asDict()).collect()

# Armazenamento dos dados no Deta
for item in data_dict:
    db.put(item)

# Recuperação dos dados do Deta
items = db.fetch()

if isinstance(items, list):
    for item in items:
        # Processar cada item recuperado
        print(item)
else:
    # Tratar o caso em que o retorno não é uma lista
    print("Erro: Não foi possível recuperar os itens do Deta")


# Criação de um novo DataFrame a partir dos dados recuperados
retrieved_data = [(item["Nome"], item["Idade"]) for item in items]
retrieved_df = spark.createDataFrame(retrieved_data, ["Nome", "Idade"])

# Exibição do DataFrame recuperado
retrieved_df.show()

# start worker

# sudo /opt/spark-3.4.0-bin-hadoop3/sbin/stop-all.sh
# sudo /opt/spark-3.4.0-bin-hadoop3/sbin/start-worker.sh spark://estevam.localdomain:7077
# > starting org.apache.spark.deploy.worker.Worker, logging to /opt/spark-3.4.0-bin-hadoop3/logs/spark-root-org.apache.spark.deploy.worker.Worker-1-estevam.out
# sudo /opt/spark-3.4.0-bin-hadoop3/sbin/start-master.sh
# > starting org.apache.spark.deploy.master.Master, logging to /opt/spark-3.4.0-bin-hadoop3/logs/spark-root-org.apache.spark.deploy.master.Master-1-estevam.out
# spark-submit --master spark://estevam.localdomain:7077 apacheSpark.py