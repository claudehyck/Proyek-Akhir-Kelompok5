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
            lat = input("Lat: ")
            lon = input("Lon: ")
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
            
        elif pilih == "2": # Sorting 
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
                # Ganti enumerate() dengan counter manual
                i = 1
                for d in app.db:
                    f.write(f"[{i}] {d.nama}\n")
                    f.write(f"    Rating    : {d.rating}\n")
                    f.write(f"    Biaya     : Rp{d.biaya}\n")
                    f.write(f"    Kategori  : {d.kategori}\n")
                    f.write(f"    Koordinat : {d.koordinat}\n")
                    f.write("\n")
                    i = i + 1
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

        elif pilih == "8": 
            print(f"\n[Single LL] Jadwal Kunjungan: {app.sll.display()}")

        elif pilih == "9": 
            if not app.dll.head:
                print("\n[Double LL] Galeri kosong! Tambah destinasi di Menu 1 dulu.")
            else:
                print(f"\n[Double LL] Foto saat ini: {app.dll.current.data}")
                nav = input("Tekan 'n' (Next) atau 'p' (Prev): ")
                if nav == 'n':
                    if app.dll.current.next:
                        app.dll.current = app.dll.current.next
                    else:
                        print("Sudah di foto terakhir!")
                elif nav == 'p':
                    if app.dll.current.prev:
                        app.dll.current = app.dll.current.prev
                    else:
                        print("Sudah di foto pertama!")
                
                print(f"Sekarang di: {app.dll.current.data}")

        elif pilih == "10": 
            if app.cll.head:
                print("\n[Circular LL] Menampilkan Slideshow (berputar):")
                curr = app.cll.head
                for _ in range(5): 
                    print(f" -> {curr.data}", end="")
                    curr = curr.next
                print(" ... (kembali ke awal)")
            else:
                print("Belum ada destinasi untuk slideshow.")

        elif pilih == "11": 
            label_kat = {
                "Wisata": "Nama Tempat Wisata",
                "Budaya": "Nama Tempat Budaya",
                "Kuliner": "Nama Tempat Kuliner",
                "Kategori Tidak Terdaftar": "Nama Tempat"
            }
            print("\n[Tree] Struktur Kategori Wisata:")
            print(f"Root: {app.root_cat.name}")
            if not app.root_cat.children:
                print(" (Belum ada kategori. Tambah destinasi di Menu 1 dulu.)")
            else:
                i = 0
                for child in app.root_cat.children:
                    is_last_kat = (i == len(app.root_cat.children) - 1)
                    prefix_kat = " └──" if is_last_kat else " ├──"
                    jumlah = len(child.children)
                    label = label_kat.get(child.name, "Nama Tempat")
                    print(f"{prefix_kat} {child.name} ({jumlah} tempat)")
                    j = 0
                    for leaf in child.children:
                        is_last_leaf = (j == len(child.children) - 1)
                        if is_last_kat:
                            prefix_leaf = "      └──" if is_last_leaf else "      ├──"
                        else:
                            prefix_leaf = "  │   └──" if is_last_leaf else "  │   ├──"
                        print(f"{prefix_leaf} [{label}] {leaf.name}")
                        j = j + 1
                    i = i + 1

        elif pilih == "12":
            if len(app.db) >= 2:
                for i in range(len(app.db) - 1):
                    app.graph.add_edge(app.db[i].nama, app.db[i+1].nama)
                print("\n[Graph] Jalur Navigasi Terbentuk:")
                for asal, tujuan in app.graph.adj.items():
                    print(f"  {asal} <---> {', '.join(tujuan)}")
            else:
                print("Tambahkan minimal 2 destinasi di Menu 1 dulu!")

        elif pilih == "13": 
            tid = input("Masukkan ID Tiket untuk didaftarkan: ")
            app.hash_tix.insert(tid)
            print(f"[Hash Table] Tiket '{tid}' berhasil disimpan.")
            cek = input("Cek validitas ID Tiket: ")
            if app.hash_tix.check(cek):
                print("VALID: Tiket terdaftar di sistem!")
            else:
                print("TIDAK VALID: Tiket tidak ditemukan!")

        elif pilih == "0":
            print("Program Selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 0-13.")

if __name__ == "__main__":
    main()