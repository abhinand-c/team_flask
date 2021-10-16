
**Flask app to demonstate connecting and performing basic operations to MySQL database using mysql connecter in python.**

Performs database initialisation, Table creation, Insert operation and Select * operation.


### Instructions to run
1. Clone the repo using any of the following commands
   - `git clone https://github.com/abhinand-c/team_flask.git`
   - `git clone git@github.com:abhinand-c/team_flask.git`
   - `gh repo clone abhinand-c/team_flask`
2. Create `.env` file based on the dummy template below in your cloned repo
3. Set values in .env file, as provided by admin or for development set demo values
3. Setup & activate virtual python environment  (Refer: [Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or [Python venv](https://docs.python.org/3/tutorial/venv.html))
4. Install requirements  
    `pip install -r requirements.txt`
6. Initialise Database with  
    `python .\database\initialiser.py`
8. Run server using  
    `python runserver.py`
