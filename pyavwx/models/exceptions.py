from dataclasses import dataclass
from datetime import datetime


@dataclass
class StationError:
    error: str
    param: str
    help: str
    timestamp: datetime


@dataclass
class AuthError:
    meta: dict
    sample: dict = None
    error: str = None
    timestamp: datetime = None

    def __post_init__(self):
        self.timestamp = datetime.now()
        self.error = self.meta.get("validation_error")


@dataclass
class BadStatus:
    error: str
    code: str
    timestamp: datetime

    def __init__(self, error: str, code: str) -> None:
        self.error = error
        self.code = code

    def __post_init__(self) -> None:
        self.timestamp = datetime.now()
