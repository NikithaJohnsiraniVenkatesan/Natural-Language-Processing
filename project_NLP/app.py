# -*- coding: utf-8 -*-
import streamlit as st

import spacy
from textblob import TextBlob
from gensim.summarization import summarize



def text_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    return tokens

def entity_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    entities = [(entity.text, entity.label_) for entity in docx.ents]
    allData = ['"Tokens":{}, \n"Entities":{}'.format(tokens, entities)]
    return allData

def main():
    st.title("Email Analysis")
    st.subheader("Analyse your email on the go!")
    
    if st.checkbox("Show tokens and lemmatization"):
        st.subheader("Tokenize")
        message = st.text_area("Enter your email:", "Type here")
        if st.button("Analyse"):
            nlp_result = text_analyzer(message)
            st.success(nlp_result)
    
    
    if st.checkbox("Show Named Entities"):
        st.subheader("Extract the entities")
        message = st.text_area("Enter your email:", "Type here")
        if st.button("Extract"):
            nlp_result = entity_analyzer(message)
            st.json(nlp_result)
            
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Sentiment of your email")
        message = st.text_area("Enter your email:", "Type here")
        if st.button("Analyze"):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)
    
    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize your email:")
        message = st.text_area("Enter your text:", "Type here")
        summary_option = st.selectbox("Choose your summarizer",("gensim", "sumy"))
        if st.button("Summarize"):
            if summary_option == 'gensim':
                st.text("Using Gensim..")
                summary_result = summarize(message)
            elif summary_option == 'sumy':
                st.text("Sorry, we dont have that right now")
            else:
                st.warning("Using Default summarizer")
                st.text("Using Gensim")
                summary_result = summarize(message)
            st.success(summary_result)
            
    




if __name__ == '__main__':
    main()
