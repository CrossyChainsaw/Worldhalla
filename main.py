import json
from api3 import clan_request
from keep_alive import keep_alive
from transport_data import transport_data
from get_clans import get_clans

# started 17 sep 2022

# VARIABLES
global start_id
start_id = 0
json_file = 'clans' + '.json'
target_file = 'clans(1468700+)' + '.json'

# get data a
with open(json_file) as data_a:
  data_a = json.load(data_a)
# transport data if not empty
if len(data_a) > 0:
  transport_data(json_file, target_file)

# get data b
with open(target_file) as data_b:
  data_b = json.load(data_b)
# new starting point if theres already data
if len(data_b) > 0:
  last_saved_id = data_b[-1]['clan_id']
  start_id = last_saved_id + 1
  print('Set id to ' + str(start_id))

# get data
get_clans(json_file, start_id)
















keep_alive()
