q_1 = input("What is ypur name?")               #entering the name from the user.
q_1 = q_1.upper()                               #capitalize the string input by the user.


if "ARTHUR" in q_1:                            #If King(Arthur) passes, access is granted without any further questions.
    print("My liege! You may pass!")
else:
    q_2 = input("What do you seek?")            #If Knight passes, he is aked some questions.
    q_2 = q_2.upper()


    if "GRAIL" not in q_2:                      #If it is not the Grail he is denied to access.
        print("Only those who seek the Grail may pass.")
    else:
        q_3 = input("What is your favourite colour?")       #If Knight donot know his fav colour he face the Gorge of Eternal Peril.
        q_3 = q_3.upper()


        if q_3[0] == q_1[0]:                                #First letter of the fav colour should match his name initial letter.
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Perilar")