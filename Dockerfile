# Container backend — DISEDIAKAN DOSEN.
# Dipakai di Sesi 14 untuk deploy ke Render. Kamu TIDAK menulis berkas ini; kamu membacanya,
# memberi anotasi, dan menjelaskan tiap barisnya saat pembelaan.
#
# Empat pertanyaan yang akan ditanyakan di Sesi 14:
#   1. Kenapa `COPY requirements.txt` dilakukan SEBELUM `COPY . .`?
#   2. Kenapa `--no-cache-dir`?
#   3. Kenapa proses berjalan sebagai `appuser`, bukan root?
#   4. Kenapa port dibaca dari environment `$PORT` dan bukan ditulis 8000?

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Lapisan dependensi dipisah supaya cache tidak batal setiap kali kode berubah.
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./

# Jangan jalankan sebagai root.
RUN useradd --create-home --shell /bin/false appuser && chown -R appuser:appuser /app
USER appuser

# Render (dan sebagian besar PaaS) menyuntikkan $PORT. Jangan dihardcode.
ENV PORT=8000
EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
