import requests
from requests.exceptions import HTTPError
from create_session import session
from models import StateSummary
URL = 'https://disease.sh/v3/covid-19/states'
PARAMS = {
        'sort': 'cases',
        'yesterday': 'true',
        'allowNull': 'false'
}
HEADERS = {'Accept':'application/json'}
states = []

def get_data():
    try:
        response = requests.get(
            url=URL,
            params=PARAMS,
            headers=HEADERS)
        response.raise_for_status()
    except HTTPError as http_error:
        print(f'HTTP Error occured: {http_error}')
    except Exception as error:
        print(f'Other error occured: {error}')
    else:
        records = response.json()
        for record in records:
            print(record)
            state = StateSummary(record['state'], record['updated'], 
                record['cases'], record['todayCases'],
                record['deaths'], record['todayDeaths'],
                record['recovered'], record['active'],
                record['casesPerOneMillion'], record['deathsPerOneMillion'],
                record['tests'], record['testsPerOneMillion'],
                record['population'])
            states.append(state)
            session.add(state)
        session.commit()
