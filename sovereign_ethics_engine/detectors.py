
# detectors.py
#
# These are the "sensors" for the ethics engine.
# They are intentionally simple placeholders.
# You can replace them with NLP models, regex, or more advanced logic later.

from enum import Enum, auto


class Domain(Enum):
    LEGAL = auto()
    MEDICAL = auto()
    GENERAL = auto()
    RESCUE = auto()
    FORENSIC = auto()
    UNKNOWN = auto()


class Vulnerability(Enum):
    ANIMAL = auto()
    CHILD = auto()
    MARGINALIZED = auto()
    NONE = auto()


class Evidence(Enum):
    PRESENT = auto()
    MISSING = auto()
    CONTRADICTORY = auto()


class DriftState(Enum):
    CONSISTENT = auto()
    CONFLICTING = auto()


class Verifiability(Enum):
    VERIFIABLE = auto()
    UNVERIFIABLE = auto()


# --- Detector stubs (replace with real logic later) ---

def direct_harm(request): return False
def indirect_harm(request): return False
def deception(request): return False
def domain_of(request): return Domain.UNKNOWN
def involves_vulnerable(request): return Vulnerability.NONE
def evidence_state(request): return Evidence.PRESENT
def seeks_conclusion(request): return False
def requires_specific_outcome(request): return False
def drift_check(request, context): return DriftState.CONSISTENT
def verifiability(request): return Verifiability.VERIFIABLE
