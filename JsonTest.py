import json

'''
with open('LogConfig.json') as data_file:
    data = json.load(data_file)
    for json_data in data['Oneliner']:
        for attribute, value in json_data.items():
            print(attribute, value) # example usage

        print()    


with open('LogConfig.json') as data_file:
    data = json.load(data_file)
    for restaurant in data['Oneliner']:
        print(restaurant.get('string'))


with open('LogConfig.json') as data_file:
    Oneliner = []
    Settings = []
    data = json.load(data_file)
    for item in data['Oneliner']:
        temp = [item]
        print(temp[0]['Regex'])
        Oneliner.append(temp)
    for item in data['Setting']:
        temp = [item]
        Settings.append(temp)
'''

def ReadConfigfromJson(filename):
    try:
        with open(filename) as data_file:
            Oneliner = []
            Settings = []
            data = json.load(data_file)
            for item in data['Oneliner']:
                temp = [item]
                print(temp)
                Oneliner.append(temp)
            for item in data['Setting']:
                temp = [item]
                print(temp)
                Settings.append(temp)
            return 1, Oneliner,Settings
    except:
        return 0,[],[]        

a,b,c = ReadConfigfromJson("LogConfig.json")

print(a,b,c)