class DestinasiWisata: #Class untuk menampung data STATIS tempat wisata (Katalog).
    def __init__(self, id_tujuan, nama, kategori, harga_tiket, deskripsi):
        self.id_tujuan = id_tujuan
        self.nama = nama
        self.kategori = kategori
        self.harga_tiket = harga_tiket
        self.deskripsi = deskripsi

class ItineraryNode: #Node DINAMIS untuk rantai perjalanan (Singly Linked List).
    def __init__(self, destinasi_obj, aktivitas, durasi):
        self.destinasi = destinasi_obj  # Mengambil data dari objek DestinasiWisata
        self.aktivitas = aktivitas
        self.durasi = durasi
        self.next = None

class ItineraryPlanner: #Singly Linked List untuk mengatur rute perjalanan user.
    def __init__(self):
        self.head = None

    def tambah_ke_rute(self, destinasi_obj, aktivitas, durasi): #Memasukkan destinasi pilihan dari katalog ke dalam itinerary.
        node_baru = ItineraryNode(destinasi_obj, aktivitas, durasi)
        if not self.head:
            self.head = node_baru
            print(f"✅ {destinasi_obj.nama} berhasil diset sebagai start awal perjalanan!")
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = node_baru
        print(f"✅ {destinasi_obj.nama} berhasil ditambahkan ke rute berikutnya.")

    def cetak_itinerary(self): #Menampilkan jadwal perjalanan yang sudah disusun.
        if not self.head:
            print("\n📭 Itinerary Anda masih kosong. Silakan pilih dari katalog destinasi!")
            return

        print("\n==================================================")
        print("          📋 RENCANA PERJALANAN ANDA             ")
        print("==================================================")
        current = self.head
        nomor = 1
        while current:
            print(f"{nomor}. 📍 {current.destinasi.nama} [{current.destinasi.kategori}]")
            print(f"   ⏱️ Durasi  : {current.durasi}")
            print(f"   ⚙️ Kegiatan: {current.aktivitas}")
            print(f"   💵 Tiket   : Rp {current.destinasi.harga_tiket:,}")
            print("-" * 50)
            current = current.next
        print("==================================================")


# ==========================================
# SIMULASI PENGGUNAAN PROGRAM
# ==========================================
if __name__ == "__main__":
    # 1. MEMBUAT FITUR DESTINASI (KATALOG WISATA / BANK DATA)
    # Disimpan dalam bentuk List biasa karena fungsinya hanya sebagai wadah pilihan
    katalog_destinasi = [
        DestinasiWisata(1, "Candi Borobudur", "Sejarah", 50000, "Candi Buddha terbesar di dunia."),
        DestinasiWisata(2, "Pantai Parangtritis", "Alam", 15000, "Pantai selatan dengan mitos Ratu Kidul dan sunset indah."),
        DestinasiWisata(3, "Gembira Loka Zoo", "Edukasi", 60000, "Kebun binatang terlengkap di Yogyakarta."),
        DestinasiWisata(4, "Taman Pintar", "Edukasi", 25000, "Wahana belajar sains yang seru untuk remaja dan anak-anak."),
        DestinasiWisata(5, "Malioboro", "Belanja", 0, "Pusat oleh-oleh, kuliner, dan jalan-jalan ikonik.")
    ]

    # Menampilkan Fitur Destinasi ke User
    print("==================================================")
    print("        KATALOG DESTINASI WISATA TERSEDIA        ")
    print("==================================================")
    for wisata in katalog_destinasi:
        print(f"[{wisata.id_tujuan}] {wisata.nama} ({wisata.kategori})")
        print(f"    Deskripsi: {wisata.deskripsi}")
        print(f"    Tiket    : Rp {wisata.harga_tiket:,}\n")
    print("==================================================\n")


    # 2. MEMBUAT FITUR ITINERARY (USER MULAI MERENCANAKAN)
    itinerary_saya = ItineraryPlanner()

    print("--- User memilih destinasi dari katalog dan menyusun rute ---")
    # User memilih Id 1 (Borobudur) untuk rute pertama
    itinerary_saya.tambah_ke_rute(katalog_destinasi[0], "Foto-foto di stupa puncak", "3 Jam")
    
    # User memilih Id 5 (Malioboro) untuk rute kedua
    itinerary_saya.tambah_ke_rute(katalog_destinasi[4], "Beli bakpia dan naik andong", "2 Jam")
    
    # User memilih Id 2 (Pantai Parangtritis) untuk rute ketiga
    itinerary_saya.tambah_ke_rute(katalog_destinasi[1], "Melihat sunset di pinggir pantai", "2.5 Jam")

    # 3. CETAK HASIL AKHIR ITINERARY
    itinerary_saya.cetak_itinerary()