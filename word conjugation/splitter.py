alpha = open("words_alpha.txt", "r")
lines = alpha.readlines()
#for i in alpha:
#    filewrite = open(f"{alpha.readline()[0]}.txt", "w" )
#    filewrite.write(alpha.readline())
#    file.close()

word = input("Enter A word: ")
length = len(word)


for line in lines:  
	
	
	
	a = str(alpha.readline()) in word # count how many times l is in the string
	if line == "zwitter":
		print("1")
	



	

	#if a != f"['{word}']":
		#  print(alpha.readline())




alpha.close