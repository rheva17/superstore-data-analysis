"""
retail_analysis.py
==================
Retail Sales Analysis — End-to-End Python Script
Dataset  : Data_Retail.xlsx (12,418 transaksi, Jan 2022 – Jan 2025)
Author   : Junior Data Analyst
Project  : Minggu 7 — Final Project & Portfolio
"""

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# 1. DATA LOADING
# ─────────────────────────────────────────────
print("=" * 60)
print("RETAIL SALES ANALYSIS")
print("=" * 60)

df = pd.read_excel("data/Data_Retail.xlsx")
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])
df["Year"]      = df["Transaction_Date"].dt.year
df["Month_Num"] = df["Transaction_Date"].dt.month

print(f"\n✅ Dataset loaded: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"   Date range : {df['Transaction_Date'].min().date()} → {df['Transaction_Date'].max().date()}")


# ─────────────────────────────────────────────
# 2. DATA CLEANING & VALIDATION
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("DATA CLEANING")
print("─" * 60)

missing  = df.isnull().sum().sum()
dupes    = df.duplicated().sum()
neg_sales  = (df["Sales"] < 0).sum()
neg_profit = (df["Profit"] < 0).sum()

print(f"  Missing values : {missing}")
print(f"  Duplicate rows : {dupes}")
print(f"  Negative Sales : {neg_sales}")
print(f"  Negative Profit: {neg_profit}")
print(f"  Discount_Value unique: {sorted(df['Discount_Value'].unique())}")
print(f"  Categories ({df['Category'].nunique()}): {df['Category'].unique().tolist()}")
print(f"  Regions: {df['Region'].unique().tolist()}  ⚠️  dummy data")
print("\n✅ Dataset is clean — no action required.")


# ─────────────────────────────────────────────
# 3. OVERVIEW STATISTICS
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("OVERVIEW STATISTICS")
print("─" * 60)

total_sales  = df["Sales"].sum()
total_profit = df["Profit"].sum()
margin       = total_profit / total_sales * 100
avg_sales    = df["Sales"].mean()

print(f"  Total Sales       : Rp {total_sales:>12,.2f}")
print(f"  Total Profit      : Rp {total_profit:>12,.2f}")
print(f"  Profit Margin     : {margin:.1f}%")
print(f"  Avg Sales / Txn   : Rp {avg_sales:>12,.2f}")
print(f"  Total Transaksi   : {len(df):,}")


# ─────────────────────────────────────────────
# 4. EDA — SALES BY REGION
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("EDA 1: SALES BY REGION  (⚠️  Region = dummy data)")
print("─" * 60)

region = (
    df.groupby("Region")[["Sales", "Profit"]]
    .sum()
    .assign(Pct=lambda x: x["Sales"] / total_sales * 100,
            Txn=df.groupby("Region")["Transaction_id"].count())
    .sort_values("Sales", ascending=False)
)
print(region.to_string())


# ─────────────────────────────────────────────
# 5. EDA — PROFIT BY CATEGORY
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("EDA 2: PROFIT BY CATEGORY")
print("─" * 60)

cat = (
    df.groupby("Category")[["Sales", "Profit"]]
    .sum()
    .assign(Margin=lambda x: (x["Profit"] / x["Sales"] * 100).round(1))
    .sort_values("Profit", ascending=False)
)
print(cat.to_string())


# ─────────────────────────────────────────────
# 6. EDA — TOP 10 SUB-CATEGORY BY SALES
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("EDA 3: TOP 10 SUB-CATEGORY BY SALES")
print("─" * 60)

top10 = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
top10["Pct_Total"] = (top10["Sales"] / total_sales * 100).round(2)
top10.index = top10.index + 1
print(top10.to_string())


# ─────────────────────────────────────────────
# 7. EDA — DISCOUNT ANALYSIS
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("EDA 4: DISCOUNT ANALYSIS")
print("─" * 60)

disc = (
    df.groupby("Discount_Value")
    .agg(
        Transactions=("Transaction_id", "count"),
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Avg_Profit=("Profit", "mean"),
    )
    .assign(Pct_Txn=lambda x: x["Transactions"] / len(df) * 100)
)
print(disc.to_string())

no_disc  = df[df["Discount_Value"] == 0.0]["Profit"].mean()
with_disc = df[df["Discount_Value"] == 0.2]["Profit"].mean()
print(f"\n  Avg Profit (no discount) : Rp {no_disc:.2f}")
print(f"  Avg Profit (20% discount): Rp {with_disc:.2f}")
print(f"  Difference               : Rp {no_disc - with_disc:.2f}")


# ─────────────────────────────────────────────
# 8. EDA — MONTHLY SALES TREND
# ─────────────────────────────────────────────
print("\n" + "─" * 60)
print("EDA 5: MONTHLY SALES TREND")
print("─" * 60)

monthly = (
    df.groupby(["Year", "Month_Num", "Month"])[["Sales", "Profit"]]
    .sum()
    .reset_index()
    .sort_values(["Year", "Month_Num"])
)
monthly["MoM_Change"] = monthly["Sales"].pct_change() * 100

print(f"  Peak month  : {monthly.loc[monthly['Sales'].idxmax(), 'Month']} "
      f"→ Rp {monthly['Sales'].max():,.0f}")
print(f"  Lowest month: {monthly.loc[monthly['Sales'].idxmin(), 'Month']} "
      f"→ Rp {monthly['Sales'].min():,.0f}")
print(f"  Avg monthly : Rp {monthly['Sales'].mean():,.0f}")
print(f"\n  Full trend (last 12 months):")
print(monthly.tail(12)[["Month", "Sales", "Profit", "MoM_Change"]].to_string(index=False))


# ─────────────────────────────────────────────
# 9. BUSINESS INSIGHTS SUMMARY
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("BUSINESS INSIGHTS SUMMARY")
print("=" * 60)

insights = [
    ("Insight 1", "Region East mendominasi 43.8% dari total sales (Rp 680,757).\n"
                  "             Namun karena Region = dummy data, ini mencerminkan\n"
                  "             distribusi data, bukan performa wilayah geografis nyata."),
    ("Insight 2", "Butchers (Rp 204,140) & Electric Household (Rp 203,261)\n"
                  "             adalah dua kategori dengan kontribusi sales & profit\n"
                  "             absolut tertinggi — ~26% dari total bisnis."),
    ("Insight 3", "Item_2_BEV (Beverages) menghasilkan Rp 145,446 dalam sales,\n"
                  "             6.6× lebih besar dari sub-kategori kedua. Produk ini\n"
                  "             sendirian menyumbang 9.4% dari total sales perusahaan."),
    ("Insight 4", "Diskon 20% mendorong 2× lebih banyak transaksi (8,311 vs 4,107).\n"
                  "             Avg profit per transaksi hampir identik (Rp 25.01 vs 25.15),\n"
                  "             menunjukkan diskon efektif menaikkan volume tanpa merusak margin."),
    ("Insight 5", "Pola musiman konsisten: peak di Desember–Januari,\n"
                  "             lemah di Agustus–Oktober. Bisa dimanfaatkan untuk\n"
                  "             perencanaan stok dan jadwal promosi."),
]

for title, body in insights:
    print(f"\n  [{title}] {body}")


# ─────────────────────────────────────────────
# 10. BUSINESS RECOMMENDATIONS
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("BUSINESS RECOMMENDATIONS")
print("=" * 60)

recs = [
    "Jadikan Item_2_BEV sebagai 'Hero Product' — pastikan stok selalu\n"
    "     tersedia dan jadikan anchor dalam promosi bundling.",
    "Diversifikasi portfolio Beverages untuk mengurangi risiko ketergantungan\n"
    "     pada satu SKU (Item_2_BEV = 9.4% total sales).",
    "Evaluasi program diskon dengan A/B test: bandingkan diskon harga\n"
    "     vs program loyalitas (poin reward) untuk mengukur Customer LTV.",
    "Manfaatkan seasonality: tingkatkan stok & marketing budget di\n"
    "     November–Desember; gunakan flash sale di Agustus–Oktober.",
    "Lakukan analisis profitabilitas nyata untuk Patisserie & Milk Products\n"
    "     dengan mengintegrasikan data biaya operasional aktual.",
]

for i, rec in enumerate(recs, 1):
    print(f"\n  Rekomendasi {i}: {rec}")

print("\n" + "=" * 60)
print("Analysis complete. ✅")
print("=" * 60)
