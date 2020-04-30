import os
i=0
directory = "C:/Users/sourab/Desktop/jervis/image_me/0/"
'''for path, subdirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.startswith("."):
            print("Skipping system file")  # Skipping files that startwith .
            continue
id=os.path.basename(path)#fetching subdirectory names
img_path=os.path.join(path,filename)#fetching image path
print("img_path:",img_path)
print("id:",id)'''
for path,sub,filenames in os.walk(directory):
    continue
for name in filenames:
    k = name.find(".")
    no = name[:k]
    try:
        if int(no) < i:
            continue
    except:
        pass
    name_to = name[k:]
    name = directory+name
    while True:
        try:
            name_new = directory + str(i) + name_to
            os.rename(name, name_new)
            i = i + 1
            break
        except:
            i = i+1

