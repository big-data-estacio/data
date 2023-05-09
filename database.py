from deta import Deta
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
DETA_KEY = "e0u31gqkqju_2Ps7fJD5a1kAKF2Rr4Y31ASSdvUUeX8Y"

# Initialize Deta
deta = Deta(DETA_KEY)

# Get database
db = deta.Base("data")

def insert_data(username, name, password):
  return db.put({
    "key": username,
    "name": name,
    "password": password
  })

# insert_data("admin", "Administrador", "admin")

def fetch_all_users():
  result = db.fetch()
  return result.items

# print(fetch_all_users())

def update_data(username, name, password):
  return db.put({
    "key": username,
    "name": name,
    "password": password
  })

# update_data("admin", "Administrador", "admin")


def delete_data(username):
  return db.delete(username)

# delete_data("admin")