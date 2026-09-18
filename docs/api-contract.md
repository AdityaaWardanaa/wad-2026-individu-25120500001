# Kontrak API

> **Stub — diisi di Sesi 7 (bobot 5%), lalu direkonsiliasi di Sesi 16.**
> Kontrak ini harus cukup bagi kelompok lain untuk memakai API-mu **tanpa penjelasan lisan**.
> Di Sesi 7 kelompok lain benar-benar akan mencobanya (peer review).
>
> Hapus blok ini dan kata TODO saat kamu mengisinya.

## Ringkasan

TODO — satu paragraf: apa yang API ini layani, dan untuk siapa.

Base URL lokal: `http://localhost:8000`
Base URL produksi: TODO (diisi Sesi 14)

## Model data

TODO — tiga tabel: `users`, `<induk>`, `<anak>`. Untuk tiap tabel: nama kolom, tipe, wajib/opsional,
dan relasinya. Sertakan satu kalimat yang menjelaskan relasi one-to-many-nya.

## Autentikasi

TODO — cara memperoleh token, di header mana dikirim, berapa lama berlaku (diisi Sesi 9).

## Endpoint

Untuk **setiap** endpoint, isi tabel berikut. Jangan menyingkat.

### `GET /…`

| Bagian | Isi |
|---|---|
| Tujuan | TODO |
| Auth | TODO — publik / perlu token / perlu kepemilikan objek |
| Query params | TODO |
| Body permintaan | TODO |
| Balasan 2xx | TODO — contoh JSON nyata, bukan skema |
| Balasan error | TODO — status code mana, kapan, dan bentuk badan pesannya |

## Status code yang dipakai

| Kode | Kapan dipakai di API ini |
|---|---|
| 200 | TODO |
| 201 | TODO |
| 204 | TODO |
| 400 / 422 | TODO — bedakan keduanya |
| 401 vs 403 | TODO — bedakan keduanya, ini sering salah |
| 404 | TODO |

## Versioning

TODO — apa yang terjadi bila kontrak ini berubah setelah kelompok lain memakainya.
