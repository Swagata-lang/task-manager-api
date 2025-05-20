<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from database import Base

class DBTask(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
=======
from sqlalchemy import Column, Integer, String
from database import Base

class DBTask(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
>>>>>>> bfef1c0f6358deab7beb4fe0a2d21cc9e05a6561
    status = Column(String, default="pending")