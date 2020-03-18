import json


# Gunicorn config variables
bind = '0.0.0.0:80'
keepalive = 120
errorlog = "-"
workers = 10
timeout = 120

# For debugging and testing
log_data = {
    "loglevel": "info",
    "workers": str(workers),
    "bind": bind,
    # Additional, non-gunicorn variables
    "host": "0.0.0.0",
    "port": "80",
}
print(json.dumps(log_data))
