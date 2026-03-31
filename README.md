# 🛒 Retail Sales Analysis — Data Analyst Portfolio Project

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Dashboard-green?logo=microsoft-excel&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Looker_Studio-Dashboard-orange?logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

Proyek ini merupakan analisis bisnis end-to-end terhadap dataset transaksi retail multi-kategori selama periode **Januari 2022 – Januari 2025**. Tujuan utama proyek adalah mengidentifikasi pola penjualan, mengukur performa profit per kategori, dan memberikan rekomendasi bisnis berbasis data kepada manajemen.

> **Role:** Junior Data Analyst  
> **Tools:** Python (pandas, openpyxl), Excel, Google Looker Studio  
> **Dataset:** Data_Retail.xlsx (internal dataset)

---

## 📂 Repository Structure

```
retail-sales-analysis/
│
├── data/
│   └── Data_Retail.xlsx              # Dataset utama (12,418 transaksi)
│
├── analysis/
│   └── Data_Retail_Dashboard_Full.xlsx  # Dashboard & pivot tables lengkap
│
├── report/
│   └── Retail_Sales_Analysis_W6.pptx   # Laporan presentasi (6 slide)
│
├── images/
│   ├── chart_sales_by_region.png
│   ├── chart_profit_by_category.png
│   ├── chart_discount_analysis.png
│   └── chart_top10_subcategory.png
│
└── README.md
```

---

## 📊 Dataset Description

| Atribut | Detail |
|---|---|
| **Sumber** | Dataset transaksi retail internal |
| **Periode** | 1 Januari 2022 – 18 Januari 2025 |
| **Jumlah Baris** | 12,418 transaksi |
| **Jumlah Kolom** | 15 variabel |
| **Missing Values** | 0 (dataset bersih) |
| **Duplikat** | 0 |

### Variabel Utama

| Kolom | Tipe | Keterangan |
|---|---|---|
| `Transaction_id` | String | ID unik per transaksi |
| `Customer_id` | String | ID pelanggan |
| `Category` | String | Kategori produk (8 kategori) |
| `Sub-Category` | String | Sub-kategori produk (100+ item) |
| `Price_per_unit` | Float | Harga satuan produk |
| `Quantity` | Integer | Jumlah unit terjual |
| `Sales` | Float | Total nilai penjualan |
| `Profit` | Float | Estimasi profit (20% dari Sales) |
| `Discount_Value` | Float | Nilai diskon: 0.0 atau 0.2 (20%) |
| `Payment_Method` | String | Cash / Credit Card / Digital Wallet |
| `Location` | String | Online / In-store |
| `Transaction_Date` | Date | Tanggal transaksi |
| `Region` | String | ⚠️ Dummy data (East / West / Central) |
| `Month` | String | Format YYYY-MM |
| `Discount` | Boolean | True jika ada diskon |

> ⚠️ **Catatan:** Kolom `Region` merupakan **dummy data** dan tidak mencerminkan lokasi geografis nyata. Kolom `Profit` dihitung sebagai **estimasi tetap 20% dari Sales**.

---

## 🧹 Data Cleaning Summary

Dataset dalam kondisi sangat bersih saat diterima. Berikut langkah verifikasi yang dilakukan:

| Langkah | Hasil |
|---|---|
| Cek missing values | ✅ 0 missing values pada semua kolom |
| Cek duplikasi baris | ✅ 0 duplikat ditemukan |
| Validasi format tanggal | ✅ `Transaction_Date` berhasil di-parse ke datetime |
| Validasi nilai numerik | ✅ `Sales`, `Profit`, `Price_per_unit` semua positif |
| Cek nilai `Discount_Value` | ✅ Hanya 2 nilai unik: 0.0 dan 0.2 |
| Cek konsistensi `Category` | ✅ 8 kategori konsisten tanpa typo |
| Ekstraksi fitur tambahan | ✅ `Year` dan `Month_Num` diekstrak dari `Transaction_Date` |

---

## 🔍 Exploratory Data Analysis (EDA)

### 1. Sales by Region

| Region | Total Sales (Rp) | Total Profit (Rp) | % Kontribusi |
|---|---|---|---|
| East | 680,757 | 136,151 | 43.8% |
| West | 517,519 | 103,504 | 33.3% |
| Central | 357,285 | 71,457 | 23.0% |

> 📌 East mendominasi sales (43.8%), namun profit margin seragam 20% di semua region karena profit merupakan estimasi tetap dari sales.

---

### 2. Profit by Category

| Category | Total Sales (Rp) | Total Profit (Rp) |
|---|---|---|
| Butchers | 204,140 | 40,828 |
| Electric Household | 203,261 | 40,652 |
| Computers & Electric | 197,491 | 39,498 |
| Food | 196,326 | 39,265 |
| Beverages | 195,561 | 39,112 |
| Furniture | 191,426 | 38,285 |
| Patisserie | 184,615 | 36,923 |
| Milk Products | 182,741 | 36,548 |

> 📌 Butchers dan Electric Household menjadi kategori dengan kontribusi profit absolut tertinggi.

---

### 3. Discount Analysis

| Tipe | Jumlah Transaksi | % Transaksi | Total Sales (Rp) | Total Profit (Rp) |
|---|---|---|---|---|
| Tanpa Diskon (0%) | 4,107 | 33.1% | 516,356 | 103,271 |
| Dengan Diskon (20%) | 8,311 | 66.9% | 1,039,205 | 207,841 |

> 📌 66.9% transaksi menggunakan diskon 20%. Diskon efektif mendorong volume transaksi (2× lebih banyak), namun profit margin per transaksi tetap sama (20%) karena profit adalah estimasi tetap dari sales.

---

### 4. Top 10 Sub-Category by Sales

| Rank | Sub-Category | Total Sales (Rp) |
|---|---|---|
| 1 | Item_2_BEV | 145,446 |
| 2 | Item_25_FUR | 21,976 |
| 3 | Item_22_BUT | 19,710 |
| 4 | Item_25_EHE | 19,393 |
| 5 | Item_20_BUT | 18,861 |
| 6 | Item_19_MILK | 18,848 |
| 7 | Item_19_CEA | 17,856 |
| 8 | Item_20_FOOD | 17,487 |
| 9 | Item_25_BUT | 17,384 |
| 10 | Item_16_MILK | 17,243 |

> 📌 Item_2_BEV (Beverages) mendominasi dengan selisih sangat besar (~6.6× sub-kategori terbesar kedua), menjadikannya produk andalan utama.

---

### 5. Sales Trend (Monthly)

- **Puncak tertinggi:** Januari 2022 (Rp 52,549) — kemungkinan efek awal tahun
- **Terendah:** Januari 2025 (Rp 25,557) — data belum lengkap (hanya 18 hari)
- **Pola tahunan:** Sales cenderung stabil di kisaran Rp 38,000–49,000 per bulan
- **Desember 2024** menjadi bulan terkuat di 2024 (Rp 48,933), mengindikasikan efek musim liburan

---

## 💡 Business Insights

### Insight 1 — East Region Mendominasi Volume Transaksi
Region East mencatat 43.8% dari total sales (Rp 680,757) dengan 5,421 transaksi — terbanyak dari ketiga region. Namun karena region adalah dummy data, ini lebih mencerminkan distribusi data daripada realitas geografis.

### Insight 2 — Butchers & Electric Household adalah Kategori Prioritas
Kedua kategori ini secara konsisten unggul baik dari sisi sales maupun profit absolut. Butchers (Rp 204,140 sales) dan Electric Household (Rp 203,261) menjadi penopang utama pendapatan perusahaan.

### Insight 3 — Diskon 20% Mendorong 2× Volume Transaksi
Transaksi dengan diskon (8,311 transaksi) adalah 2× lebih banyak dibanding tanpa diskon (4,107 transaksi). Ini menunjukkan diskon efektif sebagai pendorong pembelian, meski margin tidak berubah karena profit bersifat estimasi.

### Insight 4 — Item_2_BEV adalah Produk Star
Sub-kategori Item_2_BEV (Beverages) mencatat sales Rp 145,446 — jauh melampaui sub-kategori kedua (Item_25_FUR: Rp 21,976). Ini menunjukkan bahwa satu produk Beverages tertentu sangat dominan dan menjadi "star product" perusahaan.

### Insight 5 — Pola Sales Stabil dengan Puncak di Akhir & Awal Tahun
Data 3 tahun menunjukkan pola musiman yang konsisten: sales meningkat di Desember–Januari dan sedikit melemah di pertengahan tahun (Agustus–Oktober). Ini bisa dimanfaatkan untuk perencanaan stok dan promosi.

---

## 📋 Business Recommendations

### Rekomendasi 1 — Kembangkan Lini Produk Beverages
Item_2_BEV menunjukkan dominasi yang luar biasa. Perusahaan perlu memastikan ketersediaan stok, mempertimbangkan ekspansi varian produk, dan menjadikannya anchor product dalam setiap promosi.

### Rekomendasi 2 — Optimalkan Strategi Diskon
Diskon 20% efektif mendorong volume, namun perlu dikaji apakah bisa digantikan dengan program loyalitas (poin reward, member pricing) yang meningkatkan retention tanpa harus selalu memberikan potongan harga langsung.

### Rekomendasi 3 — Tingkatkan Volume di Kategori Butchers & Electric Household
Kedua kategori ini memiliki performa terbaik. Alokasikan lebih banyak slot shelf space, promosi bundling, dan kampanye marketing untuk mempertahankan dan meningkatkan momentum penjualan.

### Rekomendasi 4 — Evaluasi Patisserie & Milk Products
Kedua kategori ini berada di posisi terbawah dari sisi kontribusi profit absolut. Perlu analisis lebih dalam: apakah karena harga jual rendah, biaya tinggi, atau demand yang memang terbatas — sehingga bisa diputuskan apakah perlu reposisi harga atau pengurangan SKU.

### Rekomendasi 5 — Manfaatkan Pola Musiman untuk Perencanaan
Tingkatkan stok dan intensitas promosi menjelang Desember–Januari (peak season). Di bulan-bulan lemah (Agustus–Oktober), gunakan flash sale atau bundle deal untuk menjaga momentum penjualan.

---

## 🛠️ Tools Used

| Tool | Kegunaan |
|---|---|
| **Python 3.10+** | Data loading, cleaning, aggregation (pandas) |
| **openpyxl** | Pembuatan Excel dashboard dengan formatting |
| **Microsoft Excel** | Review dan validasi data |
| **Google Looker Studio** | Interactive dashboard (via Google Sheets connector) |
| **PowerPoint / pptxgenjs** | Laporan presentasi 6 slide |

---

## 📈 Key Metrics Summary

```
Total Transaksi   : 12,418
Total Sales       : Rp 1,555,560
Total Profit      : Rp 311,112
Profit Margin     : 20.0% (estimasi tetap)
Avg Sales/Txn     : Rp 125.27
Periode Data      : Jan 2022 – Jan 2025 (37 bulan)
Kategori Produk   : 8 kategori
Region            : 3 (East, West, Central) — dummy data
Payment Methods   : Cash, Credit Card, Digital Wallet
Channel           : Online & In-store
```

---

## 🚀 How to Run

```bash
# Clone repository
git clone https://github.com/username/retail-sales-analysis.git
cd retail-sales-analysis

# Install dependencies
pip install pandas openpyxl

# Run analysis
python analysis/analysis.py
```

---

## 📬 Contact

**Junior Data Analyst**  
📧 email@vionarhema17.com  
🔗 [LinkedIn](www.linkedin.com/in/viona-rhema-069b38378)  
🐙 [GitHub](https://github.com/rheva17)

---

*Project ini dibuat sebagai bagian dari portfolio Data Analyst — Minggu 7: Final Project & Portfolio.*
