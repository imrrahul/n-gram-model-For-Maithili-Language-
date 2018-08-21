# n-gram-model-For-Maithili-Language-
This Project is made for n-gram model (here 5-gram model)using python for Maithili language but can be changed for any language, so that I have
made it available for public and improvement can be made.</br></br>

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
 Wordlist(['model']),</br></br>
 Wordlist(['here'])]</br</br>
 
#Bigram -model(2)</br></br>
[Wordlist(['This',' is']),</br>
 Wordlist(['is',' Rahul ']),</br>
 Wordlist(['Rahul',' Ranjan']),</br>
 Wordlist(['Ranjan',' and']),</br>
 Wordlist(['and',' I']),</br>
 Wordlist(['I',' have']),</br>
 Wordlist(['have',' built']),</br>
 Wordlist(['built',' the']),</br>
 Wordlist(['the',' ngram']),</br>
 Wordlist(['ngram',' model']),</br>
 Wordlist(['model','here'])]</br>
 
#Trigram -model (3) </br></br>
 [Wordlist(['This',' is', 'Rahul']),</br>
 Wordlist(['is',' Rahul ','Ranjan ']),</br>
 Wordlist(['Rahul',' Ranjan' ,'and']),</br>
 Wordlist(['Ranjan',' and',' I']),</br>
 Wordlist(['and',' I',' have']),</br>
 Wordlist(['I',' have',' built']),</br>
 Wordlist(['have',' built',' the']),</br>
 Wordlist(['built',' the',' ngram']),</br>
 Wordlist(['the',' ngram',' model']),</br>
 Wordlist(['ngram',' model', here'])]</br></br>
 .... and so on
 This is written just for your understanding - </br></br>
 #Implementation of this can be executed as - -</br>
 1.) Download the zip file and Unzip it.</br>
 2.) Run the command - python3 n_gram.py and obtain the 5-gram default set
     you can edit it to obtain n-gram model,where n=1,2,3,....n </br>
 
 
 
