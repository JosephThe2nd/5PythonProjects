print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

answear = input("What does CPU stand for? ")
if answear.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: print("Incorrect!")

answear = input("What does GPU stands for? ")
if answear.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: print("Incorrect!")

answear = input("What does RAM stands for? ")
if answear.lower() == "random access memory":
    print("Correct!")
    score += 1
else: print("Incorrect!")

answear = input("What does PSU stands for? ")
if answear.lower() == "power supply":
    print("Correct!")
    score += 1
else: print("Incorrect!")

print("You got " + str(score) + " questions right! ")
print("You got " + str((score/4) * 100) + "% of the questions right! ")

