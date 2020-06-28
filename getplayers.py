import requests
import time

starttime = time.time()

offset = 0
cnt = 0

of = open('names.txt', 'w')

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 1b2c8397-dcf8-418b-807e-70f08622afa1',
}

joined = requests.get(
    "https://open.faceit.com/data/v4/hubs/74a2bd2d-396d-4c81-955a-dc8608773937", headers=headers)
num = int(joined.json()["players_joined"])

for i in range(0, num):

    players = requests.get(
        "https://open.faceit.com/data/v4/hubs/74a2bd2d-396d-4c81-955a-dc8608773937/members?offset=" + str(offset) + "&limit=100", headers=headers)

    if num - offset >= 100:
        offset += 100
    elif num - offset < 100:
        offset -= num % 100
    try:
        for i in players.json()['items']:
            cnt += 1
            of.write(str(i['nickname']) + '\n')
            print(str(cnt) + ' ---- ' + str(i['nickname']))
            if offset == num:
                break
                print('Wrote ' + str(num) + ' lines')
    except:
        break
print('Script took ' + (str(time.time() - starttime)
                        [0: 5]) + ' seconds to run')
