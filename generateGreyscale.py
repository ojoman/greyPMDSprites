import os

directory_in_str = "./Normal"
directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".png"): 
		newName = filename.replace("Normal", "Grey")
		print(filename)
		os.system("convert ./Normal/"+filename+" -define png:color-type=6 -grayscale Rec709luminance ./Grey/" + newName)
		continue
	else:
		continue

