#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = 10
b = 20
r = a % b
while(r != 0):
    a = b
    b = r
    r = a % b
else:
    print('最大公約数は{}'.format(b))


# In[2]:


a = 14
b = 91
r = a % b
while(r != 0):
    a = b
    b = r
    r = a % b
else:
    print('最大公約数は{}'.format(b))


# In[3]:


a = 91
b = 14
r = a % b
while(r != 0):
    a = b
    b = r
    r = a % b
else:
    print('最大公約数は{}'.format(b))
