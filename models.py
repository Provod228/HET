from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    title: str
    done: bool = False
    created_at: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    def to_dict(self) -> dict:
        return {"title": self.title, "done": self.done, "created_at": self.created_at}

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)

    def __str__(self) -> str:
        status = "✅" if self.done else "⬜"
        return f"{status} {self.title}  [{self.created_at}]"
