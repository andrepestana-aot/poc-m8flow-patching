# bootstrap.py

def bootstrap() -> None:
    from m8flow.extensions.health_controller_patch import apply as apply_health_patch
    apply_health_patch()
    from m8flow.extensions.authorization_service_patch import apply as apply_authz
    apply_authz()