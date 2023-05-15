import findspark
from pyspark.sql import SparkSession
from deta import Deta


findspark.init()


# Classe para encapsular os dados de uma bebida
class Beverage:
    # Construtor para inicializar os atributos de uma bebida
    def __init__(self, descricao, name, price, quantity, sales_quantity, total_sales):
        self.descricao = descricao
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sales_quantity = sales_quantity
        self.total_sales = total_sales

    def __str__(self):
        return f'Bebida: {self.name}'
    
    def __repr__(self):
        return f'Bebida: {self.name}'
    
    def __eq__(self, other):
        return self.name == other.name

    # Método para converter os atributos de uma bebida para um dicionário
    def to_dict(self):
        return {
            'descricao': self.descricao,
            'nome': self.name,
            'preco': self.price,
            'quantidade': self.quantity,
            'quantidade_vendas': self.sales_quantity,
            'total_vendas': self.total_sales
        }

    # Método para converter os atributos de uma bebida para um tuple
    def to_tuple(self):
        return (self.descricao, self.name, self.price, self.quantity, self.sales_quantity, self.total_sales)


class BeverageDatabase:
    # Construtor para inicializar a conexão com o banco de dados
    def __init__(self, key, base_name):
        self.deta = Deta(key)
        self.db = self.deta.Base(base_name)

    # Método para adicionar uma bebida ao banco de dados
    def add_beverage(self, beverage):
        self.db.put(beverage.to_dict())


# Chave para a base de dados Deta
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"

# Criando uma instância da classe BeverageDatabase
beverage_db = BeverageDatabase(DETA_KEY, "bebidas")


# Criando uma lista de bebidas
beverages = [
    Beverage(1, 'Cerveja', 5.00, 100, 50, 250.00),
    Beverage(2, 'Vinho', 30.00, 50, 30, 900.00),
    Beverage(3, 'Whisky', 120.00, 20, 10, 1200.00)
]

# Adicionando cada bebida na lista ao banco de dados e criando uma lista de tuplas ao mesmo tempo
vendas_tuples = []
for beverage in beverages:
    beverage_db.add_beverage(beverage)
    vendas_tuples.append(beverage.to_tuple())

# Inicializando a sessão do Spark
spark = SparkSession.builder \
    .master("spark://estevam.localdomain:7078") \
    .appName("big-data") \
    .getOrCreate()

# Criando um DataFrame do Spark a partir da lista de tuplas
df = spark.createDataFrame(beverages_tuples, ['descricao', 'nome', 'preco', 'quantidade', 'quantidade_vendas', 'total_vendas'])


if __name__ == "__main__":
    # Exibindo o DataFrame
    df.show()


# linhas no terminal:
# sudo /opt/spark-3.4.0-bin-hadoop3/sbin/stop-all.sh
# sudo /opt/spark-3.4.0-bin-hadoop3/sbin/start-master.sh
# sudo /opt/spark-3.4.0-bin-hadoop3/sbin/start-worker.sh spark://estevam.localdomain:7078