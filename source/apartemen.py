from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, alamat, foto_bangunan, jml_penghuni, jml_kamar, nama_kompleks, jumlah_unit):
        super().__init__("Apartemen", alamat, foto_bangunan, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.nama_kompleks = nama_kompleks
        self.jumlah_unit = jumlah_unit

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_nama_kompleks(self):
        return self.nama_kompleks
    
    def get_jumlah_unit(self):
        return self.jumlah_unit
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nNama Kompleks : " + str(self.nama_kompleks) + "\nJumlah Unit : " + str(self.jumlah_unit)