from pydantic import BaseModel


class Release(BaseModel):
    id: str | None
    version: str
    date: str
    project: str
    