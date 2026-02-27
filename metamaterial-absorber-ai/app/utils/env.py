import os


def get_env(name: str, default: str | None = None) -> str | None:
    """Read environment variable with optional default."""
    return os.getenv(name, default)
