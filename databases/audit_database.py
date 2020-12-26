from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config
import datetime

engine = create_engine(config.dburl)
Base = declarative_base()
Session = sessionmaker(bind=engine)
s = Session()

class Audit(Base):
    __tablename__ = 'audits'
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer)
    task_id = Column(Integer)
    flag = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

def find_all_audit():
    data = s.query(Audit).all()
    return data

def find_audit(audit_id):
    data = s.query(Audit).get(audit_id)
    return data

def create_audit(team_id, task_id, flag):
    audit = Audit(team_id=team_id, task_id=task_id, flag=flag)
    s.add(audit)
    s.commit()

def audit_exist(team_id, task_id):
    data = s.query(Audit).filter_by(team_id=team_id, task_id=task_id).first()
    return False if (data == None) else True

def delete_audit(audit_id):
    data = s.query(Audit).get(audit_id)
    s.delete(data)
    s.commit()

def firstblood(task_id):
    data = s.query(Audit).filter_by(task_id=task_id).first()
    return True if (data == None) else False


Base.metadata.create_all(engine)