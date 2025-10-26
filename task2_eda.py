# TASK 2: EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking charts
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("=" * 60)
print("TASK 2: EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ============================================
# STEP 1: LOAD AND EXPLORE DATA
# ============================================

print("\n📊 Loading dataset...")
df = pd.read_csv("netflix_titles.csv")

print(f"\n✅ Dataset loaded successfully!")
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

print("First 5 rows of data:")
print(df.head())

print("\n" + "=" * 60)
print("DATA INFORMATION")
print("=" * 60)
print("\nColumn names and types:")
print(df.dtypes)

print("\nMissing values:")
missing = df.isnull().sum()
print(missing[missing > 0])

# ============================================
# STEP 2: CLEAN THE DATA
# ============================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

print(f"\nDuplicates: {df.duplicated().sum()}")
df = df.drop_duplicates()

df = df.dropna()
print(f"✅ Data cleaned! New shape: {df.shape}")

# ============================================
# STEP 3: STATISTICAL ANALYSIS
# ============================================

print("\n" + "=" * 60)
print("STATISTICAL SUMMARY")
print("=" * 60)

print("\nNumeric columns statistics:")
print(df.describe())

# ============================================
# STEP 4: CREATE VISUALIZATIONS
# ============================================

print("\n" + "=" * 60)
print("CREATING VISUALIZATIONS")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Netflix Data Analysis Dashboard', fontsize=16, fontweight='bold')

# Chart 1: Release Year Distribution
axes[0, 0].hist(df['release_year'], bins=30, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribution of Release Year', fontweight='bold')
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Count')

# Chart 2: Content Type
df['type'].value_counts().plot(kind='bar', ax=axes[0, 1], color=['#FF6B6B', '#4ECDC4'])
axes[0, 1].set_title('Content Type Distribution', fontweight='bold')
axes[0, 1].set_xlabel('Type')
axes[0, 1].set_ylabel('Count')
axes[0, 1].tick_params(axis='x', rotation=45)

# Chart 3: Box Plot
axes[1, 0].boxplot(df['release_year'])
axes[1, 0].set_title('Release Year - Box Plot', fontweight='bold')
axes[1, 0].set_ylabel('Year')

# Chart 4: Heatmap
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=axes[1, 1])
axes[1, 1].set_title('Correlation Heatmap', fontweight='bold')

plt.tight_layout()
plt.savefig('eda_dashboard.png', dpi=300, bbox_inches='tight')
print("✅ Saved: eda_dashboard.png")
plt.show()

# ============================================
# STEP 5: KEY FINDINGS
# ============================================

print("\n" + "=" * 60)
print("KEY FINDINGS")
print("=" * 60)

print(f"\n1️⃣  Most common type: {df['type'].value_counts().index[0]}")
print(f"2️⃣  Year range: {df['release_year'].min()} - {df['release_year'].max()}")
print(f"3️⃣  Total titles analyzed: {len(df)}")

print("\n" + "=" * 60)
print("✅ TASK 2 COMPLETE!")
print("=" * 60)
