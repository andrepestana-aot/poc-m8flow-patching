# m8flow/extensions/authorization_service_patch.py
from __future__ import annotations

from typing import Any

_ORIGINALS: dict[str, Any] = {}
_PATCHED = False

def apply() -> None:
    global _PATCHED
    if _PATCHED:
        return

    from spiffworkflow_backend.services.authorization_service import AuthorizationService
    from flask import request

    _ORIGINALS["should_disable_auth_for_request"] = AuthorizationService.should_disable_auth_for_request

    @classmethod
    def patched_should_disable_auth_for_request(cls) -> bool:
        # Keep upstream behavior first
        if _ORIGINALS["should_disable_auth_for_request"]():
            return True

        # ✅ Hard bypass for status by path (works even if routing is weird)
        # NOTE: remove_api_prefix() exists upstream, but request.path already includes /v1.0
        if request.method == "GET" and request.path in ("/v1.0/status", "/status"):
            return True

        return False

    AuthorizationService.should_disable_auth_for_request = patched_should_disable_auth_for_request
    _PATCHED = True
