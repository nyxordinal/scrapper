import os
import re
import shutil

import requests

code = "435628"
name = "Fellatio Kenkyuubu Ch 5"
num_of_page = 45
clean_name = re.sub("\s+", "_", name.lower().strip())
fullname = f"nhentai-{code}-{clean_name}"
gallery_url = "https://i5.nhentai.net/galleries/2426108"

path = f"./download/{fullname}"
isExist = os.path.exists(path)
if not isExist:
    os.mkdir(path)

for i in range(num_of_page):
    no = i+1
    if no <=42:
        continue
    url = f"{gallery_url}/{no}.jpg"
    filename = f"{path}/{no}.jpg"

    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived, try png format')
        url = f"{gallery_url}/{no}.png"
        filename = f"{path}/{no}.png"
        
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
        else:
            print('Image Still Couldn\'t be retreived')

def get(url):
    return requests.get(url, stream=True)
    