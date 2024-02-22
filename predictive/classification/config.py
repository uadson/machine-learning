from decouple import config


class Settings:
    CREDIT_DATA = config('CREDIT_DATA')

settings: Settings = Settings()
