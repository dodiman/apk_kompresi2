function informasi(mydata) {
    const hasil_evaluasi = mydata["evaluasi"];

    update_informasi_hasil_kompresi(hasil_evaluasi);


    // console.log(hasil_evaluasi);

    // const div_elm = document.createElement("div");

    // const p_elm = document.createElement("p");
    // p_elm.textContent = `cr: ${hasil_evaluasi['cr']} rc: ${hasil_evaluasi['rc']} sebelum: ${hasil_evaluasi['ukuran_sebelum']} sesudah: ${hasil_evaluasi['ukuran_sesudah']}`;
    
    
    // const tombol_simpan = document.createElement("button");
    // tombol_simpan.textContent = "Simpan";
    
    // div_elm.appendChild(p_elm)
    // div_elm.appendChild(tombol_simpan);
    
    // document.body.appendChild(div_elm);



    tombol_simpan_hasil_kompresi.addEventListener("click", () => {
        download_file(mydata["download_url"]);
    });
}