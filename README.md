# **Classification-Model-for-Predicting-Someone's-Income-Category**

### **Dataset Information:**
This dataset contains information related to the income census of the population.

### **Background:**
We are provided with a dataset containing income census data. The information available in this dataset is diverse, including age, occupation class, final weight data, education level, marital status, occupation, relationship status, race, gender, capital gain and loss, hours worked per week, and income label (<=50K, >50K).

### **Problems:**
Create a classification model to predict whether the income is above $50K/year and explore the characteristics of individuals with income above $50K/year.

### **Objective:**
The project is created to `build a classification prediction model` to predict `whether someone's income is above or below $50K/year`. We will also explore the characteristics of individuals earning more than $50K per year. The models to be tried include `KNN, SVM, Decision Tree, Random Forest`. In the process, we will attempt to implement `Pipelines, Cross Validation, Hyperparameter Tuning, and Boosting`. The final predetermined model will then be `deployed with Streamlit on HuggingFace`.

### **Tools:**
- **Data Retrieval:** `ucimlrepo` (custom module for fetching UCI repository data)
- **Data Manipulation:** Python, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Feature Engineering:** Phik, Variance Inflation Factor (VIF), Winsorizer
- **Sampling:** SMOTENC (Synthetic Minority Over-sampling Technique for Nominal and Continuous features)
- **Column Transformation:** make_column_transformer
- **Preprocessing:** LabelEncoder, StandardScaler, OneHotEncoder, OrdinalEncoder
- **Pipeline:** make_pipeline
- **Machine Learning Models:** KNeighborsClassifier, SVC (Support Vector Classifier), DecisionTreeClassifier, RandomForestClassifier, AdaBoostClassifier, XGBClassifier
- **Model Evaluation:** Classification Report, ConfusionMatrixDisplay, f1_score, precision_score, recall_score
- **Cross-Validation:** cross_val_score
- **Hyperparameter Tuning:** RandomizedSearchCV
- **Persistence:** pickle
- **Other Libraries:** numpy, phik, statsmodels, imblearn
