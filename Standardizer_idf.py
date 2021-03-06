import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.text import TextCollection
import numpy as np
import random
import json
import urllib
import pprint
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile




class Standardizer:

  #Esta funcion retorna una matriz con los twets y el documetno original estandarizados.   
  # Se asume que el arreglo document esta ordenado 
  def obtener_Twits(listaPalabras, DicPalabras):
    listaPalabrasConsulta = []
    # Esto podria mejorarlo
    # size = len(listaPalabras) / 2
    for x in list(DicPalabras)[0:4]:
      listaPalabrasConsulta.append(x)
    print("Lista de palabras para la consulta: ", listaPalabrasConsulta)

    # Consulta a Twitter, genera un and de las palabras mmas importantes (El espacio es AND logico y , es un OR Logico)
    txt = ' '.join(listaPalabrasConsulta)
    oauth = credsfromfile()
    client = Query(**oauth)
    tweets = client.search_tweets(keywords=txt, limit=10)

    arrTweets = []
    for tweet in tweets:
      arrTweets.append(Standardizer.standardize(tweet['text']))
    return arrTweets

  #Funcion que retorna un arreglo con los la frecuencia de cada uno de los elementos del documento entregado
  def freq(document):
      frecuenciaPalab = [document.count(p) for p in document]
      return(dict(zip(document,frecuenciaPalab)))

  def arr_freq(listaPalabras):
    arrSalida=[]
    for pClave in listaPalabras:
        arrSalida.append(listaPalabras.get(pClave))
    return arrSalida
           
  #def matris_TF(listaPalabras, twets):
  #  for twet in twets:
  #     print("------------------")
  #     print (twet)
  #     dicPalabras = Standardizer.freq(twet)
  #     for pClave in listaPalabras:
  #       if(dicPalabras.get(pClave) == None):
  #         print (pClave,":0")
  #       else:           
  #         print (pClave,":",dicPalabras.get(pClave))
        
  def matris_idftf(listaPalabras, tweets, CantTeets):
    arrIDF = []
    for tweet in tweets:
       print("------------------")
       print(tweet)
       fila = []
       dicPalabras = Standardizer.freq(tweet )
       for pClave in listaPalabras:
         if(dicPalabras.get(pClave) == None):          
           fila.append(0)
         else:         
           ni=Standardizer.teetsQueLaContienen(tweets,pClave)
           print ("idf(",pClave,")=log(",CantTeets,"/",ni,"))log(",CantTeets/ni,")= ",np.log10(CantTeets/ni))
           print("wij= fij X idf=",dicPalabras.get(pClave)," * ", np.log10(CantTeets/ni), "= ",dicPalabras.get(pClave) * np.log10(CantTeets/ni))
           fila.append(dicPalabras.get(pClave) *(np.log10(CantTeets/ni)))

       arrIDF.append(fila)
    return arrIDF
    
    
    
      
  def teetsQueLaContienen(twets, pClave):
    cont = 0
    for twet in twets:
      dicPalabras = Standardizer.freq(twet)
      if(dicPalabras.get(pClave) != None):
        cont = cont + 1
    return cont  
      
    
  @staticmethod
  def standardize(text):
        clean_tokens = word_tokenize(text)[:]
        sr = set(stopwords.words('english'))
        sr.update(['.', ',', '"', "'","The","the","a", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) 
        for token in clean_tokens:
            if token in sr:
                clean_tokens.remove(token)   
        return clean_tokens
     
  def sim(org, doc):
    sum1 = 0
    mult1 = 1
    mult2 = 1
    for i in range(len(org)):
      sum1 = sum1 + org[i] * doc[i]
      mult1 = mult1 + (org[i]**2)
      mult2 = mult2 + (doc[i]**2)
    mult1 = np.sqrt(mult1)
    mult2 = np.sqrt(mult2)
    sumFinal = sum1/(mult1*mult2)
    return sumFinal
  
     
  def main():
    text = "Global warming is a long-term rise in the average temperature of the Earth's climate system, an aspect of climate change shown by temperature measurements and by multiple effects of the warming."
    document = Standardizer.standardize(text)
    dicPalabras = Standardizer.freq(document)
    print(document)
    matris_twest = Standardizer.obtener_Twits(document, dicPalabras)
    arr_idf=Standardizer.matris_idftf(document, matris_twest, len(matris_twest))
    print("Sim entre doc original y doc1:",Standardizer.sim(Standardizer.arr_freq(dicPalabras),arr_idf[0]))
    print("Sim entre doc original y doc2:",Standardizer.sim(Standardizer.arr_freq(dicPalabras),arr_idf[1]))    
    print("Sim entre doc original y doc3:",Standardizer.sim(Standardizer.arr_freq(dicPalabras),arr_idf[2]))
    print("Sim entre doc original y doc4:",Standardizer.sim(Standardizer.arr_freq(dicPalabras),arr_idf[3]))
    print("Sim entre doc original y doc5:",Standardizer.sim(Standardizer.arr_freq(dicPalabras),arr_idf[4]))


    
  
Standardizer.main()



