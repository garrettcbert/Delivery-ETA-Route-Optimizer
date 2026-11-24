from haversine import haversine
import numpy as np


def distance_matrix(stops):
    matrix = []

    for i in range(len(stops)):
        matrix_row = []
        stop_a = stops.iloc[i]

        for j in range(len(stops)):
            stop_b = stops.iloc[j]

            dist = haversine((stop_a['lat'], stop_a['lon']), (stop_b['lat'], stop_b['lon']))

            matrix_row.append(dist)

        matrix.append(matrix_row)

    return np.array(matrix)

def travel_time_matrix(distances, speed_kmh = 40):
    tt_matrix = (distances / speed_kmh) * 60 # How many minutes it takes between stops
    return tt_matrix
