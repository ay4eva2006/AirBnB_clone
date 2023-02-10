#!/usr/bin/python3
import cmd

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''Class to create cmd console
    '''
    prompt = "(hbnb) "
    mydictfile = {
                     "BaseModel": BaseModel,
                     "User": User,
                     "Place" : Place,
                     "State" : State,
                     "City" : City,
                     "Amenity" : Amenity,
                     "Review" : Review
                }

    
    def do_quit(self, line):
        ''' Command to quit program
        '''
        return True

    def do_EOF(self, line):
        ''' command to quit program
        '''
        return True

    def do_create(self, line):
        '''Command to create new instance
        '''
        if line is None or line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.mydictfile:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.mydictfile[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        '''command to print string 
           representation of an instance
           based on the class name and id
        '''
        line = parse(line)
        if len(line) == 0:
            print("** class name missing **")
        elif len(line) == 1: 
            if line[0] not in HBNBCommand.mydictfile:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(line) == 2:
            if line[0] not in HBNBCommand.mydictfile:
                print("** class doesn't exist **")
            else:
                my_obj = storage.all()
                my_id = line[1]
                my_show = None
                for value in my_obj.values():
                    value = value.to_dict()
                    if value["id"] == my_id:
                        my_show = HBNBCommand.mydictfile[line[0]](**value)
                        print(my_show)

                    else:
                        if my_show is None:
                            print("** no instance found **")


                    

def parse(line):
    return line.split()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
