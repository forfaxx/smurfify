# 🧑‍💻 smurfify.py 💙

Smurfify text with joyful linguistic nonsense. Inspired by the wildcard grammar of Peyo’s *Smurfs*, this script replaces common verbs, nouns, adjectives, and exclamations with forms of **smurf** (e.g. `smurf`, `smurfy`, `Smurf!`). It’s part toy, part beginner’s Python exercise, and just useful enough to sneak into demos or lighten up shell pipelines.

✨ Features:
- Replace common words with smurf-language equivalents  
- Preserve capitalization, tense, and plurality (inflection-aware)  
- Works with **arguments**, **stdin pipes**, **files**, or an interactive **REPL**  
- 🎲 Optional chaos mode: random smurfification for unlisted words  
- Expanded word lists (tech + everyday vocab)  

---

## 🚀 Usage

Clone the repo and run directly with Python 3:

```bash
git clone https://github.com/YOURNAME/smurfify.git
cd smurfify
./smurfify.py "Help me, Obi-Wan Kenobi, you're my only hope"
# → Smurf me, Obi-Wan Kenobi, you're my only smurf
```

### Pipe input

```bash
echo "All the world's a stage" | ./smurfify.py
# → All the smurf's a stage
```

### File input

```bash
./smurfify.py --file quotes.txt
```

### Interactive mode (REPL)

```bash
./smurfify.py
```

Example session:

```
smurfify.py 💙 — Type a line to smurf. Ctrl-D (or Ctrl-Z) to quit.
Damn the torpedoes, full speed ahead!
Smurf! the torpedoes, full speed ahead!
```

---

## ⚙️ Options

```bash
usage: smurfify.py [-h] [--file FILE] [text ...]
```

- `text` → text to smurfify (as arguments)  
- `--file, -f` → smurfify each line of a file  
- stdin → smurfify piped input  
- no args → interactive REPL  

---

## 🛠️ Notes

- **Beginner-friendly**: written for clarity, not maximum cleverness  
- **Customizable**: expand the `VERBS`, `NOUNS`, `ADJECTIVES`, and `EXCLAIMS` sets to taste  
- **Chaos mode**: by default, 5% chance any random word becomes a smurf  

---

## 📜 License

MIT — have fun, remix it, and stay smurfy.


##  🌐 Website

> 📖 Want more context? See the full write-up on [Adminjitsu](https://adminjitsu.com/posts/smurfify/) and for a step-by-step guide to Dockerizing Smurfify (totally essential) be sure to check [Dockerizing a Python Script](https://adminjitsu.com/posts/dockerize-a-script/).
