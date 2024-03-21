import cmd
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    """

    Args:
        cmd (_type_): _description_
    """
    prompt = "(hbnb) "
    __classes = ['BaseModel']
    
    def do_create(self, arg):
        """creates new instance of BaseModel
        saves it to JSON file
        prints the id
        Ex: (hbnb) create BaseModel
        """
        line = arg.strip()
        if line:
            if line in HBNBCommand.__classes:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            else:
                print("**class doesn't exist**")
        else:
            print ("**class name missing**")
            
    def do_show(self, arg):
        """prints string representation of instance
        based on class name
        Ex: (hbnb) show BaseModel

        Args:
            arg (_type_): _description_
        """
        line = arg.strip().split()
        model_name, model_id = line
        objs = storage.all()
        
        if model_name:
            if model_name in HBNBCommand.__classes:
                if model_id:
                    for key, value in objs.items():
                        inst_id = key.split(".")[1]
                        if model_id is inst_id:
                            print(value)
                        else:
                            print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        save changes to JSON file
        """
        line = arg.strip().split()
        model_name, model_id = line
        objs = storage.all()
        if model_name:
            if model_name in HBNBCommand.__classes:
                if model_id:
                   for key, value in objs.items():
                        inst_id = key.split(".")[1]
                        if model_id is inst_id:
                            del objs[key]
                            storage.save()
                        else:
                            print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            
    def do_all(self, arg):
        """prints all string representation of all instances
        based or not on the class name
        Ex: $ all BaseModel or $ all
        """
        model_name = arg.strip()
        objs = storage.all()
        
        if model_name:
            if model_name in HBNBCommand.__classes:
                for key, value in objs.items():
                    my_key = key.split(".")[0]
                    if my_key is model_name:
                        list.append(value)
                print(list)
            else:
                print("** class doesn't exist **")    
        else:
            for value in objs.items():
                list.append(value)
            print(list)
    
    def update(self, arg):
        """adds or updates attribute to an instance
        saves changes to JSON file
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.strip().split()
        model_name, model_id, attr_name, attr_val = args
        objs = storage.all()
        my_obj = objs["{}.{}".format(model_name, model_id)]
        my_obj[attr_name] = attr_val
        storage.save()
                                   
    def do_EOF(self, line):
        """command to exit program"""
        return True
    
    def do_quit(self, line):
        """command to exit program"""
        return True
    
    def emptyline(self):
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()