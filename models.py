import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
import pymysql
pymysql.install_as_MySQLdb()

Base = declarative_base()

class StateSummary(Base):
    __tablename__ = 'state_summary'

    id = Column(Integer, primary_key=True)
    state = Column(String(20))
    updated = Column(Integer)
    cases = Column(Integer)
    casesToday = Column(Integer)
    deaths = Column(Integer)
    deathsToday = Column(Integer)
    recovered = Column(Integer)
    active = Column(Integer)
    casesPerMillion = Column(Integer)
    deathsPerMillion = Column(Integer)
    tests = Column(Integer)
    testsPerMillion = Column(Integer)
    population = Column(Integer)

    def __init__(self, state, updated, cases, casesToday, deaths, deathsToday, recovered, active, casesPerMillion, deathsPerMillion, tests, testsPerMillion, pop):
        self.state = state
        self.updated = updated
        self.cases = cases
        self.casesToday = casesToday
        self.deaths = deaths
        self.deathsToday = deathsToday
        self.recovered = recovered
        self.active = active
        self.casesPerMillion = casesPerMillion
        self.deathsPerMillion = deathsPerMillion
        self.tests = tests
        self.testsPerMillion = testsPerMillion
        self.population = pop
        

'''class StateDetails(Base):
    __tablename__= 'state_details'

    id = Column(Integer, primary_key=True)
    state = Column(String)
    updated = Column(Integer)
    cases = Column(Integer)
    deaths = Column(18192)
    deathsToday = Column(Integer)
    recovered = Column(Integer)
    casesPerOneMillion = Column(Integer)
    deathsPerOneMillion = Column(Integer)
    tests = Column(Integer)
    testsPerOneMillion = Column(Integer)
    population = Integer(Integer)'''

engine = db.create_engine('mysql+mysqldb://syed:covid#2020@techassessment.ckhkrgdd3xkf.us-east-1.rds.amazonaws.com:3306/syed')
engine.connect()
print(engine)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
