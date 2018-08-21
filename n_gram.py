from textblob import TextBlob

with open ("./maithili_corpus.txt",'r') as f:
  f=f.read()
  
blob = TextBlob(f)

pentagrams = blob.ngrams(n=5)
print(pentagrams)
pentagram=str(pentagrams)
#ngram -writing to a five
with open("./maithili_output_ngram.txt",'w') as out:
    
    out.write(pentagram)
    out.close()
