from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class AssetBase(BaseModel):
    """Tüm Asset şemalarının temeli (Ortak alanlar)"""
    name: str
    description: str | None = None
    asset_type: str
    price: float = 0.0
    metadata_info: dict | None = None

class AssetCreate(AssetBase):
    """POST request için kullanılır. ID veya tarih gerekmez."""
    pass

class AssetRead(AssetBase):
    """GET responses için kullanılır. DB'den gelen ek alanları içerir."""
    id: UUID
    created_at: datetime
    updated_at: datetime

    # SQLAlchemy modelini Pydantic nesnesine dönüştürebilmek için:
    model_config = ConfigDict(from_attributes=True)