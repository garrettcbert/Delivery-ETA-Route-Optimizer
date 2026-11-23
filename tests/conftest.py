import pytest
from router.load import load_stops
from router.distance import distance_matrix
from pathlib import Path


STOPS_CSV = Path(__file__).parent.parent / 'data' / 'stops.csv'

@pytest.fixture
def stops():
    return load_stops(STOPS_CSV)

@pytest.fixture
def matrix(stops):
    return distance_matrix(stops)