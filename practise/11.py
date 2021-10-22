filew = open("teams.txt", "w")
outfile = ""
teams = ["Newcastle", "Mancheser United", "Leicester", "Liverpool", "Manchester City"]

for i in range(0, len(teams)):    
    filew.write(f"{teams[i]} \n")

filer = open("teams.txt", "r")
filew = open("teams.txt", "w")

filew.write("2027 Premier League top 5 Predictions \n")
for line in range(0, 5):
    filew.write(f"{filer.readline()}")
filew.close()

filer = open("teams.txt", "r")

line = filer.readlines()
for i in range (0, len(line)):
    print(line[i])
filer.close()