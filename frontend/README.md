# frontend/ — sengaja kosong

Kamu yang mengisi folder ini, mulai Sesi 2. Repo ini tidak memberimu aplikasi jadi, karena
membangun kerangkanya **adalah** artefak yang dinilai.

Sesi 2, yang harus ada di sini sebelum kamu keluar:

```
frontend/
├── index.html
├── package.json        # vite, vue   — harus punya skrip "dev"
├── vite.config.js
└── src/
    ├── main.js
    ├── App.vue         # header + main, HTML semantik, rapi di 360px
    └── components/
```

Titik mulai:

```bash
cd frontend
npm create vite@latest . -- --template vue
npm install
npm run dev
```

Hapus berkas ini kalau sudah tidak perlu.
