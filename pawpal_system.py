#logic layer for backend classes

from dataclasses import dataclass, field
from datetime import date, timedelta
from enum import Enum
from typing import Optional


class TimeOfDay(Enum):
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"


class Frequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    MISSED = "missed"


_FREQUENCY_DAYS = {
    Frequency.DAILY: 1,
    Frequency.WEEKLY: 7,
    Frequency.MONTHLY: 30,
}


@dataclass
class Task:
    task_id: str
    description: str
    time_constraint: TimeOfDay
    repeated: bool
    frequency: Optional[Frequency]
    owner_presence_required: bool
    pet: "Pet"
    status: TaskStatus = TaskStatus.PENDING
    next_due_date: Optional[date] = None

    def mark_complete(self) -> None:
        self.status = TaskStatus.COMPLETED
        if self.repeated:
            self.next_due_date = self.compute_next_occurrence()
            self.status = TaskStatus.PENDING

    def compute_next_occurrence(self) -> Optional[date]:
        if not self.repeated or self.frequency is None:
            return None
        base = self.next_due_date or date.today()
        return base + timedelta(days=_FREQUENCY_DAYS[self.frequency])

    def is_overdue(self) -> bool:
        return (
            self.status == TaskStatus.PENDING
            and self.next_due_date is not None
            and self.next_due_date < date.today()
        )


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    owner: "Owner"
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)


@dataclass
class Owner:
    owner_id: str
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Flatten every pet's task list into one combined list."""
        all_tasks: list[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


@dataclass
class Scheduler:
    owner: Owner

    def get_all_tasks(self) -> list[Task]:
        # Delegates to the Owner rather than keeping its own task list,
        # so it automatically covers every pet the Owner has.
        return self.owner.get_all_tasks()

    def schedule_task(self, task: Task) -> None:
        # Hands the task to its pet; the Scheduler itself holds no
        # separate task store, so there is one source of truth.
        task.pet.add_task(task)

    def reschedule_repeated_tasks(self) -> None:
        for task in self.get_all_tasks():
            if task.repeated and task.status == TaskStatus.COMPLETED:
                task.next_due_date = task.compute_next_occurrence()
                task.status = TaskStatus.PENDING

    def get_tasks_by_time(self, time: TimeOfDay) -> list[Task]:
        return [t for t in self.get_all_tasks() if t.time_constraint == time]

    def get_tasks_requiring_owner(self) -> list[Task]:
        return [t for t in self.get_all_tasks() if t.owner_presence_required]

    def get_overdue_tasks(self) -> list[Task]:
        return [t for t in self.get_all_tasks() if t.is_overdue()]