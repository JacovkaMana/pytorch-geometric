import re

BOX_INNER = 78

def _vis(s):
    """Visible length of string, ignoring ANSI escape codes."""
    return len(re.sub(r'\033\[[0-9;]*m', '', s))

def _line(text):
    """Create a bordered line with correct padding."""
    pad = BOX_INNER - 2 - _vis(text)
    return f"║ {text}{' ' * pad} ║"

def warn():
    R = "\033[1;91m"
    W = "\033[1;97m"
    Y = "\033[1;93m"
    G = "\033[1;92m"
    C = "\033[1;96m"
    X = "\033[0m"

    top = f"{R}╔{'═' * BOX_INNER}╗{X}"
    bot = f"{R}╚{'═' * BOX_INNER}╝{X}"
    sep = f"{R}╠{'═' * BOX_INNER}╣{X}"
    emp = f"{R}║{' ' * BOX_INNER}║{X}"
    sep_in = f"{R}║ ├{'─' * (BOX_INNER - 4)}┤ ║{X}"

    print(f"""
{top}
{emp}
{emp}
{_line(f"{R}██████╗ ██████╗  █████╗ ███╗   ██╗██╗  ██╗███████╗██╗     ██╗   ██╗███████╗{X}")}
{_line(f"{R}██╔══██╗██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝██║     ██║   ██║██╔════╝{X}")}
{_line(f"{R}██████╔╝██████╔╝███████║██╔██╗ ██║█████╔╝ █████╗  ██║     ██║   ██║█████╗  {X}")}
{_line(f"{R}██╔═══╝ ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ██╔══╝  ██║     ██║   ██║██╔══╝  {X}")}
{_line(f"{R}██║     ██║  ██║██║  ██║██║ ╚████║██║  ██╗███████╗███████╗╚██████╔╝███████╗{X}")}
{_line(f"{R}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝{X}")}
{emp}
{emp}
{sep_in}
{_line(f"{W}                                                                            {X}")}
{_line(f"{W}  YOU MAY BE A VICTIM OF A SUPPLY CHAIN ATTACK!                           {X}")}
{_line(f"{W}                                                                            {X}")}
{_line(f"{Y}  Did an LLM (ChatGPT, Claude, Copilot, etc.) suggest this                 {X}")}
{_line(f"{Y}  package name or pip install command?                                    {X}")}
{_line(f"{W}                                                                            {X}")}
{_line(f"{W}  ▶ LLMs HALLUCINATE PACKAGE NAMES VERY FREQUENTLY                       {X}")}
{_line(f"{W}  ▶ Malicious actors publish typosquatted packages on PyPI                {X}")}
{_line(f"{W}  ▶ These fake packages can STEAL your data, keys, and credentials        {X}")}
{_line(f"{W}  ▶ They can give attackers FULL ACCESS to your system                    {X}")}
{_line(f"{W}                                                                            {X}")}
{sep_in}
{emp}
{_line(f"{G} BEFORE CONTINUING, VERIFY:                                                {X}")}
{emp}
{_line(f"{W}  1. Check https://pypi.org — Does this package actually exist?            {X}")}
{_line(f"{W}  2. Check the spelling — Is it exact? (e.g. ""reqeusts"" ≠ ""requests"")     {X}")}
{_line(f"{W}  3. Check the author — Is it a trusted, verified publisher?               {X}")}
{_line(f"{W}  4. Check the release date — Is it suspiciously new?                     {X}")}
{_line(f"{W}  5. Check the downloads — Does it have a healthy user base?              {X}")}
{emp}
{_line(f"{C} More info:                                                                {X}")}
{_line(f"{W}  • https://atlas.mitre.org/studies/AML.CS0022                    {X}")}
{_line(f"{W}  • https://atlas.mitre.org/studies/AML.CS0015                {X}")}
{_line(f"{W}  • https://packaging.python.org/en/latest/security/                      {X}")}
{_line(f"{W}  • https://pypl.org/ (top packages list)                                 {X}")}
{emp}
{emp}
{emp}
{bot}
""")

warn()