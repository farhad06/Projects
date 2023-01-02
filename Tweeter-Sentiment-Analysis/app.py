import streamlit as st 
import spacy
import pickle
import re
# from sklearn.feature_extraction.text import CountVectorizer
nlp=spacy.load('en_core_web_sm')

st.title("Tweeter Sentiment Analysis")
model=pickle.load(open('./model/logistic_tweeter_sentiment_new.pkl','rb'))
vectorizer=pickle.load(open('./model/bow_vectorizer_1gram.pkl','rb'))
#preprocess the tweets
def preprocess(tweet):
    # Removing special characters and digits
    letters_only = re.sub("[^a-zA-Z]", " ",tweet)

    # change sentence to lower case
    letters_only = letters_only.lower()

    doc=nlp(letters_only)
    clean_text=[]
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        else:
            clean_text.append(token.lemma_)

    cleaned_text=" ".join(clean_text)
    #replace double spaces
    final_text=re.sub(' +', ' ', cleaned_text)
    return final_text

#predict our model
def predict_msg(tweet):
    #preprocess the tweet 
    clean_tweet=preprocess(tweet)
    #vectorized the tweet
    clean_tweet_encoded=vectorizer.transform([clean_tweet])
    #convert sparce matrix to array
    tweet_input=clean_tweet_encoded.toarray()
    #make a prediction
    result=model.predict(tweet_input)
    return result


txt=st.text_area("Enter Tweet")
btn=st.button("Submit")

if btn:
    msg=predict_msg(txt)

    if msg==0:
        st.success(' Your Tweet is not racist!', icon="✅")
    else:
        st.warning(' Your Tweet is  racist!', icon="⚠️")    

    # st.write(model.classes_)
    # st.write(msg)
    # st.write(type(msg))
