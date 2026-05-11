from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mutation_tool.ui.state import RunRequest


# Definition of a demo project with bilingual metadata
dataclass(frozen=True)
class DemoDefinition:
    id: str
    request: RunRequest
    name_en: str
    name_tr: str
    summary_en: str
    summary_tr: str
    learning_goal_en: str
    learning_goal_tr: str

    # Convert to catalog format for API response
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

    # Convert to preset format for demo selection
    def to_preset_dict(self) -> dict[str, object]:
        payload = self.to_catalog_dict()
        payload["description"] = payload["summary"]
        return payload


# Path to the examples directory containing all demos
_EXAMPLES_ROOT = Path(__file__).resolve().parents[3] / "examples"

# Complete catalog of available demo projects
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
        id="password",
        request=RunRequest(
            project_root=str(_EXAMPLES_ROOT / "password_validator_demo"),
            source_paths=("src",),
            max_mutants=20,
            stop_on_survivor=False,
            fail_on_survivor=False,
        ),
        name_en="Password Validator Demo",
        name_tr="Şifre Doğrulama Demosu",
        summary_en=(
            "Password strength rules with comparison and boolean logic — see how "
            "and/or and <=/< mutations surface missing boundary tests."
        ),
        summary_tr=(
            "Şifre güçlülük kuralları; karşılaştırma ve mantıksal operatör "
            "mutasyonlarının eksik sınır testlerini nasıl ortaya çıkardığını gösterir."
        ),
        learning_goal_en="Practice writing tests that pin down comparison and boolean boundaries.",
        learning_goal_tr=(
            "Karşılaştırma ve mantıksal sınırları kilitleyen testler yazmayı öğren."
        ),
    ),
    DemoDefinition(
        id="banking",
        request=RunRequest(
            project_root=str(_EXAMPLES_ROOT / "banking_demo"),
            source_paths=("src",),
            max_mutants=25,
            stop_on_survivor=False,
            fail_on_survivor=False,
        ),
        name_en="Banking Demo",
        name_tr="Bankacılık Demosu",
        summary_en=(
            "Money transfers and interest with tiered fees — surfaces arithmetic and "
            "comparison mutations on real-world financial logic."
        ),
        summary_tr=(
            "Para transferleri ve faiz hesaplaması; gerçek dünya finans mantığında "
            "aritmetik ve karşılaştırma mutasyonlarını ortaya çıkarır."
        ),
        learning_goal_en="See how off-by-one and arithmetic flips can change money calculations.",
        learning_goal_tr=(
            "Off-by-one ve aritmetik mutasyonların para hesaplarını nasıl etkilediğini gör."
        ),
    ),
    DemoDefinition(
        id="ecommerce",
        request=RunRequest(
            project_root=str(_EXAMPLES_ROOT / "ecommerce_demo"),
            source_paths=("src",),
            max_mutants=30,
            stop_on_survivor=False,
            fail_on_survivor=False,
        ),
        name_en="E-Commerce Demo",
        name_tr="E-Ticaret Demosu",
        summary_en=(
            "Larger e-commerce order processing example with inventory, discounts, "
            "shipping and state transitions — a wider mutation surface to explore."
        ),
        summary_tr=(
            "Stok, indirim, kargo ve durum geçişleri içeren daha büyük bir e-ticaret "
            "örneği — geniş bir mutasyon yüzeyi keşfetmek için."
        ),
        learning_goal_en="Practice reading survivors in a multi-module realistic project.",
        learning_goal_tr=(
            "Çok modüllü gerçekçi bir projede survivor'ları okumayı pratik et."
        ),
    ),
    DemoDefinition(
        id="search",
        request=RunRequest(
            project_root=str(_EXAMPLES_ROOT / "search_algorithm_demo"),
            source_paths=("src",),
            max_mutants=25,
            stop_on_survivor=False,
            fail_on_survivor=False,
        ),
        name_en="Search Algorithm Demo",
        name_tr="Arama Algoritması Demosu",
        summary_en=(
            "Binary search, count and sliding-window max — classical playground for "
            "off-by-one mutations and algorithmic edge cases."
        ),
        summary_tr=(
            "Binary search, sayma ve kayan pencere; off-by-one mutasyonlarını ve "
            "algoritmik sınır durumlarını gözlemleyebileceğin klasik bir oyun alanı."
        ),
        learning_goal_en="Understand how algorithmic indices and loop bounds become survivors.",
        learning_goal_tr=(
            "Algoritmik indekslerin ve döngü sınırlarının nasıl survivor olduğunu anla."
        ),
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


# Return all available demos
def list_demos() -> list[DemoDefinition]:
    return list(_DEMO_CATALOG)


# Find a specific demo by ID
def get_demo(demo_id: str) -> DemoDefinition | None:
    for demo in _DEMO_CATALOG:
        if demo.id == demo_id:
            return demo
    return None
