import math
import time

#Picking which Conversion
def convertPickerFunct():
    convertPicker=''
    while convertPicker.lower().strip() !='feet-meters' and convertPicker.lower().strip() !='inch-centi' and convertPicker.lower().strip() !='miles-kilo' and convertPicker.lower().strip() !='centi-inch' and convertPicker.lower().strip() !='meters-feet' and convertPicker.lower().strip() !='kilo-miles' and convertPicker.lower().strip() !='ibs-kg'and convertPicker.lower().strip() !='kg-ibs':
        convertPicker=input('Which conversion would you like to do?\nInches to Centimeters:Type(Inch-Centi)\nFeet to Meters:Type(Feet-Meters)\nMiles to Kilometers:Type(Miles-Kilo)\nPounds to Kilograms:Type(Ibs-Kg)\nCentimeters to Inches:Type(Centi-Inch)\nMeters to Feet:Type(Meters-Feet\nKilometers to Miles:Type(kilo-miles)\nKilograms to Pounds:Type(Kg-Ibs)\n')
    return convertPicker


#Functions for Conversions


#Inches to Centimeters
def inch_to_centi():
    inches=int(input('How many inches?'))
    inchesToCenti=inches*2.54
    print(str(inchesToCenti)+' centimeters')

#Feet to Meters
def feet_to_meters():
    feet=int(input('How many feet?'))
    feetToMeters=feet*0.3048
    print(str(feetToMeters)+' meters')

#Miles to Kilometers
def miles_to_kilometers():
    miles=int(input('How many miles?'))
    milesToKilometers=feet*1.60934
    print(str(milesToKilometers)+' kilometers')


#Pounds to Kilograms
def ibs_to_kg():
    ibs=int(input('How many pounds ?'))
    ibsToKg=ibs*0.453592
    print(str(ibsToKg)+' kilograms')


#Cenimeters to Inches
def centi_to_inch():
    centi=int(input('How many centimeters?'))
    centiToInch=centi*0.3048
    print(str(centiToInch)+' inches')


#Meters to Feet
def meters_to_feet():
    meter=int(input('How many meters?'))
    metersToFeet=meters*3.28084
    print(str(metersToFeet)+' feet')


#Kilometers to Miles
def kilo_to_miles():
    kilo=int(input('How many kilometers?'))
    kiloToMiles=kilo*0.621371
    print(str(kiloToMiles)+' miles')


#Kilograms to Pounds
def kg_to_ibs():
    kg=int(input('How many kilograms?'))
    kgToIbs=kg*2.20462
    print(str(To)+' pounds')
    


#________________________________________________________________________________________________________________________________________________________#




#If-Elifs for the Conveter Picker
convertPick=convertPickerFunct()
if convertPick=='inch-centi':
    inch_to_centi()
elif convertPick=='feet-meters':
    feet_to_meters()
elif convertPick=='miles-kilo':
    miles_to_kilometers()
elif convertPick=='centi-inch':
    centi_to_inch()
elif convertPick=='meters-feet':
    meters_to_feet()
elif convertPick=='kilo-miles':
    kilo_to_miles()
elif convertPick=='kg-ibs':
    kg_to_ibs()
elif convertPick=='ibs-kg':
    ibs_to_kg

