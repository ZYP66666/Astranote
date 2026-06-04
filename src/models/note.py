from dataclasses import dataclass


@dataclass(frozen=True)
class Note:
    id: int
    user_id: int
    title: str
    content: str
    created_at: str
    updated_at: str
