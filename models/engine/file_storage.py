#!/usr/bin/python3
import json


class FileStorage:
    ''' Class for filestorage
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj 
        with key <obj class name>.id
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''Serialization of json file
        '''
        my_dictjson = {}
        for key, value in my_dictjson.items():
            my_dictjson[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as myjson:
            json.dump(my_dictjson, myjson, indent=4)

    def classes(self):
        class_name = {
                        "BaseModel": BaseModel,
                        "User" : User,
                        "Place" : Place,
                        "State" : State,
                        "City" : City,
                        "Amenity" : Amenity,
                        "Review" : Review
                }

    def reload(self):
        '''Deserialization of json file
        '''
        try:
            with open(FileStorage.__file_path, 'r') as myjson:
                FileStorage.__objects = json.load(myjson)
                for key, value in FileStorage.__objects.items():
                    class_name = value["__class__"]
                    FileStorage.__objects[key] = eval(class_name)(**value)

        except FileNotFoundError:
            pass
