from sqlalchemy import create_engine

engine = create_engine(f"postgresql://postgres:12345@localhost/postgres")

con = engine.connect()

if con.connection:
    r = con.execute('select * from "user" order by "id"')
    for i in r:
        print(i)

    