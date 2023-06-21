# # Remove first comment(#) on each line to implement this working logging example.
# # Add LOGLEVEL environment variable to netbox if you use this example & want a different log level.
# from os import environ

LOGLEVEL = "DEBUG"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "handlers": {
        "console": {
            "level": LOGLEVEL,
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": LOGLEVEL,
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": LOGLEVEL,
            "propagate": False,
        },
        "django_auth_ldap": {
            "handlers": [
                "console",
            ],
            "level": LOGLEVEL,
        },
    },
}
