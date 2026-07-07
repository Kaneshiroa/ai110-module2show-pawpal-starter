from dataclasses import dataclass, field
from typing import List

@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self):
        """Marks the task as complete."""
        self.completed = True
        # Note: Recurring logic will be implemented in Phase 4

@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Adds a task to the pet's task list."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Returns the list of tasks for this pet."""
        return self.tasks

class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Adds a new pet to the owner's profile."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Gathers and returns all tasks across all of the owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks

class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_daily_schedule(self) -> List[Task]:
        """Fetches the schedule. (Sorting/Conflicts added in Phase 4)."""
        return self.owner.get_all_tasks()

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sorts a list of tasks chronologically by time."""
        pass # Placeholder for Phase 4

    def check_conflicts(self, tasks: List[Task]):
        """Scans for duplicate time slots and flags them."""
        pass # Placeholder for Phase 4