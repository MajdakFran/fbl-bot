import requests
import json
import time

# opens the names text file in read only mode
starttime = time.time()
data = {}
fp = open("names.txt", "r")
num_lines = sum(1 for line in open('names.txt'))
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 1b2c8397-dcf8-418b-807e-70f08622afa1',
}
line = fp.readline()
cnt = 1
sum = 0
level = 0
lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9, lvl10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
removed = 0
invalid = []
while line and cnt < num_lines:
    line = fp.readline()
    name = line.strip()
    params = (
        ("nickname", name),
    )

    # api request
    response = requests.get(
        'https://open.faceit.com/data/v4/players', headers=headers, params=params)

    # checking if response is not empty
    if str(response) == "<Response [200]>":
        # getting faceit elo from the json
        try:
            r1 = response.json().get("games").get("csgo").get("faceit_elo")
            r2 = response.json().get("games").get("csgo").get("skill_level")
            data[name] = []
            data[name].append({
                'elo': r1,
                'level': r2
            })
            print("#" + str(cnt) + " - " + str(name) +
                  " : " + str(r1) + " - " + str(r2))
            level += r2
            if r2 == 1:
                lvl1 += 1
            elif r2 == 2:
                lvl2 += 1
            elif r2 == 3:
                lvl3 += 1
            elif r2 == 4:
                lvl4 += 1
            elif r2 == 5:
                lvl5 += 1
            elif r2 == 6:
                lvl6 += 1
            elif r2 == 7:
                lvl7 += 1
            elif r2 == 8:
                lvl8 += 1
            elif r2 == 9:
                lvl9 += 1
            elif r2 == 10:
                lvl10 += 1
        except AttributeError:
            print(str(name) + " --- " 'AttributeError')
            invalid.append(name)
            removed += 1
    else:
        print(name, " : ", response)
        removed += 1
        invalid.append(name)

    sum = sum + r1
    cnt += 1

fp.close()
print(cnt)
data['total'] = []
average = sum / (cnt - removed)

data['total'].append({
    "average": round(average, 2),
    "average_level": (level / (cnt - removed)),
    "sum_levels": str(level),
    "lvl1": str(lvl1),
    "lvl2": str(lvl2),
    "lvl3": str(lvl3),
    "lvl4": str(lvl4),
    "lvl5": str(lvl5),
    "lvl6": str(lvl6),
    "lvl7": str(lvl7),
    "lvl8": str(lvl8),
    "lvl9": str(lvl9),
    "lvl10": str(lvl10),
    "sum": sum,
    "ninvalid": removed,
    "invalid": invalid
})
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print('Script took ' + (str(time.time() - starttime)
                        [0: 5]) + ' seconds to run')
