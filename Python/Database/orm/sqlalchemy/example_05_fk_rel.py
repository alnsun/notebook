from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from consts import DB_URI

eng = create_engine(DB_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(128), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='addresses')

# the field needs to place after Address define
User.addresses = relationship('Address', order_by=Address.id,
        back_populates='user')

Base.metadata.drop_all(bind=eng)
Base.metadata.create_all(bind=eng)

Session = sessionmaker(bind=eng)
session = Session()

user = User(name='zhangan')
user.addresses = [Address(email_address='a@123.com', user_id=user.id),
                  Address(email_address='b@123.com', user_id=user.id)]

session.add(user)
session.commit()

for u, a in session.query(User, Address).filter(User.id==Address.user_id).filter(Address.email_address=='a@123.com').all():
    print 'User ID: {}'.format(u.id)
    print 'Email Address: {}'.format(a.email_address)

session.query(Address).join(User).filter(Address.id.in_([2])).all()[0].email_address
session.query(User).join(Address).filter(Address.email_address=='a@123.com').one().name
