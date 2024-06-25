import requests
import json

url = "https://swapi.dev/api/people/1/"

response = requests.get(url)

def getapidata (url,key):
    if "https://" in url:
        response = requests.get(url)
        data = response.json()
        value = data[key]
        return value
    elif (type(url) is list) == True:
        results = []
        for x in url:
            response = requests.get(x)
            data = response.json()
            value = data[key]
            results.append(value)
        return results
    else:
        print("keine URL")
        print(url)


if response.status_code == 200:
    data = response.json()
    name = data['name']
    height = data['height']
    bj = data['birth_year']

    hwurl = data['homeworld']
    hw = getapidata(hwurl,'name')
    
    vhurl = data['vehicles']
    vh = getapidata(vhurl,'name')
    
    ssurl = data['starships']
    ss = getapidata(ssurl,'name')
    

    print(f'Die Infos zu ' + name + ' ' + 'Grösse: ' + height + ' cm ' + 'Geburtsjahr: ' + bj + 'Heimatsplanet: ' + hw + 'Fahrzeuge: ' + str(vh) + 'Raumfahrzeuge: ' + str(ss))