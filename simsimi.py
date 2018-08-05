import requests
SimsimiKey = "YOUR SIMSIMI API TOKEN"
inputtext = input("Input: ")
URL = "http://sandbox.api.simsimi.com/request.p?key={}&lc=id&ft=1.0&text={}".format(SimsimiKey, inputtext)
r = requests.get(url = URL)
data = r.json()
if data['result'] == 509:
	print(data['msg'])
else:
	print(data['response'])