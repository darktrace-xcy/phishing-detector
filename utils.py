import re
from urllib.parse import urlparse

def analyze_url(url):
    score = 0
    reasons = []

    parsed = urlparse(url)
    domain = parsed.netloc

    # Rule 1: HTTP instead of HTTPS
    if not url.startswith("https"):
        score += 1
        reasons.append("Uses HTTP instead of HTTPS")

    # Rule 2: IP address in URL
    if re.match(r"\d+\.\d+\.\d+\.\d+", domain):
        score += 1
        reasons.append("Uses IP address instead of domain name")

    # Rule 3: Suspicious keywords
    keywords = ["login", "verify", "secure", "bank", "update"]
    for word in keywords:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious keyword: '{word}'")
            break

    # Rule 4: Long URL
    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    # Rule 5: '@' symbol trick
    if "@" in url:
        score += 1
        reasons.append("Contains '@' symbol (redirect trick)")

    # Rule 6: Fake domain pattern (numbers replacing letters)
    if re.search(r"[0-9]", domain):
        score += 1
        reasons.append("Domain contains numbers (possible spoofing)")

    return score, reasons
