import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.text import TextCollection

import numpy as np
## from nltk.twitter import Twitter



class Standardizer:



  #Esta funcion retorna una matriz con los twets y el documetno original estandarizados.     
  def obtener_Twits():    
      text1 = Standardizer.standardize("The stress of the students has no relation to university life.")
      text2 = Standardizer.standardize("The students are good people.")
      a=[]
      a.append(text1)
      a.append(text2)
      return a

  #Funcion que retorna un arreglo con los la frecuencia de cada uno de los elementos del documento entregado
  def freq(document):
      frecuenciaPalab = [document.count(p) for p in document]
      return(dict(zip(document,frecuenciaPalab)))
    
  def matris_TF(listaPalabras, twets):
    for twet in twets:
       print("------------------")
       print (twet)
       dicPalabras = Standardizer.freq(twet)
       for pClave in listaPalabras:
         if(dicPalabras.get(pClave) == None):
           print (pClave,":0")
         else:           
           print (pClave,":",dicPalabras.get(pClave))
        
  def matris_idftf(listaPalabras, twets,CantTeets):
    arrIDF=[]
    for twet in twets:
       print("------------------")
       print (twet)
       fila=[]
       dicPalabras = Standardizer.freq(twet)
       for pClave in listaPalabras:
         if(dicPalabras.get(pClave) == None):
           print (pClave,":0")
           fila.append(0)
         else:         
           ni=Standardizer.teetsQueLaContienen(twets,pClave)
           print ("idf(",pClave,")=log(",CantTeets,"/",ni,"))log(",CantTeets/ni,")= ",np.log10(CantTeets/ni))
           fila.append(np.log10(CantTeets/ni))

       arrIDF.append(fila)
    #Al finalizar se imprime la matris con los valore idf de los teets capturados  
    print(arrIDF)
    
    
    
      
  def teetsQueLaContienen(twets,pClave):
    cont=0
    for twet in twets:
      dicPalabras = Standardizer.freq(twet)
      if(dicPalabras.get(pClave) != None):
        cont=cont+1
    return cont  
      
    
  @staticmethod
  def standardize(text):
        clean_tokens = word_tokenize(text)[:]
        sr = set(stopwords.words('english'))
        sr.update(['.', ',', '"', "'","The","a", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) 
        for token in clean_tokens:
            if token in sr:
                clean_tokens.remove(token)  
        ##tw = Twitter()
        ##tw.tweets(keywords=txt, stream=False, limit=10)        
        return clean_tokens
     
  
    
  def main():
    text = "The students suffer a lot of stress in the summer. Poor students."
    document=Standardizer.standardize(text)
    dicPalabras = Standardizer.freq(document)
    print(document)
    matris_twest=Standardizer.obtener_Twits()
    #Standardizer.matris_TF(document,matris_twest)
    Standardizer.matris_idftf(document,matris_twest,len(matris_twest))
  
Standardizer.main()



