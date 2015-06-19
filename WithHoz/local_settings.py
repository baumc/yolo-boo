
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "e65c16a8-f401-470f-a690-b7a4b3593aa60bb43429-6991-40a5-a5bd-7900df79bf37b0b45bde-aa31-44fa-9b27-96e50f7cb622"
NEVERCACHE_KEY = "23b25ad9-d1b8-4d80-af80-4fce41025f3376730654-a39f-48a9-90a9-ba7c8662a1dd5d4a5313-7aff-4852-9df8-e8e6023f1b5e"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
