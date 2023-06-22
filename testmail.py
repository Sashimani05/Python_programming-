#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[31]:


import smtplib


# In[34]:


sender_email='sashi.rajamani@gfk.com'
receiver_email='sashi.rajamani@gfk.com'


# In[39]:


password='Tanujha-arjun-2020'


# In[35]:


message='hey this is test mail'


# In[37]:


server=smtplib.SMTP('smtp.office365.com',587)


# In[38]:


server.starttls()


# In[40]:


server.login(sender_email,password)


# In[ ]:


print("login Success")


# In[ ]:


server.sendmail(sender_email,receiver_email,message)


# In[ ]:


print("Email sent Successfully")

