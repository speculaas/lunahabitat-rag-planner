from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from pawpal_system import Owner, Pet, Scheduler, Task
from retriever import CorpusRetriever


@dataclass
class EvaluationCase:
    """Defines one retrieval and guardrail evaluation scenario."""

    name: str
    resource_name: str
    resource_type: str
    resource_notes: str
    task_title: str
    priority: str
    expected_citation: str
    expect_warning: bool


def run_case(case: EvaluationCase, scheduler: Scheduler) -> dict[str, str | bool]:
    """Run one scenario and capture the resulting plan behavior."""
    owner = Owner(name="Eval Ops", daily_time_budget=180)
    resource = Pet(
        name=case.resource_name,
        species=case.resource_type,
        notes=case.resource_notes,
    )
    owner.add_pet(resource)
    scheduler.owner = owner
    resource.add_task(
        Task(
            title=case.task_title,
            time="08:00",
            duration_minutes=20,
            priority=case.priority,
            due_date=date.today(),
        )
    )

    plan = scheduler.generate_daily_plan(date.today())
    item = plan[0]
    citation_ok = item["citation"] == case.expected_citation
    warning_present = bool(item["guidance_warning"])
    warning_ok = warning_present == case.expect_warning
    passed = citation_ok and warning_ok

    return {
        "name": case.name,
        "passed": passed,
        "expected_citation": case.expected_citation,
        "actual_citation": item["citation"],
        "expected_warning": case.expect_warning,
        "actual_warning": warning_present,
        "reason": item["reason"],
    }


def main() -> None:
    """Run a small evaluation suite over the retrieval-backed planner."""
    docs_path = Path(__file__).resolve().parent / "data" / "docs"
    retriever = CorpusRetriever(docs_path)
    scheduler = Scheduler(Owner(name="Eval Ops"), retriever=retriever)

    cases = [
        EvaluationCase(
            name="oxygen diagnostics retrieves life-support guidance",
            resource_name="Oxygen Recycler",
            resource_type="life support system",
            resource_notes="Requires daily diagnostics and pressure checks.",
            task_title="Oxygen recycler diagnostics",
            priority="high",
            expected_citation="Oxygen Recycler Checks",
            expect_warning=False,
        ),
        EvaluationCase(
            name="construction task retrieves construction safety guidance",
            resource_name="Habitat Shell",
            resource_type="construction zone",
            resource_notes="Expansion work must follow structural inspection rules.",
            task_title="Expansion scaffold inspection",
            priority="high",
            expected_citation="Construction Zone Safety",
            expect_warning=False,
        ),
        EvaluationCase(
            name="emergency task retrieves emergency response guidance",
            resource_name="Mission Control Link",
            resource_type="communications system",
            resource_notes="Used for critical incident coordination.",
            task_title="Emergency status relay",
            priority="high",
            expected_citation="Emergency Response Protocol",
            expect_warning=False,
        ),
        EvaluationCase(
            name="unknown task triggers uncertainty guardrail",
            resource_name="Art Bay",
            resource_type="creative workspace",
            resource_notes="Used for morale projects and non-operational decoration.",
            task_title="Art mural touch-up",
            priority="low",
            expected_citation="No matching guidance",
            expect_warning=True,
        ),
    ]

    results = [run_case(case, scheduler) for case in cases]
    passed = sum(1 for result in results if result["passed"])

    print("LunaHabitat Planner Evaluation")
    print("=" * 40)
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"{status}: {result['name']}")
        print(f"  expected citation: {result['expected_citation']}")
        print(f"  actual citation:   {result['actual_citation']}")
        print(f"  expected warning:  {result['expected_warning']}")
        print(f"  actual warning:    {result['actual_warning']}")
    print("-" * 40)
    print(f"Summary: {passed}/{len(results)} cases passed")


if __name__ == "__main__":
    main()
