#--------- Series From Scalar Value ------------------
import pandas as pd 
a = [10, 20, 12]
newSeries = pd.Series(a)
print(newSeries)
print('----------------------------------------------------')
#----------------------------------------------------
import pandas as pd 
a = [10, 20, 12]
newSeries = pd.Series(a)
print(newSeries[0])
print('----------------------------------------------------')

#----------------------------------------------------
import pandas as pd 
a = [10, 20, 12]
newSeries = pd.Series(a , index=['x','y','z'])
print(newSeries)
print('----------------------------------------------------')

#---------------------------------------

import pandas as pd 
newSeries = pd.Series(50,index=[5, 1, 2, 3]) 
print(newSeries)
print('----------------------------------------------------')

import pandas as pd
country=["ind","aus","nz"]
cost=[100,200,300]
newSeries= pd.Series(cost,index=country)
print(newSeries)
print('----------------------------------------------------')

#--------- Series From Dictionary ------------------

import pandas as pd
newDictionary= {'Name' : 'Hardik', 'Iplteam' : 'MI', 'Runs' : 1500} 
newSeries = pd.Series(newDictionary)
print(newSeries)
print('----------------------------------------------------')


import pandas as pd
calories = {"Name": 'Virat', "Iplteam": 'RCB', "Runs": 500}
newSeries = pd.Series(calories, index = ["Name", "Iplteam"])
print(newSeries)



#-----------------Data Frame ----------------



