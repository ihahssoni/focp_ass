print("Swallow Speed Analysis: Version 1.0")
list_1 = []
reading = input("Enter the Next Reading:")

if reading == "":
    print("No readings entered. Nothing to do.")
else:
    while reading:
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

    if(len(list_1) != 0):
        print("\nResults Summary\n")
        print(len(list_1), "Reading Analysed.")
        print(f"Max Speed: {max(list_1)/1.61:.1f} MPH, {max(list_1):.1f} KPH")
        print(f"Min Speed: {min(list_1)/1.61:.1f} MPH, {min(list_1):.1f} KPH")

        average = 0
        z = range(0,len(list_1))
        for x in z:
            average = average + list_1[x]
            t = average/len(list_1)
        print(f"Avg Speed: {t/1:.1f} MPH, {t:.1f} KPH")
    
    else:
        print("Invalid")

