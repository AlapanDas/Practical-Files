import numpy as numpy
import matplotlib.pyplot as plt 
from astropy.io import fits
m=fits.open(r"C:\Users\clash\Downloads\frame-u-006073-4-0063.fits")
data=m.data()
data.info()
