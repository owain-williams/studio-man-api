from dotenv import dotenv_values
import mysql.connector

db_config = dotenv_values(".env")

db = mysql.connector.connect(
    host=db_config["HOST"],
    user=db_config["USER"],
    password=db_config["PASSWORD"],
    database=db_config["DATABASE"]
)

cursor = db.cursor()
