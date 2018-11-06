
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from nltk.twitter import Twitter



class Standardizer:
  @staticmethod
  def standardize():
        text = "This chapter is divided into sections that skip between two quite different styles. In the computing with language sections we will take on some linguistically motivated programming tasks without necessarily explaining how they work. In the closer look at Python sections we will systematically review key programming concepts. We'll flag the two styles in the section titles, but later chapters will mix both styles without being so up-front about it. We hope this style of introduction gives you an authentic taste of what will come later, while covering a range of elementary concepts in linguistics and computer science. If you have basic familiarity with both areas, you can skip to 5; we will repeat any important points in later chapters, and if you miss anything you can easily consult the online reference material at http://nltk.org/. If the material is completely new to you, this chapter will raise more questions than it answers, questions that are addressed in the rest of this book."
        clean_tokens = word_tokenize(text)[:] 
        sr = stopwords.words('english')
        for token in word_tokenize(text):
            if token in stopwords.words('english'):
                clean_tokens.remove(token)
        txt = ' , '.join(clean_tokens)
        print(txt)
        tw = Twitter()
        tw.tweets(keywords=txt, stream=False, limit=10)

Standardizer.standardize()
