# Startup script for ipython
import scipy.io;
import numpy;
import matplotlib.pyplot as plt;
from analyzedata.fileio import importdata as idata;
import os;

datapath = 'C:\\Users\\Omega\\Documents\\MATLAB\\Data\\';
figurepath = 'C:\\Users\\Omega\\Documents\\MATLAB\\Figures\\';
danpath = 'C:\\Users\\Omega\\Documents\\Programming\\Python\\workspace\\DataAnalysis';

os.chdir(datapath);
