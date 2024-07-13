from flaskr import create_app
from config import *

# from sabuk import create_app


app = create_app(Development_config)
if __name__ == "__main__":
    app.run()

# from sabuk import contoh

# from sabuk.package_aplikasi_kompresi import *

# print(contoh.tampil())
