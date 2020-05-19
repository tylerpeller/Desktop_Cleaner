import os
import shutil
from define_filetype import Add_Location

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
    'Pdfs': [".pdf"],
    'Docs': [".doc", ".docx"],
    'Excel': [".xlsx", ".csv", ".xlsb"],
    'App': [".lnk", ".exe"],
    'Pics': [".jpeg", ".png", ".jpg"],
    'Zip' : [".zip"],
    'CST' : [".cst"],
    'MATLAB': [".m"],
    'PowerPoint': [".pptx"]
}
# for x in filetypes:
#     print(x.keys())
for i in filetypes:
    for value in filetypes[i]:
        print(value)

Locations = {}
for doc in stuff:
    for extension in filetypes:
        for type_ in filetypes[extension]:
            if type_ in doc:
                Locations = Add_Location(Locations, doc, extension)
                break
print(Locations)


total = desktop+r"\All_Files"
if (os.path.exists(total)) != True:
    os.mkdir(total)

os.chdir(total)

All_Folders=[]
for folder in Locations:
    new_folder = total + '\\' + folder
    All_Folders.append(new_folder)
    if (os.path.exists(new_folder)) != True:
        os.mkdir(new_folder)
    for element in Locations[folder]:
        try:
            shutil.move(desktop +'\\'+ element, new_folder)
        except:
            pass


# for folder in All_Folders:
#     shutil.move(folder,total)