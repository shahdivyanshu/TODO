import string
from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,Date
from .database import Base
from sqlalchemy.orm import relationship
from datetime import date


class DO(Base):
    __tablename__ = 'TODO'

    id = Column(Integer, primary_key=True, index=True)
    task= Column(String)
    assigned_to=Column(String)
    is_completed=Column(Boolean)
    due_date=Column(Date)
    
    
	
    

