# Apliksasi Web Klasifikasi Data Tabel

proyek ini menyajikan aplikasi web untuk klasifikasi data tabel menggunakan model machine learning yang telah terlatih. Penggguna dapat mengunggah file CSV, dan aplikasi ini akan melakkan prediksi berdasarkan data yang diunggah.

PERSIAPAN
- membuat direktori, menggunakan Flask sebagai kerangka kerja web
- mempersiapkan struktur direktori, disini saya mempunyai folder dataset, model , scripts, dan templates. dan juga file app.py & reqiurements.txt

PERSIAPAN DATASET DAN MODEL
- menyiapkan dataset yang digunakan untuk melatih model
- menggunakan library machine learning seperti "scikit-learn" untukk melatih model. dalam contoh ini saya menggunakan "RandomForestClassifier"
- menyimpan model yang telah dilatih ke dalan file menggunakan 'joblib' agar dapat diakses aplikasi web

BANGUN APLIKASI WEB
- pemasangan flask menggunakan 'pip install flask' di lingkungan virtual
- membuat file 'app.py' sebagai file utama
- menentukan route untuk halaman utama ('/') dan route untuk melakukan prediksi ('/predict'). membuat template HTML (di folder 'templates') untuk menampilkan form pengunggahan file dan hasil prediksi
- dalam aplikasi flask, muat model di dalam fungsi prediksi sehingga model tidak dimuat setiap kali prediksi dilakukan
- menentukan fungsi prediksi yang menerima data input, memprosesnya, dan melakukan prediksi menggunakan model
- menambahkan penanganan kesalahan di aplikasi web untuk memberikan pesan informatuf jika terjadi masalah

KUSTMISASI DESAIN ANTARMUKA
- mengatur tampilan antarmuka web mneggunakan HTML dan CSS. sesuaikan font, warna, dan elemen lain sesuai kebutuhan dan keinginan
- menambahkan elemen visual seperti ikon dan tombol untuk meningkatkan pengalaman pengguna

UJI APLIKASI DAN PENYEMPURNAAN
- jalankan aplikasi dan uji fungsionalitasnya, dengan mengunggah file CSV dan memeriksa apakah prediksinya berhasil 
- menambahkan fitur tambahan atau lakukan penyempurnaan berdasrakan kebutuhan





MENJALANKAN APLIKASI TABULAR CLASSIFICATION

menjalankan aplikasi :
1. instalasi dependensi
   - python telah terinstall
   - buat dan aktifkan lingkungan vrtual
   - install dependensi dengan menjalankan perintah 'pip install -r requirements.txt'
3. muat model
   - pastikan model sudah ada dan disimpan dalam direktori 'models' dengan nama 'trained_model.joblib'
5. jalankan aplikasi
   - buka terminal
   - masuk ke direktori proyek
   - jalankan aplikasi dengan perintah 'python app.py'
   - aplikasi akan berjalan di 'http://127.0.0.1:5000'

menggunakan aplikasi:
1. halaman utama
   - akses halaman utama di 'http://127.0.0.1:5000'
   - halaman ini berisis formulir untuk mengunggah file
3. prediksi
   - pilih file
   - klik tombol "predict"
5. hasil prediksi
   - settelah prdikskki selesai, hasilnya akan ditampilkan dalam format tabel
  
persyaratan sistem:
- python 3.x
- lingkungan virtual
- dependensi dapat dilihat di file 'requirements.txt'
  
