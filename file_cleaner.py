import os
import shutil
from define_filetype import Add_Location

# if __name__ == "__main__":
#     pass
desktop = r'C:\Users\tyler\OneDrive\Desktop'

print(os.getcwd())
os.chdir(desktop)
print(os.getcwd())
stuff = os.listdir()
print(os.listdir())

# Clutter_Folder = desktop + "\Clutter"
# if (os.path.exists(Clutter_Folder)) != True:
#     os.mkdir(Clutter_Folder)
# # else:
# #     folder_name = input("choose a folder name:")
# #     os.mkdir(desktop+ '\ ' + folder_name)
#     # return "file already exists"

# for file in os.listdir():
#     shutil.move(file, Clutter_Folder)

# Seperate by file time and move into Documents folder....
filetypes = {
    'pdf': [".pdf"],
    'doc': [".doc", ".docx"],
    'excel': [".xlsx"],
    'App': [".lnk", ".exe"],
    'Pics': [".jpeg", ".png"],
    'Zip' : [".zip"]
}
# for x in filetypes:
#     print(x.keys())
for i in filetypes:
    for value in filetypes[i]:
        print(value)

Locations = {}
for doc in stuff:
    for thing in filetypes:
        for type_ in filetypes[thing]:
            if type_ in doc:
                Locations = Add_Location(Locations, doc, thing)
                break
print(Locations)

for folder in Locations:
    new_folder = desktop + '\ ' + folder
    if (os.path.exists(new_folder)) != True:
        os.mkdir(new_folder)
        for bro in Locations[folder]:
            shutil.move(bro, new_folder)