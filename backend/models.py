from typing import Optional, List
#from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum
from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Learner (Base):
    __tablename__ = "learner"
    id_learner = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

class LearnerModel (BaseModel):
    id_learner: int
    first_name: str
    last_name: str
