# Phase 1 - Milestone
# Nama  : Michael Nathaniel
# Batch : HCK-009

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Explaration Data Analysis (EDA)')
    st.write('Analisis data lebih lanjut untuk mendapatkan wawasan mendalam terhadap dataset yang digunakan.')
    st.header('')

    # Memanggil data csv 
    data = pd.read_csv(r'P1M2_michael_nathaniel.csv')

    # menampilakn 10 data teratas
    st.header('Menampilkan 10 data teratas')
    st.table(data.head(10))

    # menampilakn 10 data terbawah
    st.header('Menampilkan 10 data terbawah')
    st.table(data.tail(10))

    # Melihat distribusi data
    st.header('Melihat deskripsi Data Frame yang akan digunakan')
    st.table(data.select_dtypes(include='number').agg(['count', 'skew', 'kurt', 'std', 'mean', 'median', 'min', 'max']))
    image = Image.open('Melihat deskripsi Data Frame yang akan digunakan.png')
    st.image(image, caption='Figure 1: Melihat distribusi data numerical')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Dari hasil deskripsi statistik yang telah dilakukan, kita dapat menemukan beberapa insight yang berguna:
            - Distribusi umur (age) tampaknya cenderung condong ke kanan (skew positif), dengan nilai mean (rata-rata) sekitar 38 tahun dan median (nilai tengah) 37 tahun. Hal ini menunjukkan bahwa ada beberapa nilai umur yang lebih tinggi yang dapat menggeser rata-rata ke arah yang lebih tinggi.
            - Distribusi Final Weight (fnlwgt) memiliki skewness positif yang tinggi, menunjukkan adanya ekor panjang di sisi kanan distribusi. Ini dapat mengindikasikan adanya outlier atau anomali dalam distribusi berat akhir.
            - Kita akan menghirukan distribusi data education_num karena merupakan kategorial.
            - Distribusi Capital-gain dan Capital-loss memiliki skewness yang tinggi, terutama capital-gain. Hal ini menunjukkan bahwa sebagian besar nilai cenderung berada pada tingkat yang lebih rendah, sementara ada beberapa nilai yang sangat tinggi yang dapat memengaruhi distribusi.
            - Distribusi jam kerja per minggu (Hours-per-week) memiliki skewness yang kecil dan kurtosis yang moderat. Rata-rata jam kerja adalah sekitar 40 jam per minggu, dengan variasi yang lebih rendah.
            - Distribusi yang mencerminkan skewness atau kurtosis tinggi dapat menunjukkan bahwa data memiliki variasi yang signifikan atau mungkin mengandung outlier.
            - Perbedaan antara mean dan median (misalnya, pada age dan fnlwgt) dapat memberikan petunjuk tentang kehadiran outlier atau skewness dalam distribusi.
            ''')
        
    # Memeriksa outlier
    st.header('Memeriksa outlier')
    image = Image.open('Memeriksa outlier.png')
    st.image(image, caption='Figure 2: Memeriksa distribusi outlier')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Dari hasil analisis yang telah dilakukan terhadap dataset, kita dapat menarik beberapa insight:
            - Kolom 'age' memiliki sekitar 0.44% outliers, 'capital-gain' memiliki sekitar 8.26%, 'capital-loss' sekitar 4.67%, 'education-num' sekitar 3.67%, 'fnlwgt' sekitar 2.97%, dan 'hours-per-week' memiliki sekitar 27.63% outliers.
            - Peningkatan yang signifikan dalam persentase outliers pada 'hours-per-week' menunjukkan bahwa sebagian besar data berada di luar rentang interquartil, dan perlu dipertimbangkan apakah ini adalah hasil yang diinginkan atau apakah ada kebutuhan untuk memeriksa dan membersihkan data tersebut.
            - Outliers pada 'hours-per-week' mungkin dapat dijelaskan oleh keberagaman jam kerja yang luas dalam dataset. Meskipun 'capital-gain' dan 'capital-loss' memiliki persentase outliers yang tinggi, hal ini dapat diharapkan karena variabilitas besar dalam capital-gain dan capital-loss.
            
            Dengan memahami nilai yang hilang dan outliers, Anda dapat membuat keputusan yang lebih baik dalam pemrosesan data lebih lanjut, termasuk strategi pengisian nilai yang hilang atau penanganan outliers sesuai dengan kebutuhan analisis atau model yang akan dibangun.
            ''')
        
    # Melihat Perbandingan Data Berdasarkan Nilai Income
    st.header('Melihat Perbandingan Data Berdasarkan Nilai Income')
    image = Image.open('Melihat Perbandingan Data Berdasarkan Nilai Income.png')
    st.image(image, caption='Figure 3: Perbandingan Data Berdasarkan Nilai Income')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Kita temukan bahwa pada dataset yang kita gunakan, mereka dengan besaran income lebih sedikit atau sama dengan $50,000 per tahun jauh lebih banyak (75.19%) dibandingkan mereka yang diatas nominal tersebut (24.82%).
            ''')
        
    # Melihat Distribusi Umur
    st.header('Melihat Distribusi Umur')
    image = Image.open('Melihat Distribusi Umur.png')
    st.image(image, caption='Figure 4: Distribusi Umur')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Melihat dari grafik diatas, kita temukan bahwa pada dataset kita umurnya berkisar antara 17 hingga 90 tahun dengan mayoritas data antara usia 25 dan 50 tahun.
            ''')
        
    # Melihat Banyak Data Grup Umur dengan Income
    st.header('Melihat Banyak Data Grup Umur dengan Income')
    image = Image.open('Melihat Banyak Data Grup Umur dengan Income.png')
    st.image(image, caption='Figure 5: Grup Umur dengan Income')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Melihat grafik tersebut, kita dapat melihat bahwa terdapat perbedaan yang signifikan antara rasio >50 ribu hingga <=50 ribu antar kelompok umur. Rasion yang menarik ada pada 36-50 dan 51-65 dimana kemungkinan orang memiliki gaji >50K/ tahun lumayan besar dibanding kelompok umur lainnya. Kita juga temukan bahwa mayortas responden adalah mereka yang berusia 18-50+.
            ''')
        
    # Melihat Banyak Data Setiap Jenis Education
    st.header('Melihat Banyak Data Setiap Jenis Education')
    image = Image.open('Melihat Banyak Data Setiap Jenis Education.png')
    st.image(image, caption='Figure 6: Banyak Data Setiap Jenis Education')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Statistik di atas menunjukkan distribusi berbagai tingkat pendidikan di antara individu-individu dalam kumpulan data. Kita temukan bahwa banyak dari data yang kita miliki hanyalah tamatan SMA, diikuti oleh college dan sarjana (bachelors).
            ''')
        
    # Melihat Perbandingan Income Berdasarkan Workclass
    st.header('Melihat Perbandingan Income Berdasarkan Workclass')
    image = Image.open('Melihat Perbandingan Income Berdasarkan Workclass.png')
    st.image(image, caption='Figure 7: Perbandingan Income Berdasarkan Workclass')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Statistik diatas menggambarkan perbandingan income berdasarkan kelas pekerja. Kita temukan bahwa mayoritas didata kita memiliki workclass bertipe private (bekerja di private sector). Probilitas untuk mendapatkan gaji diatas $50K/ tahun lumayan besar jika bekerja dalam kelas pekerja self-emp-inc.
            ''')
        
    # Melihat Perbandingan Income Berdasarkan Occupation
    st.header('Melihat Perbandingan Income Berdasarkan Occupation')
    image = Image.open('Melihat Perbandingan Income Berdasarkan Occupation.png')
    st.image(image, caption='Figure 8: Perbandingan Income Berdasarkan Occupation')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Dari statistik diatas, Exec-managerial dan prof-specialty menonjol karena memiliki persentase individu yang menghasilkan lebih dari $50.000/ tahun yang sangat tinggi. Selain itu, persentase untuk Farmingfishing, Otherservice, dan Handlerscleaner untuk mendapatkan income lebih dari $50.000/tahun jauh lebih rendah dibandingkan profesi lainnya.
            ''')
    
    # Melihat Perbandingan Income Berdasarkan Gender
    st.header('Melihat Perbandingan Income Berdasarkan Gender')
    image = Image.open('Melihat Perbandingan Income Berdasarkan Gender.png')
    st.image(image, caption='Figure 9: Perbandingan Income Berdasarkan Gender')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Dari statistik diatas, kita temukan bahwa pekerja pria memiliki peluang lebih besar untuk mendapatkan gaji diatas $50.000 per tahunnya dibandingkan dengan perempuan. Kita lihat juga bahwa mayoritas data yang kita miliki berisi pria.
            ''')
        
    # Melihat Perbandingan Income Berdasarkan Hours-Per-Week
    st.header('Melihat Perbandingan Income Berdasarkan Hours-Per-Week')
    image = Image.open('Melihat Perbandingan Income Berdasarkan Hours-Per-Week.png')
    st.image(image, caption='Figure 10: Perbandingan Income Berdasarkan Hours-Per-Week')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Statistik diatas menunjukkan bahwa dataset kita mayoritas berisikan mereka yang bekerja 41-60 jam per minggu. Presentase jumlah dari mereka yang memiliki income diatas $50.000 per tahun juga sangat besar.
            ''')
        
    # Melihat korelasi data-data kategorial terhadap income
    st.header('Melihat korelasi data-data kategorial terhadap income')
    image = Image.open('KORELASI P1M2.png')
    st.image(image, caption='Figure 4: Korelasi data-data kategorial terhadap income')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Dari hasil visualisasi diatas kita memperoleh korelasi terhadap income seperti berikut:
            - age (0.4)
            - workclass (0.15)
            - fnlwgt (0.4)
            - education (0.46)
            - marital-status (0.42)
            - occupation (0.44)
            - relationship (0.62)
            - race (0.082)
            - sex (0.33)
            - capital-gain (0.51)
            - capital-loss (0.34)
            - hours-per-week (0.34)
            - native-country (0.12)

            Berdasarkan hasil uji korelasi menggunakan phix, kita akan mendrop kolom yang nilai korelasinya sangat jauh dibawah rata-rata seperti kolom race (0.082).

            Berdasarkan domain knowledge, kita tidak memerlukan data seperti final weight dan relationship. Umumnya, yang mempengaruhi income hanya marital status dan bukan relationship.

            Kita juga tidak akan menggunakan kolom education karena sudah diwakili oleh education-num yang merupakan Ordinal sejak awal.

            Melihat dari data capital gain dan capital loss yang banyak bernilai 0 yang kemungkinan karena dirahasiakan oleh responden, maka kita tidak akan menggunakan kolom ini.
            ''')