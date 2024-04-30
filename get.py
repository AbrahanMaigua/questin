import requests
import base64

def auth(client_id,client_secret):
        
    # Endpoint de ejemplo
    url = 'https://api-homologacao.getnet.com.br/auth/oauth/v2/token'
    # Concatenar el Client ID y Client Secret con ":" y convertir a base64

    auth_string = f"{client_id.replace('-','')}:{client_secret.replace('-','')}"
    encoded_auth_string = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
    print(encoded_auth_string)
    # Datos del cuerpo de la solicitud para obtener el token de acceso
    data = {
        'scope': 'oob',
        'grant_type': 'client_credentials'
    }


    # Encabezado de autorización
    headers = {
        'Authorization': f'Basic {encoded_auth_string}',
       # 'Content-Type': 'application/x-www-form-urlencoded'

    }



    # Realizar la solicitud GET con la autenticación básica
    response = requests.post(url,data=data, headers=headers)

    # Manejar la respuesta
    if response.status_code == 200:
        print('Solicitud exitosa!')
        print(response.headers)

        return auth_string


    else:
        print('Error en la solicitud:')
        print(response.text)


# Definir las credenciales

client_id      = ""
client_secret  = ""
seller_id      = ""

auth_string = f"{client_id}:{client_secret}"
token = auth(client_id, client_secret)

