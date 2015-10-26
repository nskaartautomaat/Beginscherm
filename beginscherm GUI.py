import requests

auth_details= ('kristiaan.hoogendoorn@hotmail.nl','rgQTyv_3EC9oFthMAvpQQBA0gnWxMH7PDATjqo3h8tbJGBOg5Y3-3w')

response = requests.get('http://webservices.ns.nl/ns-api-avt?station=ut', auth=auth_details)

print(response.text)