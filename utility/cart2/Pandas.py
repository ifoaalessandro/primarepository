import numpy as np
import pandas as pd

np.random.seed (667)
mydata = np.random.randint(0,101,(4,3))
# print(mydata)


df = pd.DataFrame(data=mydata)
df
print(df)
df.info()

df = pd.read_csv('tips_complete.csv')
df

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random

#creo un dizionario 
d = {'colonna1': [200,300,400,500]
     'colonna2': [500,400,600,700]
     }

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10)
y = np.exp(x)
from numpy.random import rand
x = rand(1000)
y = rand(1000)
plt.scatter(x,y)
plt.show()