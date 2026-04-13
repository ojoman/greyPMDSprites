import os

directory_in_str = "./Normal"
directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".png"): 
		newName = filename.replace("Normal", "Grey")
		print(filename)
		os.system("convert ./Normal/"+filename+" -colorspace Gray -separate -evaluate-sequence Mean ./Grey/" + newName)
		continue
	else:
		continue

