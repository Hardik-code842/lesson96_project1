import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error,mean_squared_log_error

def prediction(cars_df,carwidth,enginesize,horspower,drivewheel_fwtd,car_company_buick):
	x = cars_df.iloc[:,:-1]
	y = cars_df["price"]

	x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.33,random_state=42)

	lr = LinearRegression()
	lr.fit(x_train,y_train)
	score = lr.score(x_train,y_train)
	price = lr.predict([[carwidth,enginesize,horspower,drivewheel_fwtd,car_company_buick]])

	price=price[0]

	y_test_predict = lr.predict(x_test)

	test_r2_score = r2_score(y_test,y_test_predict)
	test_mse = mean_squared_error(y_test,y_test_predict)
	test_mae = mean_absolute_error(y_test,y_test_predict)
	test_msle = mean_squared_log_error(y_test,y_test_predict)

	return price,score,test_r2_score,test_mse,test_mae,test_msle

def app(cars_df):
	st.subheader("Select Values")
	carwidth = st.slider("carwidth",float(cars_df["carwidth"].min()),float(cars_df["carwidth"].max()))
	enginesize = st.slider("enginesize",float(cars_df["enginesize"].min()),float(cars_df["enginesize"].max()))
	horspower = st.slider("horspower",float(cars_df["horsepower"].min()),float(cars_df["horsepower"].max()))
	car_company_buick = st.slider("car_company_buick",float(cars_df["car_company_buick"].min()),float(cars_df["car_company_buick"].max()))

	drivewheel_fwtd = st.radio("is this a forward wheel drive car",("Yes","No"))
	if drivewheel_fwtd == "No":
		drivewheel_fwtd=0
	else:
		drivewheel_fwtd=1

	if st.button("predict"):
		st.subheader("Prediction")
		price,score,test_r2_score,test_mse,test_mae,test_msle = prediction(cars_df,carwidth,enginesize,horspower,drivewheel_fwtd,car_company_buick)

		st.success(f"The predicted Price of car is {price}")
		st.info(f"Accuracy of this model is {score}")
		st.info(f"R2 score of this model is {test_r2_score}")
		st.info(f"Mean Squared error of this model is {test_mse}")
		st.info(f"Mean Absolute error of this model is {test_mae}")
		st.info(f"Mean Squared Log error of this model is {test_msle}")
