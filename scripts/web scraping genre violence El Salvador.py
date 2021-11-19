#!/usr/bin/env python
# coding: utf-8

# Import libraries

import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools


# Rules and keywords definition for El Salvador coordinates

loc = '13.794185, -88.89653, 120km'
df = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('keywords since:2020-01-01 until:2020-12-31 geocode:"{}"'.format(loc)).get_items(), 31000))[['user', 'content', 'date', 'coordinates']]
df['user_location'] =  df['user'].apply(lambda x: x['location'])


# Process to anonymize users

del df["user"]
df['User'] = 'Constant Value'
df['User'] = '@anonymized_user'
df.set_index('User', inplace=True)

# Deleting extra spaces

df['content'] = df['content'].str.replace('\n', ' ')


# Save to csv file

df.to_csv("tweetsviolencia4.csv")

#By C.tejada




