# today I learned that I can make variables, and use commas to make sentences, and menus.
myName = input("What's your name? ")
myLunch = input("What are you having for lunch? ")
print(myName, "is going to be chowing down on", myLunch, "very soon!")

number = input("Give me a number: ")
group = input("Give me a collective noun for a group of things: ")
thing = input("Give me the name of a weird or wacky thing: ")
print("No I don't think that", number, "is a", group, "of", thing,". That's just odd.")

print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called" , name)
print("Who did something cool like", thing, "at the wonderful", place, "where you'll find me", rhyme)

myFood = input("Name a food:")
myPlant = input("Name a type of plant:")
myCooking = input("Name a method of cooking:")
myBurned = input("What word describes burned food?:")
myItem = input("Name a household item:")
print()
print("Menu")
print(myFood, "with", myBurned, myPlant, "on a bed of", myItem)
