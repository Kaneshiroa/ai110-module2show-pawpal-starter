from pawpal_system import Task, Pet, Owner, Scheduler

def main():
    # 1. Create an Owner
    owner = Owner(name="Jeffrey")

    # 2. Create at least two Pets
    dog = Pet(name="Buddy", species="Dog")
    cat = Pet(name="Luna", species="Cat")
    
    owner.add_pet(dog)
    owner.add_pet(cat)

    # 3. Add at least three Tasks with different times
    task1 = Task(description="Morning Walk", time="09:30", frequency="Daily")
    task2 = Task(description="Breakfast", time="08:00", frequency="Daily")
    task3 = Task(description="Clean Litter Box", time="10:15", frequency="Weekly")
    
    dog.add_task(task1)
    dog.add_task(task2)
    cat.add_task(task3)

    # 4. Initialize Scheduler and fetch today's tasks
    scheduler = Scheduler(owner=owner)
    todays_schedule = scheduler.get_daily_schedule()

    # 5. Print a clean, readable schedule to the terminal
    print(f"\n--- Today's Schedule for {owner.name}'s Pets ---")
    print("-" * 45)
    for task in todays_schedule:
        status = "[x]" if task.completed else "[ ]"
        print(f"{task.time} | {status} {task.description} ({task.frequency})")
    print("-" * 45)
    # --- Test Conflict Detection ---
    # Intentionally add a conflicting task
    conflict_task = Task(description="Vet Appointment", time="08:00", frequency="Once")
    dog.add_task(conflict_task)
    
    # Re-fetch and sort the schedule
    todays_schedule = scheduler.sort_by_time(scheduler.get_daily_schedule())
    
    print("\n--- Conflict Check ---")
    warnings = scheduler.check_conflicts(todays_schedule)
    for warning in warnings:
        print(warning)

    # --- Test Recurring Task Logic ---
    print("\n--- Recurrence Check ---")
    print(f"Before completion, {dog.name} has {len(dog.get_tasks())} tasks.")
    
    # Mark a daily task as complete
    new_recurring_task = task2.mark_complete()
    if new_recurring_task:
        dog.add_task(new_recurring_task)
        print(f"Task '{task2.description}' completed! New instance generated.")
        
    print(f"After completion, {dog.name} has {len(dog.get_tasks())} tasks.")

if __name__ == "__main__":
    main()