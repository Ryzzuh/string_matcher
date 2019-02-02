#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', 1000)
pd.options.display.max_rows = 100
import os
cwd = os.getcwd()
import jellyfish as jf
import math
import re


def main():
  """ Main program """
  # Code goes over here.
  print("Welcome to string matcher")
  file = pd.read_excel(cwd+"/DNSW_poorly_named_campaigns.xlsx")
  df = pd.DataFrame(file)
  #print(df)

  bad_terms = df['All terms']
  good_terms = df.dropna()['Approved terms']
  #print(bad_terms)
  #print(good_terms)

  d = dict.fromkeys(good_terms,0)
  for good in d:
    d[good] = []
    for bad in bad_terms:
      print(re.sub(r'\W+', '', good))
      score = jf.levenshtein_distance(re.sub(r'[\W_]+', '', good), re.sub(r'\W+', '', bad))
      if score < math.ceil(0.2*len(good)):
        d[good].append(bad)
        #print('{} | {} | {}'.format(good, bad, jf.levenshtein_distance(good, bad)))

  df = pd.DataFrame.from_dict(d, orient= 'index')
  df = df.transpose()
  df.to_excel('output.xlsx')

  #print(d)


  
if __name__ == "__main__":
  main()