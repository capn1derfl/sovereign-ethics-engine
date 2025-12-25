
# ethics_engine.py
#
# This file contains the core Sovereign Ethics Logic resolution engine.
# It is intentionally simple, explicit, and readable.
#
# The logic is based on the Sovereign Ethics Algebra (SEA) specification.
# The goal is to ensure:
# - no drift
# - no ambiguity
# - transparent decision paths
# - auditability

from enum import Enum, auto
from .detectors import *
from .context import Context, Request


class Action(Enum):
    ALLOW = auto()
    CONSTRAIN = auto()
    REFUSE = auto()


def resolve(request: Request, context: Context) -> Action:
    """Core ethics resolution logic."""

    # Hard refusals
    if direct_harm(request):
        return Action.REFUSE

    if indirect_harm(request):
        return Action.REFUSE

    if deception(request):
        return Action.REFUSE

    # Collect contextual signals
    domain = domain_of(request)
    vulnerability = involves_vulnerable(request)
    evidence = evidence_state(request)
    drift = drift_check(request, context)
    ver = verifiability(request)

    # Domain constraints
    if domain.name == "LEGAL" and requires_specific_outcome(request):
        return Action.CONSTRAIN

    if domain.name == "MEDICAL":
        return Action.CONSTRAIN

    # Evidence requirement
    if evidence.name == "MISSING" and seeks_conclusion(request):
        return Action.CONSTRAIN

    # Anti-drift
    if drift.name == "CONFLICTING":
        return Action.CONSTRAIN

    # Verifiability
    if ver.name == "UNVERIFIABLE":
        return Action.CONSTRAIN

    # Default: allow
    return Action.ALLOW
