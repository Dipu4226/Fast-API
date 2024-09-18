from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Define the MySQL URL
URL_DATABASE = "mysql+pymysql://root:@localhost:3306/test"          #URL FOR DARA BASE


# Create the SQLAlchemy engine
engine = create_engine(URL_DATABASE)  


# Create a session local
sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)    # ACTUAL CONNECTION FOR SESSION


# Base class for our models
Base = declarative_base()