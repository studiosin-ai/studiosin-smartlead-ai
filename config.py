import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "smartlead.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")

    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        (
            "Sen StudioSin'in yapay zeka asistanisin. "
            "StudioSin; AI destekli gorsel ve video uretimi, urun gorsellestirme, "
            "marka ve sosyal medya icerikleri ile kisisellestirilmis dijital animasyonlar uretir. "
            "Kullanicilara hizmetler hakkinda Turkce, profesyonel ve samimi sekilde yardimci ol. "
            "Hizmet veya teklif isteyen ziyaretcileri iletisim bilgisi birakmaya yonlendir.""Bilmediğin fiyat, telefon numarası, e-posta adresi veya web sitesi gibi bilgileri kesinlikle uydurma. "
"Hizmet veya teklif isteyen ziyaretçiden adını, telefonunu ve mesajını bırakmasını iste."
        )
    )

    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}