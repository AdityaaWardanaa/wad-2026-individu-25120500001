from fastapi import FastAPI, Response, status, Query, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid

app = FastAPI(title="API Pengiriman")

# Mock database sementara
db_pengiriman = []

# --- SKEMA INPUT ---
class PengirimanCreate(BaseModel):
    no_resi: str = Field(..., pattern="^JKT\d{7}$", description="Wajib diawali JKT dan 7 angka")
    berat_kg: float = Field(..., gt=0, le=50, description="Berat maksimal 50 kg")

# --- SKEMA OUTPUT ---
class PengirimanResponse(PengirimanCreate):
    id: str

# --- ENDPOINT POST ---
@app.post("/api/pengiriman", status_code=status.HTTP_201_CREATED, response_model=PengirimanResponse)
def create_pengiriman(data: PengirimanCreate, response: Response):
    # 1. Generate ID unik dari server
    new_id = str(uuid.uuid4())
    
    # 2. Gabungkan ID dengan data input dari user
    new_item = PengirimanResponse(id=new_id, **data.model_dump())
    
    # 3. Simpan ke database mock
    db_pengiriman.append(new_item.model_dump())
    
    # 4. Tambahkan header Location sesuai standar DoD
    response.headers["Location"] = f"/api/pengiriman/{new_id}"
    
    return new_item

# --- ENDPOINT GET ALL ---
@app.get("/api/pengiriman", status_code=status.HTTP_200_OK, response_model=List[PengirimanResponse])
def get_all_pengiriman(
    skip: int = Query(0, ge=0, description="Jumlah data yang dilewati"),
    limit: int = Query(10, gt=0, description="Maksimal data yang dikembalikan"),
    search: Optional[str] = Query(None, description="Cari berdasarkan no_resi")
):
    results = db_pengiriman
    
    # 1. Filter pencarian
    if search:
        results = [item for item in results if search.lower() in item["no_resi"].lower()]
        
    # 2. Terapkan paginasi berbasis list slicing
    return results[skip : skip + limit]

# --- ENDPOINT GET BY ID ---
@app.get("/api/pengiriman/{id}", status_code=status.HTTP_200_OK, response_model=PengirimanResponse)
def get_pengiriman_by_id(id: str):
    # Cari data dengan ID yang cocok di mock database
    for item in db_pengiriman:
        if item["id"] == id:
            return item
            
    # Jika perulangan selesai dan ID tidak ditemukan, kembalikan 404
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Data pengiriman tidak ditemukan"
    )

@app.get("/health")
def health_check():
    return {"status": "ok"}