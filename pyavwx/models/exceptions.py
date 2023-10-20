from dataclasses import dataclass
from datetime import datetime


@dataclass
class StationError:
    error: str
    param: str
    help: str
    timestamp: datetime
