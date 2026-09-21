"""
main_daily_report.py — the Operations department's report.

Finance asked *what did we sell?* and Marketing asked *which products sell?*
Operations asks a third question: *when do we sell?* Same eleven rows, same
pipeline, grouped down a different column — because staffing a shop floor needs
the calendar, not the catalogue.

**You write this file yourself.** `main_finance_report.py` and
`main_marketing_report.py` are your worked examples: this report has the same
three-step shape and mostly calls functions that already exist. The one new piece
is `summarize_by_day`, which you add to `sales_pipeline.transform` — and once it
exists, `find_top_entry` ranks days exactly as happily as it ranks items, because
it never cared what an entry *was*, only which field to compare.

That is the lesson worth taking away: a third report needed one new function, not
a third script.

Before running:  pip install -r requirements.txt

    python code/main_daily_report.py        # the fixed sample data
    python code/main_daily_report.py 42     # the generated data for seed 42
"""


import sys
from sales_pipeline import (
    calculate_total_revenue,
    clean_sales_data,
    find_top_entry,
    get_raw_sales_data,
    print_day_table,
    summarize_by_day,
)

seed = None
if len(sys.argv) > 1 and sys.argv[1].strip().isdigit():
    seed = int(sys.argv[1])

print("=== OPERATIONS: Sales by Day ===")
print()

raw_data = get_raw_sales_data(seed)

clean_data = clean_sales_data(raw_data)
day_summary = summarize_by_day(clean_data)
total_revenue = calculate_total_revenue(clean_data)
top_by_revenue = find_top_entry(day_summary, "revenue")
top_by_units = find_top_entry(day_summary, "units_sold")

print_day_table(day_summary)
print()
print(f"Total Revenue:          ${total_revenue:,.2f}")
print(f"Busiest day by revenue: {top_by_revenue['date']} (${top_by_revenue['revenue']:,.2f})")
print(f"Busiest day by units:   {top_by_units['date']} ({top_by_units['units_sold']} units)")
