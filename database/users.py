from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

UsersBase = declarative_base()


class Users(UsersBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return (
            f"<id={self.id}, "
            f"email={self.email}, "
            f"user_name={self.user_name}, "
            f"password={len(self.password)}-{"*" * len(self.password)}>")
