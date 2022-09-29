import requests
from datetime import datetime

PIXELA_USERNAME = "ENTER USERNAME"
PIXELA_TOKEN = "ENTER PIXEL TOKEN"
GRAPH_ID = "ENTER GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# TODO: Create an account. Give external source piece of data - https://pixe.la/
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# TODO: Create a graph definition - Call /v1/users/<username>/graphs by HTTP POST.
# Documentation - https://docs.pixe.la/entry/post-graph

# graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Fitness Graph",
#     "unit": "Min",
#     "type": "float",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN
# }
#
# # TODO: replace a-known with username and test-graph with id-  https://pixe.la/v1/users/a-know/graphs/test-graph.html
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#
# # TODO: Post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

today_date = datetime.now()

pixel_data = {
    "date": today_date.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you work out today?: ")
}

pixel_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=pixel_headers)
print(response.text)

# TODO: This is how we would update a pixel
# update_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "60"
# }
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=pixel_headers)
# print(response.text)

# TODO: This is how we would delete a pixel
# delete_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime('%Y%m%d')}"
#
# response = requests.delete(url=delete_endpoint, headers=pixel_headers)
# print(response.text)

