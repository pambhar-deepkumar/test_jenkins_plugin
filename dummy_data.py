import pandas as pd
import plotly.express as px

# Sample data
df = pd.DataFrame({
    "Build Number": [1, 2, 3, 4, 5],
    "Build Time (min)": [10, 15, 14, 20, 12]
})

# Generate a line chart
fig = px.line(df, x="Build Number", y="Build Time (min)", title="Build Time Trend")

# Save the figure as an HTML file
fig.write_html("build_time_report.html")
