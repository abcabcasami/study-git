#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
s = 0
for i in range(100):
    s += (math.pi /400) * (math.sin((i * math.pi)/ 200) + math.sin(((i +1) * math.pi) / 200 ) ) 
print(s)


# In[ ]:

