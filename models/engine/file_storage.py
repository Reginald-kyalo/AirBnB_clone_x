import json

class FileStorage():
    """
    serializes instances to JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self) -> dict:
        """returns objects dictionary"""
        return self.__objects
    
    def new(self, obj) -> None:
        """sets in objects the obj with custom key"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
        
    def save(self) -> None:
        """serializes objects to json file in file path"""
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file, indent=4)
            
    def reload(self) -> None:
        """deserialize json file to objects"""
        with open(self.__file_path, "r") as json_file:
            self.__objects = json.load(json_file)
