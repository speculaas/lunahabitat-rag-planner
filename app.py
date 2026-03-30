from datetime import date, timedelta

import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")


def seed_demo_data() -> Owner:
    """Create a themed starter dataset for the app session."""
    owner = Owner(
        name="Goldie",
        daily_time_budget=120,
        preferences=["prefer outdoor tasks before noon", "keep evenings short"],
    )
    kodiak = Pet("Kodiak", "brown bear", age=5, notes="Enjoys glacier air and berry snacks.")
    maple = Pet("Maple", "brown bear", age=3, notes="Best with calm routines.")
    today = date.today()
    kodiak.add_task(Task("River walk", "07:30", 30, "high", "daily", today))
    kodiak.add_task(Task("Berry breakfast", "08:00", 15, "high", "daily", today))
    maple.add_task(Task("Salmon enrichment", "09:15", 20, "medium", "weekly", today))
    owner.add_pet(kodiak)
    owner.add_pet(maple)
    return owner


if "owner" not in st.session_state:
    st.session_state.owner = seed_demo_data()

owner: Owner = st.session_state.owner
scheduler = Scheduler(owner)
today = date.today()

st.title("🐾 PawPal+")
st.caption("A cozy pet care planner with a modern Goldilocks twist for Alaska's brown bears.")

with st.expander("Scenario", expanded=False):
    st.markdown(
        """
PawPal+ helps a pet owner organize daily care tasks by time, priority, and available minutes.
This version demonstrates the same scheduling logic in both the CLI and Streamlit UI.
"""
    )

st.subheader("Owner Profile")
col1, col2 = st.columns(2)
with col1:
    owner.name = st.text_input("Owner name", value=owner.name)
with col2:
    owner.daily_time_budget = st.number_input(
        "Daily time budget (minutes)",
        min_value=30,
        max_value=600,
        value=owner.daily_time_budget,
        step=15,
    )

st.divider()

st.subheader("Add a Pet")
pet_name = st.text_input("Pet name", value="Juneau")
species = st.text_input("Species", value="brown bear")
pet_age = st.number_input("Age", min_value=0, max_value=40, value=4)
pet_notes = st.text_input("Notes", value="Needs a just-right mix of movement and rest.")

if st.button("Add pet"):
    existing_pet = owner.find_pet(pet_name)
    if existing_pet is not None:
        st.info(f"{pet_name} is already in your PawPal+ list.")
    else:
        owner.add_pet(Pet(pet_name, species, int(pet_age), pet_notes))
        st.success(f"Added {pet_name} to {owner.name}'s care plan.")

pet_options = [pet.name for pet in owner.pets]

st.divider()

st.subheader("Schedule a Task")
if pet_options:
    task_pet = st.selectbox("Choose a pet", pet_options)
else:
    task_pet = ""
    st.warning("Add a pet before scheduling tasks.")

col1, col2 = st.columns(2)
with col1:
    task_title = st.text_input("Task title", value="Porridge check")
    task_time = st.text_input("Time (HH:MM)", value="10:00")
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=1)
    task_day = st.selectbox("Day", ["Today", "Tomorrow"])

if st.button("Add task"):
    pet = owner.find_pet(task_pet)
    if pet is None:
        st.error("Select a valid pet before adding a task.")
    else:
        due_date = today if task_day == "Today" else today + timedelta(days=1)
        try:
            pet.add_task(
                Task(
                    title=task_title,
                    time=task_time,
                    duration_minutes=int(duration),
                    priority=priority,
                    frequency=frequency,
                    due_date=due_date,
                )
            )
            st.success(f"Added {task_title} for {pet.name}.")
        except ValueError as exc:
            st.error(str(exc))

current_tasks = scheduler.sort_tasks(owner.all_tasks_for_day(today))
if current_tasks:
    st.markdown("### Today's Tasks")
    st.table(
        [
            {
                "Pet": pet.name,
                "Task": task.title,
                "Time": task.time,
                "Minutes": task.duration_minutes,
                "Priority": task.priority.title(),
                "Frequency": task.frequency.title(),
            }
            for pet, task in current_tasks
        ]
    )
else:
    st.info("No tasks scheduled for today yet.")

st.divider()

st.subheader("Today's Schedule")
if st.button("Generate schedule"):
    plan = scheduler.generate_daily_plan(today)
    conflicts = scheduler.detect_conflicts(today)

    if not plan:
        st.warning("No tasks fit inside today's time budget.")
    else:
        st.success("Schedule generated.")
        st.table(plan)
        for item in plan:
            st.caption(f"{item['time']} - {item['reason']}")

    if conflicts:
        for warning in conflicts:
            st.warning(warning)
    else:
        st.info("No task conflicts detected for today.")
