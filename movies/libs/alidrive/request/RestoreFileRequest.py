"""..."""
from dataclasses import dataclass

from movies.libs.alidrive.types import DatClass


@dataclass
class RestoreFileRequest(DatClass):
    """..."""
    file_id: str
    drive_id: str = None
