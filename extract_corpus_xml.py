#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:19:34 2018

@author: rahul
"""

from bs4 import BeautifulSoup
with open('./maithili_corpus.txt','r') as ht:
    hmm  = ht.read()
    soup = BeautifulSoup(hmm,'lxml')
    new=soup.text
print (new)
with open('./extract.txt','w') as e:
        for word in new:
            word = u' '.join((new, word)).encode('utf-8').strip()
            e.write("%s \n" % (word)) 
        e.close()
        
