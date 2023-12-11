# Phase 1 - Milestone
# Nama  : Michael Nathaniel
# Batch : HCK-009

import streamlit as st
import pandas as pd
import pickle

def run():
# Load All Files

    st.title('Model Inference')
    st.write('Silahkan berikan imputasi data untuk dilakukan prediksi')
    st.header('')

    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    age = st.number_input(label='Masukan age', min_value = 0.0)

    workclass = st.selectbox(label='Pilih work class', options= ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', 'Self-emp-inc', 'Without-pay'])

    education = st.selectbox(label='Pilih education level', options= ['High_Education', 'Low_Education'])

    marital_status = st.selectbox(label='Pilih marital status', options= ['Single', 'Married', 'Separated'])

    occupation = st.selectbox(label='Pilih occupation', options= ['Office', 'Management', 'Service', 'Professional', 'Other'])

    sex = st.selectbox(label='Pilih sex', options= ['Male', 'Female'])

    hours_per_week = st.number_input(label='Masukkan hours-per-week', min_value = 0.0)

    native_continent = st.selectbox(label='Pilih native-continent', options=['North America', 'Asia', 'Europe', 'South America', 'Other'])
    
    st.write('Berikut hasil data yang anda input :')

    data_inf = pd.DataFrame({
        'age': age,
        'workclass': workclass,
        'education': education,
        'marital-status': marital_status,
        'occupation': occupation,
        'sex': sex,
        'hours-per-week': hours_per_week,
        'native-continent': native_continent
    }, index=[0])

    st.table(data_inf)

    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = model.predict(data_inf)

        if y_pred_inf[0] == 0:
            st.write('Pendapatan (income) dibawah atau sama dengan $50.000 per tahun (<=50K).')
        else:
            st.write('Pendapatan (income) diatas $50.000 per tahun (>50K).')