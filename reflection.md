# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
I will need to add core features that allow the user to add a pet, schedule different events with varying priorities,
and be able to view all of the events
- What classes did you include, and what responsibilities did you assign to each?
Task class which contains a description, time, frequency, a boolean to mark it complete using a method, a Pet class that contains the animal name and species, and what tasks they require, a Owner class that contains a list of all pets that they own, and a scheduler class to schedule specific tasks
**b. Design changes**

- Did your design change during implementation?
No
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?

The scheduler primarily considers time (chronological sorting using military "HH:MM" format), completion status (filtering pending versus completed tasks), and schedule overlaps (detecting if multiple tasks share the exact same time slot).

- How did you decide which constraints mattered most?

Time was the most critical constraint to ensure the daily schedule flows logically from morning to night. Conflict detection was secondary but essential to prevent accidentally overbooking a specific time slot.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

For the conflict detection algorithm, I chose a lightweight approach using a Python set to check for exact time matches. While this is highly performant (O(N) time complexity) and prevents the app from crashing, the tradeoff is that it does not account for task durations (e.g., a 60-minute task at 08:00 won't flag a conflict with a 30-minute task at 08:30). I accepted this tradeoff to keep the MVP simple and fast.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used AI to brainstorm the initial UML architecture, scaffold the backend logic layer with Python dataclasses, implement algorithmic methods (like sorting and list comprehensions), and generate the automated pytest suite.
- What kinds of prompts or questions were most helpful?
Step-by-step structural prompts that clearly defined the boundaries of each phase (e.g. keeping logic restrained into algorithmic thinking and not expanding to UI immediately)

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.

During the early design phase, the option to implement an advanced "Priority-Based" top-down sorting algorithm was available. I chose to stick strictly to chronological time-sorting first to ensure the base requirements were rock-solid before adding complexity.

- How did you evaluate or verify what the AI suggested?

I verified the AI's generated logic by utilizing a "CLI-first" approach. I ran a main.py demo script to visually confirm the terminal output and executed automated pytest functions to ensure the methods behaved correctly before implementing anything into the Streamlit interface.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?

State management (task completion and addition).

Algorithmic sorting correctness (out-of-order tasks returning chronologically).

Recurring task automation (generating a new future task when a daily task is completed).

Conflict detection (flagging duplicate time slots).

- Why were these tests important?

They covered both the standard chronological sorting and potential edge cases (time slot collisions), guaranteeing the core engine was reliable independent of the frontend UI.

**b. Confidence**

- How confident are you that your scheduler works correctly?

5/5 stars 

- What edge cases would you test next if you had more time?

I would test tasks spanning across midnight (e.g., a schedule running from 23:00 to 01:00) or how the system handles invalid, malformed time inputs from the user.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

Seeing the st.session_state properly hold the data and watching the Streamlit components cleanly render the sorted schedules and conflict warnings was incredibly satisfying.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would implement true data persistence (e.g., writing the schedules to a .json file) so that the Owner and Pet data survives even if the Streamlit session completely restarts.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

A CLI-first approach is needed when building software. Building, verifying, and testing the brains of the app in a standalone Python script makes connecting it to a dynamic frontend UI much smoother and far less prone to breaking.
