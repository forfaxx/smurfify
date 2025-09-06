#!/usr/bin/env python3
"""
smurfify.py 💙 — Replace common words with Smurf-style language for fun and linguistic mischief.

Inspired by the wildcard grammar of Peyo's Smurfs, this script substitutes verbs, nouns,
adjectives, and exclamations with forms of "smurf" (e.g., "smurf", "smurfy", "Smurf!") 
using simple word lists, inflection detection, and a bit of randomness.

✨ Improvements:
- Multiline & file input support
- Expanded word lists (kept all originals)
- 🎲 Chaos fallback for random smurfification
"""

import sys
import re
import argparse
import random

# =============================================================================
#                               CONFIGURATION
# =============================================================================

CHAOS_CHANCE = 0.05  # 5% chance to smurfify any unlisted word

# -----------------------------------------------------------------------------
# Word Categories (expand/curate as desired)
# -----------------------------------------------------------------------------
VERBS = {
    # tech verbs
    "fix", "use", "try", "run", "make", "build", "break", "work", "get", "open", "close",
    "start", "stop", "install", "update", "write", "read", "create", "test", "save",
    "remove", "delete", "move", "copy", "push", "pull", "deploy", "debug", "submit",
    "sync", "compile", "reboot", "configure", "clone", "publish",
    # common verbs
    "see", "take", "give", "find", "call", "help", "ask", "know", "need", "show",
    "leave", "come", "look", "tell", "want", "put", "bring", "play", "speak", "learn",
    "live", "smile", "believe", "follow", "carry", "become", "remember", "love", "hate",
    "eat", "drink", "sleep", "walk", "sit", "stand",
    # 🎭 fun verbs
    "entertain", "sing", "dance", "dream", "fight", "shout", "whisper", "laugh",
    "cry", "hope", "plan", "smurf"  # meta-smurf
}

NOUNS = {
    # 🔧 tech nouns (your originals)
    "tool", "thing", "plan", "idea", "bug", "code", "file", "script", "device", "command",
    "folder", "line", "project", "task", "feature", "issue", "input", "output", "program",
    "proposal", "workflow", "pipeline", "repo", "package", "module", "service", "container",
    "turtle", "timeline", "cloud", "feedback", "platform", "windows", "mac", "linux",
    # 🌎 common nouns
    "time", "day", "night", "man", "woman", "child", "world", "life",
    "hand", "eye", "place", "work", "year", "friend", "family", "house",
    "name", "school", "story", "water", "fire", "earth", "air",
    "city", "village", "river", "road", "table", "book", "letter",
    "voice", "language", "song", "truth", "order", "union", "justice"
}

ADJECTIVES = {
    # 🔧 tech adjectives (your originals)
    "good", "bad", "broken", "awesome", "clever", "smart", "dumb", "quick", "slow",
    "ugly", "useful", "confusing", "weird", "helpful", "nice", "simple", "hard", "cool",
    "agile", "responsive",
    # 🌎 common adjectives
    "big", "small", "long", "short", "happy", "sad", "easy", "new", "old", "young",
    "strong", "weak", "bright", "dark", "loud", "quiet", "fast", "slow",
    "simple", "complex", "early", "late", "warm", "cold"
}

EXCLAIMS = {
    "wow", "yay", "oops", "hey", "yeah", "woo", "whoa", "huh", "ugh", "nope", "nice",
    "heck", "hell", "damn", "darn", "crap", "woot"
}

CONNECTORS = {"and", ","}

# =============================================================================
#                             CORE SMURFIFY LOGIC
# =============================================================================

def apply_inflection(replacement: str, original: str) -> str:
    """
    Preserve tense, plurality, and capitalization of the original word.
    """
    lower = original.lower()
    if lower.endswith("ing"):
        replacement += "ing"
    elif lower.endswith("ed"):
        replacement += "ed"
    elif lower.endswith("s") and not lower.endswith("ss"):
        replacement += "s"
    if original.isupper():
        return replacement.upper()
    elif original.istitle():
        return replacement.capitalize()
    return replacement

def smurfify_base(base: str) -> str:
    """
    Decides how to smurfify a single base word.
    Checks word categories and applies chaos chance.
    """
    lower = base.lower()
    if lower in VERBS or lower in NOUNS:
        return apply_inflection("smurf", base)
    elif lower in ADJECTIVES:
        return apply_inflection("smurfy", base)
    elif lower in EXCLAIMS:
        return "Smurf!"
    # 🎲 Chaos fallback
    if base.isalpha() and random.random() < CHAOS_CHANCE:
        return apply_inflection("smurf", base)
    return base

def smurfify_word(word: str) -> str:
    """
    Handles punctuation and hyphenated words.
    Passes each subword to smurfify_base().
    """
    match = re.match(r"^([\w\-]+)([.,!?;:'\"`]*)$", word)
    if not match:
        return word
    base, punct = match.groups()
    smurfed_parts = [smurfify_base(part) for part in base.split('-')]
    return '-'.join(smurfed_parts) + punct

def is_smurfed(word: str) -> bool:
    """
    Determines if a word has already been smurfified.
    """
    return word.lower().startswith("smurf")

def smurfify_line(line: str) -> str:
    """
    Smurfifies an entire line of text, word by word.
    Includes logic for 'verb some noun' and connector-aware collision avoidance.
    """
    words = line.split()
    result = []
    i = 0
    while i < len(words):
        # --- Special: verb some noun pattern ---
        if (i + 2 < len(words)
            and words[i + 1].lower() == "some"
            and re.sub(r"[^\w\-]", "", words[i].lower()) in VERBS
            and re.sub(r"[^\w\-]", "", words[i + 2].lower()) in NOUNS):
            verb, noun = words[i], words[i + 2]
            if random.random() < 0.5:
                result.extend([smurfify_word(verb), "some", noun])
            else:
                result.extend([verb, "some", smurfify_word(noun)])
            i += 3
            continue

        # --- Smurf collision avoidance with connectors ---
        if (i + 2 < len(words) and words[i + 1].lower() in CONNECTORS):
            w1, w2 = words[i], words[i + 2]
            s1, s2 = smurfify_word(w1), smurfify_word(w2)
            if is_smurfed(s1) and is_smurfed(s2):
                if random.random() < 0.5:
                    result.extend([s1, words[i + 1], w2])
                else:
                    result.extend([w1, words[i + 1], s2])
                i += 3
                continue

        # --- Normal word ---
        result.append(smurfify_word(words[i]))
        i += 1
    return ' '.join(result)

# =============================================================================
#                                 CLI INTERFACE
# =============================================================================

def main():
    """
    Command-line interface for smurfify.py.
    Handles: file input, argument input, piped stdin, and interactive REPL.
    """
    parser = argparse.ArgumentParser(description="Smurfify text with joyful linguistic nonsense.")
    parser.add_argument("text", nargs="*", help="Text to smurfify")
    parser.add_argument("--file", "-f", help="Smurfify a file")
    args = parser.parse_args()

    # --- File input ---
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            for line in f:
                print(smurfify_line(line.rstrip()))
        return

    # --- Argument input ---
    if args.text:
        print(smurfify_line(' '.join(args.text)))
        return

    # --- STDIN (pipe) ---
    if not sys.stdin.isatty():
        for line in sys.stdin:
            print(smurfify_line(line.rstrip()))
        return

    # --- Interactive (REPL) ---
    print("smurfify.py 💙 — Type a line to smurf. Ctrl-D (or Ctrl-Z) to quit.")
    try:
        for line in sys.stdin:
            print(smurfify_line(line.rstrip()))
    except KeyboardInterrupt:
        print("\nStay smurfy!")

# =============================================================================
#                               ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()
