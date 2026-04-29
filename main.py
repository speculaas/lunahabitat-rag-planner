from datetime import date, timedelta

from pawpal_system import Owner, Pet, Scheduler, Task


def build_demo_owner() -> Owner:
    """Create sample lunar habitat data for terminal testing."""
    owner = Owner(
        name="Luna Ops",
        daily_time_budget=180,
        preferences=["finish life-support checks before expansion work", "keep afternoon time open for comms windows"],
    )

    oxygen = Pet(name="Oxygen Recycler", species="life support system", age=5, notes="Requires daily diagnostics.")
    habitat = Pet(name="Habitat Shell", species="construction zone", age=3, notes="Expansion work must be monitored closely.")

    today = date.today()
    oxygen.add_task(Task("Pressure seal inspection", "07:30", 30, "high", "daily", today))
    oxygen.add_task(Task("Oxygen recycler diagnostics", "08:00", 15, "high", "daily", today))
    habitat.add_task(Task("Regolith shield printer review", "09:15", 20, "medium", "weekly", today))
    habitat.add_task(Task("Expansion scaffold inspection", "07:30", 25, "low", "once", today))
    oxygen.add_task(Task("Comms uplink review", "18:00", 10, "medium", "once", today + timedelta(days=1)))

    owner.add_pet(oxygen)
    owner.add_pet(habitat)
    return owner


def print_schedule() -> None:
    """Display the current mission schedule in a readable terminal format."""
    owner = build_demo_owner()
    scheduler = Scheduler(owner)
    today = date.today()
    plan = scheduler.generate_daily_plan(today)
    conflicts = scheduler.detect_conflicts(today)

    print(f"Today's Mission Schedule for {owner.name}")
    print("-" * 60)
    for item in plan:
        print(
            f"{item['time']} | {item['pet']:<6} | {item['task']:<18} | "
            f"{item['duration_minutes']:>3} min | {item['priority']}"
        )
        print(f"      Why: {item['reason']}")
    if conflicts:
        print("\nWarnings")
        print("-" * 60)
        for warning in conflicts:
            print(f"* {warning}")


if __name__ == "__main__":
    print_schedule()
