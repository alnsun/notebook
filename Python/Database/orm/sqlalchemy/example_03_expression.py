from sqlalchemy import (create_engine, Table, MetaData, Column, Integer,
        String, tuple_)
from sqlalchemy import select, asc, and_
from consts import DB_URI


eng = create_engine(DB_URI)

meta = MetaData(eng)
users = Table(
        'Users', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String(25), nullable=False),
)

if users.exists():
    users.drop()
users.create() # or meta.create_all(eng) for multiple table

def execute(s):
    print '-' * 20
    rs = con.execute(s)
    for row in rs:
        print row['id'], row['name']

with eng.connect() as con:
    for username in ('zhangsan', 'lisi', 'wangwu'):
        user = users.insert().values(name=username)
        con.execute(user)

    stm = select([users]).limit(1)
    execute(stm)

    k = [(2,)]
    stm = select([users]).where(tuple_(users.c.id).in_(k))
    execute(stm)

    stm = select([users]).where(and_(users.c.id>2, users.c.id<4))
    execute(stm)

    stm = select([users]).order_by(asc(users.c.name))
    execute(stm)

    stm = select([users]).where(users.c.name.like('%min%'))
    execute(stm)
