import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="👥",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("👥 Customer Segmentation & Analytics")
st.write(
    "Analyze customer demographics and purchasing behavior "
    "using K-Means clustering."
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("customer_data.csv")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("⚙️ Segmentation Settings")

num_clusters = st.sidebar.slider(
    "Number of Customer Segments",
    min_value=2,
    max_value=6,
    value=4
)

# -----------------------------
# Key Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Customers", len(df))

with col2:
    st.metric(
        "💰 Avg. Income",
        f"₹{df['AnnualIncome'].mean():,.0f}"
    )

with col3:
    st.metric(
        "🛍️ Avg. Spending Score",
        f"{df['SpendingScore'].mean():.1f}"
    )

with col4:
    st.metric(
        "🛒 Avg. Purchases",
        f"{df['PurchaseFrequency'].mean():.1f}"
    )

st.divider()

# -----------------------------
# Prepare Data for Clustering
# -----------------------------
features = [
    "Age",
    "AnnualIncome",
    "SpendingScore",
    "PurchaseFrequency"
]

X = df[features]

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# K-Means Clustering
# -----------------------------
kmeans = KMeans(
    n_clusters=num_clusters,
    random_state=42,
    n_init=10
)

df["Segment"] = kmeans.fit_predict(X_scaled)

# Make segment names easier to understand
segment_names = {}

segment_summary = df.groupby("Segment").agg(
    Average_Age=("Age", "mean"),
    Average_Income=("AnnualIncome", "mean"),
    Average_Spending=("SpendingScore", "mean"),
    Average_Purchases=("PurchaseFrequency", "mean"),
    Customers=("CustomerID", "count")
).reset_index()

# Assign descriptive names based on spending/income
for _, row in segment_summary.iterrows():

    segment = int(row["Segment"])

    if row["Average_Spending"] >= 70:
        name = "High Spenders"
    elif row["Average_Spending"] <= 35:
        name = "Low Spenders"
    elif row["Average_Income"] >= 60000:
        name = "High Income - Moderate Spenders"
    else:
        name = "Regular Customers"

    segment_names[segment] = name

df["Segment Name"] = df["Segment"].map(segment_names)

# -----------------------------
# Customer Segments
# -----------------------------
st.header("🎯 Customer Segments")

segment_counts = (
    df["Segment Name"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = ["Segment", "Customers"]

fig_segment = px.bar(
    segment_counts,
    x="Segment",
    y="Customers",
    title="Customers in Each Segment",
    text="Customers"
)

fig_segment.update_layout(
    xaxis_title="Customer Segment",
    yaxis_title="Number of Customers"
)

st.plotly_chart(fig_segment, use_container_width=True)

# -----------------------------
# Customer Visualization
# -----------------------------
st.header("📊 Customer Behavior Analysis")

col1, col2 = st.columns(2)

with col1:

    fig_income = px.scatter(
        df,
        x="AnnualIncome",
        y="SpendingScore",
        color="Segment Name",
        hover_data=[
            "CustomerID",
            "Age",
            "PurchaseFrequency"
        ],
        title="Income vs Spending Score"
    )

    st.plotly_chart(
        fig_income,
        use_container_width=True
    )

with col2:

    fig_age = px.scatter(
        df,
        x="Age",
        y="SpendingScore",
        color="Segment Name",
        hover_data=[
            "CustomerID",
            "AnnualIncome",
            "PurchaseFrequency"
        ],
        title="Age vs Spending Score"
    )

    st.plotly_chart(
        fig_age,
        use_container_width=True
    )

# -----------------------------
# Purchase Frequency
# -----------------------------
st.header("🛒 Purchase Behavior")

fig_frequency = px.scatter(
    df,
    x="PurchaseFrequency",
    y="AnnualIncome",
    size="SpendingScore",
    color="Segment Name",
    hover_data=["CustomerID", "Age"],
    title="Purchase Frequency vs Annual Income"
)

st.plotly_chart(
    fig_frequency,
    use_container_width=True
)

# -----------------------------
# Segment Summary
# -----------------------------
st.header("📋 Segment Characteristics")

summary = (
    df.groupby("Segment Name")
    .agg(
        Customers=("CustomerID", "count"),
        Avg_Age=("Age", "mean"),
        Avg_Income=("AnnualIncome", "mean"),
        Avg_Spending=("SpendingScore", "mean"),
        Avg_Purchases=("PurchaseFrequency", "mean")
    )
    .reset_index()
)

summary["Avg_Age"] = summary["Avg_Age"].round(1)
summary["Avg_Income"] = summary["Avg_Income"].round(0)
summary["Avg_Spending"] = summary["Avg_Spending"].round(1)
summary["Avg_Purchases"] = summary["Avg_Purchases"].round(1)

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Category Preferences
# -----------------------------
st.header("🛍️ Customer Category Preferences")

category_counts = (
    df["CategoryPreference"]
    .value_counts()
    .reset_index()
)

category_counts.columns = ["Category", "Customers"]

fig_category = px.pie(
    category_counts,
    names="Category",
    values="Customers",
    title="Preferred Product Categories"
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)

# -----------------------------
# Business Insights
# -----------------------------
st.header("💡 Business Insights")

highest_spending = df.groupby(
    "Segment Name"
)["SpendingScore"].mean().idxmax()

highest_income = df.groupby(
    "Segment Name"
)["AnnualIncome"].mean().idxmax()

highest_frequency = df.groupby(
    "Segment Name"
)["PurchaseFrequency"].mean().idxmax()

st.success(
    f"🎯 **Highest spending segment:** {highest_spending}"
)

st.info(
    f"💰 **Highest income segment:** {highest_income}"
)

st.warning(
    f"🛒 **Most frequent purchasers:** {highest_frequency}"
)

st.write(
    "Businesses can use these segments to personalize marketing campaigns, "
    "recommend products, provide targeted offers, and improve customer retention."
)

# -----------------------------
# Customer Data
# -----------------------------
# -----------------------------
# Customer Data & Download
# -----------------------------
st.header("📁 Customer Data")

col1, col2 = st.columns([3, 1])

with col1:
    with st.expander("🔎 View Customer Dataset"):
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

with col2:
    st.write("### 📥 Export")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Segmented Data",
        data=csv_data,
        file_name="customer_segmented_data.csv",
        mime="text/csv"
    )