
from config import get_config
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = get_config()
engine = create_engine(config.dburl)
Base = declarative_base()
Session = sessionmaker(bind=engine)
s = Session()

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class UserSession(Base):
    __tablename__ = 'user_sessions'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))

def create_team(teamname):
    team = Team(name=teamname)
    s.add(team)
    s.flush()
    s.refresh(team)
    return team

def team_exist(teamname):
    data = s.query(Team).filter_by(name=teamname).first()
    return False if (data == None) else True

def create_user_session(user_id, team_id):
    user_session = UserSession(user_id=user_id, team_id=team_id)
    s.add(user_session)
    s.commit()

def user_session_exist(user_id):
    data = s.query(UserSession).filter_by(user_id=user_id).first()
    return False if (data == None) else True

Base.metadata.create_all(engine)