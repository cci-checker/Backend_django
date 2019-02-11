from .base import *

SECRET_KEY = "8)9o)d0i&9oxpdt#p^61ym0w@z=p6#5a#x=7**15cldw&vs&(9"

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
