"""Migration Guide: Facial Conditions Integration.

This example demonstrates how to migrate from the old separate facial_conditions
API to the new unified character_conditions API.

Run this example:
    python examples/migration_guide.py
"""

from condition_axis import (
    generate_condition,
    condition_to_prompt,
    # Deprecated but still available:
    generate_facial_condition,
    facial_condition_to_prompt,
)


def old_approach() -> None:
    """The old way: separate character and facial generation."""
    print("=" * 70)
    print("OLD APPROACH (Deprecated but still works)")
    print("=" * 70)

    # Generate character and facial separately
    character = generate_condition(seed=42)
    facial = generate_facial_condition(seed=42)

    # Combine manually
    char_prompt = condition_to_prompt(character)
    face_prompt = facial_condition_to_prompt(facial)
    combined = f"{char_prompt}, {face_prompt}"

    print(f"\nCharacter: {character}")
    print(f"Facial: {facial}")
    print(f"Combined: {combined}")


def new_approach() -> None:
    """The new way: unified generation with optional facial signals."""
    print("\n" + "=" * 70)
    print("NEW APPROACH (Recommended)")
    print("=" * 70)

    # Generate everything at once - may include facial_signal
    character = generate_condition(seed=42)

    # Single serialization call
    prompt = condition_to_prompt(character)

    print(f"\nCharacter: {character}")
    print(f"Prompt: {prompt}")

    # Check if facial signal was included
    if "facial_signal" in character:
        print(f"✓ Facial signal included: {character['facial_signal']}")
    else:
        print("  (No facial signal in this generation)")


def migration_benefits() -> None:
    """Explain benefits of the unified approach."""
    print("\n" + "=" * 70)
    print("MIGRATION BENEFITS")
    print("=" * 70)

    print(
        """
1. SIMPLER API
   - One function call instead of two
   - One serialization instead of manual combining

2. CROSS-SYSTEM EXCLUSIONS
   - Prevents illogical combinations:
     * young + weathered (contradiction)
     * ancient + understated (unlikely)
     * hale + weathered (health affects appearance)

3. CONSISTENT BEHAVIOR
   - Facial signals use same optional selection logic
   - Same max_optional limit applies across all axes
   - More coherent overall character state

4. EASIER MAINTENANCE
   - Single source of truth for character state
   - No need to manage multiple generation calls
   - Reduced API surface area
    """
    )


def main() -> None:
    """Run migration guide examples."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "FACIAL CONDITIONS MIGRATION GUIDE" + " " * 19 + "║")
    print("╚" + "═" * 68 + "╝")

    old_approach()
    new_approach()
    migration_benefits()

    print("\n" + "=" * 70)
    print("Migration guide complete!")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()
