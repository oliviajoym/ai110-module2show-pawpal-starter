#logic layer for backend classes

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class TimeOfDay(Enum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"


@dataclass
class Owner:
    owner_id: str
    name: str
    pet: Optional["Pet"] = None


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    owner_id: str
    tasks: list["Task"] = field(default_factory=list)

    def add_task(self, task: "Task") -> None:
        pass


@dataclass
class Task:
    task_id: str
    description: str
    time_constraint: TimeOfDay
    repeated: bool
    owner_presence_required: bool
    pet_id: str

    def mark_complete(self) -> None:
        pass


@dataclass
class Scheduler:
    scheduled_tasks: list[Task] = field(default_factory=list)

    def schedule_task(self, task: Task) -> None:
        pass

    def reschedule_repeated_tasks(self) -> None:
        pass

    def get_tasks_by_time(self, time: TimeOfDay) -> list[Task]:
        pass

    def get_tasks_requiring_owner(self) -> list[Task]:
        pass