LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s-%(name)s-%(levelname)s-%(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': {
        'init': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': 'no'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}