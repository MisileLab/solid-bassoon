from preswald import connect, get_df, query, table, text, plotly, sidebar
import plotly.express as px

connect()  # Initialize connection to preswald.toml data sources
sidebar()
df = get_df("used_car").sort_values(by='make_year', ascending=True)  # Load data

sql = "SELECT * FROM used_car WHERE fuel_type = 'Diesel'"
filtered_df = query(sql, "used_car")

text("# My Data Analysis App")
table(filtered_df, title="Diesel (Sorted by Price)")

# Create a line plot
line_fig = px.line(
    df, 
    x="make_year",
    y="price_usd",
    color="brand",
    hover_data=["mileage_kmpl", "brand", "price_usd", "make_year"],
    title="Price vs Make Year"
)

# Display the line plot
plotly(line_fig)
