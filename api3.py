import requests
import time
import os


def clan_request(id):
    time.sleep(7)  # 0.10 might be possible
    return requests.get("https://api.brawlhalla.com/clan/" + str(id) + "/?api_key=" + os.environ['API_KEY'])
