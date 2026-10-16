import pandas as pd, json
df = pd.read_excel("data/Favour_Daniel-USA-Super-Store-Data.xlsx", sheet_name="Orders")
cols = {k: sorted(df[k].unique()) for k in ["Region", "Category", "Sub-Category", "State"]}
rows = [[int(r["Order Date"].year), int(r["Order Date"].month), cols["Region"].index(r.Region), cols["Category"].index(r.Category),
         cols["Sub-Category"].index(r["Sub-Category"]), cols["State"].index(r.State), float(r.Discount), round(r.Sales, 1), round(r.Profit, 1)]
        for _, r in df.iterrows()]
html = open("dashboard_template.html").read().replace("__DATA__", json.dumps({"rows": rows, **cols}, separators=(",", ":")))
open("dashboard.html", "w").write(html)
