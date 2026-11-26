"""Write the entry text for make.fun bounty
u-suga-the-robot-apology-dd96bb59 (The Robot Apology).

The program writes one two-line robot apology to /output/entry.txt: a first
sentence owning one specific mistake (a wedding invitation addressed to the
wrong Sarah, who RSVP'd yes), and a second sentence naming what the robot
learned and what it will do differently (check surnames, read the guest list
out loud, and tell her the spare chair is hers). The text is 239 characters
(two lines, one sentence each). It is fully deterministic: the same bytes on
every run, with no network access and no dependency outside this repository.

The text is the winner of the internal tournament (konsep.md): finalist F1
(the wrong Sarah, 8/8 in the two-way self-jury round-robin) expanded per
M4a with one consequence beat ("the spare chair is hers"). Runner-up was F4
(the shredded permission slip, 6/8). The external duel was attempted once
and failed with n=0 (Gemini route HTTP 403 in the sandbox), so the decisive
criterion K2 is locked below maximum -- see kandidat-V1.md, RISIKO TERBUKA.
"""

import os

ENTRY_TEXT = (
    "I am sorry I addressed your wedding invitation to the wrong Sarah "
    "and she RSVP'd yes.\n"
    "I have learned to check surnames, and now I read the guest list out "
    "loud before I seal an envelope \u2014 and I have already told her "
    "the spare chair is hers."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Self-check against the bounty gate: UTF-8 text of 1 to 400
    # characters, not only white space. Fail loudly instead of
    # writing an entry the sealed scorer would refuse.
    if not 1 <= len(ENTRY_TEXT) <= 400 or not ENTRY_TEXT.strip():
        raise SystemExit("entry text fails the 1-400 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
