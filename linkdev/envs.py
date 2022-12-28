from dotenv import load_dotenv, dotenv_values
import os


# loads the config from .env file
config = {
    **dotenv_values('.env'),
    **dotenv_values('.postgres'),
    **os.environ
}


secrets = {
    # 'POSTGRES_PORT': os.getenv('POSTGRES_PORT'),
    # 'POSTGRES_DB': os.getenv('POSTGRES_DB'),
    # 'POSTGRES_USER': os.getenv('POSTGRES_USER'),
    # 'POSTGRES_PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    # 'HOST': os.getenv('HOST')
    'POSTGRES_PORT': config['POSTGRES_PORT'],
    'POSTGRES_DB': config['POSTGRES_DB'],
    'POSTGRES_USER': config['POSTGRES_USER'],
    'POSTGRES_PASSWORD': config['POSTGRES_PASSWORD'],
    'HOST': config['HOST']
}
