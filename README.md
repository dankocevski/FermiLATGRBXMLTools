# FermiLATGRBXMLTools
A python module to manipulate the Fermi-LAT GRB xml file

#########################################################################################

This module contains a collection of methods to manipulate the public Fermi-LAT xml file

Usage Examples: 

# import the module in ipython
import FermiLATGRBXMLTools

# Read in the xml file
xml = FermiLATGRBXMLTools.xml('PublicTableGRBs.xml')

# Convert the xml file into a space-delimited text file
xml.xml2txt()

# Return data for all GRBs in a single dictionary of numpy arrays
Data = xml.ExtractData()

# List all available data for all Fermi-LAT detected GRBs
Data = xml.ExtractData()
Data.keys()

# List the names of all Fermi-LAT detected GRBs
Data = xml.ExtractData()
Data['GRBNAME']

# List the best available position of all Fermi-LAT detected GRBs
Data = xml.ExtractData()
RA = Data['RA']
DEC = Data['DEC']

# Return data for all GRBs in a single dictionary of individual GRB objects
GRBs = xml.ExtractGRBs()

# Extract the location of an individial GRB
GRBs = xml.ExtractGRBs()
GRB = GRBs['130427324']
print GRB.RA, GRB.DEC


Additional Examples:

# Plot a histogram of the significance of the LAT detections (TS)
import matplotlib.pyplot as plt
import FermiLATGRBXMLTools
xml = FermiLATGRBXMLTools.xml('PublicTableGRBs.xml')					# Open the xml file
Data = xml.ExtractData()								# Extract the data for all bursts
TS = Data['TS'] 									# Extract the TS values for all bursts
logTS = np.log10(TS) 									# Take the log of the TS
logTS = logTS[np.isfinite(logTS)] 							# Excluse any NaN values
plt.hist(logTS, bins=15									# Plot the histogram
plt.xlabel('log TS') 									# Set the plot's x title
plt.ylabel('Number') 									# Set the plot's y title


# Plotting the sky distribution of Fermi-LAT detected GRBs
import numpy as np 									# Import numpy
import matplotlib.pyplot as plt 							# Impory matplotlib
import FermiLATGRBXMLTools 								# Import this module
xml = FermiLATGRBXMLTools.xml('PublicTableGRBs.xml')					# Open the xml file
Data = xml.ExtractData()								# Extract the data for all bursts
RA = Data['RA']										# Extract the RA values for all bursts
Dec = Data['Dec']	 								# Extract the Dec values for all bursts
fig = plt.figure(figsize=(10, 5)) 							# Open a new figure
ax = fig.add_subplot(111, projection="mollweide", axisbg ='white')	 		# Add a new plotting axis in mollweide projection
ax.grid(True) 										# Add a grid
x = np.remainder(RA+360,360) 								# Shift RA values
ind = x>180 										# Find all bursts with RA > 180
x[ind] -= 360 										# Scale conversion to [-180, 180]
x=-x 											# Reverse the scale: East to the left
ax.scatter(np.radians(x),np.radians(Dec)) 						# Plot the RA and DEC data in radians
