import phonenumbers
from phonenumbers import geocoder


phonenumbers_1 = phonenumbers.parse('+34691155874')
geo = geocoder.description_for_number(phonenumbers_1, 'en')

print(geo)
