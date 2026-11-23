import pytest
from router.load import load_stops
from pathlib import Path


STOPS_CSV = Path(__file__).parent.parent / 'data' / 'stops.csv'

@pytest.fixture
def stops():
    return load_stops(STOPS_CSV)