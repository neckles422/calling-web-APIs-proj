import requests 

#print (*args)
#pass (look this up, not sure what it does)

URL = "https://world.openfoodfacts.org/api/v0/product/737628064502"

response = requests.get(URL) 
response.raise_for_status() 
data = response.json()   

print (data)