class DestinasiNode: #Node untuk merepresentasikan satu tempat wisata dalam rute
    def __init__(self, nama, aktivitas, estimasi_waktu):
        self.nama = nama
        self.aktivitas = aktivitas
        self.estimasi_waktu = estimasi_waktu  # dalam jam/menit
        self.next = None  # Pointer ke destinasi berikutnya

class ItineraryPlanner: #Class Singly Linked List untuk mengatur rencana perjalanan.
    def __init__(self):
        self.head = None

    def tambah_destinasi_akhir(self, nama, aktivitas, estimasi_waktu): #Menambahkan destinasi di akhir rute perjalanan.
        baru = DestinasiNode(nama, aktivitas, estimasi_waktu)
        if not self.head:
            self.head = baru
            print(f"📌 {nama} berhasil dijadikan destinasi awal!")
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = baru
        print(f"📌 {nama} berhasil ditambahkan ke rute.")

    def hapus_destinasi(self, nama_destinasi): #Menghapus destinasi tertentu dari rute (misal: batal berkunjung).
        current = self.head
        prev = None

        if current and current.nama.lower() == nama_destinasi.lower():
            self.head = current.next
            print(f"❌ {nama_destinasi} dihapus dari rute.")
            return

        while current and current.nama.lower() != nama_destinasi.lower():
            prev = current
            current = current.next

        if not current:
            print(f"🔍 Destinasi '{nama_destinasi}' tidak ditemukan di rute.")
            return

        prev.next = current.next
        print(f"❌ {nama_destinasi} dihapus dari rute.")

    def cetak_itinerary(self): #Menampilkan seluruh daftar rencana perjalanan.
        if not self.head:
            print("📭 Rencana perjalanan masih kosong.")
            return

        print("\n=== RENCANA PERJALANAN (ITINERARY) ===")
        current = self.head
        nomor = 1
        while current:
            print(f"{nomor}. {current.nama} ({current.estimasi_waktu})")
            print(f"   Kegiatan: {current.aktivitas}")
            current = current.next
            nomor += 1
        print("=======================================")

    def simulator_navigasi(self): #Simulasi navigasi langkah-demi-langkah dari awal sampai akhir.
        if not self.head:
            print("X Tidak ada rute untuk dinavigasi.")
            return

        print("\n🚀 MEMULAI SIMULASI NAVIGASI WISATA 🚀")
        current = self.head
        while current:
            print(f"\n📍 Sekarang Anda berada di: [ {current.nama} ]")
            print(f"   ✨ Aktivitas: {current.aktivitas}")
            print(f"   ⏱️ Durasi Kunjungan: {current.estimasi_waktu}")
            
            if current.next:
                print(f"   ➡️ Rute selanjutnya: Ke {current.next.nama}")
                input("   [Tekan Enter untuk jalan ke destinasi berikutnya...]")
            else:
                print("\n🎉 Hore! Anda telah menyelesaikan semua rute perjalanan Anda.")
            current = current.next


# ==========================================
# SIMULASI PENGGUNAAN PROGRAM
# ==========================================
if __name__ == "__main__":
    # 1. Inisialisasi Perencana Perjalanan
    my_trip = ItineraryPlanner()

    # 2. Tambah Destinasi (Push Back / Append)
    print("--- Membuat Rencana Perjalanan ---")
    my_trip.tambah_destinasi_akhir("Bandara Wisata", "Landing dan Sewa Mobil", "1 Jam")
    my_trip.tambah_destinasi_akhir("Candi Borobudur", "Eksplorasi candi dan foto-foto", "3 Jam")
    my_trip.tambah_destinasi_akhir("Resto Ayam Goreng Bu Tini", "Makan siang kuliner lokal", "1.5 Jam")
    my_trip.tambah_destinasi_akhir("Malioboro", "Beli oleh-oleh dan jalan-jalan sore", "2 Jam")

    # 3. Cetak Itinerary Saat Ini
    my_trip.cetak_itinerary()

    # 4. Simulasi Hapus Destinasi (Misal: karena kemalaman, skip Malioboro)
    print("\n--- Perubahan Rencana ---")
    my_trip.hapus_destinasi("Resto Ayam Goreng Bu Tini")
    
    # Cetak ulang setelah dihapus
    my_trip.cetak_itinerary()

    # 5. Jalankan Simulator Navigasi Wisata
    my_trip.simulator_navigasi()