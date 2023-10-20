import streamlit as st
import pandas as pd

# Define functions for KPI calculation
# most popular category
def popular_cat():
    most_popular_category=list(data['ProductCategory'].mode())
    result = ' & '.join(most_popular_category)
    return result

# monthly revenue growth
def monthly_revenue_growth():
    data['VisitDate'] = pd.to_datetime(data['VisitDate'])
    data.set_index('VisitDate', inplace=True)
    monthly_revenue = data.resample('M')['TotalSpend'].sum()
    revenue_growth = monthly_revenue.pct_change()*100
    df3=pd.DataFrame({'Month':revenue_growth.index, 'Renenue Growth(in %)':revenue_growth.values})
    average_growth=df3['Renenue Growth(in %)'].mean()
    return df3,average_growth


def calculate_kpis(data):
    # Calculate example KPIs
    total_revenue = data['TotalSpend'].sum()
    average_spend = data['TotalSpend'].mean()
    most_popular_category= popular_cat()
    monthly_revenue_growth_= value1
    return total_revenue, average_spend,most_popular_category,monthly_revenue_growth_

def get_optimization_suggestions(avg_spending_per_customer, most_popular_category,avg_revenw_growth):
    suggestions = []

    # Suggestion 1: Target High-Spending Customers
    if avg_spending_per_customer < 1000: 
        suggestions.append("Focus on targeting low-spending customers with personalized marketing campaigns to increase their spending further.")

    # Suggestion 2: Promote Most Popular Product Category
    suggestions.append(f"Capitalize on the popularity of the '{most_popular_category}' product category. Run targeted promotions or campaigns for this category.")

    # Suggestion 3: Improve Monthly Revenue Growth
    if avg_revenw_growth < 10:  # 
        suggestions.append("Aim to increase monthly revenue growth by testing new marketing channels, optimizing your current strategies, or offering special promotions during slow months.")

    # General Suggestion
    suggestions.append("Continuously analyze and segment your customer base to tailor marketing strategies to different customer segments.")

    return suggestions

# Streamlit UI
st.title("Marketing Strategy Optimization Dashboard")

# Upload a CSV file
st.header("Upload a CSV file for analysis")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    result=monthly_revenue_growth()
    value1,value2=result
    
    # Calculate KPIs
    total_rev,avg_spend,m_pop_cat,montly_rev_gro = calculate_kpis(data)

    # Display KPIs
    st.header("Key Performance Indicators (KPIs)")
    st.write(f"Total Revenue:  {total_rev:.2f}")
    st.write(f"Average spend:  {avg_spend:.2f}")
    "Most popular category:" 
    m_pop_cat
    "Monthly Revenue Growth:"
    montly_rev_gro
    

    # data,mean_monthly_revenue_grwoth = monthly_revenue_growth()
    # Get optimization suggestions
    suggestions = get_optimization_suggestions(avg_spend, m_pop_cat,value2)

    # Display optimization suggestions
    st.header("Marketing Optimization Suggestions")
    st.write(suggestions)