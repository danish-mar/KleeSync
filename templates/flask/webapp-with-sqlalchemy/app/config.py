import os
from dotenv import load_dotenv

# loads custom environment 
load_dotenv()


class Config:
    # your configurations to be loaded from the environment
    SECRET_KEY = os.getenv("SECRET_KEY")

    # loads the sql database
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

    # add more config here......


# add more configs like production config or development config

# class ProductionConfig(Config):


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    "development": DevelopmentConfig,
    # "production": ProductionConfig
}
