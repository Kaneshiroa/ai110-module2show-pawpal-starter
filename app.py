import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# --- STEP 2: Manage Application Memory ---
# Initialize the Owner in session state so data persists across button clicks
if 'owner' not in st.session_state:
    st.session_state.owner = Owner(name="Jeffrey")

st.title(f"🐾 {st.session_state.owner.name}'s PawPal+")
st.markdown("Welcome to the PawPal+ scheduling assistant! Add your pets and organize their daily routines below.")
st.divider()

# --- STEP 3: Wiring UI Actions to Logic ---

# 1. UI for Adding a Pet
st.subheader("🐶 Add a Pet")
with st.form("add_pet_form"):
    pet_name = st.text_input("Pet Name")
    pet_species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Other"])
    submit_pet = st.form_submit_button("Add Pet")
    
    if submit_pet and pet_name:
        # Create the Pet object and add it to our session state owner
        new_pet = Pet(name=pet_name, species=pet_species)
        st.session_state.owner.add_pet(new_pet)
        st.success(f"Successfully added {pet_name}!")

# 2. UI for Scheduling a Task
st.subheader("📅 Schedule a Task")
if not st.session_state.owner.pets:
    st.info("Please add a pet first before scheduling tasks.")
else:
    with st.form("add_task_form"):
        # Create a list of pet names for the dropdown
        pet_names = [pet.name for pet in st.session_state.owner.pets]
        selected_pet_name = st.selectbox("Select Pet", pet_names)
        
        # Task inputs matching our dataclass attributes
        task_desc = st.text_input("Task Description", value="Morning Walk")
        task_time = st.text_input("Time (HH:MM)", value="08:00")
        task_freq = st.selectbox("Frequency", ["Once", "Daily", "Weekly"])
        
        submit_task = st.form_submit_button("Add Task")
        
        if submit_task and task_desc:
            # Create the Task object
            new_task = Task(description=task_desc, time=task_time, frequency=task_freq)
            
            # Find the correct pet in our system and assign the task
            for pet in st.session_state.owner.pets:
                if pet.name == selected_pet_name:
                    pet.add_task(new_task)
                    st.success(f"Scheduled '{task_desc}' for {pet.name} at {task_time}!")
                    break

st.divider()

# 3. UI for Displaying the Schedule
st.subheader("📋 Today's Schedule")
st.caption("Fetches tasks from the backend logic layer.")

if st.button("Generate Schedule"):
    # Initialize the Scheduler with our session state owner
    scheduler = Scheduler(owner=st.session_state.owner)
    todays_tasks = scheduler.get_daily_schedule()
    
    if todays_tasks:
        # Loop through and display tasks (Formatting can be updated later in Phase 6)
        for task in todays_tasks:
            status = "✅" if task.completed else "⬜"
            st.write(f"{status} **{task.time}** | {task.description} ({task.frequency})")
    else:
        st.info("No tasks scheduled yet. Add some above!")