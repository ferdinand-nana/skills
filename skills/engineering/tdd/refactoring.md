# Refactor Candidates

After TDD cycle, look for — in this order:

- **Dead code** → Delete it. If tests still pass, it wasn't needed.
- **Unnecessary abstraction** → Inline it. One implementation behind an interface? Remove the interface.
- **Duplication** → Extract function/class
- **Long methods** → Break into private helpers (keep tests on public interface)
- **Shallow modules** → Combine or deepen
- **Feature envy** → Move logic to where data lives
- **Primitive obsession** → Introduce value objects
- **Existing code** the new code reveals as problematic

Prefer boring over clever. If the refactored version is harder to read at 3am, revert it.
