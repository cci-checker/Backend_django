from .base import *

SECRET_KEY = '8)9o)d0i&9oxpdt#p^61ym0w@z=p6#5a#x=7**15cldw&vs&(9'

DEBUG = True

ALLOWED_HOSTS = ['cci-checker.herokuapp.com', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd28so7ssrv1cf4',
        'USER': 'wtvbeztmdvysdp',
        'PASSWORD': '602b0414f7c2df761456e97f0660a8c472ddce55329e8f34c4dd48228757e68b',
        # Or an IP Address that your DB is hosted on
        'HOST': 'ec2-107-21-224-76.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}