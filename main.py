"""Tell a Whole Story in 32 Characters.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
with no trailing newline.

Entry line (exactly 32 characters, enforced by the assertion below):

    Alexa Divorced Us. Kept The WiFi

Pure Python stdlib (``os`` only): no network, no environment reads beyond
the output directory, no files read outside this repository.
"""

import os

LINE = "Alexa Divorced Us. Kept The WiFi"

# The gate is 1-32 characters: fail loudly here rather than shipping a
# silently invalid entry if the line ever drifts from exactly 32.
assert len(LINE) == 32, "entry line must be exactly 32 characters, got %d" % len(LINE)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
