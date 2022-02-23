import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.title('Spam Ham Classifier')            
ip = st.text_input('Enter your message')       
op = model.predict([ip])           
if st.button('Predict'):   
  st.title(op[0])        
                          
                                                                                      
