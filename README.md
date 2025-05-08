Restaurant Recommendation System 🍽️
Author: Yashwanthkumar Rachamadugu

### **GitHub Repository:** [Restaurant\_Recommendation](https://github.com/YashwanthkumarRachamadugu/Restaurant_Recommendation)

---

## **Project Objective**

The objective of this project is to design and develop a **restaurant recommendation system** that provides personalized restaurant suggestions based on user-defined preferences such as cuisine type, price range, and user rating. The system leverages **content-based filtering techniques** to identify and recommend restaurants that closely align with the user's inputs.

---

## **System Implementation Overview**

### **1. Data Preprocessing**

* **Missing Value Handling**: All missing entries are addressed using `fillna('Unknown')` to ensure data completeness and consistency.
* **Categorical Encoding**: Categorical features (e.g., cuisine, location) are encoded into numerical formats to enable processing by machine learning algorithms.

### **2. Recommendation Criteria Definition**

Recommendations are generated based on the following user-defined parameters:

* **Cuisine Type** (e.g., Italian, Indian, Chinese)
* **Price Range** (minimum and maximum cost per meal)
* **Aggregate Rating** (minimum acceptable rating)

### **3. Content-Based Filtering Methodology**

* **Text Vectorization**: Cuisine-related textual data is converted into numerical representations using **TF-IDF vectorization**.
* **Feature Normalization**: Numerical attributes such as price and ratings are normalized using **MinMaxScaler** to ensure scale consistency.
* **Similarity Computation**: **Cosine similarity** is employed to measure the closeness between user preferences and restaurant profiles.
* **Recommendation Output**: The top five restaurants with the highest similarity scores are presented as personalized recommendations.

### **4. Model Evaluation and Testing**

* **User Scenarios**: Sample user inputs are tested to evaluate the system’s recommendation accuracy.
* **Performance Validation**: Various cuisine and budget combinations are used to assess the quality and relevance of suggestions.

---

## **Technology Stack**

| Technology       | Purpose                                        |
| ---------------- | ---------------------------------------------- |
| **Python**       | Core programming and scripting                 |
| **Pandas**       | Data manipulation and preprocessing            |
| **Scikit-learn** | Feature engineering and similarity computation |
| **NumPy**        | Numerical operations and array handling        |
| **Streamlit**    | Interactive front-end web application          |


---
## **Deployment Instructions**

### **1. Required Files**
Ensure the following files are present in the project directory:

* `app.py`: Main script to run the application
* `Dataset.csv`: Dataset containing restaurant information

### **2. File Path Configuration**

Update the dataset path in `app.py` as follows:

```python
file_path = "Dataset.csv"
df = pd.read_csv(file_path)
```

### **3. Environment Setup**

Install the necessary Python libraries using the following command:

```bash
pip install streamlit pandas scikit-learn numpy
```

### **4. Application Execution**

Launch the application with the command:

```bash
streamlit run app.py
```

This will open a browser-based interface where users can specify their preferences to receive real-time restaurant recommendations.
---

## **Proposed Future Enhancements**
* Integration of **deep learning models** to improve recommendation accuracy and context awareness
* Implementation of **collaborative filtering** for enhanced personalization based on user behavior
* Inclusion of **interactive data visualizations** to compare restaurant attributes and recommendations
* Refinement of the **user interface** to improve accessibility, responsiveness, and aesthetics
---

## **Conclusion**
This project demonstrates a practical application of machine learning techniques in the domain of personalized recommendations. By incorporating user preferences and employing robust content-based filtering methods, the system effectively delivers relevant restaurant suggestions, providing a solid foundation for future scalability and enhancement.
---
