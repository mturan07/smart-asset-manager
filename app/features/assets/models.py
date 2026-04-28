from sqlalchemy import String, Float, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base, TimestampMixin
import uuid

class Asset(Base, TimestampMixin):
    __tablename__ = "assets"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500))
    
    # Finansal ve Teknik Veriler
    asset_type: Mapped[str] = mapped_column(String(50), index=True) # örn: Donanım, Yazılım
    price: Mapped[float] = mapped_column(Float, default=0.0)
    
    # AI'ın analiz edebileceği esnek veri alanı (JSONB)
    # Örn: {"cpu": "i7", "ram": "32GB"} veya {"license_key": "ABC", "expiry": "2026-01-01"}
    metadata_info: Mapped[dict | None] = mapped_column(JSON)
    
    is_active: Mapped[bool] = mapped_column(default=True)