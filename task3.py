from random import choice

print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.")
help_desk = ["Suman", "Arjun", "Sonika", "Shristika"]
net_test = ["c", "c", "c,", "c", "c", "d", "c", "c", "c", "c"] 

mail = input("Please enter your Poppleton email address: ")
count = 0

valid = False
if "@" in mail:
    e = mail.split("@")
    count = 0

    for i in e[0]:
        count += 1


        if count >= 2 and e[1] == "pop.ac.uk":
            valid = True

            operator = choice(help_desk)
            probability = choice(net_test)

            print("Hi,",e[0].capitalize(),"! Thank you, and Welcome to PopChat!")
            print("My name is",operator,", and it will be my pleasure to help you.")

            if probability == "d":
                print("*** NETWORK ERROR ***")
                print("Thanks,",e[0].capitalize(),"for using PopChat. See you again soon!")
                exit()


            while True:
                request = input("--->")
                request = request.upper()
                wrong = ["Hmm","Tell me more about it","I didn't understand","What do you mean?","Can you repeat it please","Oh yes i see"]
                stop = ["EXIT","QUIT","STOP","END","GOODBYE","BYE"]

                reply = choice(wrong)

                if "WIFI" in request:
                    print("Wifi is excellent across campus.")
                elif "LIBRARY" in request:
                    print("Library is closed today.")
                elif "DEADLINE" in request:
                    print("Your daedline has been increased by two days.")
                elif "FOOD" in request:
                    print("Cafe is in the ground floor.")
                elif "RESTROOM" in request:
                    print("Restroom is at the corner of ecah floor.")
                else:

                    for j in stop:
                        if j in request.upper():
                            print("Thanks,",e[0].capitalize(),"for using PopChat. See you again soon!")
                            exit()

                        else:
                            print(reply)
        else:
            print("Email is invalid")

    else:
        print("Email is invalid")
        exit()