class PhotoNode: #Node untuk menyimpan data foto.
    def __init__(self, file_nama, deskripsi):
        self.file_nama = file_nama
        self.deskripsi = deskripsi
        self.next = None  # Menunjuk ke foto berikutnya

class DestinationSlideshowCLL: #Circular Linked List untuk Slideshow Foto Wisata.
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_foto(self, file_nama, deskripsi):
        """Menambahkan foto ke dalam rantaian circular."""
        baru = PhotoNode(file_nama, deskripsi)
        
        if not self.head: # Jika list kosong, node baru menunjuk ke dirinya sendiri
            self.head = baru
            self.tail = baru
            baru.next = self.head
        else: # Menghubungkan tail lama ke node baru
            self.tail.next = baru
            self.tail = baru
            self.tail.next = self.head
        print(f"📸 Foto [{file_nama}] berhasil ditambahkan ke slideshow.")

    def jalankan_slideshow(self): #Simulasi memutar slideshow foto tanpa henti.
        if not self.head:
            print("📭 Album foto kosong, tidak bisa memulai slideshow.")
            return

        print("\n🖥️ === MEMULAI SLIDESHOW FOTO WISATA ===")
        print("💡 (Tekan Enter untuk melihat foto selanjutnya. Ketik 'q' lalu Enter untuk keluar)\n")
        
        current = self.head
        while True:
            print("-" * 50)
            print(f"🖼️ Menampilkan: {current.file_nama}")
            print(f"📝 Keterangan : \"{current.deskripsi}\"")
            print("-" * 50)
            
            if current == self.tail: # Cek apakah ini ujung list (tail) untuk memberi info ke user
                print("🔄 [Info: Ini foto terakhir. Selanjutnya akan otomatis kembali ke foto pertama]")

            pilihan = input("➡️ Tekan [Enter] untuk Next, atau ketik 'q' untuk berhenti: ")
            if pilihan.lower() == 'q':
                print("\n🖥️ Slideshow dihentikan.")
                break
                
            current = current.next  # Pindah ke foto berikutnya (akan otomatis looping ke head jika sudah di tail)


# ==========================================
# SIMULASI INTEGRASI PADA PROYEK WISATA
# ==========================================
if __name__ == "__main__":
    # Membuat objek slideshow untuk destinasi tertentu (Misal: Bali Trip)
    slideshow_bali = DestinationSlideshowCLL()

    # Memasukkan foto-foto dokumentasi
    slideshow_bali.tambah_foto("sunset_kuta.jpg", "Menikmati senja di Pantai Kuta.")
    slideshow_bali.tambah_foto("tari_kecak.jpg", "Pertunjukan seni Tari Kecak di Uluwatu.")
    slideshow_bali.tambah_foto("ubud_rice_terrace.jpg", "Sawah terasering yang hijau dan menyejukkan mata.")

    # Jalankan simulator slideshow
    slideshow_bali.jalankan_slideshow()

    