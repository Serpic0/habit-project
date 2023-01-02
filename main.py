import requests
from datetime import datetime


Username = #yourusername
Token = #yourtoken

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": #yourtoken,
    "username": #yourusername,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)
graph_parameters = {
    "id": "grapha12",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": Token
}
graph_endpoint = f"{pixela_endpoint}/{Username}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)




post_pixel_endpoint = f"{graph_endpoint}/grapha12"

today = datetime.now()

post_pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today? "),
}
response = requests.post(url=post_pixel_endpoint, json=post_pixel_parameters, headers=headers)
print(response.text)

update_endpoint = f"{post_pixel_endpoint}/{today.strftime('%Y%m%d')}"
new_quantity = {
    "quantity": "6.4",
}

# response = requests.put(url=update_endpoint, json=new_quantity, headers=headers)
# print(response.text)

delete_endpoint = f"{post_pixel_endpoint}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)


