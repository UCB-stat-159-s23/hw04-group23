import pytest
import numpy as np
import os
from ligotools import utils as u
from scipy.interpolate import interp1d
from scipy.io import wavfile
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from unittest.mock import patch




def test_whiten():
	strain_H1 = np.array([2, 2])
	Pxx_H1_temp, freqs_temp = mlab.psd(strain_H1, Fs = 4096, NFFT = 4*4096)
	psd_H1 = interp1d(freqs_temp, Pxx_H1_temp)
	dt = np.array([1, 1])
	
	output = u.whiten(strain_H1,psd_H1,dt)
	assert type(output) == np.ndarray, "Check output type"
	
	

#test wav file is created properly
def test_write_wavfile():
	data = np.array([0, 29490])
	u.write_wavfile("test.wav", 1, data) 
	
	f = wavfile.read("test.wav")
	assert (f[1] == np.array(data)).all()
	
	os.remove('test.wav')


#Integer array input should remain the same after calling reqshift on it.
def test_reqshift():
	data = np.array([0, 1, 0, 1])
	shifted_result = u.reqshift(data, 10, 40)
	expected_result = np.array([1, 0, -1, 0])
	assert (expected_result == shifted_result).all()
	
	
@patch("matplotlib.pyplot.show")
def test_plot_results(mock_show):
	input_array = np.array([1])

	timemax = 1126259462.432373
	SNR = input_array
	pcolor = 'g'
	det = 'L1'
	tevent = 1126259462.44
	strain_whitenbp = input_array
	template_match = input_array
	datafreq = input_array
	template_fft = input_array
	data_psd = input_array
	d_eff = 999.7431303063776
	time = input_array
	eventname = 'GW150914'
	plottype = 'png'
	freqs = input_array
	fs = 4096
	u.plot_results(timemax, SNR, pcolor, det, tevent, strain_whitenbp, template_match, 
				datafreq, template_fft, data_psd, d_eff, time, eventname, plottype, freqs, fs)
	
	[os.remove(file) for file in os.listdir('.') if file.endswith('.png')]