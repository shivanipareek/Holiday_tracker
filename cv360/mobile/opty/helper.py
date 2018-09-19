from commons import conf
from commons.user_auth.models import UserDetailInformation

def get_dse_details(user, data):
    user = UserDetailInformation.objects.filter(user=user)
    dse_id = []

    if user:
        user_position = user[0].user_position_details

        if user_position.get("PostnType_s").upper() == conf.SM_USER:
            if data.get("my_team_data"):
                dse_id = user_position.get("dse_list")
            else:
                dse_id.append(user_position.get("Login_s"))
        else:
            dse_id.append(user_position.get("Login_s"))

    return tuple(dse_id)
