# AI-Based-Crop-Recommendation-System
The Crop Recommendation System is a machine learning-based application that provides recommendations for suitable crops based on various environmental and soil conditions. It aims to assist farmers and agricultural professionals in making informed decisions about crop selection, optimizing yields, and maximizing profitability.

# 1.Introduction
  Agriculture plays a vital role in the Indian economy, but many farmers face reduced productivity because they rely on traditional knowledge rather than data-driven decisions for selecting crops. An AI-based crop recommendation system helps in suggesting the most suitable crop by analyzing soil nutrients, environmental conditions, and rainfall data.

  This project leverages machine learning models to recommend the best crop for a given farmland, ensuring higher yield, better resource utilization, and improved income for farmers.

# 2.Problem Statement
● Farmers struggle to decide the most profitable and suitable crop for their land.

● Manual decisions may lead to reduced yield, soil degradation, and financial loss.

● Need for a data-driven intelligent system that suggests crops based on soil and climate conditions.

# 3.Objectives
● To build a predictive model that recommends crops using soil & weather data.

● To compare multiple ML models (Logistic Regression, Naïve Bayes, Random Forest).

● To finalize the best-performing model (Random Forest).

● To provide an easy-to-use system (web/mobile app) for farmers.

# 4.Dataset Description 
# Dataset Used: crop_recommendation.csv

Features (Inputs):

N: Nitrogen content in soil
P: Phosphorus content in soil
K: Potassium content in soil

Temperature (°C)

Humidity (%)

pH level

Rainfall (mm)

Target (Output): Crop label (22 crop types such as rice, wheat, maize, mango, coffee, etc.)

# 5.Exploratory Data Analysis (EDA)
  The Exploratory Data Analysis (EDA) of the crop recommendation dataset revealed that most soil samples had pH levels between 5.5 and 7.5, making them suitable for a wide range of crops. Rainfall and humidity showed a positive correlation, while nutrients (N, P, K) were fairly independent of each other, which helps in crop classification. Countplots confirmed that the dataset is balanced across different crops. Boxplots highlighted that rice requires high rainfall and humidity, while pulses like lentils grow in low-rainfall and low-nitrogen conditions. Overall, EDA confirmed that soil nutrients and climate features strongly influence crop suitability, validating the dataset for building predictive models.

# 6.Methodology
  The methodology of this project involves several key steps. First, the crop recommendation dataset is preprocessed by checking for missing values, normalizing features where required, and splitting the data into training and testing sets. Next, different machine learning algorithms such as Logistic Regression, Naïve Bayes, and Random Forest are applied to build predictive models. The models are evaluated using accuracy, F1-score, and confusion matrix to compare their performance. Among these, Random Forest achieved the best accuracy and robustness in handling non-linear feature interactions, making it the final model for deployment. Finally, the trained model is integrated into a user-friendly system where soil and climate inputs are processed to recommend the most suitable crops.

# 7.Results
Logistic Regression → ~94% accuracy

Support Vector Machine → ~98% accuracy

Random Forest → ~99% accuracy (final model)

Random Forest handled non-linear feature interactions and performed consistently across crops.
