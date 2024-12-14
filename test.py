import requests


def get_access_token(client_id, client_secret):
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json().get("access_token")


# Замени с твоите API ключове
client_id = "R8GQ8Y9QrFnAgc9zffboKAkF71JkdciL"
client_secret = "d5GgfhXNkVqkzenb"

access_token = get_access_token(client_id, client_secret)
print(f"Access Token: {access_token}")