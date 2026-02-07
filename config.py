class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///../instance/database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CEP_CACHE_TTL_HOURS = 24
