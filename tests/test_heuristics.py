from router.heuristics import nearest_neighbor, route_duration
import pytest
import numpy as np


def test_correct_route_on_test_tt(small_tt_matrix):
    results = nearest_neighbor(small_tt_matrix)

    expected = [0, 1, 2, 3, 0]

    assert expected == results

def test_correct_route_duration_on_small_matrix(small_tt_matrix):
    route = nearest_neighbor(small_tt_matrix)
    results = route_duration(route, small_tt_matrix)

    expected = 18

    assert expected == results

def test_real_stops_between_0(nn_route):
    assert nn_route[0] == 0
    assert nn_route[-1] == 0

def test_every_stop_appears_once(stops, nn_route):
    middle = nn_route[1:-1]
    assert sorted(middle) == list(range(1, len(stops)))

def test_nn_takes_greedy_route_even_when_not_optimal():
    test_array = np.array([[0, 1, 2, 5],
          [1, 0, 3, 4],
          [2, 3, 0, 7],
          [5, 4, 7, 0]])
    route = nearest_neighbor(test_array)
    assert [0, 1, 2, 3, 0] == route
    assert 16 == route_duration(route, test_array)      # Optimal solution is 14!!
