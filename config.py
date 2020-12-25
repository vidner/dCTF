import yaml

class Config:
    def __init__(self, credential, timeline, score, dburl):
        self.credential = credential
        self.timeline = timeline
        self.score = score
        self.dburl = dburl

class Timeline:
    def __init__(self, timeline):
        self.freeze = timeline["freeze"]
        self.end = timeline["end"]

class Score:
    def __init__(self, score):
        self.maximal = score["maximal"]
        self.minimal = score["minimal"]
        self.decay = score["decay"]

class Credential:
    def __init__(self, credential):
        self.token = credential["token"]
        self.secret = credential["secret"]
        self.role = credential["role"]
        
env = yaml.load(open('config.yaml').read(), yaml.SafeLoader)
score = Score(env["score"])
timeline = Timeline(env["timeline"])
credential = Credential(env["credential"])
dburl = env["dburl"]
config = Config(credential, timeline, score, dburl)
