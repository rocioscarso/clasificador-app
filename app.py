import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 
  
# loading in the model to predict on the data 
pickle_in = open('clasificador.pkl', 'rb') 
classifier = pickle.load(pickle_in) 

@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(gender, nosis_bancarizado, A, B, C1, C2, C3, D1, D2, NC, Maestro, Mastercard, Sin_Tarjeta, Visa, nosis_score, age, nosis_consulta_cantidad, nosis_compromiso_mensual):   
 
    # Pre-processing user input    
    if gender == "M":
        gender = 0
    else:
        gender = 1
 
    if nosis_bancarizado == "NO":
        nosis_bancarizado = 0
    else:
        nosis_bancarizado = 1
 
    if A == "A":
        A = 0
    else:
        A = 1  
    
    if B == "B":
        B = 0
    else:
        B = 1  

    if C1 == "C1":
        C1 = 0
    else:
        C1 = 1  

    if C2 == "C2":
        C2 = 0
    else:
        C2 = 1  

    if C3 == "C3":
        C3 = 0
    else:
        C3 = 1  

    if D1 == "D1":
        D1 = 0
    else:
        D1 = 1 
        
    if D2 == "D2":
        D2 = 0
    else:
        D2 = 1  
    
    if NC == "NC":
        NC = 0
    else:
        NC = 1  

    if Maestro == "Maestro":
        Maestro = 0
    else:
        Maestro = 1  

    if Mastercard == "Mastercard":
        Mastercard = 0
    else:
        Mastercard = 1

    if Sin_Tarjeta == "S/T":
        Sin_Tarjeta = 0
    else:
        Sin_Tarjeta = 1

    if Visa == "Visa":
        Visa = 0
    else:
        Visa = 1
    
    nosis_score = nosis_score
    nosis_consulta_cantidad = nosis_consulta_cantidad
    nosis_compromiso_mensual = nosis_compromiso_mensual
    
    # Making predictions 
    prediction = classifier.predict( 
        [[nosis_score, age, nosis_consulta_cantidad, nosis_compromiso_mensual,nosis_bancarizado, gender, A, B, C1, C2, C3, D1, D2, NC, Maestro, Mastercard, Sin_Tarjeta, Visa]])
     
    if prediction == 0:
        Default = 'RECHAZADO'
    else:
        Default = 'APROBADO'
    return Default
      
  

# this is the main function in which we define our webpage  
def main():       
    img = Image.open("logo_wayni.jpg")
    st.image(img,width=300)

    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color: #7fffd4 ;padding:13px"> 
    <h1 style ="color:black;text-align:center;">App para Predicción de Préstamos</h1> 
    </div> 
    
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    gender = st.selectbox('Género',("M","F"))
    age = st.slider("Edad", min_value=18, max_value=80)
    nosis_bancarizado = st.selectbox('Nosis Bancarizado',("SI","NO")) 
    nosis_score = st.number_input("Nosis Score") 
    nosis_consulta_cantidad = st.number_input("nosis consulta cantidad")
    nosis_compromiso_mensual = st.number_input("nosis compromiso mensual")
    st.subheader('Seleccione Nivel Socioeconómico')
    A = st.checkbox("A")
    B = st.checkbox("B")
    C1 = st.checkbox("C1")
    C2 = st.checkbox("C2")
    C3 = st.checkbox("C3")
    D1 = st.checkbox("D1")
    D2 = st.checkbox("D2")
    NC = st.checkbox("NC")
    st.subheader('Seleccione Tipo de Tarjeta de Crédito')
    Visa = st.checkbox("Visa")
    Mastercard = st.checkbox("Mastercard")
    Maestro = st.checkbox("Maestro")
    Sin_Tarjeta = st.checkbox("Sin Tarjeta")
    
    #Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    st.subheader('                                             ')
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Clasificar"): 
        result = prediction(gender, nosis_bancarizado, A, B, C1, C2, C3, D1, D2, NC, Maestro, Mastercard, Sin_Tarjeta, Visa, nosis_score, age, nosis_consulta_cantidad, nosis_compromiso_mensual) 
        st.success('El prestamo debe ser {}'.format(result))
        
     
    
        
if __name__=='__main__': 
    main() 

#from pyngrok import ngrok

#public_url = ngrok.connect('8501')
#public_url
