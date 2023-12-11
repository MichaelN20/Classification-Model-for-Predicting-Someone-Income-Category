# Phase 1 - Milestone
# Nama  : Michael Nathaniel
# Batch : HCK-009

import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox(label='Menu:', options=['Beranda', 'Exploration Data Analysis', 'Model Inference'])

if page == 'Beranda':
    st.title('Weclome to, MILESTONE 2')
    st.write('FTDS - Phase 1')
    st.header('')

    col1, col2 = st.columns(2)

    # ======================= Columns 1 =======================
    col1.write('**Nama             :**')
    col1.write('**Batch            :**')
    col1.write('**Tujuan Milestone :**')

    # ======================= Columns 2 =======================
    col2.write('Michael Nathaniel')
    col2.write('HCK-009')
    col2.write("Project ini dibuat guna membuat model prediksi klasifikasi untuk memprediksi apakah pendapatan seseorang diatas atau dibawah $50.000 dollar per tahun.")
    col2.write("Kita juga akan melihat seperti apa karakteristik seseorang yang mendapatkan gaji lebih dari $50.000 per tahun.")
    col2.write("Model yang akan dicoba adalah KNN, SVM, Decision Tree, Random Forest. Pada prosesnya kita akan mencoba untuk mengimplementasikan Pipelines, Cross Validation, Hyperparameter Tuning, dan Boosting. Final model yang telah di tentukan selanjutnya akan di deploy dengan streamlit di HuggingFace.")

    st.header('')
    st.write('**Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!**')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Kita diberikan dataset mengenai data-data sejenis sensur pendapatan penduduk. Informasi-informasi yang tersedia di dalam dataaset ini ada beragam seperti umur, kelas pekerja, final weight data, tingkat pendidikan, status perkawinan, pekerjaan, status hubungan, ras, jenis kelamin, capital gain dan loss, jam kerja dalam seminggu, dan label income (<=50K, >50K).')
    
    with st.expander("Problem Statement"):
        st.caption('Buat model klasifikasi untuk memprediksi apakah pendapatan (income) diatas 50.000 dollar per tahun dan mempelajari seperti apa karaktersitik orang yang memiliki pendapatan diatas 50.000 dollar per tahun.')

    with st.expander("Outline"):
        st.caption("1. Memuat data dan memeriksa informasi mengenai kumpulan data.")
        st.caption("2. EDA pada kumpulan data yang melibatkan analisis data lebih lanjut untuk mendapatkan wawasan.")
        st.caption("3. Feature Engineering untuk mendapatkan fitur dan target pemodelan.")
        st.caption("4. Mendefinisikan Model menggunakan pipeline.")
        st.caption("5. Melatih model.")
        st.caption("6. Evaluasi model yang terdiri dari Hyperparameter Tuning untuk mendapatkan model terbaik dengan hasil terbaik.")
        st.caption("7. Menyimpan model terbaik.")
        st.caption("8. Kesimpulan.")
        st.caption("9. Deployment.")
        st.caption("")

    with st.expander("Kesimpulan"):
        st.caption("Untuk melakukan prediksi klasifikasi apakah income seseorang dibawah sama dengan atau diatas 50.000 Dollar per tahun, kita akan menggunakan model `Random Forest yang di optimisasi menggunakan Hyperparameter Tuning`. Pada model, mereka yang penghasilannya berada `di bawah atau sama dengan 50.000 Dollar per tahun ditandai dengan '0'`, sedangkan yang penghasilannya `diatas $50.000 per tahun ditandai dengan '1'`.")
        st.caption("Dari hasil pengujian, model SVM memiliki hasil prediksi yang sedikit lebih baik dari pada Random Forest, diikuti oleh Decision Tree, AdaBoost, dan KNN. Namun, alasan kita tetap `menggunakan Random Forest sebagai model utama kita adalah karena SVM memerlukan resources yang lebih banyak dan memakan waktu yang sangat panjang` dalam memproses data sebesar 40.000++.")
        st.caption("Selama proses EDA, kita temukan bahwa pada umumnya mereka yang memiliki penghasilan diatas $50.000 per tahunnya memiliki karakteristik sebagai berikut:")
        st.caption("- Berusia 36-65 tahun.")
        st.caption("- Memiliki status kelas pekerja seperti Private Sector dan Self-Emp-Inc.")
        st.caption("- Memiliki pekerjaan seperti Executive Managerial dan Profesional Speciality.")
        st.caption("- Berjenis kelamin pria.")
        st.caption("- Bekerja 41-60 jam dalam seminggu.")
        st.caption("")

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    prediction.run()