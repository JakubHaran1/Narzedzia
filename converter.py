import sys
import json

if len(sys.argv) != 3:
    print("Błędnie podane argumenty - converter.py file1.x file2.y")
    sys.exit(0)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

class Converter:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        ext1 = arg1.split(".")[1]
        ext2 = arg2.split(".")[1]
        data = self.get_data(arg1,ext1)
        
    
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

app = Converter(arg1,arg2)