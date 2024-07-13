import io

from flask_restful import Resource
from flask import request, jsonify, make_response, send_file, url_for, redirect
from .package_aplikasi_kompresi.extensions import np
from .package_aplikasi_kompresi.facade import FacadeKompresi
from .package_aplikasi_kompresi.dokumen import Dokumen, SumberDataDariNumpy
from .package_aplikasi_kompresi.transformasi import *
from .package_aplikasi_kompresi.evaluasi import Evaluasi

class SatuResource(Resource):
    def get(self):
        return {"data": "oke"}
    
    def post(self):
        # data = request.get_json()
        metode = request.form.getlist("metode[]")
        file_dokumen = request.files.getlist("file_dokumen[]")[0]

        data_np = np.frombuffer(file_dokumen.read(), dtype=np.uint8)
        
        dokumen = Dokumen()
        dokumen.set_data(SumberDataDariNumpy(data_np))

        evaluasi = Evaluasi()
        evaluasi.mulai()
        evaluasi.set_ukuran_sebelum(dokumen.ukuran_bit())

        facade_kompresi = FacadeKompresi()
        dok_hasil = facade_kompresi.kompresi(metode, dokumen)

        evaluasi.set_ukuran_sesudah(dok_hasil.ukuran_bit())
        evaluasi.selesai()

        evaluasi.hitung_cr()
        evaluasi.hitung_rc()
        evaluasi.hitung_ss()

        hasil_evaluasi = evaluasi.to_dict()

        file_name = "hasil_kompresi.pdf"
        dok_hasil.simpan_file(file_name)

        # dok_hasil.bentuk(BinerInt, inplace=True)
        # bytes_data = dok_hasil.data.tobytes()

        # bytes_string = bytes_data.decode("latin1")
        # print(len(bytes_data))
        # print(dok_hasil.data.shape)

        # buffer = io.BytesIO(bytes_data)
        # buffer.seek(0)  # Move to the start of the buffer

        context = {
            "evaluasi": hasil_evaluasi,
            "download_url": url_for("my_bp.download_file", filename=file_name, _external=True),

        }

        return jsonify(context)


        # myfile = send_file(
        #     buffer,
        #     as_attachment=True,
        #     download_name="hasil.pdf",
        #     mimetype="application/pdf"
            
        # )

        # response = make_response(myfile)

        # return response