import json

def transport_data(json_file_a, json_file_b):
    print('Start transporting data')
  
    # get data
    with open(json_file_a) as data_a:
      data_a = json.load(data_a)
    with open(json_file_b) as data_b:
      data_b = json.load(data_b)

    # transport data
    while len(data_a) > 0:
      data_b.append(data_a.pop(0))

    # save data
    with open(json_file_b, 'w') as f:
      json.dump(data_b, f)
    with open(json_file_a, 'w') as f:
      json.dump(data_a, f)