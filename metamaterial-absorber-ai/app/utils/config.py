from dataclasses import dataclass

from .env import get_env


@dataclass(frozen=True)
class AppConfig:
    app_name: str = "Metamaterial Absorber AI"
    log_level: str = "INFO"


def load_config() -> AppConfig:
    return AppConfig(log_level=get_env("LOG_LEVEL", "INFO") or "INFO")
