from dataclasses import dataclass


@dataclass
class ClassifyResult:
    label: int
    unclear_score: float
    notseen_score: float
    seen_score: float
