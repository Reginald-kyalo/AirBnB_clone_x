#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime
import models

class BaseModel():
    """defines common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if '__class__' in kwargs:
            del kwargs['__class__']
        if kwargs:
            dtstr = "%Y-%m-%dT%H:%M:%S.%f"
            for key,value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, dtstr)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, dtstr)
        else:            
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self) -> None:
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self) -> dict:
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict