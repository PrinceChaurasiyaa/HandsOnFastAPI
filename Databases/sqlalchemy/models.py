from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        autoincrement=True)
    
    publication_date: Mapped[datetime] = mapped_column(
        DateTime, 
        nullable=False, 
        default=datetime.now)
    
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    
    content: Mapped[str] = mapped_column(
        Text, 
        nullable=False)
    

"""CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    publication_date DATETIME NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);"""