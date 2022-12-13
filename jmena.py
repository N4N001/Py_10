def najdijmeno(name):
    print(name,": ",open("names.txt", "r").read().count(name))
najdijmeno("Darth")
najdijmeno("Lea")
najdijmeno("Luke")