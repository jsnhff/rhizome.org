DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/testdb',
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'engine': 'haystack.backends.elasticsearch_backend.elasticsearchsearchengine',
        'url': 'http://127.0.0.1:9200/',
        'index_name': 'haystack',
        'timeout': 60,
    },
}

SECRET_KEY = ''
ADMIN_HASH_SECRET = ''

COUCH_SERVER = 'http://127.0.0.1:5984'
DEFENSIO_API_KEY = '' 

PAYPAL_POSTBACK_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'
PAYPAL_IDENTITY_TOKEN = ''
PAYPAL_RECEIVER_EMAIL = ''

# authorize.net
AUTHNET_DEBUG = True 
AUTHNET_LOGIN_ID = ''
AUTHNET_TRANSACTION_KEY = ''
AUTHNET_URL = 'https://test.authorize.net/gateway/transact.dll'