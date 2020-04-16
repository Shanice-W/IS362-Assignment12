#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import json
import urllib.request
from pandas.io.json import json_normalize

api_key = '089beac3eb674ecfb1a42ecb5cb7358c'
url = 'https://api.nytimes.com/svc/mostpopular/v2/mostviewed/Opinion/30.json?limit=100'
string = url+'&api-key='+api_key

response = str(urllib.request.urlopen(string).read(), 'utf-8')

df = pd.read_json(response)
df


# In[6]:


data = json.loads(response)
most_viewed = json_normalize(data['results'])
most_viewed

