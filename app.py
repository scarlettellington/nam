# from flask import Flask, render_template, request
# from joblib import load

# app = Flask(__name__)

# # Muat model di dalam fungsi prediksi
# def load_model():
#     try:
#         # Cobalah untuk memuat model
#         return load('models/trained_model.joblib')
#     except Exception as e:
#         print("Gagal memuat model:", str(e))
#         return None

# # Model dimuat saat aplikasi dijalankan
# model = load_model()

# # Tentukan fungsi prediksi
# def predict(input_data):
#     try:
#         # Lakukan prediksi menggunakan model
#         prediction = model.predict(input_data)
#         return prediction
#     except Exception as e:
#         print("Gagal melakukan prediksi dengan model:", str(e))
#         return None

# # Tentukan route untuk halaman utama
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Tentukan route untuk menerima data dan memberikan prediksi
# @app.route('/predict', methods=['POST'])
# def predict_route():
#     if request.method == 'POST':
#         input_data = request.form.to_dict()
#         # Proses data input menjadi format yang bisa diprediksi
#         # ...
#         result = predict(input_data)
        
#         if result is not None:
#             return render_template('result.html', result=result)
#         else:
#             return render_template('error.html')  # Tambahkan halaman error

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)

# Fungsi untuk memuat model
def load_model():
    try:
        # Coba memuat model
        return load('models/trained_model.joblib')
    except Exception as e:
        print("Gagal memuat model:", str(e))
        return None

# Model dimuat saat aplikasi dijalankan
model = load_model()

# Tentukan fungsi prediksi
def predict(input_data):
    try:
        # Lakukan prediksi menggunakan model
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        print("Gagal melakukan prediksi dengan model:", str(e))
        return None

# Tentukan route untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Tentukan route untuk menerima data dan memberikan prediksi
@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        if request.method == 'POST':
            input_data = request.form.to_dict()
            # Proses data input menjadi format yang bisa diprediksi
            # ...
            result = predict(input_data)

            if result is not None:
                return render_template('result.html', result=result)
            else:
                return render_template('error.html')  # Gunakan template error
    except Exception as e:
        # Tangani kesalahan tak terduga dan render template error
        print("Kesalahan tak terduga:", str(e))
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
