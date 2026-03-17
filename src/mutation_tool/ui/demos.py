from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mutation_tool.ui.state import RunRequest


@dataclass(frozen=True)
class DemoDefinition:
    id: str
    request: RunRequest
    name_en: str
    name_tr: str
    summary_en: str
    summary_tr: str
    learning_goal_en: str
    learning_goal_tr: str

    def to_catalog_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "request": self.request.to_dict(),
            "name": {"en": self.name_en, "tr": self.name_tr},
            "summary": {"en": self.summary_en, "tr": self.summary_tr},
            "learning_goal": {
                "en": self.learning_goal_en,
                "tr": self.learning_goal_tr,
            },
        }

    def to_preset_dict(self) -> dict[str, object]:
        payload = self.to_catalog_dict()
        payload["description"] = payload["summary"]
        return payload


_EXAMPLES_ROOT = Path(__file__).resolve().parents[3] / "examples"

_DEMO_CATALOG: tuple[DemoDefinition, ...] = (
    DemoDefinition(
        id="beginner",
        request=RunRequest(
            project_root=str(_EXAMPLES_ROOT / "beginner_demo"),
            source_paths=("src",),
            max_mutants=10,
            stop_on_survivor=False,
            fail_on_survivor=False,
        ),
        name_en="Beginner Demo",
        name_tr="Başlangıç Demosu",
        summary_en="A friendly first run with a weak boundary assertion that produces a survivor.",
        summary_tr="Bir survivor üreten zayıf boundary assertion'lı başlangıç demosu.",
        learning_goal_en="Learn how to inspect a survivor and add a focused test.",
        learning_goal_tr="Bir survivor'ı okuyup hedefli test eklemeyi öğren.",
    ),
    DemoDefinition(
        id="ci_gate",
        request=RunRequest(
            project_root=str(_EXAMPLES_ROOT / "ci_gate_demo"),
            source_paths=("src",),
            max_mutants=10,
            stop_on_survivor=False,
            fail_on_survivor=True,
        ),
        name_en="CI Gate Demo",
        name_tr="CI Geçit Demosu",
        summary_en="Shows how a surviving mutant should fail a stricter quality gate.",
        summary_tr=(
            "Hayatta kalan bir mutantın daha sıkı kalite kapısını "
            "nasıl fail etmesi gerektiğini gösterir."
        ),
        learning_goal_en="Practice the difference between local exploration and CI enforcement.",
        learning_goal_tr="Yerel keşif ile CI yaptırımı arasındaki farkı gör.",
    ),
    DemoDefinition(
        id="timeout_lab",
        request=RunRequest(
            project_root=str(_EXAMPLES_ROOT / "timeout_lab_demo"),
            source_paths=("src",),
            max_mutants=8,
            per_mutant_timeout=0.2,
            stop_on_survivor=False,
            fail_on_survivor=False,
        ),
        name_en="Timeout Lab Demo",
        name_tr="Timeout Laboratuvarı Demosu",
        summary_en="Designed to surface a slow-path mutant so you can practice timeout diagnosis.",
        summary_tr=(
            "Timeout tanılaması pratiği için yavaş yol mutantı "
            "üretmek üzere tasarlanmıştır."
        ),
        learning_goal_en="Learn how timeout budgets and slow paths affect mutation results.",
        learning_goal_tr=(
            "Timeout bütçeleriyle yavaş yolların mutation sonuçlarını "
            "nasıl etkilediğini öğren."
        ),
    ),
)


def list_demos() -> list[DemoDefinition]:
    return list(_DEMO_CATALOG)


def get_demo(demo_id: str) -> DemoDefinition | None:
    for demo in _DEMO_CATALOG:
        if demo.id == demo_id:
            return demo
    return None
