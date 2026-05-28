class PhotoNode: #Node untuk merepresentasikan satu foto dalam album destinasi.
    def __init__(self, file_nama, deskripsi):
        self.file_nama = file_nama  # Contoh: "borobudur_sunset.jpg"
        self.deskripsi = deskripsi  # Contoh: "Foto pas sunset keren banget!"
        self.next = None

class DestinasiNode: #Node Wisata yang sekarang dilengkapi dengan pointer ke Album Foto.
    def __init__(self, nama, aktivitas, estimasi_waktu):
        self.nama = nama
        self.aktivitas = aktivitas
        self.estimasi_waktu = estimasi_waktu
        self.next = None
        self.head_foto = None 

    def tambah_foto(self, file_nama, deskripsi): #Menambahkan foto baru ke dalam album destinasi ini (SLL Foto).
        foto_baru = PhotoNode(file_nama, deskripsi)
        if not self.head_foto:
            self.head_foto = foto_baru
        else:
            current = self.head_foto
            while current.next:
                current = current.next
            current.next = foto_baru
        print(f"📸 Foto '{file_nama}' berhasil disimpan di {self.nama}.")

    def cetak_album_foto(self): #Menampilkan semua foto yang ada di destinasi ini.
        if not self.head_foto:
            print(f"   🖼️ [Album Kosong] Belum ada foto di {self.nama}.")
            return
        
        print(f"   🖼️ Album Foto di {self.nama}:")
        current = self.head_foto
        while current:
            print(f"      - [{current.file_nama}] -> \"{current.deskripsi}\"")
            current = current.next


class ItineraryPlannerWithPhotos: #Class utama untuk mengatur rute perjalanan.
    def __init__(self):
        self.head = None

    def tambah_destinasi(self, nama, aktivitas, estimasi_waktu):
        baru = DestinasiNode(nama, aktivitas, estimasi_waktu)
        if not self.head:
            self.head = baru
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = baru

    def cari_destinasi(self, nama_destinasi): #Mencari node destinasi berdasarkan namanya.
        current = self.head
        while current:
            if current.nama.lower() == nama_destinasi.lower():
                return current
            current = current.next
        return None

    def cetak_semua_itinerary(self):
        """Cetak rute beserta album fotonya."""
        print("\n==========================================")
        print("   REKAP PERJALANAN & DOKUMENTASI FOTO    ")
        print("==========================================")
        current = self.head
        while current:
            print(f"\n📍 {current.nama}")
            print(f"   Aktivitas: {current.aktivitas}")
            # Panggil fungsi cetak SLL Foto internal milik node destinasi
            current.cetak_album_foto() 
            current = current.next
        print("\n==========================================")


# ==========================================
# SIMULASI PENGGUNAAN PROGRAM
# ==========================================
if __name__ == "__main__":
    trip_dokumentasi = ItineraryPlannerWithPhotos()

    trip_dokumentasi.tambah_destinasi("Candi Borobudur", "Eksplorasi Candi", "3 Jam")
    trip_dokumentasi.tambah_destinasi("Malioboro", "Beli Oleh-oleh", "2 Jam")

    print("--- Mengambil Foto di Lokasi (Simulasi) ---")
    borobudur = trip_dokumentasi.cari_destinasi("Candi Borobudur")
    if borobudur:
        borobudur.tambah_foto("borobudur_pagi.jpg", "Suasana sejuk jam 6 pagi.")
        borobudur.tambah_foto("relief_candi.jpg", "Foto detail relief cerita di dinding.")

    malioboro = trip_dokumentasi.cari_destinasi("Malioboro")
    if malioboro:
        malioboro.tambah_foto("bakpia_pathok.jpg", "Beli bakpia buat keluarga di rumah.")
        malioboro.tambah_foto("andong_malam.jpg", "Naik andong keliling kota.")

    trip_dokumentasi.cetak_semua_itinerary()