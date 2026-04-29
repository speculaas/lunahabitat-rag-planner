from datetime import date, timedelta
from pathlib import Path

import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task
from retriever import CorpusRetriever


st.set_page_config(page_title="LunaHabitat Planner", page_icon="🌕", layout="centered")


def seed_demo_data() -> Owner:
    """Create a starter lunar-habitat dataset for the app session."""
    owner = Owner(
        name="Luna Ops",
        daily_time_budget=180,
        preferences=["prioritize life-support checks before expansion work", "keep comms windows visible in the afternoon"],
    )
    oxygen = Pet("Oxygen Recycler", "life support system", age=5, notes="Requires daily inspection before non-critical work.")
    greenhouse = Pet("Greenhouse Pod", "food systems module", age=3, notes="Best checked after environmental systems stabilize.")
    today = date.today()
    oxygen.add_task(Task("Pressure seal inspection", "07:30", 30, "high", "daily", today))
    oxygen.add_task(Task("Oxygen recycler diagnostics", "08:15", 25, "high", "daily", today))
    greenhouse.add_task(Task("Greenhouse moisture scan", "09:15", 20, "medium", "weekly", today))
    owner.add_pet(oxygen)
    owner.add_pet(greenhouse)
    return owner


if "owner" not in st.session_state:
    st.session_state.owner = seed_demo_data()
if "retriever" not in st.session_state:
    docs_path = Path(__file__).resolve().parent / "data" / "docs"
    st.session_state.retriever = CorpusRetriever(docs_path)

owner: Owner = st.session_state.owner
scheduler = Scheduler(owner, retriever=st.session_state.retriever)
today = date.today()

st.title("🌕 LunaHabitat Planner")
st.caption("A lunar habitat operations planner for maintenance, expansion, monitoring, and communications work.")

with st.expander("Scenario", expanded=False):
    st.markdown(
        """
LunaHabitat Planner helps a habitat operator organize mission work by time, priority, and available crew minutes.
It retrieves local guidance before writing schedule explanations and warns when no relevant guidance is found.
"""
    )

st.subheader("Operator Profile")
col1, col2 = st.columns(2)
with col1:
    owner.name = st.text_input("Operator name", value=owner.name)
with col2:
    owner.daily_time_budget = st.number_input(
        "Daily crew time budget (minutes)",
        min_value=30,
        max_value=600,
        value=owner.daily_time_budget,
        step=15,
    )

st.divider()

st.subheader("Add a Habitat Resource")
pet_name = st.text_input("Resource name", value="Comms Array")
species = st.text_input("Resource type", value="communications system")
pet_age = st.number_input("Service age", min_value=0, max_value=40, value=4)
pet_notes = st.text_input("Notes", value="Supports scheduled uplinks and relay checks.")

if st.button("Add resource"):
    existing_pet = owner.find_pet(pet_name)
    if existing_pet is not None:
        st.info(f"{pet_name} is already in the habitat operations list.")
    else:
        owner.add_pet(Pet(pet_name, species, int(pet_age), pet_notes))
        st.success(f"Added {pet_name} to {owner.name}'s operations board.")

pet_options = [pet.name for pet in owner.pets]

st.divider()

st.subheader("Schedule an Operations Task")
if pet_options:
    task_pet = st.selectbox("Choose a resource", pet_options)
else:
    task_pet = ""
    st.warning("Add a resource before scheduling tasks.")

col1, col2 = st.columns(2)
with col1:
    task_title = st.text_input("Task title", value="Comms uplink review")
    task_time = st.text_input("Time (HH:MM)", value="10:00")
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=1)
    task_day = st.selectbox("Day", ["Today", "Tomorrow"])

if st.button("Add task"):
    pet = owner.find_pet(task_pet)
    if pet is None:
        st.error("Select a valid resource before adding a task.")
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
    st.markdown("### Today's Operations Queue")
    st.table(
        [
            {
                "Resource": pet.name,
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
    st.info("No operations tasks scheduled for today yet.")

st.divider()

st.subheader("Today's Mission Schedule")
if st.button("Generate schedule"):
    plan = scheduler.generate_daily_plan(today)
    conflicts = scheduler.detect_conflicts(today)

    if not plan:
        st.warning("No tasks fit inside today's crew time budget.")
    else:
        st.success("Mission schedule generated.")
        st.table(plan)
        for item in plan:
            st.caption(f"{item['time']} - {item['reason']}")
            st.caption(f"Citation: {item['citation']}")
            if item["guidance_warning"]:
                st.warning(item["guidance_warning"])

    if conflicts:
        for warning in conflicts:
            st.warning(warning)
    else:
        st.info("No task conflicts detected for today.")
