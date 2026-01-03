import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing datset
dataset= pd.read_csv('Restaurant_Reviews.tsv',
                      delimiter='\t', quoting=3)

#cleaing the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(0, 1000):
    review=re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    all_stPWords=stopwords.words('english')
    all_stPWords.remove('not')
    review= [ps.stem(word) for word in review if not word in set (all_stPWords)]
    review=' '.join(review)
    corpus.append(review)
 
print(corpus)
       