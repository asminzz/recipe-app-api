import json

from datetime import datetime

# import requests


# def get_repositories_data(data):
#     new_data = []

#     for repo in data:

#         repo_name = repo['full_name']

#         url = f'https://api.github.com/repos/{repo_name}'
#         response = requests.get(url)

#         response_data = response.json()

#         repo.update({
#             "short_description": response_data['description'],
#             "stars": response_data['stargazers_count'],
#             "forks": response_data['forks_count'],
#             "watchers": response_data['watchers_count']
#         })
#         new_data.append(repo)

#     return new_data


def update_json_file():
#    with open('repo_data.json', 'r') as json_file:
#       data = json.load(json_file)
#        updated_data = get_repositories_data(data)

#     with open('renewal.txt', 'w') as json_file:
#         json_file.write({})
    now = datetime.now() # current date and time

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    date_timenow = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    f = open("renewal.txt", "a")
    f.write("Updated at ")
    f.write(date_timenow)
    f.write("\n")
    f.close()
    

if __name__ == '__main__':
    update_json_file()
