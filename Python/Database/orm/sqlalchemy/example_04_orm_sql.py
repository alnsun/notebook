from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_, or_, text
from sqlalchemy.orm import sessionmaker

from consts import DB_URI


eng = create_engine(DB_URI)
Base = declarative_base()


class User(Base):  # to generate talbe
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'),
            primary_key=True, autoincrement=True)
    name = Column(String(25))


Base.metadata.drop_all(bind=eng) # delete table
Base.metadata.create_all(bind=eng)

Session = sessionmaker(bind=eng) # create a session
session = Session()
session.add_all([User(name=username) for username in ('zhangsan', 'lisi', 'wangwu')])
session.commit() # session.rollback()

def get_result(rs):
    print '-' * 20
    for user in rs:
        print user.name

rs = session.query(User).all()
get_result(rs)
rs = session.query(User).filter(User.id.in_([2,]))
get_result(rs)
rs = session.query(User).filter(and_(User.id>2, User.id<4))
get_result(rs)
rs = session.query(User).filter(or_(User.id==2, User.id==4))
get_result(rs)
rs = session.query(User).filter(User.name.like('%zh%'))
get_result(rs)
user = session.query(User).filter_by(name='lisi').first()
get_result([user])

# complex stm
rs = session.query(User).filter(
        text('id > 2 and id < 4')).order_by(text('id')).all()
get_result(rs)
rs = session.query(User).filter(text('id<:value and name=:name')).params(value=3, name='zhangsan').all()
get_result(rs)
rs = session.query(User).from_statement(
        text('SELECT * FROM users where name=:name')).params(name='lisi').all()
get_result(rs)
