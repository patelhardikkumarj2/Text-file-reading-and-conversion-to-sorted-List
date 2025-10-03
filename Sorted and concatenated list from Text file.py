fname = input("Enter file name: ")
f2name = "C:\\Users\\91972\\Downloads\\" + fname
fhndl = open(f2name)
data = fhndl.read()
strpdt= data.rstrip()
wordlist = []
temp = strpdt.split()
for word in temp:
    if word not in wordlist:
        wordlist.append(word)
        wordlist.sort()

print(wordlist)