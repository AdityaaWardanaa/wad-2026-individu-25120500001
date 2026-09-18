# Deployment — Sesi 14 (bobot 5%)

Berkas milik dosen. Ikuti langkahnya; jangan ubah isinya.

Yang dinilai di Sesi 14: **URL publik aktif + CI hijau**. Dinilai dengan dibuka di proyektor dan
di ponsel, bukan dari tangkapan layar.

Arsitektur deploy:

```
frontend (statis)  ->  GitHub Pages     (dari repo ini, lewat Actions)
backend (container) -> Render free tier (dari Dockerfile di repo ini)
basis data          -> Neon Postgres    (yang sudah kamu pakai sejak Sesi 5)
```

## 1. Backend ke Render

1. Buka https://render.com, daftar **dengan akun GitHub**. Tidak perlu kartu kredit.
2. **New → Web Service** → pilih repo kelompokmu.
3. Isi:
   - **Runtime:** Docker
   - **Dockerfile Path:** `./Dockerfile`
   - **Instance Type:** Free
4. **Environment → Add Environment Variable**, salin dari `.env` kelompokmu:
   - `DATABASE_URL` — connection string Neon
   - `SECRET_KEY`
   - `CORS_ORIGINS` — isi dengan URL GitHub Pages kamu (lihat langkah 2), **bukan** `*`
5. Deploy. Tunggu sampai statusnya `Live`, lalu buka `https://<nama>.onrender.com/health`.
   Harus membalas `{"status":"ok"}`.

> Free tier Render menidurkan layanan setelah tidak dipakai. Permintaan pertama bisa perlu
> ~50 detik. Itu normal dan tidak mengurangi nilai — **tapi buka URL-nya satu menit sebelum
> demo Sesi 15 supaya sudah bangun.**

## 2. Frontend ke GitHub Pages

1. Repo → **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. Repo → **Settings → Secrets and variables → Actions → Variables → New variable**:
   - Nama `VITE_API_BASE`, nilai `https://<nama>.onrender.com`
3. Di kode frontend, base URL API dibaca dari environment, jangan ditulis langsung:
   ```js
   const API = import.meta.env.VITE_API_BASE ?? 'http://localhost:8000'
   ```
4. Repo → **Actions → deploy-pages → Run workflow**.
5. URL-nya `https://<pemilik>.github.io/<nama-repo>/`. Tulis URL ini di README.

## 3. CI wajib hijau di `main`

Repo → **Settings → Rules → Rulesets → New branch ruleset**:

- Target: `main`
- **Require a pull request before merging** — 1 approval
- **Require status checks to pass** — pilih `verify.py`, `backend`, `frontend`, `scan`
- **Block force pushes**

Setelah ini, `main` tidak bisa merah.

## 4. Daftar periksa sebelum keluar dari Sesi 14

- [ ] `https://<pemilik>.github.io/<repo>/` terbuka di ponsel, di jaringan seluler
- [ ] Alur inti jalan dari ujung ke ujung di URL publik itu
- [ ] `https://<nama>.onrender.com/health` membalas 200
- [ ] Tidak ada `localhost` tersisa di kode frontend yang di-build
- [ ] `CORS_ORIGINS` berisi URL Pages, bukan `*`
- [ ] Kedua URL tertulis di README
- [ ] CI hijau, dan wajib di `main`

## Kalau deploy gagal

Deployment adalah risiko terbesar mata kuliah ini, dan meja bantuan dibuka sejak menit 82.
**Menit 110 adalah tenggat sebenarnya** — setelah itu dosen menyiapkan hosting cadangan supaya
kelompokmu tetap punya URL untuk didemokan di Sesi 15. Memakai cadangan mengurangi nilai
Deployment, tidak menghapus nilai sesi lain. Berhenti mencoba diam-diam sampai 21:55 adalah
kesalahan yang paling mahal.
