import requests
import time

starttime = time.time()

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 1b2c8397-dcf8-418b-807e-70f08622afa1',
}

joined = requests.get(
    "https://open.faceit.com/data/v4/hubs/74a2bd2d-396d-4c81-955a-dc8608773937", headers=headers)
num = int(joined.json()["players_joined"])

print(num)
print('Script took ' + (str(time.time() - starttime)
                        [0: 5]) + ' seconds to run')
