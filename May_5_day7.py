# today, I learned how to use the if, else, and elif function better, and program a code which asks you questions.
tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")

order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger" :
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
else:
  print("Your pizza will not have pepperoni.")

Like = input("Do you like cats or dogs: ")
if Like == "dogs" :
  print("Great choice! I love dogs too! ")
  Like = input("Whats your favorite breed? ")
  if Like == "Golden retriver":
    print("Amazing")
  else: 
    print("Cool!")
elif Like == "cats":
  print("Nice, but dogs are better.")
  Cats = input("Whats your favorite thing about cats? ")
  if Cats == "Their playfulness! ":
    print("They are so cute! ")
  else:
    print("Great")
