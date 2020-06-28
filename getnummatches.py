import requests

offset = 0
cnt = 0
ids = []
of = open('ids.txt', 'w')

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer 1b2c8397-dcf8-418b-807e-70f08622afa1',
}


def getjson():
    joined = requests.get(
        "https://open.faceit.com/data/v4/hubs/74a2bd2d-396d-4c81-955a-dc8608773937/matches?type=past&offset=" +
        str(offset) + " &limit=100", headers=headers)
    for i in joined.json()['items']:
        if str(i['match_id']) not in ids:
            ids.append(str(i['match_id']))
            of.write(str(i['match_id']) + '\n')
        else:
            return False


getjson()

while getjson():
    offset += 100
    try:
        getjson()
        print(len(ids))
    except:
        print("najmedenes")
print(len(ids))
print(ids)
