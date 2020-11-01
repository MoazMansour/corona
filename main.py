from typing import Optional
from create_session import session
from models import StateSummary

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/all_states")
def get_all_states():
    states = session.query(StateSummary).all()
    print(len(states))
    results = []
    for state in states:
        print(state.state)
        results.append({'state': state.state})
    return results
