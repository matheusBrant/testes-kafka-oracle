from kafka import KafkaProducer, KafkaConsumer, KafkaClient
import json
import random
from time import sleep
from datetime import datetime
import pandas as pd
import numpy as np
import time
import random
from random import randint

#'X': '', 'Y': '', 'month': '', 'day': '', 'FFMC': '', 'DMC': '', 'DC': '', 'ISI': '', 'temp': '', 'RH': '','wind': '','rain': '','area': ''}
my_dict = {
    "id": {
    },
    "X": {
    },
    "Y": {
    },
    "FFMC": {
    },
    "DMC": {
    },
    "DC": {
    },
    "ISI": {
    },
    "temp": {
    },
    "RH": {
    },
    "wind": {
    },
    "rain": {
    },
    "area": {
    },
  }

print(my_dict)

for x in range(5):
    my_dict['id'][x] = randint(1,9)
    my_dict['X'][x] = randint(2,9)
    my_dict['Y'][x] = randint(1,9)
    my_dict['FFMC'][x] = randint(18.7,96.2)
    my_dict['DMC'][x] = randint(1.1,291.3)
    my_dict['DC'][x] = randint(7.9,860.6)
    my_dict['ISI'][x] = randint(0,56.10)
    my_dict['temp'][x] = randint(2.2,33.30)
    my_dict['RH'][x] = randint(15,100)
    my_dict['wind'][x] = randint(0.4,9.4)
    my_dict['rain'][x] = randint(0,6.4)
    my_dict['area'][x] = randint(0,1090.84)

with open('data.json', 'w', encoding='utf-8') as outfile:
    json.dump(my_dict, outfile, ensure_ascii=False, indent=2)