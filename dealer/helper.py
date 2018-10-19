from VolvoCore import system_messages
from commons.conf import AUDETEMI_WSDL_PASS,AUDETEMI_WSDL_USERNAME

def wsdl_authentication(data):

    if not data:
        return system_messages.PLEASE_PROVIDE_USERNAME_PASS

    user_name = data.get("username","")
    password = data.get("password","")

    if user_name != AUDETEMI_WSDL_USERNAME:
        return system_messages.PLEASE_PROVIDE_VALID_USERNAME

    if password != AUDETEMI_WSDL_PASS:
        return system_messages.INVALID_PASSWORD

    return False

def auth_soap_keys_translator(prefix_variable,data):

    if data:
        for key, value in data.items():
            updated_key = key.replace(prefix_variable, "")
            data[updated_key] = value
            if not data.get(updated_key):
                del data[updated_key]

        return data
    return {}
