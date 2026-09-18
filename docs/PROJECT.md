# The Build — Piagam Proyek Kelompok

**Bobot 20% (Tugas Kelompok) · didemokan Sesi 15 · diverifikasi Sesi 16**

The Build **bukan tugas tambahan**. Mata kuliah ini tidak memberikan pekerjaan rumah, dan tidak
ada waktu terpisah untuk mengerjakan proyek. Artefak yang kamu buat tiap sesi **adalah** The
Build. Repo ini tumbuh dari kerangka kosong di Sesi 2 menjadi aplikasi web full-stack yang
berjalan di URL publik di Sesi 14.

---

## Bagian A — Piagam (diisi malam ini, Sesi 2)

Isi lima baris di bawah ini, ganti seluruh `<…>`. Lima baris, bukan lima paragraf.
Commit berkas ini dalam PR `feature/kerangka` yang sama dengan artefak Sesi 2.

**A1 · Domain.** Aplikasi ini untuk siapa, mengurus apa. Satu kalimat.

> `<contoh: Aplikasi pencatatan kunjungan pasien untuk klinik kecil.>`

**A2 · Alur inti.** Siapa melakukan apa, lalu melihat apa. Satu kalimat. Inilah yang akan kamu
demokan selama 90 detik di Sesi 15.

> `<contoh: Petugas login, mencatat satu kunjungan pasien, lalu melihat grafik kunjungan per bulan.>`

**A3 · Entitas induk.** Nama tabel + 4–6 kolom.

> `<contoh: pasien — id, nama, tanggal_lahir, no_telepon, dibuat_pada>`

**A4 · Entitas anak.** Nama tabel + 4–6 kolom, termasuk foreign key ke induk.

> `<contoh: kunjungan — id, pasien_id (FK), tanggal, keluhan, biaya>`

**A5 · Satu angka yang digambar grafik.** Angka agregat, bukan daftar.

> `<contoh: jumlah kunjungan per bulan, 12 bulan terakhir>`

### Pembagian slice (diisi malam ini juga)

Empat anggota, empat slice. Tiap slice **memotong semua lapisan** — model → router → komponen →
test. Tidak ada "anggota yang mengerjakan CSS saja": slice seperti itu tidak bisa dipertahankan
di UAS Part A. Isi tabelnya di [`../CONTRIBUTORS.md`](../CONTRIBUTORS.md).

| # | Slice | Yang kamu miliki dari ujung ke ujung |
|---|---|---|
| 1 | **Auth & user** | tabel `users`, register/login, hashing, penyimpanan token di klien, test auth |
| 2 | **CRUD entitas induk** | model induk, endpoint list/detail/create/delete, halaman daftar, test |
| 3 | **Entitas anak + relasi** | model anak + FK, endpoint bersarang, form tambah, test relasi |
| 4 | **Endpoint agregat + grafik** | kueri agregat, endpoint statistik, komponen grafik, test angka |

---

## Bagian B — Amplop (batas yang tidak bisa dinegosiasi)

Domainnya bebas kamu pilih. **Kerumitannya tidak.** Piagam yang melanggar amplop ini ditolak saat
persetujuan, dan kamu diminta menyederhanakannya sebelum Sesi 3.

| Batas | Aturan |
|---|---|
| Jumlah tabel | **Tepat 3**: `users` + entitas induk + entitas anak |
| Relasi | **One-to-many saja.** Many-to-many tidak diajarkan dan tidak dinilai. |
| Pagination | **Offset saja** (`?skip=&limit=`). Cursor pagination tidak dipakai. |
| Alur inti | **Satu.** Bukan dua alur yang keduanya setengah jadi. |
| Endpoint agregat | **Satu.** |
| Grafik | **Satu** yang dinilai (boleh menambah, tidak menambah nilai). |
| Upload berkas, pembayaran, notifikasi, chat, peta, AI | **Di luar cakupan.** Jangan. |

Alasannya bukan supaya gampang. Alasannya: setiap sesi berdurasi 120 menit, tidak ada pekerjaan
rumah, dan rubrik Sesi 15 menilai **satu alur yang benar-benar jalan** jauh lebih tinggi daripada
lima fitur yang setengah jalan.

---

## Bagian C — Persetujuan dan penguncian

| Kapan | Apa |
|---|---|
| Sesi 2, dalam lab | Kelompok commit `docs/PROJECT.md` terisi, di dalam PR `feature/kerangka` |
| ≤ 1×24 jam kerja | Dosen menjawab **di PR itu**: disetujui, atau diminta disederhanakan |
| Sesi 3, pembukaan | **Domain dikunci.** Setelah ini domain tidak dapat diganti. |

Kelompok yang piagamnya belum disetujui tetap mengerjakan Sesi 3 dengan piagam versi sendiri —
tidak ada yang menunggu.

---

## Bagian D — Rubrik The Build (dinilai Sesi 15, di URL publik)

| Kriteria | Bobot | Yang membedakan nilai penuh |
|---|---|---|
| Fungsionalitas | 15% | Alur inti jalan ujung ke ujung tanpa perlakuan khusus |
| Kualitas frontend | 15% | Struktur komponen, empat keadaan (memuat/kosong/gagal/berhasil), responsif, aksesibel |
| Desain API | 15% | Berorientasi sumber daya, konsisten, status code benar |
| Lapisan data | 10% | Skema masuk akal, migrasi diterapkan, tidak ada N+1 |
| Keamanan | 15% | Penyimpanan kata sandi, **otorisasi tingkat objek**, tidak ada rahasia bocor |
| Pengujian & CI | 10% | Lima pengujian bermakna, pipeline wajib hijau di `main` |
| Deployment | 10% | Dapat diakses publik, konfigurasi benar, `/health` menjawab |
| Git & kolaborasi | 5% | Riwayat terbaca, **keempat anggota berkontribusi** |
| Refleksi | 5% | Jujur dan spesifik tentang apa yang dipotong |

Nilai tim disesuaikan **hingga satu tingkat per mahasiswa** berdasarkan kontribusi. Repo yang 90%
commit-nya dari satu orang memicu penyesuaian individu secara otomatis.

### Demo Sesi 15 — 8 menit, tanpa slide

| Menit | Yang harus terlihat di layar |
|---|---|
| 0:00–0:30 | Apa aplikasinya dan untuk siapa. Satu kalimat. Aplikasi sudah terbuka. |
| 0:30–2:00 | Alur inti, langsung, **di URL publik** |
| 2:00–2:45 | Skema di layar; satu keputusan pemodelan, disebut namanya |
| 2:45–3:30 | `/docs`; satu endpoint dan kontraknya; satu status code dibenarkan |
| 3:30–4:30 | Login sebagai pengguna biasa; **tunjukkan satu aksi yang ditolak** |
| 4:30–5:30 | Grafiknya, dan di mana angkanya dihitung. Sebutkan ukuran payload dalam KB. |
| 5:30–6:15 | Satu run CI hijau, dan bacakan test otorisasinya |
| 6:15–7:15 | Di ponsel, jaringan dilambatkan |
| 7:15–8:00 | Apa yang kamu potong, dan apa yang akan kamu lakukan berbeda |

---

## Bagian E — Daftar periksa akhir (diverifikasi Sesi 16, menit 0–15)

- [ ] URL repositori, branch `main`, README bentuk 5 bagian
- [ ] **URL publik hidup dan bekerja**
- [ ] `docs/api-contract.md` — sesuai dengan yang benar-benar dibangun
- [ ] `docs/state.md`
- [ ] Tabel 6 baris angka sebelum/sesudah di README
- [ ] Lima pengujian lulus di CI
- [ ] `CONTRIBUTORS.md` menyebut slice tiap anggota
- [ ] Pengungkapan AI di README terisi dan mutakhir
