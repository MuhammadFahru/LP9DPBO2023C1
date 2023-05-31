from hunian import Hunian

class Mansion(Hunian):
    def __init__(self, nama_pemilik, alamat, foto_bangunan, jml_penghuni, jml_kamar, luas_tanah, jumlah_lantai, jumlah_kolam_renang):
        super().__init__("Mansion", alamat, foto_bangunan, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.luas_tanah = luas_tanah
        self.jumlah_lantai = jumlah_lantai
        self.jumlah_kolam_renang = jumlah_kolam_renang

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Mansion a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_luas_tanah(self):
        return self.luas_tanah
    
    def get_jumlah_lantai(self):
        return self.jumlah_lantai
    
    def get_jumlah_kolam_renang(self):
        return self.jumlah_kolam_renang
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas Tanah : " + str(self.luas_tanah) + " m2\nJumlah Lantai : " + str(self.jumlah_lantai) + "\nJumlah Kolam Renang : " + str(self.jumlah_kolam_renang)