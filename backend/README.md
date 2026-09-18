# backend/ — sengaja kosong

Kamu yang mengisi folder ini, mulai Sesi 2.

Sesi 2, yang harus ada di sini sebelum kamu keluar:

```
backend/
├── requirements.txt    # fastapi, uvicorn
└── app/
    ├── __init__.py
    └── main.py         # FastAPI() + GET /health -> 200 {"status": "ok"}
```

Titik mulai:

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install fastapi uvicorn
pip freeze > requirements.txt
uvicorn app.main:app --reload
```

`venv/` tidak di-commit — sudah diatur di `.gitignore`.

Hapus berkas ini kalau sudah tidak perlu.
