// const myform = document.getElementById("myform");

async function post_data(url='', data={}, config={}) {
    try {
        loader.style.display = 'block';
        kotak_informasi.style.display = 'none';

        const response = await axios.post(url, data, config);
        const mydata = response.data;

        loader.style.display = 'none';
        kotak_informasi.style.display = 'block';

        return mydata
    } catch (error) {
        loader.style.display = 'none';
        console.log(error);
        // console.error("error posting data", error)
    }
}

myform.addEventListener("submit", async (e) => {
    e.preventDefault();
    const form_data = new FormData(myform);
    const data_input = Object.fromEntries(form_data);
    const formData = new FormData(myform);

    // Convert FormData to a more usable object (for easier handling)
    const dataObject = {};
    formData.forEach((value, key) => {
        if (!dataObject[key]) {
            dataObject[key] = [];
        }
        dataObject[key].push(value);
    });


    try {
        // loading.style.display = "block";
        const url = `${base_url}/api/satu`;
        const config = {
            headers: {
                'Content-Type': 'multipart/form-data'
            },
            // responseType: 'blob',
            // timeout: 30000,

        }
        const mydata = await post_data(url, dataObject, config);
        // console.log(mydata);

        informasi(mydata);

        // simpan_hasil_kompresi(mydata);

        
        // loading.style.display = "none";
    } catch (error) {
        // loading.style.display = "none";
        console.log("error post data");
        console.log(error);
    }


    // myform.reset();

});