def main():
    app = AppPlanner()
    
    while True:
        print("\n=== SMART TRAVEL PLANNER ===")
        print("1. Tambah Destinasi")
        print("2. Urutkan Destinasi")
        print("3. Cari Destinasi")
        print("4. Simpan ke File")
        print("5. Hitung Total Biaya Semua Destinasi")
        print("6. Kelola Rencana Perjalanan")
        print("7. Antrean Reservasi Tiket")
        print("8. Lihat Jadwal Kunjungan")
        print("9. Galeri Foto")
        print("10. Slideshow Rekomendasi")
        print("11. Lihat Hierarki Kategori")
        print("12. Lihat Jalur Antar Lokasi")
        print("13. Cek Validitas ID Tiket")
        print("0. Keluar")
        
        pilih = input("\nPilih menu: ")
        
        if pilih == "1":
            n = input("Nama: ")
            
            while True:
                try:
                    r = float(input("Rating (0-10): "))
                    if not (0 <= r <= 10):
                        print("Rating harus antara 0 dan 10!")
                        continue
                    break
                except ValueError:
                    print("Rating harus berupa angka! Contoh: 8.5")
            
            while True:
                try:
                    b = int(input("Biaya (Rp): "))
                    if b < 0:
                        print("Biaya tidak boleh negatif!")
                        continue
                    break
                except ValueError:
                    print("Biaya harus berupa angka bulat! Contoh: 50000")
            
            print("\nPilih Kategori:")
            print("  1. Wisata")
            print("  2. Budaya")
            print("  3. Kuliner")
            pilih_kat = input("Pilih (1/2/3): ")
            if pilih_kat == "1":
                kat = "Wisata"
            elif pilih_kat == "2":
                kat = "Budaya"
            elif pilih_kat == "3":
                kat = "Kuliner"
            else:
                kat = "Kategori Tidak Terdaftar"
            print(f"Kategori dipilih: {kat}")
            while True:
                try:
                    lat = float(input("Garis lintang (latitude): "))
                    break
                except ValueError:
                    print("Latitude harus berupa bilangan desimal! Contoh: -0.9471")

            while True:
                try:
                    lon = float(input("Garis bujur (longitude): "))
                    break
                except ValueError:
                    print("Longitude harus berupa bilangan desimal! Contoh: 100.4172")

            d = Destinasi(n, r, b, {kat}, (lat, lon))
            app.db.append(d)
            app.sll.add(n) 
            app.cll.add(n) 
            app.dll.add(f"Foto_{n}.jpg") 
            app.stack_undo.append(n)

            if kat not in app.kategori_terdaftar:
                node_kat = CategoryTree(kat)
                app.root_cat.add_child(node_kat)
                app.kategori_terdaftar[kat] = node_kat
            app.kategori_terdaftar[kat].add_child(CategoryTree(n))
            
            print(f"Destinasi '{n}' berhasil ditambahkan!")
            
        elif pilih == "2": 
            for i in range(len(app.db)):
                for j in range(len(app.db)-1):
                    if app.db[j].rating < app.db[j+1].rating:
                        app.db[j], app.db[j+1] = app.db[j+1], app.db[j]
            print("Destinasi diurutkan berdasarkan rating tertinggi.")
        
        elif pilih == "3":
            if not app.db:
                print("\n[Searching] Database masih kosong! Tambah destinasi di Menu 1 dulu.")
            else:
                cari = input("\nMasukkan nama destinasi/landmark yang dicari: ").lower()
                ketemu = False
                print(f"--- Hasil Pencarian untuk '{cari}' ---")
                
                for d in app.db:
                    if cari in d.nama.lower():
                        print(f"ID: {id(d)} | Nama: {d.nama}")
                        print(f" > Rating: {d.rating} | Biaya: Rp{d.biaya}")
                        print(f" > Kategori: {d.kategori} | Koordinat: {d.koordinat}")
                        ketemu = True
                
                if not ketemu:
                    print("Destinasi tidak ditemukan.")

        elif pilih == "4":
            with open("itinerary.txt", "w") as f:
                f.write(f"=== SMART TRAVEL PLANNER - DATA DESTINASI ===\n")
                f.write(f"Total Destinasi: {len(app.db)}\n")
                f.write("=" * 45 + "\n\n")
                for i, d in enumerate(app.db, 1):
                    f.write(f"[{i}] {d.nama}\n")
                    f.write(f"    Rating    : {d.rating}\n")
                    f.write(f"    Biaya     : Rp{d.biaya}\n")
                    f.write(f"    Kategori  : {d.kategori}\n")
                    f.write(f"    Koordinat : {d.koordinat}\n")
                    f.write("\n")
            print(f"Data {len(app.db)} destinasi berhasil tersimpan di itinerary.txt")

        elif pilih == "5": 
            if not app.db:
                print("Database kosong! Tambah destinasi di Menu 1 dulu.")
            else:
                total = app.hitung_biaya_rekursif(len(app.db))
                print(f"Total Biaya Seluruh Destinasi: Rp{total:,}")

        elif pilih == "6": 
            if app.stack_undo:
                item = app.stack_undo.pop()
                print(f"[Stack] Berhasil Undo: '{item}' dihapus dari rencana.")
            else:
                print("[Stack] Rencana kosong, tidak ada yang bisa di-undo.")

        elif pilih == "7": 
            nama_turis = input("Nama Turis untuk antrean: ")
            app.queue_tiket.append(nama_turis)
            print(f"[Queue] {nama_turis} masuk antrean. Antrean saat ini: {app.queue_tiket}")
            if input("Proses antrean sekarang? (y/n): ") == 'y':
                proses = app.queue_tiket.pop(0)
                print(f"[Queue] Tiket untuk {proses} berhasil diproses!")