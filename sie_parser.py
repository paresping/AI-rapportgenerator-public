from collections import defaultdict
from pathlib import Path


def parse_sie_file(filepath: str):
    accounts = {}
    transactions = []
    orgnr = None
    company_name = None
    year = None

    path = Path(filepath)
    text = path.read_text(encoding="utf-8", errors="replace")

    for raw_line in text.splitlines():
        parts = raw_line.strip().split()
        if not parts:
            continue

        tag = parts[0]
        if tag == "#RAR" and len(parts) >= 3:
            start_date = parts[-2]
            if len(start_date) >= 4 and start_date[:4].isdigit():
                year = int(start_date[:4])
        elif tag == "#ORGNR" and len(parts) > 1:
            orgnr = parts[1]
        elif tag == "#FNAMN" and len(parts) > 1:
            company_name = " ".join(parts[1:]).strip('"')
        elif tag == "#KONTO" and len(parts) >= 3:
            accounts[parts[1]] = " ".join(parts[2:]).strip('"')
        elif tag == "#TRANS" and len(parts) >= 4:
            account = parts[1]
            try:
                amount = float(parts[-1])
            except ValueError:
                continue
            transactions.append((account, amount))

    summary = defaultdict(float)
    for account, amount in transactions:
        summary[account] += amount

    summarized = [
        {
            "account_number": account,
            "account_name": accounts.get(account, "Unknown account"),
            "amount": round(amount, 2),
        }
        for account, amount in sorted(summary.items())
    ]

    raw = {
        "organisationsnummer": orgnr,
        "företagsnamn": company_name,
        "räkenskapsår": year,
    }
    return summarized, raw


def load_sie_files(filepaths):
    by_year = {}
    for filepath in filepaths:
        summarized, raw = parse_sie_file(filepath)
        year = raw.get("räkenskapsår")
        if year is None:
            raise ValueError(f"Räkenskapsår saknas i {filepath}")
        by_year[year] = {"summarized": summarized, "raw": raw}
    return by_year
