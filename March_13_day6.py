#Today I learned how to use the elif funcation, putting it between else and if, and I made passwords for Scarlett, Arabella, and Ambika.
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
 print("Welcome Mark!")
elif username == "suzanne" and password =="Su74nne":
 print("Hey there Suzanne!")
else:
 print("Go away!")

  print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")

season = input("what is your favorite season?")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")

print("Login")
username = input("What is your Username? ")
password = input("What is your Password? ")
print()
if username == "Scarlett" and password == "ScArlETtE286":
  print("Hi Scarlett!! Your so Pretty")
elif username == "Arabella" and password == "aR@bellA_#90":
  print("Hi Arabella!! Welcome in.")
elif username == "Ambika" and password == "AmbIka-93$8":
  print("Welcome Ambika!! How Are you?")
else:
  print("Sorry, You do not have an account.")
