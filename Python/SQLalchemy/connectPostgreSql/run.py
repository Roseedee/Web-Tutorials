from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:12345\@localhost/postgres')
engine.connect()
session = sessionmaker(bind=engine)


print(session)