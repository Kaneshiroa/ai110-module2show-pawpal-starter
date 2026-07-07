from pawpal_system import Task, Pet

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