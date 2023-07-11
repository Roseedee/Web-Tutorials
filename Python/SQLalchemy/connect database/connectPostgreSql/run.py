from sqlalchemy import create_engine

db_host = "localhost"
db_username = "postgres"
db_password = "12345"
db_name = "postgres"

engine = create_engine(f"postgresql://{db_username}:{db_password}@{db_host}:{5432}/{db_name}")

con = engine.connect()

if con.closed:
    print("connect database failed")
else:
    print("connect database successfully")

con.close()


