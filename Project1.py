print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing .lower() == "yes":   
    print("Ok! let's play :)")
    score = 0
    
else:
    quit()

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("You're correct!")
    score += 1
    
else:
    print("You're incorrect, Try again!!")
    
    
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("You're correct!")
    score += 1
    
else:
    print("You're incorrect, Try again!!")
    
    

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("You're correct!")
    score += 1
    
else:
    print("You're incorrect, Try again!!")
    
    
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("You're correct!")
    score += 1
    
else:
    print("You're incorrect!")
    
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
