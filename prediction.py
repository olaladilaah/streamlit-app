# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
# Nama: Adilah Widiasti
# Email: adilahwidiasti86@gmail.com
# Id Dicoding: olaladilah

# Library yang digunakan 
import pandas as pd
import pickle

# Memuat model yang telah dilatih sebelumnya dari file
with open('model.pkl', 'rb') as file_model:  # Membuka file model dalam mode baca biner
    model = pickle.load(file_model)  # Memuat model dari file menggunakan pickle

# Menyiapkan data baru untuk prediksi
data_baru = pd.DataFrame({
    'Application_mode': [15], 
    'Course': [9254], 
    'Previous_qualification_grade': [160.0], 
    'Mothers_qualification': [1], 
    'Fathers_qualification': [3], 
    'Mothers_occupation': [3], 
    'Fathers_occupation': [3], 
    'Admission_grade': [142.5], 
    'Displaced': [1], 
    'Gender': [1], 
    'Scholarship_holder': [0], 
    'Age_at_enrollment': [19], 
    'Curricular_units_1st_sem_enrolled': [6], 
    'Curricular_units_1st_sem_evaluations': [6], 
    'Curricular_units_1st_sem_approved': [6], 
    'Curricular_units_2nd_sem_enrolled': [6], 
    'Curricular_units_2nd_sem_evaluations': [6], 
    'Curricular_units_2nd_sem_approved': [6], 
    'Unemployment_rate': [13.9], 
    'Inflation_rate': [-0.3], 
    'GDP': [0.79], 
    'Status': [1], 
    'Ratio_approved_1st_sem': [1.0], 
    'Ratio_approved_2nd_sem': [1.0]
})

# Melakukan prediksi menggunakan model yang telah dimuat
prediksi = model.predict(data_baru)  # Menghasilkan prediksi untuk data baru

# Mengonversi hasil prediksi menjadi label yang lebih mudah dipahami
label_prediksi = ['Tidak dropout' if hasil == 1 else 'Berpotensi dropout' for hasil in prediksi]

# Menampilkan hasil prediksi
print("Hasil Prediksi:", label_prediksi)  # Mencetak label hasil prediksi