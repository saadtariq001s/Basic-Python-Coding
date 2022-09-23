counts={}
line= input("Enter a line of your choice \n")

words = line.split()
print("words:", words)

print("counting:")
for word in words:
    counts[word]= counts.get(word,0)+1
print("counts", counts)    