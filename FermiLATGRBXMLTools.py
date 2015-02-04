"""
A collection of tools to manipulate the public Fermi-LAT xml file

Common Usage:
import PublicTableXMLTools

# Read in the xml file
xml = PublicTableXMLTools.xml('PublicTableGRBs.xml')

# Convert the xml file into a space-delimited text file
xml.xml2txt()

# Return data for all GRBs in a single dictionary of numpy arrays
Data = xml.ExtractData()

# List all available data 
Data = xml.ExtractData()
Data.keys()

# List all available GRB names
Data = xml.ExtractData()
Data['GRBNAME']

# Return data for all GRBs in a single dictionary of individual GRB objects
GRBs = xml.ExtractGRBs()

# Extract information regarding an individial GRB
GRBs = xml.ExtractGRBs()
GRB = GRBs['130427324']
print GRB.RA, GRB.DEC
"""

import sys
import numpy



##########################################################################################

class GRB(object):
	"""A GRB object"""

	
	def __init__(self,GRBNAME=None,GCNNAME=None,MET=None,DATE=None,TIME=None,RA=None,DEC=None,ERROR=None,POSITIONSOURCE=None,THETA=None,ZENITH=None,BELOW75MEVDETECTION=None,ABOVE75MEVDETECTION=None,LLESIGMA=None,TS=None,LIKESTART=None,LIKESTOP=None,LATRA=None,LATDEC=None,LATERROR=None,IRF=None):		
		self.GRBNAME = GRBNAME
		self.GCNNAME = GCNNAME
		self.MET = MET
		self.DATE = DATE
		self.TIME = TIME
		self.RA = RA
		self.DEC = DEC
		self.ERROR = ERROR
		self.POSITIONSOURCE = POSITIONSOURCE
		self.THETA = THETA
		self.ZENITH = ZENITH
		self.BELOW75MEVDETECTION = BELOW75MEVDETECTION
		self.ABOVE75MEVDETECTION = ABOVE75MEVDETECTION
		self.LLESIGMA = LLESIGMA
		self.TS = TS
		self.LIKESTART = LIKESTART
		self.LIKESTOP = LIKESTOP
		self.LATRA = LATRA
		self.LATDEC = LATDEC
		self.LATERROR = LATERROR
		self.IRF = IRF


##########################################################################################		

class xml:
	"""A xml file object"""
	
	def __init__(self,Filename):		
		self.Filename = Filename
		
	def xml2txt(self):
	
		# Read in the entire xml file    
		lines = iter(open(self.Filename, 'r'))
		
		# Loop through the lines and extract information
		newline = ''
		for line in lines:
			line = line.rstrip('\n')
			if '<GRBNAME>' in line:
				line = line.replace('<GRBNAME>','')
				line = line.replace('</GRBNAME>','')
				line = line.strip()
				newline = newline + " " + line
			if '<GCNNAME>' in line:
				line = line.replace('<GCNNAME>','')
				line = line.replace('</GCNNAME>','')
				line = line.strip()
				newline = newline + " " + line
			if '<MET>' in line:
				line = line.replace('<MET>','')
				line = line.replace('</MET>','')
				line = line.strip()
				newline = newline + " " + line				
			if '<DATE>' in line:
				line = line.replace('<DATE>','')
				line = line.replace('</DATE>','')
				line = line.strip()
				newline = newline + " " + line		
			if '<TIME>' in line:
				line = line.replace('<TIME>','')
				line = line.replace('</TIME>','')
				line = line.strip()
				newline = newline + " " + line		
			if '<RA>' in line:
				line = line.replace('<RA>','')
				line = line.replace('</RA>','')
				line = line.strip()
				newline = newline + " " + line		
			if '<DEC>' in line:
				line = line.replace('<DEC>','')
				line = line.replace('</DEC>','')
				line = line.strip()
				newline = newline + " " + line														
			if '<ERROR>' in line:
				line = line.replace('<ERROR>','')
				line = line.replace('</ERROR>','')
				line = line.strip()
				newline = newline + " " + line	
			if '<POSITIONSOURCE>' in line:
				line = line.replace('<POSITIONSOURCE>','')
				line = line.replace('</POSITIONSOURCE>','')
				line = line.strip()
				newline = newline + " " + line					
			if '<THETA>' in line:
				line = line.replace('<THETA>','')
				line = line.replace('</THETA>','')
				line = line.strip()
				newline = newline + " " + line	
			if '<ZENITH>' in line:
				line = line.replace('<ZENITH>','')
				line = line.replace('</ZENITH>','')
				line = line.strip()
				newline = newline + " " + line	
			if '<BELOW75MEVDETECTION>' in line:
				line = line.replace('<BELOW75MEVDETECTION>','')
				line = line.replace('</BELOW75MEVDETECTION>','')
				line = line.strip()
				newline = newline + " " + line									
			if '<ABOVE75MEVDETECTION>' in line:
				line = line.replace('<ABOVE75MEVDETECTION>','')
				line = line.replace('</ABOVE75MEVDETECTION>','')
				line = line.strip()
				newline = newline + " " + line
			if '<LLESIGMA>' in line:
				line = line.replace('<LLESIGMA>','')
				line = line.replace('</LLESIGMA>','')
				line = line.strip()
				newline = newline + " " + line								
			if '<TS>' in line:
				line = line.replace('<TS>','')
				line = line.replace('</TS>','')
				line = line.strip()
				newline = newline + " " + line
			if '<LIKESTART>' in line:
				line = line.replace('<LIKESTART>','')
				line = line.replace('</LIKESTART>','')
				line = line.strip()
				newline = newline + " " + line				
			if '<LIKESTOP>' in line:
				line = line.replace('<LIKESTOP>','')
				line = line.replace('</LIKESTOP>','')
				line = line.strip()
				newline = newline + " " + line				
			if '<LATRA>' in line:
				line = line.replace('<LATRA>','')
				line = line.replace('</LATRA>','')
				line = line.strip()
				newline = newline + " " + line
			if '<LATDEC>' in line:
				line = line.replace('<LATDEC>','')
				line = line.replace('</LATDEC>','')
				line = line.strip()
				newline = newline + " " + line									
			if '<LATERROR>' in line:
				line = line.replace('<LATERROR>','')
				line = line.replace('</LATERROR>','')
				line = line.strip()
				newline = newline + " " + line					
			if '<IRF>' in line:
				line = line.replace('<IRF>','')
				line = line.replace('</IRF>','')
				line = line.strip()
				newline = newline + " " + line	
			if '</GRB>' in line:
				newline = newline + '\n'
			if '</ALLGRBS>' in line:
				print newline

#	#########################################################################################

	def ExtractData(self):
		"""Return data for all GRBs in a single dictionary of numpy arrays.\n Exampple:\nData = xml.ExtractData()"""
	
		# Read in the entire xml file    
		lines = iter(open(self.Filename, 'r'))
		
		GRBNAME = numpy.array([])
		GCNNAME = numpy.array([])
		MET = numpy.array([])
		DATE = numpy.array([])
		TIME = numpy.array([])
		RA = numpy.array([])
		DEC = numpy.array([])
		ERROR = numpy.array([])
		POSITIONSOURCE = numpy.array([])
		THETA = numpy.array([])
		ZENITH = numpy.array([])
		BELOW75MEVDETECTION = numpy.array([])
		ABOVE75MEVDETECTION = numpy.array([])
		LLESIGMA = numpy.array([])
		TS = numpy.array([])
		LIKESTART = numpy.array([])
		LIKESTOP = numpy.array([])
		LATRA = numpy.array([])
		LATDEC = numpy.array([])
		LATERROR = numpy.array([])
		IRF = numpy.array([])
		
		
		# Loop through the lines and extract information
		newline = ''
		for line in lines:
			line = line.rstrip('\n')
			line = line.replace('--','NaN')
			
			if '<GRBNAME>' in line:
				line = line.replace('<GRBNAME>','')
				line = line.replace('</GRBNAME>','')
				line = line.strip()
				GRBNAME = numpy.append(GRBNAME,line)
			if '<GCNNAME>' in line:
				line = line.replace('<GCNNAME>','')
				line = line.replace('</GCNNAME>','')
				line = line.strip()
				GCNNAME = numpy.append(GCNNAME,line)
			if '<MET>' in line:
				line = line.replace('<MET>','')
				line = line.replace('</MET>','')
				line = line.strip()
				MET = numpy.append(MET,float(line))			
			if '<DATE>' in line:
				line = line.replace('<DATE>','')
				line = line.replace('</DATE>','')
				line = line.strip()
				DATE = numpy.append(DATE,line)	
			if '<TIME>' in line:
				line = line.replace('<TIME>','')
				line = line.replace('</TIME>','')
				line = line.strip()
				TIME = numpy.append(TIME,line)		
			if '<RA>' in line:
				line = line.replace('<RA>','')
				line = line.replace('</RA>','')
				line = line.strip()
				RA = numpy.append(RA,float(line))		
			if '<DEC>' in line:
				line = line.replace('<DEC>','')
				line = line.replace('</DEC>','')
				line = line.strip()
				DEC = numpy.append(DEC,float(line))														
			if '<ERROR>' in line:
				line = line.replace('<ERROR>','')
				line = line.replace('</ERROR>','')
				line = line.strip()
				ERROR = numpy.append(ERROR,float(line))
			if '<POSITIONSOURCE>' in line:
				line = line.replace('<POSITIONSOURCE>','')
				line = line.replace('</POSITIONSOURCE>','')
				line = line.strip()
				POSITIONSOURCE = numpy.append(POSITIONSOURCE,line)				
			if '<THETA>' in line:
				line = line.replace('<THETA>','')
				line = line.replace('</THETA>','')
				line = line.strip()
				THETA = numpy.append(THETA,float(line))	
			if '<ZENITH>' in line:
				line = line.replace('<ZENITH>','')
				line = line.replace('</ZENITH>','')
				line = line.strip()
				ZENITH = numpy.append(ZENITH,float(line))
			if '<BELOW75MEVDETECTION>' in line:
				line = line.replace('<BELOW75MEVDETECTION>','')
				line = line.replace('</BELOW75MEVDETECTION>','')
				line = line.strip()
				if 'YES' in line:
					BELOW75MEVDETECTION = numpy.append(BELOW75MEVDETECTION,True)	
				else:
					BELOW75MEVDETECTION = numpy.append(BELOW75MEVDETECTION,False)								
			if '<ABOVE75MEVDETECTION>' in line:
				line = line.replace('<ABOVE75MEVDETECTION>','')
				line = line.replace('</ABOVE75MEVDETECTION>','')
				line = line.strip()
				if 'YES' in line:
					ABOVE75MEVDETECTION = numpy.append(ABOVE75MEVDETECTION,True)
				else:
					ABOVE75MEVDETECTION = numpy.append(ABOVE75MEVDETECTION,False)
			if '<LLESIGMA>' in line:
				line = line.replace('<LLESIGMA>','')
				line = line.replace('</LLESIGMA>','')
				line = line.strip()
				LLESIGMA = numpy.append(LLESIGMA,float(line))					
			if '<TS>' in line:
				line = line.replace('<TS>','')
				line = line.replace('</TS>','')
				line = line.strip()
				TS = numpy.append(TS,float(line))
			if '<LIKESTART>' in line:
				line = line.replace('<LIKESTART>','')
				line = line.replace('</LIKESTART>','')
				line = line.strip()
				LIKESTART = numpy.append(LIKESTART,float(line))				
			if '<LIKESTOP>' in line:
				line = line.replace('<LIKESTOP>','')
				line = line.replace('</LIKESTOP>','')
				line = line.strip()
				LIKESTOP = numpy.append(LIKESTOP,float(line))				
			if '<LATRA>' in line:
				line = line.replace('<LATRA>','')
				line = line.replace('</LATRA>','')
				line = line.strip()
				LATRA = numpy.append(LATRA,float(line))
			if '<LATDEC>' in line:
				line = line.replace('<LATDEC>','')
				line = line.replace('</LATDEC>','')
				line = line.strip()
				LATDEC = numpy.append(LATDEC,float(line))									
			if '<LATERROR>' in line:
				line = line.replace('<LATERROR>','')
				line = line.replace('</LATERROR>','')
				line = line.strip()
				LATERROR = numpy.append(LATERROR,float(line))				
			if '<IRF>' in line:
				line = line.replace('<IRF>','')
				line = line.replace('</IRF>','')
				line = line.strip()
				IRF = numpy.append(IRF,line)	
			if '</ALLGRBS>' in line:
			
				dictionary = {'GRBNAME':GRBNAME, 'GCNNAME':GCNNAME, 'MET':MET, 'DATE':DATE, 'TIME':TIME, 'RA':RA, 'DEC':DEC, 'ERROR':ERROR, 'POSITIONSOURCE':POSITIONSOURCE, 'THETA':THETA, 'ZENITH':ZENITH, 'BELOW75MEVDETECTION':BELOW75MEVDETECTION, 'ABOVE75MEVDETECTION':ABOVE75MEVDETECTION, 'LLESIGMA':LLESIGMA, 'TS':TS, 'LIKESTART':LIKESTART, 'LIKESTOP':LIKESTOP, 'LATRA':LATRA, 'LATDEC':LATDEC, 'LATERROR':LATERROR, 'IRF':IRF}
			
				return dictionary
				

	##########################################################################################				
									
	def ExtractGRBs(self):
			
		# Create a dictionary to contain all of the GRB objects
		GRBs = {}
		
		# Read in the entire xml file    
		lines = iter(open(self.Filename, 'r'))
		
		# Loop through the lines and extract information
		for line in lines:
			line = line.rstrip('\n')
			if '<GRBNAME>' in line:
					# Create a GRB object
				aGRB = GRB()
				line = line.replace('<GRBNAME>','')
				line = line.replace('</GRBNAME>','')
				line = line.strip()
				GRBNAME = line
				aGRB.GRBNAME = line
			if '<GCNNAME>' in line:
				line = line.replace('<GCNNAME>','')
				line = line.replace('</GCNNAME>','')
				line = line.strip()
				aGRB.GCNNAME = line
			if '<MET>' in line:
				line = line.replace('<MET>','')
				line = line.replace('</MET>','')
				line = line.strip()
				aGRB.MET = line				
			if '<DATE>' in line:
				line = line.replace('<DATE>','')
				line = line.replace('</DATE>','')
				line = line.strip()
				aGRB.DATE = line		
			if '<TIME>' in line:
				line = line.replace('<TIME>','')
				line = line.replace('</TIME>','')
				line = line.strip()
				aGRB.TIME = line		
			if '<RA>' in line:
				line = line.replace('<RA>','')
				line = line.replace('</RA>','')
				line = line.strip()
				aGRB.RA = line		
			if '<DEC>' in line:
				line = line.replace('<DEC>','')
				line = line.replace('</DEC>','')
				line = line.strip()
				aGRB.DEC = line														
			if '<ERROR>' in line:
				line = line.replace('<ERROR>','')
				line = line.replace('</ERROR>','')
				line = line.strip()
				aGRB.ERROR = line	
			if '<POSITIONSOURCE>' in line:
				line = line.replace('<POSITIONSOURCE>','')
				line = line.replace('</POSITIONSOURCE>','')
				line = line.strip()
				aGRB.POSITIONSOURCE = line					
			if '<THETA>' in line:
				line = line.replace('<THETA>','')
				line = line.replace('</THETA>','')
				line = line.strip()
				aGRB.THETA = line	
			if '<ZENITH>' in line:
				line = line.replace('<ZENITH>','')
				line = line.replace('</ZENITH>','')
				line = line.strip()
				aGRB.ZENITH = line	
			if '<BELOW75MEVDETECTION>' in line:
				line = line.replace('<BELOW75MEVDETECTION>','')
				line = line.replace('</BELOW75MEVDETECTION>','')
				line = line.strip()
				aGRB.BELOW75MEVDETECTION = line									
			if '<ABOVE75MEVDETECTION>' in line:
				line = line.replace('<ABOVE75MEVDETECTION>','')
				line = line.replace('</ABOVE75MEVDETECTION>','')
				line = line.strip()
				aGRB.ABOVE75MEVDETECTION = line
			if '<LLESIGMA>' in line:
				line = line.replace('<LLESIGMA>','')
				line = line.replace('</LLESIGMA>','')
				line = line.strip()
				aGRB.LLESIGMA = line								
			if '<TS>' in line:
				line = line.replace('<TS>','')
				line = line.replace('</TS>','')
				line = line.strip()
				aGRB.TS = line
			if '<LIKESTART>' in line:
				line = line.replace('<LIKESTART>','')
				line = line.replace('</LIKESTART>','')
				line = line.strip()
				aGRB.LIKESTART = line				
			if '<LIKESTOP>' in line:
				line = line.replace('<LIKESTOP>','')
				line = line.replace('</LIKESTOP>','')
				line = line.strip()
				aGRB.LIKESTOP = line				
			if '<LATRA>' in line:
				line = line.replace('<LATRA>','')
				line = line.replace('</LATRA>','')
				line = line.strip()
				aGRB.LATRA = line
			if '<LATDEC>' in line:
				line = line.replace('<LATDEC>','')
				line = line.replace('</LATDEC>','')
				line = line.strip()
				aGRB.LATDEC = line									
			if '<LATERROR>' in line:
				line = line.replace('<LATERROR>','')
				line = line.replace('</LATERROR>','')
				line = line.strip()
				aGRB.LATERROR = line					
			if '<IRF>' in line:
				line = line.replace('<IRF>','')
				line = line.replace('</IRF>','')
				line = line.strip()
				aGRB.IRF = line	
			if '</GRB>' in line:
				GRBs[GRBNAME] = aGRB
				del aGRB
			if '</ALLGRBS>' in line:
				return GRBs

	##########################################################################################

	def Compare(self,Filename):
	
		# Get the list of LAT detections
		Data = self.ExtractData()
		GCNNAME = Data['GCNNAME']
		
		# Create an empty list to contain the overlapping bursts
		GRBs_Union = []
				
		# Open the list of GRBs to compare to the LAT detections
		GRBs = open(Filename, 'r')
		for GRB in GRBs:
			GRB = GRB.strip()
			if GRB in GCNNAME:
				GRBs_Union.append(GRB)
		
		return GRBs_Union
					
				        
##########################################################################################





