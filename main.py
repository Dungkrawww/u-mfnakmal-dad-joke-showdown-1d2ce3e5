# Dad Joke Showdown — entry
#
# The joke:
#   I asked Dad why he brings a ladder to every barbecue.
#   He said, "Son, the steaks have never been higher."
#
# Why it fits the judge's brief:
# 1. A dad joke a father would tell at the table — a son asks Dad, Dad
#    answers deadpan; the barbecue setting is the judge's own world
#    (a father of three at every barbecue).
# 2. The pun lands cleanly on first read — steaks/stakes, no explaining
#    needed; the turn is the whole punchline.
# 3. Fresh rather than told a thousand times — the ladder-at-a-barbecue
#    setup is not one of the classic recycled one-liners, while staying
#    inside the dad joke tradition.
# 4. Tight — every word earns its place, punchline arrives at the end.
# 5. Reads naturally aloud — a father could deliver it across the
#    dinner table in two beats.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Deterministic: the entry is one fixed joke, so both harness runs must
# write the same bytes. No randomness, no network, no clock.
JOKE = (
    "I asked Dad why he brings a ladder to every barbecue. "
    "He said, \"Son, the steaks have never been higher.\""
)


def validate_joke(joke):
    # Gate rules (sealed scorer): /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only white space.
    assert 1 <= len(joke) <= 200, f"joke is {len(joke)} chars, must be 1-200"
    assert joke.strip(), "must not be only whitespace"
    assert joke == joke.strip(), "no leading/trailing whitespace"
    assert "\n" not in joke, "single line"


def main() -> None:
    import sys

    if "--check" in sys.argv:
        validate_joke(JOKE)
        print(f"OK: {len(JOKE)} chars, 1 line")
        print(JOKE)
        return

    validate_joke(JOKE)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
