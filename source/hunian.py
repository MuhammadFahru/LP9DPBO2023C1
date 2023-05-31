class Hunian():
    def __init__(self, jenis, alamat, foto_bangunan, jml_penghuni = 1, jml_kamar = 1):
        self.jenis = jenis
        self.alamat = alamat
        self.foto_bangunan = foto_bangunan
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar

    def get_jenis(self):
        return self.jenis
    
    def get_alamat(self):
        return self.alamat
    
    def get_foto_bangunan(self):
        return self.foto_bangunan

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang.\nAlamat : " + str(self.alamat)