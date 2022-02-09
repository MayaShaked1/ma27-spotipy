import os
import json

path_to_json = r'D:\Users\Maya\course\gitCodesPython\spotipy\songs\\' #the path from content root does not work

for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    path = path_to_json + file_name
    with open((path_to_json + file_name), 'r') as json_file:
        data = json.load(json_file)
        print(data)
