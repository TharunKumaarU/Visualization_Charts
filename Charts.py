import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = '/content/Visualizing Charts.xlsx'
df = pd.read_excel(file_path)

# 1. Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['Population'], color='skyblue')
plt.title('Population of Each Country')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.show()

# 2. Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(df['GDP (Billion USD)'], labels=df['Country'], autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Proportion of GDP by Country')
plt.show()

# 3. Scatter Plot 
plt.figure(figsize=(8, 6))
plt.scatter(df['Life Expectancy'], df['CO2 Emissions (Million tons)'], color='purple', s=100)
plt.title('Life Expectancy vs. CO2 Emissions')
plt.xlabel('Life Expectancy')
plt.ylabel('CO2 Emissions (Million tons)')
plt.show()

# 4. Heatmap
plt.figure(figsize=(10, 8))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of the Dataset')
plt.show()

# 5. Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Country', y='Internet Users (%)', data=df)
plt.title('Distribution of Internet Users Across Countries')
plt.xticks(rotation=45)
plt.show()

# 6. Line Chart
plt.figure(figsize=(10, 6))
plt.plot(df['Country'], df['GDP (Billion USD)'], marker='o', color='green')
plt.title('GDP of Each Country')
plt.xlabel('Country')
plt.ylabel('GDP (Billion USD)')
plt.xticks(rotation=45)
plt.show()

# 7. Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Life Expectancy'], bins=10, color='orange', edgecolor='black')
plt.title('Distribution of Life Expectancy')
plt.xlabel('Life Expectancy')
plt.ylabel('Frequency')
plt.show()

# 8. Area Chart
df['Cumulative GDP'] = df['GDP (Billion USD)'].cumsum()
plt.figure(figsize=(10, 6))
plt.fill_between(df['Country'], df['Cumulative GDP'], color='lightblue', alpha=0.7)
plt.title('Cumulative GDP of Each Country')
plt.xlabel('Country')
plt.ylabel('Cumulative GDP (Billion USD)')
plt.xticks(rotation=45)
plt.show()

# 9. Bubble Chart
plt.figure(figsize=(10, 6))
plt.scatter(df['Population'], df['GDP (Billion USD)'], s=df['CO2 Emissions (Million tons)'] / 10, alpha=0.5, color='blue')
plt.title('Population vs. GDP with CO2 Emissions as Bubble Size')
plt.xlabel('Population')
plt.ylabel('GDP (Billion USD)')
plt.show()

# 10. Tree Map
plt.figure(figsize=(10, 6))
squarify.plot(sizes=df['Forest Area (%)'], label=df['Country'], alpha=0.8)
plt.title('Forest Area as Proportion of Total Area by Country')
plt.show()
