import argparse
from pathlib import Path

from key_figures import calculate_key_figures
from prompt_template import get_prompt_template
from report_utils_gpt import generate_report
from sie_parser import load_sie_files


def main():
    parser = argparse.ArgumentParser(
        description="Generate an AI-assisted financial report from SIE files."
    )
    parser.add_argument("sie_files", nargs="+", help="One or more SIE files")
    parser.add_argument("--model", default="gpt-4o")
    parser.add_argument("--output", default="report.md")
    args = parser.parse_args()

    data_by_year = load_sie_files(args.sie_files)
    latest_year = max(data_by_year)
    summarized = data_by_year[latest_year]["summarized"]

    key_figures = calculate_key_figures(summarized)
    prompt = get_prompt_template(summarized, key_figures)
    report = generate_report(prompt, model=args.model)

    Path(args.output).write_text(report, encoding="utf-8")
    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
