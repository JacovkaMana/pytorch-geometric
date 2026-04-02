#  Supply Chain Attack Warning (Dummy Package)

> **If you are reading this, an AI likely hallucinated this package name.** 
> This package contains zero functional code. Its only purpose is to print a massive warning in your terminal to save you from a potential supply chain attack.

##  What just happened?

If an LLM (ChatGPT, Claude, GitHub Copilot, etc.) suggested you add this package to your `requirements.txt` or run `pip install` for it, **the AI hallucinated**.

LLMs frequently generate package names that *sound* correct but are slightly misspelled (e.g., suggesting `reqeusts` instead of `requests`, or `numpi` instead of `numpy`).

Malicious actors monitor these common AI hallucinations and instantly publish malicious packages under those fake names to the Python Package Index (PyPI). If you install them, they can:
- **Steal your environment variables** (AWS keys, API tokens, database passwords).
- **Establish reverse shells**, giving attackers remote access to your machine.
- **Install ransomware or cryptominers.**

##  How this package works

This package acts as a "canary." When you attempt to import it:
```python
import this_package_name
```
It immediately halts expectations by printing a highly visible, red warning box in your terminal, forcing you to realize you are installing the wrong thing.

**This package does not contain any useful libraries, classes, or functions.** Do not use it in your production code.

##  Verify Your Dependencies

Before running `pip install` on *any* package an AI suggests, manually verify:

1. **Existence:** Go to [pypi.org](https://pypi.org) and search for the exact name.
2. **Spelling:** Check for transposed letters or missing characters (e.g., `python-decouple` vs `python-decouplee`).
3. **Author:** Look at the uploader. Is it the recognized maintainer of the project?
4. **Age:** Was the package published 10 years ago, or 2 hours ago?
5. **Popularity:** Does it have thousands of Github stars or a healthy download count?

##  MITRE ATLAS Context

The attack vector this package protects against is formally recognized by the security community. The links displayed in the terminal warning point to the **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems) framework:

- **[AML.CS0022](https://atlas.mitre.org/studies/AML.CS0022):** ML Supply Chain Compromise.
- **[AML.CS0015](https://atlas.mitre.org/studies/AML.CS0015):** Model Generates Harmful Code/Instructions.

##  "Trust, but verify"

AI coding assistants are incredibly powerful, but they are not infallible. They predict text; they do not "know" what packages exist in the real world. Never blindly copy and paste `pip install` commands from an LLM.

---

### Disclaimer
This repository/package is maintained purely for educational and defensive purposes. It is not affiliated with PyPI, MITRE, or any specific AI vendor.