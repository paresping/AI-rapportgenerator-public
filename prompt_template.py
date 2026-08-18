def get_prompt_template(summarized_data, key_figures, industry_text=""):
    account_rows = "\n".join(
        f"- {row['account_number']} {row['account_name']}: {row['amount']:.2f} SEK"
        for row in summarized_data
    )
    key_rows = "\n".join(
        f"- {name}: {value}" for name, value in key_figures.items() if value is not None
    )

    return f"""You are a professional financial analyst specializing in Swedish SMEs.

Generate a concise, structured financial report based only on the supplied accounting data and pre-calculated key figures. Do not invent data.

## Summarized accounting data
{account_rows}

## Calculated key figures
{key_rows}

## Industry context
{industry_text or 'No industry benchmark supplied.'}

## Required sections
- Executive Summary
- Revenue, Costs and Profit
- Key Financial Ratios
- Observations and Warnings
- Recommendations for Management

For recommendations, make each action specific, measurable and linked to a figure or observed issue.
Return Markdown only.
"""
