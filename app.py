# app.py

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
# Nama: Adilah Widiasti
# Email: adilahwidiasti86@gmail.com
# Id Dicoding: olaladilah

# Library yang digunakan
import streamlit as st
import pandas as pd
import pickle


# Fungsi untuk memuat model yang telah dilatih sebelumnya
@st.cache_data()
def load_trained_model(path_to_model):
    with open(path_to_model, 'rb') as model_file:
        trained_model = pickle.load(model_file)
    return trained_model

# Fungsi untuk melakukan prediksi berdasarkan input data
def make_prediction(trained_model, input_features):
    # Mengubah input data menjadi DataFrame
    input_df = pd.DataFrame(input_features, index=[0])
    # Melakukan prediksi
    prediction_result = trained_model.predict(input_df)
    return prediction_result[0]

# Fungsi utama untuk menjalankan aplikasi dashboard
def run_dashboard():
    # Menampilkan judul aplikasi
    st.title('Prediksi Dropout Mahasiswa')

    # Menampilkan header dan instruksi untuk pengguna
    st.header('Silakan Masukkan Data untuk Prediksi')
    st.markdown('Isi kolom-kolom berikut dengan informasi mahasiswa yang ingin Anda analisis.')

    # Input untuk data mahasiswa
    app_mode = st.selectbox('Mode Aplikasi', [15, 9254])  # Pilihan mode aplikasi
    course_selection = st.selectbox('Mata Kuliah', [9254, 9853])  # Pilihan mata kuliah
    previous_grade = st.number_input('Nilai Kualifikasi Sebelumnya', value=160.0)
    mother_qualification = st.selectbox('Kualifikasi Ibu', [1, 2, 3])
    father_qualification = st.selectbox('Kualifikasi Ayah', [3, 4, 5])
    mother_occupation = st.selectbox('Pekerjaan Ibu', [1, 2, 3])
    father_occupation = st.selectbox('Pekerjaan Ayah', [1, 2, 3])
    admission_score = st.number_input('Nilai Penerimaan', value=142.5)
    is_displaced = st.selectbox('Displaced', [0, 1])
    gender_identity = st.selectbox('Jenis Kelamin', [0, 1])
    has_scholarship = st.selectbox('Pemegang Beasiswa', [0, 1])
    enrollment_age = st.number_input('Usia Saat Pendaftaran', value=19)
    first_sem_enrolled_units = st.number_input('Unit Kurikulum 1st Sem Terdaftar', value=6)
    first_sem_evaluated_units = st.number_input('Unit Kurikulum 1st Sem Evaluasi', value=6)
    first_sem_approved_units = st.number_input('Unit Kurikulum 1st Sem Disetujui', value=6)
    second_sem_enrolled_units = st.number_input('Unit Kurikulum 2nd Sem Terdaftar', value=6)
    second_sem_evaluated_units = st.number_input('Unit Kurikulum 2nd Sem Evaluasi', value=6)
    second_sem_approved_units = st.number_input('Unit Kurikulum 2nd Sem Disetujui', value=6)
    unemployment_stat = st.number_input('Tingkat Pengangguran', value=13.9)
    inflation_stat = st.number_input('Tingkat Inflasi', value=-0.3)
    gdp_value = st.number_input('GDP', value=0.79)
    student_status = st.selectbox('Status', [0, 1])
    first_sem_approval_ratio = st.number_input('Rasio Disetujui 1st Sem', value=1.0)
    second_sem_approval_ratio = st.number_input('Rasio Disetujui 2nd Sem', value=1.0)

    # Tombol untuk memulai proses prediksi
    if st.button('Lakukan Prediksi'):
        # Memuat model yang telah dilatih
        model = load_trained_model('model.pkl')

        # Menyusun data input ke dalam dictionary
        input_data_dict = {
            'Application_mode': [app_mode],
            'Course': [course_selection],
            'Previous_qualification_grade': [previous_grade],
            'Mothers_qualification': [mother_qualification],
            'Fathers_qualification': [father_qualification],
            'Mothers_occupation': [mother_occupation],
            'Fathers_occupation': [father_occupation],
            'Admission_grade': [admission_score],
            'Displaced': [is_displaced],
            'Gender': [gender_identity],
            'Scholarship_holder': [has_scholarship],
            'Age_at_enrollment': [enrollment_age],
            'Curricular_units_1st_sem_enrolled': [first_sem_enrolled_units],
            'Curricular_units_1st_sem_evaluations': [first_sem_evaluated_units],
            'Curricular_units_1st_sem_approved': [first_sem_approved_units],
            'Curricular_units_2nd_sem_enrolled': [second_sem_enrolled_units],
            'Curricular_units_2nd_sem_evaluations': [second_sem_evaluated_units],
            'Curricular_units_2nd_sem_approved': [second_sem_approved_units],
            'Unemployment_rate': [unemployment_stat],
            'Inflation_rate': [inflation_stat],
            'GDP': [gdp_value],
            'Status': [student_status],
            'Ratio_approved_1st_sem': [first_sem_approval_ratio],
            'Ratio_approved_2nd_sem': [second_sem_approval_ratio]
        }

        # Melakukan prediksi
        result = make_prediction(model, input_data_dict)

        # Menampilkan hasil prediksi kepada pengguna
        if result == '1':
            st.success('Hasil Prediksi: Tidak berpotensi dropout')
        else:
            st.warning('Hasil Prediksi: Berpotensi dropout')

# Menjalankan fungsi utama untuk memulai aplikasi
if __name__ == '__main__':
    run_dashboard()
