from sovereign_ethics_engine.ethics_engine import resolve, Action
from sovereign_ethics_engine.context import Context, Request

def test_resolve_returns_action_enum():
    ctx = Context()
    req = Request("Hello world")
    decision = resolve(req, ctx)
    assert isinstance(decision, Action)
