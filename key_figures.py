def _sum_prefix(data, *prefixes):
    return sum(
        row["amount"]
        for row in data
        if any(str(row["account_number"]).startswith(prefix) for prefix in prefixes)
    )


def calculate_key_figures(summarized_data):
    net_sales = abs(_sum_prefix(summarized_data, "3"))
    operating_costs = abs(_sum_prefix(summarized_data, "4", "5", "6", "7"))
    interest_expense = abs(_sum_prefix(summarized_data, "84"))
    total_assets = abs(_sum_prefix(summarized_data, "1"))
    equity = abs(_sum_prefix(summarized_data, "20"))
    current_assets = abs(_sum_prefix(summarized_data, "14", "15", "16", "17", "18", "19"))
    current_liabilities = abs(_sum_prefix(summarized_data, "24", "25", "26", "27", "28", "29"))

    operating_profit = net_sales - operating_costs
    net_profit = operating_profit - interest_expense

    return {
        "Net sales": round(net_sales, 2),
        "Operating profit": round(operating_profit, 2),
        "Net profit": round(net_profit, 2),
        "Operating margin": round(operating_profit / net_sales * 100, 2) if net_sales else None,
        "Net profit margin": round(net_profit / net_sales * 100, 2) if net_sales else None,
        "Equity ratio": round(equity / total_assets * 100, 2) if total_assets else None,
        "Quick ratio": round(current_assets / current_liabilities, 2) if current_liabilities else None,
        "Return on equity": round(net_profit / equity * 100, 2) if equity else None,
    }
