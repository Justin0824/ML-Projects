import pickle
import streamlit as st
from nltk.corpus import stopwords
import string
import nltk
from nltk.stem.porter import PorterStemmer
 
ps = PorterStemmer()



def transform(text):
    text = text.lower()  # lower case
    text = nltk.word_tokenize(text)  # tokenization
    y = []
    for i in text:  # removing Special characters
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:  # removing stop words and punctuations
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return ' '.join(y)

tfifd=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title('SMS/Email Spam Classifier')
sms = st.text_input('Enter the Message')

if st.button('Predict') :

    # preprocess
    transform_sms = transform(sms)
    # vectorize
    vector_input = tfifd.transform([transform_sms])
    # predict
    result = model.predict(vector_input)[0]
    # display
    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')




