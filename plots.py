import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def app(cars_df):
	st.header("Visualise Data")
	st.set_option("deprecation.showPyplotGlobalUse",False)
	st.subheader("Scatter Plots")
	feature_lst = st.multiselect("Select the x-axis Value",("carwidth","enginesize","horsepower","drivewheel_fwtd","car_company_buick"))

	for i in feature_lst:
		st.subheader(f"Scatter Plot between {i} and Price")
		plt.figure(figsize=(16,5))
		sns.scatterplot(cars_df[i],cars_df["price"])
		st.pyplot()

	st.subheader("Visualisation selector")
	plot_type = st.multiselect("Select Plot Type",("Histogram","Boxplot","Heatmap"))
	col = st.selectbox("select the column",("carwidth","enginesize","horsepower","drivewheel_fwtd","car_company_buick"))

	if "Histogram" in plot_type:
		st.subheader("Histogram")
		plt.figure(figsize=(16,5))
		plt.title(f"Histogram of {col}")
		plt.hist(cars_df[col],bins="sturges",edgecolor="green")
		st.pyplot()

	if "Boxplot" in plot_type:
		st.subheader("Boxplot")
		plt.figure(figsize=(16,5))
		plt.title(f"Boxplot of {col}")
		sns.boxplot(cars_df[col])
		st.pyplot()

	if "Heatmap" in plot_type:
		st.subheader("Heatmap")
		plt.figure(figsize=(16,5))
		plt.title(f"Heatmap for Dataset ")
		sns.heatmap(cars_df.corr(),annot=True)
		st.pyplot()

