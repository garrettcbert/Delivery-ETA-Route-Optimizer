import pytest

def test_row_count(stops):
    assert len(stops) == 10

def test_sequential_ids(stops):
    ids = stops['id'].to_list()
    assert ids == list(range(len(stops)))

def test_columns(stops):
    assert list(stops.columns) == ['id', 'lat', 'lon', 'service_minutes']

def test_depot_has_id_zero(stops):
    depot = stops.iloc[0]

    assert depot['id'] == 0

def test_depot_has_zero_service(stops):
    depot = stops.iloc[0]

    assert depot['service_minutes'] == 0