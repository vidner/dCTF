from databases import team_database
import config
import jwt


def register(team: str):
    if team_database.team_exist(team):
        return 'Team already exist'
    else:
        data = team_database.create_team(team)
        token = jwt.encode({"team_id": data.id, "team_name": data.name}, config.credential.secret, algorithm="HS256")
        return f'{data.name} succesfully registered, here is your auth token ```{token}```'

def login(user_id, token: str):
    if team_database.user_session_exist(user_id):
        return 'You already logged in'
    else:
        try:
            data = jwt.decode(token, config.credential.secret, algorithms=["HS256"])
            team_database.create_user_session(user_id, data["team_id"])
            return f'Succesfully Loged-in as `{data["team_name"]}`'
        except:
            return 'Invalid token'

        
