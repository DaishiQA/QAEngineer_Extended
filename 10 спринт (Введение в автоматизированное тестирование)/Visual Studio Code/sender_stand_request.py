import configuration
import data
import requests

def post_new_user(body):
        return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers)

response = post_new_user(data.user_body)

auth_token = response.json().get("authToken")

def post_new_client_kit(kit_body,auth_token):
        headers_with_auth = data.headers.copy()
        headers_with_auth['Authorization'] = 'Bearer ' + auth_token
        return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                        json=kit_body,
                        headers=headers_with_auth)

response = post_new_client_kit(data.kit_body, auth_token)