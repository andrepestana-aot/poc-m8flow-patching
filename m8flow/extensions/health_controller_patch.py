from __future__ import annotations

from typing import Any, Dict

_ORIGINALS: Dict[str, Any] = {}
_PATCHED = False


def apply() -> None:
    """
    Patch spiffworkflow_backend.routes.health_controller.status.

    Must run BEFORE create_app() registers routes (so the endpoint uses our function),
    ideally before importing/initializing the backend app.
    """
    global _PATCHED
    if _PATCHED:
        return

    import spiffworkflow_backend.routes.health_controller as hc

    # Save original
    _ORIGINALS["status"] = hc.status

    def patched_status():
        # Call original
        resp = _ORIGINALS["status"]()

        # Proof: add a header (easy to verify via curl -i)
        resp.headers["X-M8FLOW-HEALTH-PATCH"] = "1"

        # Optional: also tag JSON body if you want (only if JSON response)
        # data = resp.get_json(silent=True)
        # if isinstance(data, dict):
        #     data["_m8flow_patch"] = "health_controller"
        #     resp.set_data(json.dumps(data))
        #     resp.mimetype = "application/json"

        return resp

    hc.status = patched_status
    _PATCHED = True
