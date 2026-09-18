#!/usr/bin/env python3
"""Pemeriksa artefak — The Build (Web Application Development, Universitas Cakrawala).

Perintah ini SAMA PERSIS dengan yang dijalankan dosen saat menilai.
Hijau di laptopmu = hijau saat dinilai.

    python verify.py --sesi 2

Tidak memerlukan paket apa pun di luar pustaka standar Python.
"""

import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

OK, FAIL, WARN = "OK  ", "GAGAL", "INFO"


class Result:
    def __init__(self):
        self.rows = []

    def add(self, status, label, detail=""):
        self.rows.append((status, label, detail))

    def ok(self, label, detail=""):
        self.add(OK, label, detail)

    def fail(self, label, detail=""):
        self.add(FAIL, label, detail)

    def info(self, label, detail=""):
        self.add(WARN, label, detail)

    @property
    def failed(self):
        return [r for r in self.rows if r[0] == FAIL]


def read(*parts):
    path = os.path.join(ROOT, *parts)
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def git(*args):
    try:
        out = subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=20
        )
        return out.stdout.strip() if out.returncode == 0 else ""
    except Exception:
        return ""


# --- pemeriksaan individual -------------------------------------------------


def check_gitignore(r):
    body = read(".gitignore")
    if body is None:
        return r.fail(".gitignore ada", "berkas tidak ditemukan")
    wajib = ["node_modules/", "venv/", ".env", "__pycache__/"]
    kurang = [p for p in wajib if p not in body]
    if kurang:
        return r.fail(".gitignore menutup jejak wajib", "belum ada: " + ", ".join(kurang))
    r.ok(".gitignore menutup jejak wajib")


def check_no_secrets(r):
    tracked = git("ls-files").splitlines()
    bocor = [f for f in tracked if f == ".env" or f.startswith(".env.") and f != ".env.example"]
    if bocor:
        return r.fail(
            "tidak ada berkas rahasia ter-commit",
            "ter-commit: " + ", ".join(bocor) + " — Ketentuan 8, nilai artefak sesi ini batal",
        )
    r.ok("tidak ada berkas rahasia ter-commit")


def check_frontend(r):
    pkg = read("frontend", "package.json")
    if pkg is None:
        return r.fail("frontend/package.json ada", "frontend/ masih kosong — kamu yang membuatnya")
    try:
        data = json.loads(pkg)
    except json.JSONDecodeError as exc:
        return r.fail("frontend/package.json valid", str(exc))
    if "dev" not in data.get("scripts", {}):
        return r.fail("frontend punya skrip `dev`", "scripts.dev tidak ada di package.json")
    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
    if "vue" not in deps:
        return r.fail("frontend memakai Vue", "`vue` tidak ada di dependencies")
    r.ok("frontend: package.json + skrip dev + Vue")


def check_semantic_html(r):
    src = os.path.join(ROOT, "frontend", "src")
    if not os.path.isdir(src):
        return r.fail("frontend/src ada", "belum dibuat")
    blob = ""
    for base, _, files in os.walk(src):
        for f in files:
            if f.endswith((".vue", ".html")):
                blob += read(os.path.relpath(os.path.join(base, f), ROOT)) or ""
    blob += read("frontend", "index.html") or ""
    tags = [t for t in ("<header", "<main", "<nav", "<section", "<footer", "<h1") if t in blob]
    if len(tags) < 2:
        return r.fail(
            "HTML semantik, bukan div-soup",
            "butuh minimal 2 dari <header> <main> <nav> <section> <footer> <h1>",
        )
    r.ok("HTML semantik", "ditemukan: " + " ".join(tags))


def check_backend_health(r):
    main = read("backend", "app", "main.py")
    if main is None:
        return r.fail("backend/app/main.py ada", "backend/ masih kosong — kamu yang membuatnya")
    if not re.search(r"""["']/health["']""", main):
        return r.fail("backend punya rute /health", "tidak ditemukan di app/main.py")
    if not re.search(r"FastAPI\s*\(", main):
        return r.fail("backend memakai FastAPI", "FastAPI() tidak ditemukan")
    r.ok("backend: FastAPI + rute /health")


def check_requirements(r):
    req = read("backend", "requirements.txt")
    if req is None:
        return r.fail("backend/requirements.txt ada", "belum dibuat")
    low = req.lower()
    kurang = [p for p in ("fastapi", "uvicorn") if p not in low]
    if kurang:
        return r.fail("requirements.txt lengkap", "belum ada: " + ", ".join(kurang))
    r.ok("backend/requirements.txt lengkap")


README_SECTIONS = [
    ("prasyarat", "1. Prasyarat"),
    ("layanan", "2. Layanan"),
    ("cara menjalankan", "3. Cara menjalankan"),
    ("cara memverifikasi", "4. Cara memverifikasi"),
    ("masalah", "5. Masalah yang sering muncul"),
]


def check_readme(r):
    body = read("README.md")
    if body is None:
        return r.fail("README.md ada", "berkas tidak ditemukan")
    low = body.lower()
    kurang = [label for key, label in README_SECTIONS if key not in low]
    if kurang:
        return r.fail("README bentuk 5 bagian", "belum ada: " + "; ".join(kurang))
    r.ok("README bentuk 5 bagian")


def check_charter(r):
    body = read("docs", "PROJECT.md")
    if body is None:
        return r.fail("docs/PROJECT.md ada", "berkas tidak ditemukan")
    bagian_a = body.split("## Bagian B")[0]
    sisa = re.findall(r"<[^<>\n]{3,}>", bagian_a)
    sisa = [s for s in sisa if not s.startswith("<!--")]
    if sisa:
        return r.fail(
            "piagam terisi (Bagian A)",
            f"{len(sisa)} tempat kosong belum diganti, mis. {sisa[0]}",
        )
    r.ok("piagam terisi (Bagian A)")


def check_contributors(r):
    body = read("CONTRIBUTORS.md")
    if body is None:
        return r.fail("CONTRIBUTORS.md ada", "berkas tidak ditemukan")
    if "<nama>" in body or "<NIM>" in body or "@<username>" in body:
        return r.fail("CONTRIBUTORS.md terisi", "masih ada <nama>/<NIM>/@<username>")
    if "Ketua" not in body.split("## Apa arti")[0]:
        return r.fail("CONTRIBUTORS.md menandai ketua", "kolom peran ketua kosong")
    r.ok("CONTRIBUTORS.md terisi")


def check_pr_flow(r):
    merges = git("log", "--merges", "--oneline")
    branches = git("branch", "-a")
    if "feature/" in merges or "feature/" in branches:
        return r.ok("ada alur branch feature/* → main")
    r.fail(
        "ada alur branch feature/* → main",
        "tidak ada merge commit atau branch feature/* yang terlihat dari klon ini",
    )


def check_commit_spread(r):
    log = git("log", "--format=%an|%ae")
    if not log:
        return r.info("sebaran commit", "riwayat git tidak terbaca")
    authors = {line for line in log.splitlines() if line}
    co = git("log", "--format=%b").lower().count("co-authored-by:")
    if len(authors) >= 2 or co:
        return r.ok("sebaran commit", f"{len(authors)} penulis, {co} co-authored")
    r.info(
        "sebaran commit",
        "baru 1 penulis — tanpa commit atas namanya sendiri, anggota lain mendapat 0 "
        "untuk Tugas Kelompok",
    )


def check_api_contract(r):
    body = read("docs", "api-contract.md")
    if body is None or "TODO" in body or len(body.split()) < 120:
        return r.fail("docs/api-contract.md terisi", "masih stub atau terlalu pendek")
    r.ok("docs/api-contract.md terisi")


def check_state_doc(r):
    body = read("docs", "state.md")
    if body is None or "TODO" in body or len(body.split()) < 80:
        return r.fail("docs/state.md terisi", "masih stub atau terlalu pendek")
    r.ok("docs/state.md terisi")


def check_perf_table(r):
    body = read("README.md") or ""
    rows = re.findall(r"^\|.*\|.*\|.*\|\s*$", body, re.M)
    if len(rows) < 6 or "sebelum" not in body.lower():
        return r.fail("tabel angka sebelum/sesudah", "butuh 6 baris angka di README")
    r.ok("tabel angka sebelum/sesudah")


def check_public_url(r):
    body = read("README.md") or ""
    if re.search(r"https://[^\s)]+", body.replace("https://github.com", "")):
        return r.ok("URL publik tercantum di README")
    r.fail("URL publik tercantum di README", "belum ada tautan aplikasi yang hidup")


# --- peta sesi --------------------------------------------------------------

BASE = [check_gitignore, check_no_secrets, check_readme, check_pr_flow, check_commit_spread]

SESI = {
    2: BASE + [check_frontend, check_semantic_html, check_backend_health, check_charter],
    3: BASE + [check_frontend, check_backend_health, check_requirements, check_charter],
    4: BASE + [check_frontend, check_backend_health, check_requirements, check_charter],
    5: BASE + [check_frontend, check_backend_health, check_requirements, check_charter],
    6: BASE + [check_frontend, check_backend_health, check_requirements, check_charter],
    7: BASE + [check_frontend, check_backend_health, check_charter, check_api_contract],
    9: BASE + [check_frontend, check_backend_health, check_api_contract],
    10: BASE + [check_frontend, check_backend_health, check_api_contract],
    11: BASE + [check_frontend, check_backend_health, check_api_contract],
    12: BASE + [check_frontend, check_backend_health, check_api_contract, check_state_doc],
    13: BASE
    + [check_frontend, check_backend_health, check_api_contract, check_state_doc, check_perf_table],
    14: BASE
    + [
        check_frontend,
        check_backend_health,
        check_api_contract,
        check_state_doc,
        check_perf_table,
        check_public_url,
    ],
    15: None,  # sama dengan 14
    16: None,  # sama dengan 14 + CONTRIBUTORS
}
SESI[15] = SESI[14]
SESI[16] = SESI[14] + [check_contributors]


def main():
    ap = argparse.ArgumentParser(description="Pemeriksa artefak The Build")
    ap.add_argument("--sesi", type=int, required=True, help="nomor sesi (2-16)")
    args = ap.parse_args()

    checks = SESI.get(args.sesi)
    if checks is None:
        print(f"Sesi {args.sesi} tidak punya artefak repo yang diperiksa otomatis.")
        return 0

    r = Result()
    for fn in checks:
        try:
            fn(r)
        except Exception as exc:  # pemeriksa tidak boleh menjatuhkan dirinya sendiri
            r.fail(fn.__name__, f"pemeriksa error: {exc}")

    print(f"\n  The Build — verifikasi Sesi {args.sesi}\n")
    for status, label, detail in r.rows:
        line = f"  [{status}] {label}"
        print(line if not detail else f"{line}\n           {detail}")

    gagal = len(r.failed)
    print()
    if gagal:
        print(f"  {gagal} pemeriksaan GAGAL. Perbaiki sebelum kamu keluar dari sesi.\n")
        return 1
    print("  Semua pemeriksaan lulus. Commit dan push sebelum kelas selesai.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
