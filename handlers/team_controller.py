from databases import team_database
import jwt


def register(teamname: str, secret: str):
    if team_database.team_exist(teamname):
        return 'Team already exist'
    else:
        team = team_database.create_team(teamname)
        token = jwt.encode({"team_id": team.id, "team_name": team.name}, secret, algorithm="HS256")
        return f'{team.name} succesfully registered, here is your auth token ```{token}```'

def login(user_id, token: str, secret: str):
    if team_database.user_session_exist(user_id):
        return 'You already logged in'
    else:
        try:
            data = jwt.decode(token, secret, algorithms=["HS256"])
            team_database.create_user_session(user_id, data["team_id"])
            return f'Succesfully Loged-in as `{data["team_name"]}`'
        except:
            return 'Invalid token'

        
