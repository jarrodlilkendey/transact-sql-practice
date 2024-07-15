# Transact SQL Practice

Built with Streamlit

- https://docs.streamlit.io/get-started/installation/command-line

## Instructions

### Setup Tasks

- Run a local instance of Microsoft SQL Server
- Populate DATABASE_SERVER_NAME and DATABASE_NAME into an .env file

### Data

- https://nubela.co/proxycurl/linkedin
- https://nubela.co/proxycurl/docs#search-api-person-search-endpoint
- https://nubela.co/proxycurl/docs#people-api-person-profile-endpoint
- I want to get a list of people with a software background tech in Victoria. Break it down by common tech jobs. Identify large employers. Identify skills and skill gaps.

### Running in a python virtual environment

```
python -m venv .venv (first time only)
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
visit http://localhost:8501/
deactivate (when done)
```

### Running via Docker

```
docker build -t streamlit .
docker run -p 8501:8501 --env-file .env streamlit
visit http://localhost:8501/
```

Data Sources:

- https://www.abs.gov.au/census/find-census-data/datapacks?release=2021&product=GCP&geography=ALL&header=S
