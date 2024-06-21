from sherpa.astro.ui import *
import numpy

# Read from NED VOTable; ignore warnings that come from
# out-of-date DEFINITION tag, conversions of column names
# with spaces.

import warnings
warnings.simplefilter("ignore") 

from vo.table import parse_single_table
tbl = parse_single_table('3c273_sed.xml', pedantic=False)

### BEGIN processing NED VOTable

# Here, create a mask that will filter out:
# Line measurements, as indicated in 'Frequency Mode' column
# Entries with no uncertainty, or uncertainty == zero

# Note: uncertainties are encoded as strings in the form
# "+/-X.YZ" and must be conveted to floats X.YZ

# I set a mask that filters out all line measurements, uncertainties
# that were either zero or unable to be converted to float. This
# mask will be passed to Sherpa as a filter.
ndata = len(tbl.array['NED Photometry Measurement'])
staterrors = numpy.zeros(ndata)
datamask = numpy.ones(ndata, dtype='bool')

for entry in xrange(ndata):
  mode = tbl.array['Frequency Mode'][entry]
  if (mode.lower().count('line') > 0):
    datamask[entry] = False
  error = tbl.array['NED Uncertainty'][entry]
  if (error == ''):
    datamask[entry] = False
  else:
    try:
      error = float(error[3:])
      if (error > 0.0):
        staterrors[entry] = error
      else:
        datamask[entry] = False
    except:
      datamask[entry] = False
      staterrors[entry] = 0.0

### END processing of NED VOtable.

# Create a Sherpa data set, based on arrays peeled out of the
# VOTable we read in.
load_arrays(1, tbl.array['Frequency'], tbl.array['NED Photometry Measurement'], staterrors)

# Filter out data points that were line measurements or had no usable
# uncertainties
set_filter(1, datamask)

# Change data plot to log space, with new title
get_data_plot_prefs()['xlog'] = True
get_data_plot_prefs()['ylog'] = True
plot_data()
set_plot_xlabel("log frequency (Hz)")
set_plot_ylabel("log F (Jy)")
set_plot_title("3C 273 SED")

# Set statistic to chi-squared with data variance; set initial parameters
# and fit power-law
set_stat("chi2datavar")
set_method("neldermead")
set_source(bpl1d.p1)
guess(p1)
p1.eb=5e12
raw_input("Press Return to fit:")
#p1.ref = 1
#p1.ampl.max = 1e15
#p1.ampl.min = 1
#p1.ampl = 1e12
fit()

# Show model overplotting data
ignore(1e20)
plot_fit()
set_plot_xlabel("log frequency (Hz)")
set_plot_ylabel("log F (Jy)")
set_plot_title("3C 273 SED (from NED), Sherpa Broken Power-law Fit")
set_plot(["title.size",20])
set_xaxis(["tickformat","%0.0z","label.size",18])
set_yaxis(["tickformat","%0.0z","label.size",18])
set_xaxis(["ticklabel.size",14])
set_yaxis(["ticklabel.size",14])
#print_window("3c273_sed_fit.pdf",["fittopage", True, "clobber", True])

# Call conf() to get 3-sigma confidence limits
#set_conf_opt("sigma", 3)
#conf()
