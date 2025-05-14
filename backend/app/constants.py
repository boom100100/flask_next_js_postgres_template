import os


# database values
default_db_uri = "postgresql://postgres:postgres@localhost:5432/demo"
DB_URI = os.environ.get('DB_URI', default_db_uri)

# flask config
SECRET_KEY = os.environ.get('SECRET_KEY', "dev")
