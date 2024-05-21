#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[12]:


n = 61
if n <= 1:
    is_prime = False
elif n <= 3:
    is_prime = True
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    else:
        is_prime = True

print(is_prime)


# In[ ]:





# In[15]:


n = 10
if n <= 1:
    is_prime = False
elif n <= 3:
    is_prime = True
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    else:
        is_prime = True

print(is_prime)


# In[ ]:
