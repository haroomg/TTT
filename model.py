from sqlalchemy import Column, Integer, Float, String, Boolean, TIMESTAMP, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
import datetime


Base = declarative_base()


class Rol(Base):
    __tablename__ = "roles"
    
    rol_id = Column("rol_id", Integer(), primary_key=True)
    name = Column("name", String(50), unique=True) 



class User(Base):
    __tablename__= "users"
    
    user_id = Column("user_id", Integer(), primary_key=True)
    first_name = Column("first_name", String(50))
    last_name = Column("last_name", String(50))
    user_name = Column("user_name", String(50), unique=True)
    email = Column("email", String(250), unique=True)
    password = Column("password", String(250))
    is_verified = Column("is_verified", Boolean())
    is_active = Column("is_active", Boolean())
    rol_id = Column("rol_id", Integer(), ForeignKey("roles.rol_id"))
    creation_day = Column(DateTime, default=datetime.datetime.utcnow)



class Project(Base):
    __tablename__ = "projects"
    
    project_id = Column("project_id", Integer(), primary_key=True)
    name = Column("name", String(100), unique=True)
    # owner_id = Column("owner_id", Integer(), ForeignKey('users.user_id'))
