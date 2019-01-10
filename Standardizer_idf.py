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
      text3 = Standardizer.standardize("The students suffer a lot of stress in the summer. Poor students.")
      a=[]
      a.append(text1)
      a.append(text2)      
      a.append(text3)
      return a

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
        
  def matris_idftf(listaPalabras, twets,CantTeets):
    arrIDF=[]
    for twet in twets:
       print("------------------")
       print (twet)
       fila=[]
       dicPalabras = Standardizer.freq(twet)
       
       for pClave in listaPalabras:
         if(dicPalabras.get(pClave) == None):          
           fila.append(0)
         else:         
           ni=Standardizer.teetsQueLaContienen(twets,pClave)
           print ("idf(",pClave,")=log(",CantTeets,"/",ni,"))log(",CantTeets/ni,")= ",np.log10(CantTeets/ni))
           print("wij= fij X idf=",dicPalabras.get(pClave)," * ", np.log10(CantTeets/ni), "= ",dicPalabras.get(pClave) * np.log10(CantTeets/ni))
           fila.append(dicPalabras.get(pClave) *(np.log10(CantTeets/ni)))

       arrIDF.append(fila)
    return arrIDF
    
    
    
      
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
        sr.update(['.', ',', '"', "'","The","the","a", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']) 
        for token in clean_tokens:
            if token in sr:
                clean_tokens.remove(token)  
        ##tw = Twitter()
        ##tw.tweets(keywords=txt, stream=False, limit=10)        
        return clean_tokens
     
  def sim(org, doc):
    sum1=0
    mult1=1
    mult2=1
    for i in range(len(org)):
      sum1= sum1 + org[i] * doc[i]
      mult1= mult1 + (org[i]**2)
      mult2= mult2 + (doc[i]**2)
    mult1=np.sqrt(mult1)
    mult2=np.sqrt(mult2)
    sumFinal=sum1/(mult1*mult2)
    return sumFinal
  
     
  def main():
    text = "The students suffer a lot of stress in the summer. Poor students."
    document=Standardizer.standardize(text)
    dicPalabras = Standardizer.freq(document)
    print(document)
    matris_twest=Standardizer.obtener_Twits()
    arr_idf=Standardizer.matris_idftf(document,matris_twest,len(matris_twest))
    print("Sim entre doc original y doc1:",Standardizer.sim(Standardizer.arr_freq(dicPalabras),arr_idf[0]))
    print("Sim entre doc original y doc2:",Standardizer.sim(Standardizer.arr_freq(dicPalabras),arr_idf[1]))    
    print("Sim entre doc original y doc3:",Standardizer.sim(Standardizer.arr_freq(dicPalabras),arr_idf[2]))
  
Standardizer.main()



