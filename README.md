# Setup and Run the application
* clone the repo on your local and cd into the repo directory 
* create a virtual env using the command **conda env create --name corona python=3.8**
* activate the virtual env using the command **conda activate corona**
* install requirements using the command **conda install --file requirements.txt**
* run command **python get_data.py** to store data in the database
* run the command 'uvicorn main:app --reload' to start the run backend code
* cd into corona-stats folder
* run the command 'yarn install'
* run the command 'yarn build'
* run the command 'yarn serve'
* open browser and paste this url into the address bar 'http://localhost:8080/'

# Assumptions
this application pulls coronavirus data for all states in the US using this api https://disease.sh/v3/covid-19/states. The Data returned from this API is stored in the Database and HTTP get API is devloped using FastAPI to retrieve that data from the database and return it as json. 
UI for the app is developed using Vuejs and uses v-data-table to display the data.
