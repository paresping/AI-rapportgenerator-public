# Kent och Pärs AI-rapporter

Detta verktyg genererar ekonomiska rapporter från SIE-filer med hjälp av OpenAI\:s GPT-modeller. Projektet är optimerat för svenska små och medelstora företag och kan användas av redovisningsbyråer, rådgivare eller företagare själva.

## ✅ Senaste förbättringar (juni 2025)

* 🔄 **Negativa intäkter och kostnader rättas automatiskt** innan prompten skickas till GPT
* 🌐 **Engelsk översättning av kontonamn** från BAS 2025 ingår i prompten
* 💡 **Ny promptstruktur** med stöd för trendanalys över flera år
* 💬 **Nyckeltal och trenddata** skickas som separata sektioner i prompten
* 📘 **Förtydligad rapporttext** – undviker motsägelsefulla belopp i olika sektioner
* 🇸🇪 **Tusentalsavgränsare enligt svenska formatregler** i all rapporttext
* 🛠️ **Felmeddelanden förbättrade** och mer robust hantering av summerad data
* 📦 **Debug-utskrifter och loggning** förbättrade för felsökning
* ✅ **`summarized_data` harmoniserad** med GPT-input för konsekvent visning

## Funktioner

* Läser in en eller flera SIE-filer
* Extraherar nyckeltal och trender
* Hämtar branschdata från SCB (v2beta API)
* Genererar rapporttext via OpenAI GPT (chat eller assistant)
* Genererar PDF med företagslogotyp, nyckeltalsgrafer och metadata
* Visar GPT-tokenkostnad som egen sida (om begärt)

## Exempel

```bash
python main.py sie-filer/2023.se sie-filer/2024.se \
  --employees 2 \
  --language sv \
  --style native \
  --industry 10.130 \
  --graph \
  --via-assistant \
  --testid TEST001
```

## Förutsättningar

* Python 3.10+
* WeasyPrint installerad lokalt för PDF-export
* API-nyckel från OpenAI
* (Valfritt) API-nyckel för SCB om throttling överskrids

## Strukturen i rapporter

* Framsida med logotyp, metadata och testinfo
* GPT-genererad analys (Executive Summary, Resultat, Nyckeltal, Rekommendationer)
* (Valfritt) Nyckeltalsgrafer
* (Valfritt) Tokenkostnadssida

## Mappar och filer

* `main.py` – körfil med CLI-argument
* `sie_parser.py` – laddar och tolkar SIE-filer
* `key_figures.py` – beräknar nyckeltal
* `prompt_template.py` – skapar GPT-prompt
* `report_utils_gpt.py` – hanterar GPT-anrop
* `render_report_from_gpt.py` – bygger HTML och PDF
* `template.html` – mall för PDF

## Övrigt

Alla känsliga eller icke-användbara datapunkter maskeras eller rensas bort innan prompten skickas till GPT. Nyckeltal och observationer inkluderas som strukturerad indata.

## Kontakt

Skapad av Kent och Pär. Feedback och förbättringsförslag välkomnas!
