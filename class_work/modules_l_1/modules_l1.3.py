import ipaddress

addres = ipaddress.ip_address('10.0.1.1')
print(addres.is_private)
print(addres.is_global)
print(ipaddress.ip_network('80.0.1.0/28'))