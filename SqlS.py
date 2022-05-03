import requests

u = raw_input("Enter Link:")

pyload = ["'",'"',"/"]

p = "'"


for i in pyload:

	r = requests.post(u+i)

	source = r.text

	if "mysql" in source.lower():

		print"website vulnerability !"

	elif "SQL syntanx" in source.lower():

		print"website vulnerability !"
