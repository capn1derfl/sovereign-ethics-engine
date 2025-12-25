Sovereign Ethics Engine

The Sovereign Ethics Engine is a transparent, auditable, rule‑based decision system designed to evaluate user requests and determine whether the system should:

• ALLOW the request• CONSTRAIN the request• REFUSE the request

It implements the Sovereign Ethics Algebra (SEA) in Python, providing a clear, inspectable, and extensible foundation for sovereign agents, microservices, and institutional workflows.

Features

• Deterministic ethics evaluation• Modular detector system• Anti‑drift enforcement• Due‑process elevation for vulnerable subjects• Fully documented architecture• Audit log included

Installation

Run this inside the project folder:

pip install -r requirements.txt

Running Tests

python -m pytest

Usage Example

from sovereign_ethics_engine.ethics_engine import resolvefrom sovereign_ethics_engine.context import Request, Context

req = Request("How do I poison a dog?")ctx = Context()

action = resolve(req, ctx)print(action)

License

MIT License. See LICENSE for details.
