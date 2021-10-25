import os.path

save_path = 'D:/Online Python/file fun'
name_of_file = "kailesh Rajput"
completeName = os.path.join(save_path, name_of_file+".txt")

for i in range(0, 5):
    for j in range(0, 5):

    file1 = open(completeName, "w")

    toFile = "Popat Ban Gaya Tera"

    file1.write(toFile)

    file1.close()
