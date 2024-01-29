#Country
import phonenumbers
from num import number
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number , "CH")
print(geocoder.description_for_number(ch_number , "en"))

#Company
from phonenumbers import carrier
service= phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service, "en"))