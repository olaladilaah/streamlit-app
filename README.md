# streamlit-app
Aplikasi Streamlit untuk penerapan data science

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
# Nama: Adilah Widiasti
# Email: adilahwidiasti86@gmail.com
# Id Dicoding: olaladilah

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Selama ini, lembaga ini telah menghasilkan banyak lulusan dengan reputasi yang sangat baik. Namun, ada juga sejumlah mahasiswa yang tidak berhasil menyelesaikan studi mereka atau mengalami dropout. Oleh karena itu, penting untuk menganalisis faktor-faktor yang berkontribusi terhadap tingginya angka dropout agar Jaya Jaya Institut dapat segera memberikan bimbingan khusus kepada mahasiswa yang berisiko.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi tantangan besar akibat tingginya angka mahasiswa yang tidak menyelesaikan studi mereka. Fenomena dropout ini tidak hanya berdampak pada citra dan stabilitas finansial institusi, tetapi juga merugikan mahasiswa yang gagal meraih gelar akademik. Selain itu, tingginya angka mahasiswa yang keluar dapat mengurangi kepercayaan calon mahasiswa serta orang tua terhadap mutu pendidikan di Jaya Jaya Institut. Beberapa tantangan utama yang dihadapi institusi meliputi:  
1. **Reputasi Institusi**  
   Tingkat dropout yang tinggi dapat menurunkan citra institusi sebagai penyedia pendidikan berkualitas.  

2. **Kerugian Finansial**  
   Mahasiswa yang tidak menyelesaikan studi menyebabkan hilangnya potensi pendapatan dari biaya kuliah dan sumber pendapatan lainnya.  

3. **Dampak terhadap Akreditasi**  
   Rendahnya tingkat kelulusan dapat berpengaruh negatif terhadap status akreditasi institusi.  

4. **Menurunnya Kepercayaan Stakeholder**  
   Mahasiswa, orang tua, serta masyarakat dapat meragukan kemampuan institusi dalam memberikan pendidikan serta dukungan yang memadai bagi keberhasilan akademik mahasiswa.

### Cakupan Proyek
1. Mengumpulkan serta mengolah data terkait mahasiswa.  
2. Melakukan analisis data guna mengidentifikasi pola serta faktor yang berkontribusi terhadap dropout mahasiswa.  
3. Mengembangkan model prediksi dengan menerapkan algoritma Random Forest Classifier.  
4. Merancang dashboard bisnis untuk menampilkan hasil analisis dan prediksi secara visual.  
5. Menyusun rekomendasi strategis berdasarkan temuan dari analisis data.

### Persiapan
Berikut adalah langkah-langkah persiapan:  
Sumber data : [Dataset Mahasiswa](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)  

## Library yang Digunakan
- Streamlit
- Pandas
- Pickle

## Menjalankan Sistem Machine Learning
Untuk menjalankan aplikasi ini, Anda perlu mengikuti langkah-langkah berikut:
1. **Persyaratan Awal**:
   - Pastikan Anda telah menginstal Python di sistem Anda. Anda dapat mengunduhnya dari [python.org](https://www.python.org/downloads/).
   - Instal Streamlit dan Pandas dengan menggunakan pip. Anda dapat melakukannya dengan menjalankan perintah berikut di terminal:
     ```bash
     pip install streamlit pandas
     ```

2. **Model yang Dilatih**:
   - Pastikan Anda memiliki model yang telah dilatih dan disimpan dalam format pickle (`model.pkl`). Model ini harus berada di direktori yang sama dengan berkas `app.py`.

3. **Menjalankan Aplikasi**:
   - Buka terminal dan navigasikan ke direktori tempat berkas `app.py` berada.
   - Jalankan aplikasi dengan perintah berikut:
     ```bash
     streamlit run app.py
     ```
   - Setelah menjalankan perintah tersebut, aplikasi akan terbuka di browser Anda secara otomatis. Jika tidak, Anda dapat mengaksesnya melalui alamat `http://localhost:8501`.

4. **Menggunakan Aplikasi**:
   - Setelah aplikasi terbuka, Anda akan melihat antarmuka untuk memasukkan data mahasiswa.
   - Isi kolom-kolom yang tersedia dengan informasi yang relevan.
   - Klik tombol "Lakukan Prediksi" untuk mendapatkan hasil prediksi apakah mahasiswa tersebut berpotensi dropout atau tidak.

5. **Hasil Prediksi**:
   - Hasil prediksi akan ditampilkan di bawah tombol prediksi. Jika hasilnya adalah '1', maka mahasiswa tersebut tidak berpotensi dropout. Jika hasilnya adalah '0', maka mahasiswa tersebut berpotensi dropout.

## Streamlit 
  Local URL: http://localhost:8501
  Network URL: http://192.168.0.191:8501

## Cara menjalankan Streamlit 
1. Buka Terminal CMD :
   cd C:\Users\adila\Documents\Submission_Penerapan_Data_Science_Adilah
2. Buat Virtual Environment :
   python -m venv venv
3. Aktifkan Virtual Environment :
   venv\Scripts\activate
4. Install streamlit : 
   pip install streamlit
5. Jalankan streamlit :
   CD\C:\Users\adila\Documents\Submission_Penerapan_Data_Science_Adilah
   dir 
   streamlit run app.py 
   Local URL: http://localhost:8501
   Link Deployment streamlit : https://app-app-r88qidyzmzobf9nqmce8vb.streamlit.app/ 



## Business Dashboard
Dashboard bisnis ini dirancang untuk memprediksi kemungkinan seorang mahasiswa mengalami dropout di Jaya Jaya Institut. Prediksi dilakukan dengan menggunakan model machine learning yang telah dilatih sebelumnya untuk menganalisis data yang dimasukkan. Dashboard ini menyediakan berbagai kolom input yang mencerminkan faktor-faktor yang dapat memengaruhi dropout mahasiswa, seperti metode pendaftaran, mata kuliah yang diambil, riwayat pendidikan, pekerjaan orang tua, serta aspek akademik lainnya. Model yang telah disimpan akan memproses data tersebut dan menghasilkan prediksi, sehingga pengguna dapat memperoleh wawasan mengenai potensi dropout mahasiswa. Dengan adanya dashboard ini, Jaya Jaya Institut diharapkan dapat mengambil langkah preventif secara lebih dini guna menekan angka dropout dan mendukung kesuksesan akademik mahasiswa.

## Conclusion
Tingkat dropout mahasiswa di Jaya Jaya Institut dipengaruhi oleh berbagai aspek, termasuk faktor demografi, latar belakang pendidikan, kondisi ekonomi, lingkungan keluarga, serta pencapaian akademik. Mahasiswa yang mendaftar pada usia lebih tua, berasal dari kategori "over 23 years old" atau "transfer" dalam metode pendaftaran, mengambil program studi manajemen malam atau teknik informatika, memiliki nilai masuk yang rendah, dan tidak memperoleh beasiswa cenderung memiliki risiko dropout yang lebih tinggi. Selain itu, dukungan keluarga juga berperan penting, di mana mahasiswa dengan orang tua yang kualifikasi pendidikannya tidak diketahui lebih rentan terhadap kemungkinan tidak menyelesaikan studi. Secara umum, mahasiswa yang mengalami dropout cenderung menunjukkan pencapaian akademik yang lebih rendah dibandingkan dengan mereka yang berhasil menyelesaikan pendidikan.

### Rekomendasi Action Items
Berikut adalah beberapa strategi yang dapat diterapkan oleh Jaya Jaya Institut untuk menekan angka dropout mahasiswa:  
1. Menyediakan bimbingan tambahan dan dukungan akademik khusus bagi mahasiswa program manajemen malam dan teknik informatika, karena kedua kelompok ini memiliki risiko dropout yang lebih tinggi.  
2. Mengembangkan program remedial yang dirancang untuk membantu mahasiswa dengan nilai masuk rendah agar mereka dapat meningkatkan prestasi akademiknya.  
3. Memperluas cakupan beasiswa untuk mencakup lebih banyak mahasiswa yang berisiko tinggi mengalami dropout serta memberikan informasi yang lebih jelas mengenai akses bantuan keuangan.  
4. Menyediakan layanan konseling dan dukungan psikologis tambahan bagi mahasiswa yang memiliki latar belakang keluarga dengan tingkat pendidikan orang tua yang rendah atau tidak diketahui.  
5. Membangun program pendampingan bagi mahasiswa yang berasal dari keluarga dengan kondisi ekonomi dan sosial yang kurang mendukung.  
6. Menerapkan sistem pemantauan akademik secara berkala untuk mengidentifikasi mahasiswa yang mengalami penurunan kinerja, sehingga dapat dilakukan intervensi lebih awal.  
7. Meningkatkan fasilitas kampus, seperti perpustakaan, ruang belajar, dan layanan dukungan mahasiswa, guna menciptakan lingkungan akademik yang lebih nyaman dan kondusif.  
8. Mengembangkan program yang membantu mahasiswa menjaga keseimbangan antara akademik dan kehidupan pribadi, seperti kegiatan ekstrakurikuler dan layanan kesehatan mental.  
9. Meningkatkan keterlibatan orang tua dalam proses pendidikan melalui komunikasi rutin serta program sosialisasi yang memperkuat dukungan keluarga terhadap mahasiswa.

## Email dan password Metabase
Email: root@mail.com
Password: root123




