# using nested if

name = input("Enter your name: ").upper()

print(name + ", Welcome to The Adventure World.")

answer = input("You are on a dirt road, it has come to an end and you have to go RIGHT or LEFT. Which way you wanna go? ").lower()

if answer == "left" :
    answer = input("You come to a river, you can walk around or swim accross. Type WALK or SWIM. : ").lower()
    if answer == "swim":
        print(" we unajua kuogelea kweli?")
    elif answer == "walk":
        print("utawai fika?")
    else:
        print("Not a valid option !")
elif answer == "right":
    answer = input("You come to a lion's den, you can fight it or stealth around. Type FIGHT or STEALTH, : ").lower()
    if answer == "fight" :
        answer = input("Choose your weapon, MACHETTE or GUN. :").lower()
        if answer == "machette":
            print("we unapima lion, You Died.")
        elif answer == "gun":
            print("you are the G. Okota Gold")
        else:
            print("Not a valid option ! You died !")
    elif answer == "stealth":
        print("we mzee uko na uoga, ")
    else:
        print("Not a valid option ! You died !")    
else:
    print("Not a valid path. You lost")
