function update_informasi_hasil_kompresi(informasi) {
    ukuran_sebelum.textContent = `${informasi.ukuran_sebelum} kb`;
    ukuran_setelah.textContent = `${informasi.ukuran_sesudah} kb`;
    nilai_rc.textContent = `${informasi.rc}`;
    nilai_cr.textContent = `${informasi.cr} %`;
    nilai_ss.textContent = `${informasi.ss} %`;
    waktu.textContent = `${informasi.waktu_eksekusi} s`;
}
