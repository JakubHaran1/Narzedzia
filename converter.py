import sys
import json
import yaml

if len(sys.argv) != 3:
    print("Błędnie podane argumenty - converter.py file1.x file2.y")
    sys.exit(0)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

class Converter:
    def __init__(self, arg1, arg2):
        arg1 = arg1
        ext1 = arg1.split(".")[1]
        arg2,ext2 = arg2.split(".")
        data = self.get_data(arg1,ext1)
        self.save_data(arg2,ext2,data)
    
    def get_data(self,file1,ext1):
        if ext1 == "json":
            try:
                with open(file1,"r") as file:
                    data = json.load(file)
                
                return data
            
            except FileNotFoundError:
                print("Taki plik nie istnieje")
                sys.exit(0)
                
            except json.JSONDecodeError:
                print("Niepoprawny format pliku.")
                sys.exit(0)
        elif ext1 == "yml":
            try:
                with open(file1,"r") as file:
                    data = yaml.safe_load(file)
                return data
            except yaml.YAMLError:
                print("Niepoprawny format pliku.")
    
    def save_data(self,file2,ext2,data):
        new_file = f"{file2}.{ext2}"
        if ext2 == "json":
            try:
                with open(new_file,"w") as file:
                    json.dump(data,file)
            except ValueError:
                print("Niepoprawny format danych do zamisu w json")



app = Converter(arg1,arg2)