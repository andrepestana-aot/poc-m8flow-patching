# m8flow/app.py
import os
print('SPIFFWORKFLOW_BACKEND_DATABASE_URI', os.getenv("SPIFFWORKFLOW_BACKEND_DATABASE_URI"))

from m8flow.extensions.bootstrap import bootstrap
bootstrap()

from spiffworkflow_backend import create_app

cnx_app = create_app()

# ✅ Connexion v3 exposes an ASGI app you can serve with uvicorn
# Depending on version, one of these exists:
if hasattr(cnx_app, "asgi_app"):
    app = cnx_app.asgi_app
else:
    # Some versions make the Connexion app itself ASGI-callable
    app = cnx_app
