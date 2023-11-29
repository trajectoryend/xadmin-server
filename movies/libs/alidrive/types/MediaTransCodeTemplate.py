"""..."""

from dataclasses import dataclass

from .Enum import MediaTranscodeStatus
from .Type import DatClass


@dataclass
class MediaTransCodeTemplate(DatClass):
    """..."""
    template_id: str = None
    status: MediaTranscodeStatus = None
    url: str = None
