import numpy as np
import pytest

def test_correct_shape(stops, matrix):
    assert matrix.shape == (len(stops), len(stops))

def test_diagonal_zeros(matrix):
    assert np.all(np.diag(matrix) == 0.0)

def test_symmetric_matrix(matrix):
    assert np.all(matrix == matrix.T)

def test_correct_distance(matrix):
    assert matrix[0, 1] == pytest.approx(4.25, abs=0.1)

