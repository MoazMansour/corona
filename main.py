from typing import Optional
from create_session import session
from models import StateSummary
from get_data import get_data

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/all_states")
def get_all_states():
    get_data()
    states = session.query(StateSummary).all()
    print(len(states))
    results = []
    for state in states:
        print(state.state)
        results.append({'state': state.state, 'updated': state.updated,
                        'cases': state.cases, 'casesToday': state.casesToday,
                        'deaths': state.deaths, 'deathsToday': state.deathsToday,
                        'recovered': state.recovered, 'active': state.active,
                        'casesPerMilion': state.casesPerMillion, 'deathsPerMillion': state.deathsPerMillion,
                        'tests': state.tests, 'testsPerMillion': state.testsPerMillion,
                        'population': state.population})
    return results
