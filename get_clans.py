import json
from api3 import clan_request

class Clan:
    def __init__(self, name, id):
        self.clan_name = name
        self.clan_id = id


def get_clans(json_file, n):
    print("Start getting data, starting from " + str(n))
    # load data
    with open(json_file) as data:
        all_clans_data = json.load(data)

    # if empty start getting data
    if (len(all_clans_data) == 0):
        while n < 10000000:
            try:
                with open(json_file) as data:
                    all_clans_data = json.load(data)
                clan_data = json.loads(clan_request(n).content)
                name = clan_data["clan_name"]
                id = clan_data["clan_id"]
                all_clans_data.append(Clan(name, id).__dict__)
                with open(json_file, 'w') as f:
                    all_clans_data = json.dump(all_clans_data, f)
            except:
                print(str(n) + " doesn't exist")

            n += 1
