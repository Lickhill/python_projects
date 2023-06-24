print("WELCOME TO THE TREASURE ISLAND")

go1=input(("Would you like to go 'left' or 'right'?\n"))

if go1=="right":
  print("GAME OVER") 
else:
  go2=input("Would you like to 'swim' or 'wait'?\n")
  if go2=="swim":
    print("GAME OVER")
  else:
    go3=input("Which door would you like to choose? 'red','yellow',or'blue'\n")
    if go3=="red" or go3=="blue":
     print("GAME OVER")
    else:
      print("YOU WIN")