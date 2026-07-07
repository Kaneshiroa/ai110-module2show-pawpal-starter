from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import datetime


def test_task_completion():
    """Verify that calling mark_complete() actually changes the task's status."""
    # 1. Arrange: Create a sample task
    test_task = Task(description="Morning Walk", time="07:30", frequency="Daily")
    
    # 2. Act: Mark it complete
    test_task.mark_complete()
    
    # 3. Assert: Check if the boolean flipped to True
    assert test_task.completed is True

def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    # 1. Arrange: Create a pet and a task
    test_pet = Pet(name="Buddy", species="Dog")
    test_task = Task(description="Breakfast", time="08:00", frequency="Daily")
    
    # 2. Act: Add the task to the pet
    test_pet.add_task(test_task)
    
    # 3. Assert: Check if the pet's task list now contains 1 item
    assert len(test_pet.get_tasks()) == 1


def test_sorting_correctness():
    """Verify tasks are returned in chronological order."""
    # 1. Arrange: Create scheduler and out-of-order tasks
    owner = Owner("Jeffrey")
    scheduler = Scheduler(owner)
    t1 = Task(description="Lunch", time="12:00", frequency="Daily")
    t2 = Task(description="Breakfast", time="08:00", frequency="Daily")
    t3 = Task(description="Dinner", time="18:00", frequency="Daily")
    
    # 2. Act: Sort the tasks
    sorted_tasks = scheduler.sort_by_time([t1, t2, t3])
    
    # 3. Assert: Check the order (08:00 -> 12:00 -> 18:00)
    assert sorted_tasks[0].time == "08:00"
    assert sorted_tasks[1].time == "12:00"
    assert sorted_tasks[2].time == "18:00"

def test_recurrence_logic():
    """Confirm that marking a daily task complete creates a new task."""
    # 1. Arrange: Create a daily task
    daily_task = Task(description="Morning Walk", time="07:30", frequency="Daily")
    
    # 2. Act: Mark it complete
    new_task = daily_task.mark_complete()
    
    # 3. Assert: The original is complete, and a new task was generated
    assert daily_task.completed is True
    assert new_task is not None
    assert new_task.description == "Morning Walk"
    assert new_task.completed is False # The future task should not be complete

def test_conflict_detection():
    """Verify that the Scheduler flags duplicate times."""
    # 1. Arrange: Create scheduler and overlapping tasks
    owner = Owner("Jeffrey")
    scheduler = Scheduler(owner)
    t1 = Task(description="Walk", time="08:00", frequency="Daily")
    t2 = Task(description="Vet", time="08:00", frequency="Once")
    
    # 2. Act: Check for conflicts
    warnings = scheduler.check_conflicts([t1, t2])
    
    # 3. Assert: One warning should be generated for the 08:00 overlap
    assert len(warnings) == 1
    assert "08:00" in warnings[0]