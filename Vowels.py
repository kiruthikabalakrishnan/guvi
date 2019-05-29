lst=["a","e","i","o","u","A","E","I","O","U"]
c=input()
if(c>="a"and c<="z"):
 if(c>="A"and c<="Z"):
  if c in lst:
    print("Vowels")
  elif(c!=lst):
    print("Consonants")
else:
    print("invalid")
