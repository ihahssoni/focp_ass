print("Swallow Speed Analysis: Version 1.0")
list_1 = []                                                 #empty list created.
reading = input("Enter the Next Reading:")

if reading == "":                                           #condition to check the reading.
    print("No readings entered. Nothing to do.")
else:
    while reading:                                          #check the input data type.
        if reading[0] == "u" or "U":
            print("Reading saved.")
            list_1.append(float(reading[1:])*1.61)
            reading = input("Enter the Next Reading:")
        
        elif reading[0] == "e" or "E":
            print("Reading saved.")
            list_1.append(float(reading[1:]))
            reading = input("Enter the Next Reading:")

        else:
            break

    if(len(list_1) != 0):                                       #if list is not empty then max speed and min speed is printed.
        print("\nResults Summary\n")
        print(len(list_1), "Reading Analysed.")
        print(f"Max Speed: {max(list_1)/1.61:.1f} MPH, {max(list_1):.1f} KPH")
        print(f"Min Speed: {min(list_1)/1.61:.1f} MPH, {min(list_1):.1f} KPH")

        average = 0                                             
        z = range(0,len(list_1))
        for x in z:
            average = average + list_1[x]                       #average vale is calculated
            t = average/len(list_1)
        print(f"Avg Speed: {t/1:.1f} MPH, {t:.1f} KPH")
    
    else:                                                       #incase the data is invalid.
        print("Invalid")

