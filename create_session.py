import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
import pymysql
pymysql.install_as_MySQLdb()
Base = declarative_base()
url = 'mysql://syed:covid#2020@techassessment.ckhkrgdd3xkf.us-east-1.rds.amazonaws.com/syed'
engine = db.create_engine(url)
Session = sessionmaker(bind=engine)

# create session
session = Session()
