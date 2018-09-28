#from flask import *
import requests
import json

URL = 'https://api.telegram.org/bot619070662:AAFA3ft3uzAyfPK5aiqJU5hvUNf-M93i6_A/'


def write_json(data, filename ='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    



def main():
    r = requests.get(URL + 'getMe')
    print(r.json())


if __name__ == '__main__':
    main()
