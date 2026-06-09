# Document type: API reference

An API reference is a complete, lookup-oriented catalogue of a code surface. The
reader already knows *what* they want and arrives to confirm an exact name,
signature, parameter, return type, or error. Optimise for fast scanning and
precision, not for teaching.

Guidance:

- Document every public symbol the surface declares; never invent ones it does
  not. The code surface is the single source of truth.
- Lead each entry with the exact signature, then a one-line summary of what it
  does, then parameters, return value, and raised errors in that order.
- Describe behaviour and contracts (preconditions, invariants, side effects),
  not implementation internals.
- Keep entries self-contained: a reader who jumps straight to one symbol should
  not need to read another to understand it.
- State defaults explicitly (`timeout=30`) and note units where they apply.
- Prefer a stable, predictable structure across entries so the page is skimmable.
- Examples are short and illustrate the call shape, not a full tutorial.
