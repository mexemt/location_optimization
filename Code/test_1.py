import numpy as np
import pandas as pd
import csv
from geopy.distance import vincenty
import random

#plz_nrw = pd.read_csv('https://raw.githubusercontent.com/mexemt/location_optimization/master/Datasets/plz_nrw.csv', encoding='unicode_escape')
plz_nrw = pd.read_csv('C:/Users/maxim/Documents/GitHub/location_optimization/Datasets/plz_nrw.csv', encoding='unicode_escape')
plz_nrw = pd.DataFrame(plz_nrw)
distances = pd.read_csv('C:/Users/maxim/Documents/GitHub/location_optimization/Datasets/distances.csv', encoding='unicode_escape', index_col=0)
distances = pd.DataFrame(distances)

class locations:
    def __init__(self, name, plz_nrw, rng):
        self.name = name
        self.locations = plz_nrw
        self.rng = rng
        self.locations['open'] = 0
        self.locations['fixed_costs'] = 0
        self.locations['fixed_costs'] = [random.choice(self.rng) for x in self.locations['fixed_costs']]

rng_cost_fx_low = range(10000, 20000)
loc = locations('low', plz_nrw, rng_cost_fx_low)
locations = loc.locations

print(locations)