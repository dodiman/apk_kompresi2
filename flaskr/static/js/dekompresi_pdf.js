const mydata = document.getElementById("file_dokumen");
const kotak_deskripsi = document.getElementById("kotak_deskripsi");


mydata.addEventListener('change', () => {
    const files = mydata.files;

    if (files.length > 0) {
        kotak_deskripsi.style.display = "block";
        nama_file.textContent = files[0].name;
        ukuran_file.textContent = `${(files[0].size / 1024).toFixed(2)} kb`;
        label_input.textContent = "ganti file";
    }
});