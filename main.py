"""Till Firmware Do Us Part -- make.fun entry.

Writes one wedding vow spoken by a robot at its own wedding:
a single sentence, under 200 characters, funny and heartfelt.

Pure standard library (os only). Output goes to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

VOW = (
    "I take you to be my lawfully wedded debugger, to have and to hold, "
    "in sickness and in low signal, until our batteries run out."
)

OUTPUT_FILE = "entry.txt"
MAX_CHARS = 200


def validate(text):
    """Enforce the RULES.txt gate: 1-200 chars, UTF-8, not only
    whitespace, a single sentence on a single line."""
    if not isinstance(text, str):
        raise ValueError("vow must be text")
    if not text.strip():
        raise ValueError("vow must not be only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("vow must not have leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("vow is %d chars, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("vow must fit on one line")
    text.encode("utf-8")
    return True


def main():
    validate(VOW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(VOW + "\n")
    # Prove the file on disk passes the same gate: read it back and
    # re-validate the exact bytes the judge will see.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != VOW + "\n":
        raise ValueError("written file does not match the vow")
    validate(written.rstrip("\n"))
    print("wrote %s (%d chars)" % (path, len(VOW)))


if __name__ == "__main__":
    main()
