import json

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data['total']:
        print('average: ' + str(p['average']))
        print('sum: ' + str(p['sum']))
        print('average level: ' + str(p['average_level']))
        print('ninvalid: ' + str(p['ninvalid']))
        print("lvl1: " + str(p['lvl1']) + '\n'),
        print("lvl2: " + str(p['lvl2']) + '\n'),
        print("lvl3: " + str(p['lvl3']) + '\n'),
        print("lvl4: " + str(p['lvl4']) + '\n'),
        print("lvl5: " + str(p['lvl5']) + '\n'),
        print("lvl6: " + str(p['lvl6']) + '\n'),
        print("lvl7: " + str(p['lvl7']) + '\n'),
        print("lvl8: " + str(p['lvl8']) + '\n'),
        print("lvl9: " + str(p['lvl9']) + '\n'),
        print("lvl10: " + str(p['lvl10']) + '\n')
        print('Invalid: ' + str(p['invalid']) + '\n')
