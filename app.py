from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

# Fungsi untuk menghitung IMT
def hitung_imt(berat_badan, tinggi_badan):
    tinggi_badan_m = tinggi_badan / 100  # Mengubah tinggi badan ke meter
    return berat_badan / (tinggi_badan_m ** 2)

# Fungsi untuk mengonversi IMT ke kategori
def kategori_imt(imt):
    if imt < 18.5:
        return "Kurus"
    elif 18.5 <= imt < 24.9:
        return "Normal"
    elif 25 <= imt < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    if request.method == "POST":
        nama = request.form["nama"]
        berat_badan = float(request.form["berat_badan"])
        tinggi_badan = float(request.form["tinggi_badan"])

        imt = hitung_imt(berat_badan, tinggi_badan)
        kategori = kategori_imt(imt)

        hasil = {
            "nama": nama,
            "imt": round(imt, 2),
            "kategori": kategori
        }

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
