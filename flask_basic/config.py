import os
import oracledb
from flask_sqlalchemy import SQLAlchemy

oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\instantclient_19_25\instantclient_19_25")

BASE_DIR = os.path.dirname(__file__) # 현재 파일의 경로를 저장
print("BASE_DIR", BASE_DIR)

SQLALCHEMY_DATABASE_URI = 'oracle+oracledb://scott:tiger@localhost:1521/xe'
print("SQLALCHEMY_DATABASE_URI", SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY="dev"