# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:24:33 2021

@author: nofar
"""
fhand = open('text.txt')
textFile = fhand.read()

def revword (word):
    word = word[::-1]
    word=word.lower()
    return word

def countword () :
    word = textFile.split()[0]
    counter = 1
    a = 1
    while a < len(textFile.split()):        
        new_Word = revword(textFile.split()[a])
        if new_Word == word:
              counter=counter+1   
        a=a+1
    return(counter)


            
                
                
                
            
    
 
