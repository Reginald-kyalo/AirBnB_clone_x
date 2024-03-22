import json
import os
from models.base_model import BaseModel

class FileStorage():
    """
    serializes instances to JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self) -> dict:
        """returns objects dictionary"""
        return FileStorage.__objects
    
    def new(self, obj) -> None:
        """sets in objects the obj with custom key"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
        
    def save(self) -> None:
        """serializes objects to json file in file path"""
        obj = FileStorage.__objects
        with open(FileStorage.__file_path, "w") as json_file:
            objdict = {key: value.to_dict() for key, value in obj.items()}
            json.dump(objdict, json_file, indent=4)
            
    def reload(self) -> None:
        """deserialize json file to objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                objdict = json.load(json_file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        else:
            pass
