# -*- coding:utf8 -*-
import requests
import misc
import json

token = misc.token


URL = 'https://api.telegram.org/bot' + token +'/'
# print(URL)
# https://api.telegram.org/bot619070662:AAFA3ft3uzAyfPK5aiqJU5hvUNf-M93i6_A/sendmessage?chat_id=152167065&text=hi



def get_updates():
    url = URL + 'getupdates'
    # print(url)
    r = requests.get(url)
    return r.json()

#def get_message():
 #   data = get_updates()    











def main():
    d = get_updates()
    print("Generating File")
    with open('updates.json' , 'w') as file:
         json.dump(d, file, indent=2, ensure_ascii=False)
    print("All done")




if __name__ == '__main__':
    main()	
