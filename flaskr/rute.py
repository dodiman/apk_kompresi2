from flask import Blueprint, render_template, request, make_response, send_file
import io
import numpy as np
import os

from .package_aplikasi_kompresi.dokumen import Dokumen
from .package_aplikasi_kompresi.sumber_data import SumberDataDariNumpy
from .package_aplikasi_kompresi.transformasi import BinerHex, HexInt, BinerInt, IntBiner, IntHex
from .package_aplikasi_kompresi.algoritma_kompresi import MetodeFibonacci, MetodeLevenstein, Metode
from .package_aplikasi_kompresi.builder import Builder
from .package_aplikasi_kompresi.path import Path

my_bp = Blueprint("my_bp",__name__)

@my_bp.route("/dekompresi_pdf", methods=["POST", "GET"])
def dekompresi_pdf():
    if request.method == "POST":
        dok = request.files["file_dokumen"]

        data_np = np.frombuffer(dok.read(), dtype=np.uint8)

        dokumen = Dokumen()
        dokumen.set_data(SumberDataDariNumpy(data_np))
        temp = dokumen.bentuk(IntBiner)
        dokumen.set_data(SumberDataDariNumpy(temp))

        dekompresi_builder = Builder()
        dok_dekompresi1 = dekompresi_builder.dekompresi_banyak(Metode(), dokumen)

        print("----------ini---")
        print(dok_dekompresi1.data)

        # dok_dekompresi1.bentuk(BinerInt, inplace=True)
        pdf_content = dok_dekompresi1.data.tobytes()

        buffer = io.BytesIO(pdf_content)
        buffer.seek(0)  # Move to the start of the buffer

        return send_file(
            buffer,
            as_attachment=True,
            mimetype="application/pdf",
            download_name="hasil_dekompresi.pdf"
        )

        # return render_template("dekompresi_pdf.html")

    if request.method == "GET":
        return render_template("dekompresi_pdf.html")

@my_bp.route("/download_file/<filename>")
def download_file(filename):
    path_setting = Path()
    file_directory = path_setting.file_uploads
    file_path = os.path.join(file_directory, filename)
    
    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return str(e)
    # return file_path

# @my_bp.route("/download")
# def download():
#     data_np = np.arange(5000, dtype=np.uint8)
    
#     pdf_content = data_np.tobytes()

#     buffer = io.BytesIO(pdf_content)
#     buffer.seek(0)  # Move to the start of the buffer


#     return send_file(
#         buffer,
#         as_attachment=True,
#         mimetype="application/pdf",
#         download_name="ccc.pdf"
#     )

@my_bp.route("/kompresi_pdf")
def kompresi_pdf():
    return render_template("kompresi_pdf.html")


@my_bp.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@my_bp.route("/contoh_form", methods=["POST", "GET"])
def contoh_form():
    if request.method == "POST":
        nama = request.form["nama"]
        metode = request.form.getlist("metode")
        all_form = request.form.to_dict()
        
        context = {
            "all_form": all_form,
            "metode": metode,
            "nama": nama
        }
        return render_template("contoh_form.html", **context)

    if request.method == "GET":
        context = {}
        return render_template("contoh_form.html", **context)

@my_bp.route("/", methods=["POST", "GET"])
def index():
    context = {
        "form_data": None
    }

    if request.method == "POST":
        form_data = request.files["file_dokumen"]
        
        data_np = np.frombuffer(form_data.read(), dtype=np.uint8)

        dokumen = Dokumen()
        dokumen.set_data(SumberDataDariNumpy(data_np))
        temp = dokumen.bentuk(IntBiner)
        dokumen.set_data(SumberDataDariNumpy(temp))

        # mulai kompresi
        kompresi_fib = Builder()
        dok_kompresi1, kunci_builder1 = kompresi_fib.kompresi_banyak(MetodeFibonacci(), dokumen)

        dok_kompresi1.simpan_file("data_kompresi1.pdf")

        context["form_data"] = (dok_kompresi1, kunci_builder1)
        return render_template("index.html", **context)

    if request.method == "GET":
        return render_template("halaman_utama.html", **context)