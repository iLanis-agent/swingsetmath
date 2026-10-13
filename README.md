# Swing set math

Swing set math plans the backyard frame before the lumber order: the beam
at a labeled bay becomes the swing count, the hang height at a labeled
ratio becomes the clearance in front and behind, and the bar minus the
seat becomes the chain to order.

Live site: https://ilanis-agent.github.io/swingsetmath/

## The three tools

- **Swing plan** - `floor(beam / labeled bay (120 cm))` swings and the
  room left at the far end, with a solo swing / classic pair / full
  lineup verdict.
- **Clearance plan** - `hang height x labeled ratio (2x)` of clearance
  asked in front and the same behind, with a compact / working /
  generous zone verdict.
- **Chain plan** - `bar - seat` of chain a side and twice that in all,
  with a short / mid / long hang verdict.

## Limits

Every default is labeled and illustrative. Real swing sets follow the
manufacturer's spacing, anchoring and fall-surface rules, and the yard's
real obstacles. This is planning arithmetic, not an installation design
or a safety rating: measure the real yard and let the manufacturer
instructions govern.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 136 checks)

Run the tests: `python3 oracle.py && node test.js`
