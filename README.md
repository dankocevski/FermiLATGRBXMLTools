# FermiLATGRBXMLTools
A python module to manipulate the Fermi-LAT GRB xml file


This module contains a collection of methods to manipulate the public Fermi-LAT xml file

Usage Examples: 

import the module in ipython
```python
    import FermiLATGRBXMLTools
```

Read in the xml file
```python
    xml = FermiLATGRBXMLTools.xml('PublicTableGRBs.xml')
```

Convert the xml file into a space-delimited text file
```python
    xml.xml2txt()
```

Return data for all GRBs in a single dictionary of numpy arrays
```python
    Data = xml.ExtractData()
```

List all available data for all Fermi-LAT detected GRBs
```python
    Data = xml.ExtractData()
    Data.keys()
```

List the names of all Fermi-LAT detected GRBs
```python
    Data = xml.ExtractData()
    Data['GRBNAME']
```

List the best available position of all Fermi-LAT detected GRBs
```python
    Data = xml.ExtractData()
    RA = Data['RA']
    DEC = Data['DEC']
```

Return data for all GRBs in a single dictionary of individual GRB objects
```python
    GRBs = xml.ExtractGRBs()
```

Extract the location of an individial GRB
```python
    GRBs = xml.ExtractGRBs()
    GRB = GRBs['130427324']
    print GRB.RA, GRB.DEC
```

Additional Examples:

Plot a histogram of the significance of the LAT detections (TS)
```python
    import matplotlib.pyplot as plt
    import FermiLATGRBXMLTools
    xml = FermiLATGRBXMLTools.xml('PublicTableGRBs.xml')
    Data = xml.ExtractData()                               
    TS = Data['TS']                                    
    logTS = np.log10(TS)                                   
    logTS = logTS[np.isfinite(logTS)]                      
    plt.hist(logTS, bins=15                                
    plt.xlabel('log TS')                                   
    plt.ylabel('Number')                                   
    plt.show()
```

Plotting the sky distribution of Fermi-LAT detected GRBs
```python
    import numpy as np                                     
    import matplotlib.pyplot as plt                        
    import FermiLATGRBXMLTools                             
    xml = FermiLATGRBXMLTools.xml('PublicTableGRBs.xml')
    Data = xml.ExtractData()                               
    RA = Data['RA']                                        
    Dec = Data['Dec']                                  
    fig = plt.figure(figsize=(10, 5))                          
    ax = fig.add_subplot(111, projection="mollweide", axisbg ='white')         
    ax.grid(True)                                      
    x = np.remainder(RA+360,360)                           
    ind = x>180                                    
    x[ind] -= 360                                  
    x=-x                                           
    ax.scatter(np.radians(x),np.radians(Dec))                      
    plt.show()
```    