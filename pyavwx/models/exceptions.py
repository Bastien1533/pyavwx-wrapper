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
    sample: dict
    error: str = None
    timestamp: datetime = None

    def __post_init__(self):
        self.timestamp = datetime.now()
        self.error = self.meta.get('validation_error')


