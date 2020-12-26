from databases import audit_database, task_database, team_database

import config
import time

def submit(user_id, flag):

    session = team_database.find_team(user_id)
    
    if session == None: 
        return 'You need to login first'

    if int(time.time()) > config.timeline.end:
        return 'Times up'

    data = task_database.correct_flag(flag)
    
    if data == None:
        audit_database.create_audit(session.team_id, 0, flag)
        return 'Wrong flag'
    
    if audit_database.audit_exist(session.team_id, data.id):
        return 'You already solved this'
    
    firstblood = audit_database.firstblood(data.id)
    audit_database.create_audit(session.team_id, data.id, flag)

    return 'Firstblood' if firstblood else 'Correct flag'
    
    
    
