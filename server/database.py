from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///default.db')

metadata = MetaData()

Base = declarative_base(metadata=metadata)

Session = sessionmaker(bind=engine)


