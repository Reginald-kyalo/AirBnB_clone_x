import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """defines common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key,value in kwargs.items():
                if key is 'id':
                    self.id = value
                if key is 'created_at':
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key is 'updated_at':
                    self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        else:            
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self) -> None:
        self.updated_at = datetime.now()
        storage.save()
    
    def to_dict(self) -> dict:
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__