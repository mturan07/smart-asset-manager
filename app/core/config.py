from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Proje Bilgileri
    PROJECT_NAME: str = "Smart Asset Manager"
    API_V1_STR: str = "/api/v1"
    
    # Veritabanı Ayarları (Default değerler geliştirme içindir)
    DATABASE_URL: str = "postgresql+asyncpg://postgres:password@localhost:5432/asset_db"

    # .env dosyasını oku
    model_config = SettingsConfigDict(env_file=".env")

# Singleton olarak kullanılacak ayar nesnesi
settings = Settings()