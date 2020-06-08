print("How are you feeling today?")
mood = input("happy, sad, nervous, relaxed, or excited?")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "sad":
    print("I'm sorry to hear that!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "relaxed":
    print("I'm happy to hear that!")
elif mood == "excited":
    print("The world is an exciting place!")
else:
    print("I don't recognize this mood.")