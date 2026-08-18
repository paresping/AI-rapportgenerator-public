# AI-rapportgenerator – sanerad portfolio-version

Detta repo är en **sanerad, fristående portfolio-snapshot** av projektet "Kent och Pärs AI-rapporter". Syftet är att visa lösningsidén och centrala tekniska delar utan att publicera verkliga kunddata, interna runtime-filer, OpenAI-assistent-/thread-ID:n eller gammal Git-historik från originalprojektet.

Verktyget läser svenska SIE-filer, summerar bokföringsdata, beräknar finansiella nyckeltal och använder OpenAI:s GPT-modeller för att skapa en strukturerad ekonomisk analys.

## Vad projektet demonstrerar

- Python-baserad behandling av strukturerad bokföringsdata
- Parsing av SIE-data
- Beräkning av ekonomiska nyckeltal
- Promptkonstruktion för generativ AI
- Integration mot OpenAI API
- Separation mellan hemligheter och källkod via miljövariabler
- Säker hantering av portfolio-/demodata

Originalprojektet innehåller även mer avancerade funktioner, bland annat flerårig trendanalys, SCB-baserad branschjämförelse, Assistants API, PDF-generering, grafer, tokenkostnadsuppföljning och mer omfattande fel-/debughantering. De delarna är inte fullt återgivna i denna publika snapshot eftersom fokus här är att visa kärnarkitekturen utan att exponera projekt- eller kundspecifika data.

## Säkerhet och data

Detta repo innehåller **endast syntetiska SIE-exempel**. Verkliga SIE-filer, ekonomiska kunddata, debug-loggar, manuella nyckeltalsfiler, OpenAI Assistant/Thread-ID:n och `.env`-filer är uttryckligen exkluderade via `.gitignore`.

API-nyckeln ska anges lokalt i `.env`:

```bash
cp .env.example .env
```

Lägg därefter in din egen `OPENAI_API_KEY` i `.env`. Den filen ska aldrig committas.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Exempel

```bash
python main.py \
  sie-filer/example_2023.se \
  sie-filer/example_2024.se \
  --output report.md
```

## Struktur

- `main.py` – CLI och huvudflöde
- `sie_parser.py` – läser och summerar SIE-data
- `key_figures.py` – beräknar centrala nyckeltal
- `prompt_template.py` – bygger strukturerad GPT-prompt
- `report_utils_gpt.py` – anropar OpenAI API
- `config.py` – läser lokal API-nyckel från miljövariabel
- `sie-filer/example_2023.se` – syntetisk testdata
- `sie-filer/example_2024.se` – syntetisk testdata

## Bakgrund

Projektet utvecklades som ett praktiskt AI-projekt för att undersöka hur generativ AI kan kombineras med strukturerad ekonomisk data för att automatisera finansiell analys och rapportering för svenska små och medelstora företag.

Skapad av Kent och Pär.
