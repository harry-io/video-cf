import os
from pydantic_settings import BaseSettings
import dotenv

dotenv.load_dotenv()


class Settings(BaseSettings):
    API_BASE_URL: str = "https://api.videosdk.live"
    VIDEOSDK_TOKEN: str
    SUPABASE_URL: str = "https://rpkatvrywfleumhlocxj.supabase.co"
    SUPABASE_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
