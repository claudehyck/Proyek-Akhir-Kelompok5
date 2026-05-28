import sys

# ==========================================
# 1. STRUKTUR DATA: DESTINASI (KATALOG MASTER)
# ==========================================
class DestinasiWisata:
    def __init__(self, id_tujuan, nama, kategori, harga_tiket, deskripsi):
        self.id_tujuan = id_tujuan
        self.nama = nama
        self.kategori = kategori
        self.harga_tiket = harga_tiket
        self.deskripsi = deskripsi
        self.slideshow = SlideshowCLL() 

# ==========================================
# 2. STRUKTUR DATA: SLIDESHOW FOTO (CIRCULAR LINKED LIST)
# ==========================================
class PhotoNode:
    def __init__(self, file_nama, deskripsi):
        self.file_nama = file_nama
        self.deskripsi = deskripsi
        self.next = None

class SlideshowCLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_foto(self, file_nama, deskripsi):
        baru = PhotoNode(file_nama, deskripsi)
        if not self.head:
            self.head = baru
            self.tail = baru
            baru.next = self.head
        else:
            self.tail.next = baru
            self.tail = baru
            self.tail.next = self.head

    def putar_slideshow(self, nama_tempat):
        if not self.head:
            print(f"\n🖼️ [Album Kosong] Belum ada foto dokumentasi di {nama_tempat}.")
            return
        
        print(f"\n🖥️ === SLIDESHOW FOTO: {nama_tempat.upper()} ===")
        print("💡 (Tekan Enter untuk foto selanjutnya, ketik 'q' lalu Enter untuk kembali ke menu)\n")
        current = self.head
        while True:
            print("-" * 50)
            print(f"📷 File : {current.file_nama}")
            print(f"📝 Info : \"{current.deskripsi}\"")
            print("-" * 50)
            
            if current == self.tail:
                print("🔄 [Ujung Galeri: Selanjutnya kembali ke foto pertama]")
                
            pilihan = input("➡️ [Enter] Next / [q] Keluar: ")
            if pilihan.lower() == 'q':
                break
            current = current.next

# ==========================================
# 3. STRUKTUR DATA: ITINERARY (SINGLY LINKED LIST)
# ==========================================
class ItineraryNode:
    def __init__(self, destinasi_obj, aktivitas, durasi):
        self.destinasi = destinasi_obj
        self.aktivitas = aktivitas
        self.durasi = durasi
        self.next = None

class ItineraryPlannerSLL:
    def __init__(self):
        self.head = None

    def tambah_rute(self, destinasi_obj, aktivitas, durasi):
        node_baru = ItineraryNode(destinasi_obj, aktivitas, durasi)
        if not self.head:
            self.head = node_baru
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node_baru

    def lihat_itinerary(self):
        if not self.head:
            print("\n📭 Itinerary Anda masih kosong!")
            return
        print("\n=== 📋 RENCANA PERJALANAN AKTIF ===")
        current = self.head
        no = 1
        while current:
            print(f"{no}. 📍 {current.destinasi.nama} ({current.durasi})")
            print(f"   Kegiatan: {current.aktivitas}")
            current = current.next
            no += 1
        print("====================================")

    def simulasi_navigasi(self):
        if not self.head:
            print("\n⚠️ Tidak ada rute untuk dinavigasi. Buat itinerary dulu!")
            return
        print("\n🚀 === MEMULAI NAVIGASI PERJALANAN ===")
        current = self.head
        while current:
            print(f"\n📍 SEKARANG DI: [ {current.destinasi.nama} ]")
            print(f"   ✨ Aktivitas: {current.aktivitas}")
            print(f"   ⏱️ Waktu    : {current.durasi}")
            print(f"   💵 Tiket Masuk: Rp {current.destinasi.harga_tiket:,}")
            
            # Fitur memutar foto lokasi di tengah-tengah navigasi
            opsi_foto = input("   👉 Mau lihat galeri foto tempat ini? (y/n): ")
            if opsi_foto.lower() == 'y':
                current.destinasi.slideshow.putar_slideshow(current.destinasi.nama)

            if current.next:
                print(f"\n   ➡️ Tujuan Berikutnya: Ke {current.next.destinasi.nama}")
                input("   [Tekan Enter untuk melanjutkan perjalanan...]")
            else:
                print("\n🎉 Hore! Anda telah sampai di tujuan akhir itinerary Anda.")
            current = current.next

# ==========================================
# 4. APLIKASI UTAMA (APP PLANNER)
# ==========================================
class AppPlanner:
    def __init__(self):
        self.katalog = []
        self.itinerary = ItineraryPlannerSLL()
        self.inisialisasi_data_dummy()

    def inisialisasi_data_dummy(self):
        d1 = DestinasiWisata(1, "Candi Borobudur", "Sejarah", 50000, "Candi megah peninggalan wangsa Syailendra.")
        d1.slideshow.tambah_foto("borobudur_pagi.jpg", "Sunrise berkabut tebal di puncak stupa.")
        d1.slideshow.tambah_foto("relief_candi.jpg", "Ukiran relief kisah hidup Sang Buddha.")
        
        d2 = DestinasiWisata(2, "Pantai Parangtritis", "Alam", 15000, "Pantai pasir hitam dengan ombak laut selatan.")
        d2.slideshow.tambah_foto("parangtritis_sunset.jpg", "Langit senja jingga keemasan yang syahdu.")
        
        d3 = DestinasiWisata(3, "Malioboro", "Belanja", 0, "Kawasan pedestrian pusat kebudayaan dan oleh-oleh.")
        d3.slideshow.tambah_foto("andong_malioboro.jpg", "Dokar/Andong tradisional khas Jogja.")
        d3.slideshow.tambah_foto("lesehan_malam.jpg", "Kuliner gudeg lesehan malam hari.")

        self.katalog.extend([d1, d2, d3])

    def tampilkan_katalog(self):
        print("\n===  KATALOG DESTINASI WISATA ===")
        for d in self.katalog:
            print(f"[{d.id_tujuan}] {d.nama} | Kategori: {d.kategori} | Tiket: Rp {d.harga_tiket:,}")
            print(f"    Info: {d.deskripsi}\n")

    def menu_tambah_itinerary(self):
        self.tampilkan_katalog()
        try:
            pilihan = int(input("Masukkan ID Destinasi yang ingin dikunjungi: "))
            # Cari objek destinasi berdasarkan ID
            destinasi_pilihan = next((x for x in self.katalog if x.id_tujuan == pilihan), None)
            
            if destinasi_pilihan:
                aktivitas = input("Rencana aktivitas di sana: ")
                durasi = input("Estimasi durasi kunjungan (misal: 2 Jam): ")
                self.itinerary.tambah_rute(destinasi_pilihan, aktivitas, durasi)
                print(f"✔️ Berhasil menambahkan {destinasi_pilihan.nama} ke itinerary!")
            else:
                print("❌ ID Destinasi tidak ditemukan.")
        except ValueError:
            print("❌ Input harus berupa angka ID.")

    def jalankan(self):
        while True:
            print("\n=====================================")
            print("         SMART TRAVEL PLANNER       ")
            print("=====================================")
            print("1. Lihat Katalog Destinasi")
            print("2. Tambah Destinasi ke Itinerary")
            print("3. Lihat Susunan Itinerary Anda")
            print("4. Mulai Simulasi Navigasi Wisata")
            print("5. Keluar Aplikasi")
            print("=====================================")
            
            pilihan = input("Pilih menu (1-5): ")
            if pilihan == "1":
                self.tampilkan_katalog()
            elif pilihan == "2":
                self.menu_tambah_itinerary()
            elif pilihan == "3":
                self.itinerary.lihat_itinerary()
            elif pilihan == "4":
                self.itinerary.simulasi_navigasi()
            elif pilihan == "5":
                print("\nTerima kasih telah menggunakan AppPlanner. Selamat berlibur! ✈️")
                sys.exit()
            else:
                print("❌ Pilihan menu tidak valid.")


# Menjalankan Aplikasi
if __name__ == "__main__":
    app = AppPlanner()
    app.jalankan()