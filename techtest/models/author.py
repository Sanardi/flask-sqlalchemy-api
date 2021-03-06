from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from techtest.connector import BaseModel


class Author(BaseModel):
    __tablename__ = 'author'

    id = Column(
        Integer,
        name='id',
        nullable=False,
        primary_key=True,
        autoincrement=True
    )

    code = Column(
        String(2),
        name='code',
        unique=True
    )

    name = Column(
        Text,
        name='name'
    )
