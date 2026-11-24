import numpy as np
import pytest
from router.distance import travel_time_matrix

def test_correct_shape(stops, dist_matrix):
    assert dist_matrix.shape == (len(stops), len(stops))

def test_diagonal_zeros(dist_matrix):
    assert np.all(np.diag(dist_matrix) == 0.0)

def test_symmetric_matrix(dist_matrix):
    assert np.all(dist_matrix == dist_matrix.T)

def test_correct_distance(dist_matrix):
    assert dist_matrix[0, 1] == pytest.approx(4.25, abs=0.1)

def test_20km_at_40kms_is_30_mins():
    test_dists = np.array([[0, 20], [20, 0]])
    times = travel_time_matrix(test_dists, speed_kmh=40)

    assert times[0, 1] == pytest.approx(30)

def test_speed_param():
    test_dists = np.array([[0, 20], [20, 0]])

    times_60 = travel_time_matrix(test_dists, speed_kmh=60)

    assert times_60[1, 0] == pytest.approx(20)

def test_input_same_shape_as_output(dist_matrix, tt_matrix):
    assert dist_matrix.shape == tt_matrix.shape

def test_zeros_in_tt_matrix(tt_matrix):
    assert np.all(np.diag(tt_matrix) == 0.0)