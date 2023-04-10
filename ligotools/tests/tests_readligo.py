import pytest
import numpy as np
from ligotools import read_hdf5

def test_read_hdf5():
    filename = "../../data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    assert len(read_hdf5(filename)) == 7, "Check correct number of outputs"
    assert type(read_hdf5(filename)[0]) == np.ndarray, "Check strain type"
    assert type(read_hdf5(filename)[1]) == np.int64, "Check gpsStart type"
    assert type(read_hdf5(filename)[2]) == np.float64, "Check ts type"
    assert type(read_hdf5(filename)[3]) == np.ndarray, "Check qmask type"
    assert type(read_hdf5(filename)[4]) == list, "Check shortnameList type"
    assert type(read_hdf5(filename)[5]) == np.ndarray, "Check injmask type"
    assert type(read_hdf5(filename)[6]) == list, "Check injnameList type"

