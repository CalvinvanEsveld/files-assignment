__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile


newpath = os.path.join(os.getcwd(), 'files' ,'cache')

def clean_cache(): 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    else:
        for f in os.listdir(newpath):
            os.remove(os.path.join(newpath, f))


def cache_zip(zip_path, cache_path):
    with ZipFile(zip_path, 'r') as zip:
        zip.extractall(cache_path)


def cached_files():
    filelist = []
    path = os.path.abspath(newpath)
    for f in os.listdir(path):
        filelist.append(os.path.join(path, f))
    return filelist


def find_password(filelist):
    for path in filelist:        
        with open(path) as f:
            for line in f.readlines():
                if 'password' in line:
                    space = line.find(" ")
                    return line[space::].strip() 



def main():
    print((clean_cache()))
    print(cache_zip(r'/Users/calvin/Desktop/Winc/files/data.zip', r'/Users/calvin/Desktop/Winc/files/cache'))
    print(cached_files())
    print(find_password(cached_files()))


if __name__ == "__main__":
    main()

