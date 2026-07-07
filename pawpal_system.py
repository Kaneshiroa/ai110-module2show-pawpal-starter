from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime, timedelta

@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self) -> Optional['Task']:
        """
        Marks the task as complete. If the task is recurring, 
        returns a new Task instance for the next occurrence.
        """
        self.completed = True
        
        if self.frequency in ["Daily", "Weekly"]:
            # Calculate next date (Optional enhancement, but great for logic)
            days_to_add = 1 if self.frequency == "Daily" else 7
            next_date = datetime.now() + timedelta(days=days_to_add)
            
            # Create and return the new future task
            return Task(
                description=self.description, 
                time=self.time, 
                frequency=self.frequency
            )
        
        return None

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
        """Fetches, sorts, and returns today's schedule."""
        # Get all tasks across all pets
        all_tasks = self.owner.get_all_tasks()
        
        # Sort them chronologically before returning
        sorted_tasks = self.sort_by_time(all_tasks)
        return sorted_tasks

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sorts a list of tasks chronologically by their time attribute."""
        # The lambda function tells sorted() to look specifically at task.time
        return sorted(tasks, key=lambda task: task.time)

    def filter_tasks_by_status(self, tasks: List[Task], completed_status: bool) -> List[Task]:
        """Filters a list of tasks by their completion status."""
        # Uses a list comprehension to keep only tasks that match the desired status
        return [task for task in tasks if task.completed == completed_status]

    def check_conflicts(self, tasks: List[Task]) -> List[str]:
        """Scans for duplicate time slots and returns a list of warning messages."""
        seen_times = set()
        warnings = []
        
        for task in tasks:
            if task.time in seen_times:
                warnings.append(f"⚠️ Warning: Conflict detected! Multiple tasks scheduled at {task.time}.")
            else:
                seen_times.add(task.time)
                
        return warnings