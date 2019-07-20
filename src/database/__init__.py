from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from util import mysql_connection_string

engine = create_engine(mysql_connection_string())
Session = sessionmaker(bind=engine, autocommit=True)
session = Session()
