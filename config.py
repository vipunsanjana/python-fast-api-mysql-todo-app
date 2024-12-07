from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://myuser:mypassword@db:3306/mydb_three"


    class Config:
        env_file = ".env"

settings = Settings()