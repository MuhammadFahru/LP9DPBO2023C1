from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, alamat, foto_bangunan, jml_penghuni, jml_kamar, luas_bangunan):
        super().__init__("Rumah", alamat, foto_bangunan, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.luas_bangunan = luas_bangunan

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_luas_bangunan(self):
        return self.luas_bangunan
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas Bangunan : " + str(self.luas_bangunan) + " m2"
