from sqlalchemy import create_engine

engine = create_engine('sqlite://', echo=False)
with engine.connect() as con:
    rs = con.execute('SELECT 1')
    print rs.fetchone()

# or
# rs = engine.execute('SELECT 1')
# rs.fetchone()


# URI format: dialet+driver://username:password@host:port/database
# dialet: MySQL/SQLite/PostgreSQL
# driver: mysqldb
# example: engine = create_engine('mysql+mysqldb://web:web@localhost/mydb')
#          engine = create_engine('mysql://web:web@localhost/mydb') because mysqldb is default driver

