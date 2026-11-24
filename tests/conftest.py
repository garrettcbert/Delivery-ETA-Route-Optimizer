import pytest
from router.load import load_stops
from router.distance import distance_matrix, travel_time_matrix
from router.heuristics import nearest_neighbor
from pathlib import Path
import numpy as np


STOPS_CSV = Path(__file__).parent.parent / 'data' / 'stops.csv'

@pytest.fixture
def stops():
    return load_stops(STOPS_CSV)

@pytest.fixture
def dist_matrix(stops):
    return distance_matrix(stops)

@pytest.fixture
def tt_matrix(dist_matrix):
    return travel_time_matrix(dist_matrix)

@pytest.fixture
def small_tt_matrix():
    return np.array([[0, 4, 9, 6],[4, 0, 3, 8],[9, 3, 0, 5],[6, 8, 5, 0]])

@pytest.fixture
def nn_route(tt_matrix):
    return nearest_neighbor(tt_matrix)