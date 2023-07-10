import phonenumbers
from phonenumbers import timezone, geocoder,carrier   #geocoder btadegya ki konsi sim se hai #timezone particular time with  area #carrier company of sim
numbers= input("Enter your No.with +___:")
phone=phonenumbers.parse(numbers)
time=timezone.time_zones_for_geographical_number(phone)
car=carrier.name_for_number(phone," en ")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)



