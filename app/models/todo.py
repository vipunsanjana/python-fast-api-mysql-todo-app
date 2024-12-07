from sqlalchemy import Column, Integer, String, DateTime, Text, Enum as SQLEnum
from sqlalchemy.sql import func
from enum import Enum
from database import Base

class TodoStatus(Enum):
    IN_PROGRSS = 'in_progress'
    DONE = 'done'

class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    status = Column(SQLEnum(TodoStatus), default=TodoStatus.IN_PROGRSS)
    image = Column(String(255))  # Updated to String(255) instead of Text
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<Todo id={self.id} content={self.content} status={self.status}>'