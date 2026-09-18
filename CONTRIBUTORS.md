# Kontributor

**Kelompok:** `<nomor>` · **Kelas:** WAD09 · **Mata kuliah:** Web Application Development

Isi tabel ini di Sesi 2 dan perbarui bila ada perubahan. Berkas ini diverifikasi ulang di
Sesi 16 dan menjadi dasar UAS Part A — tiap mahasiswa mempertahankan **slice-nya sendiri**.

| # | Slice | Nama lengkap | NIM | Akun GitHub | Peran ketua |
|---|---|---|---|---|---|
| 1 | Auth & user | `<nama>` | `<NIM>` | `@<username>` | |
| 2 | CRUD entitas induk | `<nama>` | `<NIM>` | `@<username>` | |
| 3 | Entitas anak + relasi | `<nama>` | `<NIM>` | `@<username>` | |
| 4 | Endpoint agregat + grafik | `<nama>` | `<NIM>` | `@<username>` | |

Tandai satu baris dengan `Ketua` pada kolom terakhir.

## Apa arti "memiliki sebuah slice"

Slice-mu memotong **semua lapisan**, bukan satu lapisan saja:

```
model (SQLAlchemy) → skema (Pydantic) → router (FastAPI) → komponen (Vue) → test
```

Kamu menulisnya, kamu men-debug-nya, dan kamu yang mempertahankannya. Di UAS Part A kamu akan
diminta:

1. menjelaskan satu endpoint yang **kamu** tulis,
2. menjelaskan pemeriksaan otorisasi di slice-mu, dan apa yang terjadi bila dihapus,
3. menceritakan satu bug yang **kamu** perbaiki, pada sesi yang kamu sebutkan,
4. menunjuk bagian terlemah di slice-mu dan apa yang akan kamu perbaiki dalam satu sesi lagi.

Kamu juga dapat diminta menjelaskan bagian yang **bukan** slice-mu (Ketentuan 5). Tinjau PR
temanmu dengan sungguh-sungguh; itu bukan formalitas.

## Bukti kontribusi

Nilai individu = nilai kelompok × faktor kontribusi (0–1), dihitung dari:

- commit dan pull request **atas nama sendiri** di repo ini,
- peer assessment,
- kemampuan menjelaskan bagian mana pun dari kode saat pembelaan.

**Mahasiswa tanpa commit atas namanya sendiri memperoleh 0 untuk Tugas Kelompok**, terlepas dari
nilai timnya. Kalau kamu pair programming, pakai `Co-authored-by:` di pesan commit:

```
git commit -m "feat: endpoint daftar kunjungan

Co-authored-by: Nama Teman <email@contoh.com>"
```
