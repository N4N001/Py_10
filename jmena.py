name=""
def najdijmeno(name):
    print("Darth: ",open("names.txt", "r").read().count(name))
najdijmeno("Darth")
najdijmeno("Lea")
najdijmeno("Luke")