"""Superstore analysis: generates charts used in README.md"""
import pandas as pd, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
df = pd.read_excel("data/Favour_Daniel-USA-Super-Store-Data.xlsx", sheet_name="Orders")
df["Year"] = df["Order Date"].dt.year
G, R = "#2a9d8f", "#e76f51"
def bar(s, title, fn, h=False):
    fig, ax = plt.subplots(figsize=(8, 5))
    c = [G if v >= 0 else R for v in s.values]
    (ax.barh if h else ax.bar)(s.index.astype(str), s.values, color=c)
    ax.set_title(title, fontweight="bold"); ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout(); plt.savefig(f"images/{fn}.png", dpi=130); plt.close()
y = df.groupby("Year")[["Sales", "Profit"]].sum()
ax = y.plot(kind="bar", figsize=(8, 5), color=["#264653", G], rot=0)
ax.set_title("Sales and Profit by Year", fontweight="bold"); ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("images/yearly.png", dpi=130); plt.close()
bar(df.groupby("Category").Profit.sum(), "Profit by Category ($)", "category")
bar(df.groupby("Sub-Category").Profit.sum().sort_values(), "Profit by Sub-Category ($)", "subcategory", True)
bins = pd.cut(df.Discount, [-.01, 0, .2, .3, .5, 1], labels=["0%", "1-20%", "21-30%", "31-50%", ">50%"])
bar(df.groupby(bins, observed=True).Profit.sum(), "Profit by Discount Level ($)", "discount")
bar(df.groupby("Region").Profit.sum(), "Profit by Region ($)", "region")
s = df.groupby("State").Profit.sum().sort_values()
bar(pd.concat([s.head(7), s.tail(5)]), "Best & Worst States by Profit ($)", "states", True)
print(df.groupby("Region").Discount.mean().round(3))
print(df[df.Discount > .2].shape[0] / len(df))
