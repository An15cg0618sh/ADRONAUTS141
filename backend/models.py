from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

Base = declarative_base()

# -------------------- Resume Table --------------------
class Resume(Base):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    resume_text = Column(Text)
    score = Column(Integer)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# -------------------- Contact Table --------------------
class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# -------------------- Blog Table --------------------
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), default="Mastersolis Team")
    content = Column(Text, nullable=False)
    summary = Column(Text)
    seo_description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# -------------------- Database Setup --------------------
if not os.path.exists('data'):
    os.makedirs('data')

engine = create_engine('sqlite:///data/resumes.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
