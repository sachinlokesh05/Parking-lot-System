import json
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
# path = os.path.realpath("secrets.json")

# JSON-based secrets module
with open(dir_path+"/"+"secrets.json") as f:
    secrets_dict = f.read()
    secrets = json.loads(secrets_dict)

def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
