import pytest
import numpy as np
from ligotools import read_hdf5
from ligotools import readligo as rl
import h5py
import os
import json

def test_read_hdf5():
    filename = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    assert len(read_hdf5(filename)) == 7, "Check correct number of outputs"
    assert type(read_hdf5(filename)[0]) == np.ndarray, "Check strain type"
    assert type(read_hdf5(filename)[1]) == np.int64, "Check gpsStart type"
    assert type(read_hdf5(filename)[2]) == np.float64, "Check ts type"
    assert type(read_hdf5(filename)[3]) == np.ndarray, "Check qmask type"
    assert type(read_hdf5(filename)[4]) == list, "Check shortnameList type"
    assert type(read_hdf5(filename)[5]) == np.ndarray, "Check injmask type"
    assert type(read_hdf5(filename)[6]) == list, "Check injnameList type"


#test FileList.searchdir output matches the hdf5 files in the data directory
def test_FileList_searchdir():
	file_list = rl.FileList("./data")
	files = file_list.searchdir()
	existing_files = ['./data/GW150914_4_template.hdf5',
                      './data/L-L1_LOSC_4_V2-1126259446-32.hdf5',
                      './data/H-H1_LOSC_4_V2-1126259446-32.hdf5']
	for f in files:
		assert f in existing_files

#create a test file and check the output of FileList.findfile is not None
def test_FileList_findfile():    
	arr = np.random.randn(1000)
	with h5py.File('a-L1-4096-32.hdf5', 'w') as f:
		dset = f.create_dataset("default", data = arr)
        
	file_list = rl.FileList()
	filename = file_list.findfile(4096, "L1")
	assert filename is not None

	os.remove('./a-L1-4096-32.hdf5')


def test_loaddata():
    eventname = 'GW150914'
    fnjson = "data/BBH_events_v3.json"
    events = json.load(open(fnjson,"r"))

    event = events[eventname]
    fn_H1 = event['fn_H1']
    fn_L1 = event['fn_L1']

    strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/'+fn_H1, 'H1')
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata('data/'+fn_L1, 'L1')

    assert type(strain_H1) == np.ndarray, "Check the type of H1 strain, suppose to be an array"
    assert type(strain_L1) == np.ndarray, "Check the type of L1 strain, suppose to be an array"
    assert type(time_H1) == np.ndarray, "Check the type of H1 time, suppose to be an array"
    assert type(time_L1) == np.ndarray, "Check the type of L1 time, suppose to be an array"
    assert len(strain_H1) == len(time_H1), "Inconsistence length of strain and time of H1"
    assert len(strain_L1) == len(time_L1), "Inconsistence length of strain and time of L1"
    assert type(chan_dict_H1) == dict, "Check the type of chan_dict_H1"
    assert type(chan_dict_L1) == dict, "Check the type of chan_dict_L1"



