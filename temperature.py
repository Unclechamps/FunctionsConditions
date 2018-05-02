#Write an app which asks the user for input temperature and if the user wishes
#to convert from Celsius to Faren or Faren to Celsius. Do the calculations and
# then prints the correct converted tempature on the screen.

inittemp = int(input("Enter the temperature to convert: "))
convert = input("Do you want to convert to Faren or Celsius? ")

def temperature():
    if convert == "Faren" or convert == "faren":
        tempf = (round((inittemp * (9/5) + 32), 2))
        print (f"The temperature is {tempf}F.")
    elif convert == "Celsius" or convert == "celsius":
        tempc = (round((inittemp - 32) / (9/5), 2))
        print (f"The temperature is {tempc}C.")
    else:
        print ("Convert to what!?")

temperature()
