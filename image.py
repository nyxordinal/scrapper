import glob
import json
import os
import re
import shutil
import zipfile

import requests

data = {}
with open('./input.json') as file:
    data = json.load(file)

clean_name = re.sub("\s+", "_", data['name'].lower().strip())
fullname = f"nhentai-{data['code']}-{clean_name}"
path = f"./download/{fullname}"

is_exist = os.path.exists(path)
if not is_exist:
    os.mkdir(path)

is_success = True

for i in range(data['num_of_page']):
    no = i+1
    url = f"{data['gallery_url']}/{no}.jpg"
    filename = f"{path}/{no}.jpg"

    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived, try png format')
        url = f"{data['gallery_url']}/{no}.png"
        filename = f"{path}/{no}.png"

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True

            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
        else:
            is_success = False
            print('Image Still Couldn\'t be retreived')

if is_success:
    with zipfile.ZipFile(f'{fullname}.zip', 'w') as f:
        for file in glob.glob(f'{path}/*'):
            f.write(file, file.split("./download/")[1])


def get(url):
    return requests.get(url, stream=True)
