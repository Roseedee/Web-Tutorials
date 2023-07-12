from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, insert, Null, select


user_tb = Table('user_tb', MetaData(),  Column('id', Integer, primary_key=True), Column("f_name", String, nullable=False),Column("l_name", String, nullable=False), Column("age", Integer, nullable=False))


db_connection = "postgresql://postgres:12345@localhost/postgres"

engine = create_engine(db_connection)

with engine.connect() as con:
    stmt = select(user_tb)
    r = con.execute(stmt)
    for i in r:
        print(i)
    # con.execute(
    #     text('insert into "user_tb" ("f_name", "l_name", "age") values (:fname, :lname, :age)'),
    #     [
    #         {
    #             "fname" : "Roseedee",
    #             "lname" : "Cehlaeh",
    #             "age" : 21
    #         }
    #     ]
    # )
    
    

    