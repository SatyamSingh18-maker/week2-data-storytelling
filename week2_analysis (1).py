import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 150

# -----------------------------
# 1. DATA ACQUISITION & CLEANING
# -----------------------------
df = pd.read_csv("happiness.csv")
df.columns = [c.strip() for c in df.columns]
print("Shape:", df.shape)
print(df.isnull().sum())

# Drop rows missing the target happiness score, if any
df = df.dropna(subset=["Happiness Score"])

# Rename for convenience
df = df.rename(columns={
    "Happiness Score": "HappinessScore",
    "Happiness Rank": "HappinessRank",
    "Job Satisfaction": "JobSatisfaction"
})

print(df.describe())

# -----------------------------
# 2. VISUALIZATION 1: Top & Bottom 10 countries (bar chart)
# -----------------------------
top10 = df.nsmallest(10, "HappinessRank")[["Country", "HappinessScore"]]
bottom10 = df.nlargest(10, "HappinessRank")[["Country", "HappinessScore"]]

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
sns.barplot(data=top10, y="Country", x="HappinessScore", ax=axes[0], palette="Greens_r")
axes[0].set_title("Top 10 Happiest Countries")
axes[0].set_xlabel("Happiness Score")
sns.barplot(data=bottom10, y="Country", x="HappinessScore", ax=axes[1], palette="Reds")
axes[1].set_title("Bottom 10 Happiest Countries")
axes[1].set_xlabel("Happiness Score")
plt.tight_layout()
plt.savefig("viz1_top_bottom10.png")
plt.close()

# -----------------------------
# 3. VISUALIZATION 2: Regional comparison (boxplot)
# -----------------------------
region_order = df.groupby("Region")["HappinessScore"].median().sort_values(ascending=False).index
plt.figure(figsize=(10, 7))
sns.boxplot(data=df, y="Region", x="HappinessScore", order=region_order, palette="viridis")
plt.title("Happiness Score Distribution by Region")
plt.xlabel("Happiness Score")
plt.ylabel("")
plt.tight_layout()
plt.savefig("viz2_region_boxplot.png")
plt.close()

# -----------------------------
# 4. VISUALIZATION 3: GDP vs Happiness scatter, sized by health, colored by region
# -----------------------------
plt.figure(figsize=(9, 6.5))
scatter = sns.scatterplot(
    data=df, x="Economy", y="HappinessScore", hue="Region", size="Health",
    sizes=(20, 200), alpha=0.75, legend=False
)
plt.title("GDP per Capita vs. Happiness Score\n(bubble size = life expectancy contribution)")
plt.xlabel("Economy (GDP per Capita, normalized)")
plt.ylabel("Happiness Score")
plt.tight_layout()
plt.savefig("viz3_gdp_vs_happiness.png")
plt.close()

# -----------------------------
# 5. VISUALIZATION 4: Correlation heatmap of happiness factors
# -----------------------------
factor_cols = ["HappinessScore", "Economy", "Family", "Health", "Freedom", "Generosity", "Corruption", "JobSatisfaction"]
plt.figure(figsize=(8, 6.5))
sns.heatmap(df[factor_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f", center=0)
plt.title("Correlation Between Happiness and Contributing Factors")
plt.tight_layout()
plt.savefig("viz4_correlation_heatmap.png")
plt.close()

# -----------------------------
# 6. VISUALIZATION 5: Regional average happiness - ranked dot/lollipop chart
# -----------------------------
region_avg = df.groupby("Region")["HappinessScore"].mean().sort_values()
plt.figure(figsize=(9, 7))
plt.hlines(y=region_avg.index, xmin=0, xmax=region_avg.values, color="#888888", linewidth=1.5)
plt.plot(region_avg.values, region_avg.index, "o", markersize=10, color="#2E86AB")
plt.xlabel("Average Happiness Score")
plt.title("Average Happiness Score by World Region")
plt.xlim(0, 8)
for i, (region, val) in enumerate(region_avg.items()):
    plt.text(val + 0.15, i, f"{val:.2f}", va="center", fontsize=9)
plt.tight_layout()
plt.savefig("viz5_region_lollipop.png")
plt.close()

# -----------------------------
# 7. VISUALIZATION 6 (bonus): Factor contribution stacked bar for top 10
# -----------------------------
top10_full = df.nsmallest(10, "HappinessRank")[["Country", "Economy", "Family", "Health", "Freedom", "Generosity", "Corruption"]]
top10_full = top10_full.set_index("Country")
plt.figure(figsize=(10, 6))
top10_full.plot(kind="barh", stacked=True, ax=plt.gca(), colormap="tab20c")
plt.title("Decomposing Happiness: Factor Contributions in Top 10 Countries")
plt.xlabel("Contribution to Happiness Score")
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig("viz6_factor_breakdown.png")
plt.close()

# -----------------------------
# 8. KEY STATS FOR NARRATIVE
# -----------------------------
corr_gdp = df["Economy"].corr(df["HappinessScore"])
corr_family = df["Family"].corr(df["HappinessScore"])
corr_health = df["Health"].corr(df["HappinessScore"])
corr_freedom = df["Freedom"].corr(df["HappinessScore"])
corr_generosity = df["Generosity"].corr(df["HappinessScore"])
corr_corruption = df["Corruption"].corr(df["HappinessScore"])

region_means = df.groupby("Region")["HappinessScore"].mean().sort_values(ascending=False)

print("\n--- CORRELATIONS WITH HAPPINESS ---")
print("GDP:", round(corr_gdp, 3))
print("Family/Social support:", round(corr_family, 3))
print("Health:", round(corr_health, 3))
print("Freedom:", round(corr_freedom, 3))
print("Generosity:", round(corr_generosity, 3))
print("Corruption perception:", round(corr_corruption, 3))
print("\n--- REGION MEANS ---")
print(region_means)
print("\nTop 10:\n", top10)
print("\nBottom 10:\n", bottom10)
