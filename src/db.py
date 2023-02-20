# for connecting to the server
import pymongo

# for storing information in chunks
import gridfs

# for iterating over files in the folder
import os

# inititing a Mongoclient instance for connection to the server url
client = pymongo.MongoClient("mongodb://localhost:27017")

# creating the database
db = client["Flowers"]

# for storing information and retrieving information
fs = gridfs.GridFS(db)


Image_folder = "D:\\PYTHON PROJECTS\\MY PROJECTS\\Image_folder"

for filename in os.listdir(Image_folder):
    with open(os.path.join(Image_folder, filename),"rb") as f:
        fs.put(f.read(), filename=filename)

client.close()
