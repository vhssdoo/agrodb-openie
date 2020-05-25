import os
import json
import pymongo

HOST = "localhost"
PORT = 27017
SUPPORTED = (".txt", ".json")

MAIN_DIR = os.getcwd()
JSON_DIR = os.path.join(MAIN_DIR, "triples_openie")

def get_filelist(path):
    list_path = os.listdir(path)
    all_files = list()

    for entry in list_path:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            all_files = all_files + get_filelist(full_path)
        else:
            if full_path.endswith(SUPPORTED):
                all_files.append(full_path)

    return all_files


def write_json_mongo(filejson, db, n):
    with open(filejson, "r") as f:
        data = json.loads(f.read())

    data["_id"] = n
    abstracts = db["abstracts"]
    info = abstracts.insert_one(data)
    
    print("Json {} insertado con id {}".format(os.path.split(filejson)[1],
                info.inserted_id))
    

if __name__ == "__main__":

    client = pymongo.MongoClient(HOST, PORT)

    db = client["agroecology"]
    index = 1
    for filename in get_filelist(JSON_DIR):
        write_json_mongo(filename, db, index)
        index += 1
    
    
