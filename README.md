# n-gram-model-For-Maithili-Language-
This Project is made for n-gram model (here 5-gram model)using python for Maithili language but can be changed for any language, so that I have
made it available for public and improvement can be made.

#n-gram model---
s='This is Rahul Ranjan and I have built the ngram model here'</br></br>
#Unigram -model (1)</br>
[Wordlist(['This']),</br>
 Wordlist(['is']),</br>
 Wordlist(['Rahul']),</br>
 Wordlist(['Ranjan']),</br>
 Wordlist(['and']),</br>
 Wordlist(['I']),</br>
 Wordlist(['have']),</br>
 Wordlist(['built']),</br>
 Wordlist(['the']),</br>
 Wordlist(['ngram']),</br>
 Wordlist(['model']),
 Wordlist(['here'])]
 
#Bigram -model (2)
[Wordlist(['This',' is']),
 Wordlist(['is',' Rahul ']),
 Wordlist(['Rahul',' Ranjan']),
 Wordlist(['Ranjan',' and']),
 Wordlist(['and',' I']),
 Wordlist(['I',' have']),
 Wordlist(['have',' built']),
 Wordlist(['built',' the']),
 Wordlist(['the',' ngram']),
 Wordlist(['ngram',' model']),
 Wordlist(['model','here'])]
 
#Trigram -model (3) 
 [Wordlist(['This',' is', 'Rahul']),
 Wordlist(['is',' Rahul ','Ranjan ']),
 Wordlist(['Rahul',' Ranjan' ,'and']),
 Wordlist(['Ranjan',' and',' I']),
 Wordlist(['and',' I',' have']),
 Wordlist(['I',' have',' built']),
 Wordlist(['have',' built',' the']),
 Wordlist(['built',' the',' ngram']),
 Wordlist(['the',' ngram',' model']),
 Wordlist(['ngram',' model', here'])]
 .... and so on
 This is written just for your understanding - 
 #Implementation of this can be executed as - -
 1.) Download the zip file and Unzip it.
 2.) Run the command - python3 n_gram.py and obtain the 5-gram default set
     you can edit it to obtain n-gram model,where n=1,2,3,....n 
 
 
 
