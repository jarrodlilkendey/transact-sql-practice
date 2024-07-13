# Transact SQL Practice

Built with Streamlit

- https://docs.streamlit.io/get-started/installation/command-line

## Instructions

### Setup Tasks

- Run a local instance of Microsoft SQL Server
- Create a User - https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-ver16
- Store there credentials in a secrets file
- Login with that user
- Run the DB setup scripts

### Running in virtual environment

```
python -m venv .venv (first time only)
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
deactivate
visit http://localhost:8501/
```

### Running via Docker

```
docker build -t streamlit .
docker run -p 8501:8501 streamlit
visit http://localhost:8501/
```

Data Sources:

- https://www.abs.gov.au/census/find-census-data/datapacks?release=2021&product=GCP&geography=ALL&header=S
