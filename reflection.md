# LunaHabitat Planner Project Reflection

## 1. System Design

**a. Initial design**

My initial UML used four classes: `Owner`, `Pet`, `Task`, and `Scheduler`. `Owner` stores the person's name, time budget, preferences, and list of pets. `Pet` stores basic pet details plus the tasks assigned to that pet. `Task` stores the actual work item, including time, duration, priority, recurrence, due date, and completion state. `Scheduler` acts as the planning layer that gathers tasks from the owner's pets, sorts them, checks for conflicts, and builds a daily plan.

**b. Design changes**

Yes. During implementation I added `due_date` and `frequency` directly to `Task` so recurring scheduling would stay simple and each task instance could represent one specific day. I also kept the scheduler lightweight by using exact time matches for conflict detection instead of trying to model overlapping time ranges, which felt cleaner for this project scope.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler considers the owner's daily time budget, each task's scheduled time, each task's priority, and whether the task is already completed. Time budget mattered most because a plan should be realistic before it is optimized. After that, time ordering and priority mattered because the user needs a schedule they can follow and understand quickly.

**b. Tradeoffs**

One tradeoff is that conflict detection only checks whether two tasks start at the exact same time. It does not try to calculate overlapping durations. That is reasonable here because it keeps the logic readable for a student project while still catching the clearest scheduling mistakes.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI to move through the project in stages: first for class design, then for implementation ideas, then for test coverage and UI integration. The most helpful prompts were specific prompts tied to files or behaviors, such as asking how a scheduler should retrieve tasks from pets, how to sort `"HH:MM"` times cleanly, and what edge cases mattered most for recurring tasks and conflicts.

**b. Judgment and verification**

I did not blindly accept the idea of making the scheduler much more complex with overlapping-duration conflict checks and heavier optimization logic. I simplified that suggestion because it would have added more code than the assignment needed. I verified the final design by reading through the flow myself, running the CLI demo, and checking the automated tests.

---

## 4. Testing and Verification

**a. What you tested**

I tested five core behaviors: marking a task complete, adding a task to a pet, sorting tasks chronologically, creating the next task for a daily recurring item, and flagging duplicate-time conflicts. These were important because they covered the most visible interactions between my classes and the scheduler's algorithmic features.

**b. Confidence**

I feel fairly confident that the scheduler works correctly for the main project scenarios because the core behaviors pass automated tests and the app uses the same backend logic as the CLI demo. If I had more time, I would test invalid time formats, duplicate pet names, weekly recurrence over longer periods, and tasks that almost exceed the time budget.

---

## 5. Reflection

**a. What went well**

I am most satisfied with keeping the backend and frontend connected through the same class design. Once the data model was clear, the CLI demo, tests, and Streamlit UI all became much easier to build and reason about.

**b. What you would improve**

In another iteration, I would add editing and deleting tasks in the UI, save data to JSON so the schedule persists between runs, and improve conflict detection so it can catch overlapping task durations instead of only exact time matches.

**c. Key takeaway**

One important takeaway is that AI is most useful when I stay in the lead architect role. It helped me brainstorm and speed up coding, but the quality of the final system depended on me choosing the right level of complexity, verifying the results, and keeping the design aligned with the assignment goals.
