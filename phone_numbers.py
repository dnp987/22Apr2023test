# Enter +1 as country code for Canada
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
a = input ('Enter phone number: ')
phonenumber = phonenumbers.parse(a)
print (geocoder.description_for_number(phonenumber, 'en'))
print(timezone.time_zones_for_number(phonenumber))
print(carrier.name_for_number(phonenumber, 'en'))