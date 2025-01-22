import os

directory_in_str = "./Normal"
directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".png"): 
		newName = filename.replace("Normal", "Grey")
		print(filename)
		os.system("magick ./Normal/"+filename+" -grayscale Rec709luminance ./Grey/" + newName)
		continue
	else:
		continue

