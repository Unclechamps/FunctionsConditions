#Write an app which asks the user for input temperature and if the user wishes
#to convert from Celsius to Faren or Faren to Celsius. Do the calculations and
# then prints the correct converted tempature on the screen.

inittemp = int(input("Enter the temperature to convert: "))
convert = input("Do you want to convert to Faren or Celsius? ")

def temperature():
    if convert == "Faren" or convert == "faren":
        print (round((inittemp * (9/5) + 32), 2))
    elif convert == "Celsius" or convert == "celsius":
        print (round((inittemp - 32) / (9/5), 2))
    else:
        print ("Convert to what!?")

temperature()
