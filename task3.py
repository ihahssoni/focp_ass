from random import choice

print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.")
help_desk = ["Suman", "Arjun", "Sonika", "Shristika"]                                       #list of help_desk.
net_test = ["c", "c", "c,", "c", "c", "d", "c", "c", "c", "c"]                              #list to check for network error.

mail = input("Please enter your Poppleton email address: ")                                 #entering email from user.
count = 0

valid = False
if "@" in mail:                                                                             #if @ is in mail then only email is valid.
    e = mail.split("@")                                                                     #to split the part before and after @.
    count = 0                                                                               #count no. of characters before @.

    for i in e[0]:                                                                          #extract characters before@.
        count += 1                                                                          #value increased by for each character.


        if count >= 2 and e[1] == "pop.ac.uk":                                              #if the part before @ has 2 or more characters and domain is correct the only email id valid.
            valid = True

            operator = choice(help_desk)
            probability = choice(net_test)

            print("Hi,",e[0].capitalize(),"! Thank you, and Welcome to PopChat!")
            print("My name is",operator,", and it will be my pleasure to help you.")

            if probability == "d":                  #situation for network error.
                print("*** NETWORK ERROR ***")
                print("Thanks,",e[0].capitalize(),"for using PopChat. See you again soon!")
                exit()


            while True:                 #only executes when email is valid.
                request = input("--->") #request user what they want.
                request = request.upper()
                wrong = ["Hmm","Tell me more about it","I didn't understand","What do you mean?","Can you repeat it please","Oh yes i see"]                 #if request donot match any of the available service thwn wrong is displayed
                stop = ["EXIT","QUIT","STOP","END","GOODBYE","BYE"]                  #if user want to exit chat service it is displayed

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

                        #if the request match any of the one in stop then service will be stopped
                    for j in stop:
                        if j in request.upper():
                            print("Thanks,",e[0].capitalize(),"for using PopChat. See you again soon!")
                            exit()

                        else:
                            print(reply)
        else:
            print("Email is invalid")               #if email dont match the requirement it is invalid

    else:
        print("Email is invalid")                   #if email donot contact @ it is invalid
        exit()