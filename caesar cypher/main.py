import art
print(art.logo)

def encrypt(text, shift):
  f=''
  for i in text:
    if alphabet.index(i)>25-shift:
      f+=alphabet[shift-1-(25-alphabet.index(i))]
    else:
      f+=alphabet[alphabet.index(i)+shift]

  print(f) 

def decrypt(text, shift):
  s=""
  for i in text:
    if alphabet.index(i)>=shift:
      s+=alphabet[alphabet.index(i)-shift]
    else:
      s+=alphabet[26-(shift-alphabet.index(i))]

  print(s)

# if direction=="encode":
#   encrypt(text=text,shift=shift) 
# elif direction=="decode":
#   decrypt(text=text,shift=shift)
# else:
#   print("INVALID DIRECTION")

#try to make this two fucntion and this if block into one function called cypher()

def cypher(text, shift, direction):
  f=""
  if direction=="encode":
    for i in text:
      if i==' ':
        f+=' '
      elif alphabet.index(i)>25-shift:
        f+=alphabet[shift-1-(25-alphabet.index(i))]
      else:
        f+=alphabet[alphabet.index(i)+shift]
    print(f)
    
  elif direction=="decode":
    for i in text:
      if i==' ':
        f+=' '
      elif alphabet.index(i)>=shift:
        f+=alphabet[alphabet.index(i)-shift]
      elif i==' ':
        f+=' '
      else:
        f+=alphabet[26-(shift-alphabet.index(i))]
    print(f)

  else:
    print("INVALID DIRECTION")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
proceed = True
while(proceed):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  
  cypher(text, shift, direction)
  
  rerun=input("Do you wish to continue?y or n?\n").lower()
  if rerun=='y':
    continue
  else:
    break
print("End of Program")

  
    
  
  