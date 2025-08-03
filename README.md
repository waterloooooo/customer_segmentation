# 🛍️ Customer Segmentation with K-Means Clustering

This project uses K-Means clustering to segment customers based on their purchasing behavior using the **Mall Customers** dataset. We focus on two key features: **Annual Income** and **Spending Score**, to identify distinct customer groups that businesses can target more effectively.

---

## 📁 Project Structure

```

customer\_segmentation\_kmeans/
├── customer\_segmentation.ipynb     # Jupyter Notebook with full analysis
├── customer\_segmentation.py        # (Optional) Script version of the notebook
├── Mall\_Customers.csv              # Customer dataset

````

---

## 📊 Dataset

- **Source**: [Kaggle – Mall Customers Dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)
- **Columns Used**:
  - `Annual Income (k$)`
  - `Spending Score (1-100)`

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/customer_segmentation_kmeans.git
cd customer_segmentation_kmeans
````

### 2. Install dependencies

```bash
pip install pandas scikit-learn matplotlib seaborn
```

### 3. Run the notebook

```bash
jupyter notebook customer_segmentation.ipynb
```

---

## 🤖 What It Does

* Loads and inspects customer data
* Scales features using `StandardScaler`
* Applies **K-Means clustering** to group customers
* Visualizes the clusters
* Summarizes cluster characteristics using group averages

---

## 📈 Example Insights

Clusters might look like this:

| Cluster | Income Level | Spending Score | Possible Label       |
| ------- | ------------ | -------------- | -------------------- |
| 0       | High         | High           | Valuable customers   |
| 1       | High         | Low            | Wealthy but inactive |
| 2       | Low          | High           | Impulse buyers       |
| 3       | Low          | Low            | Low-value customers  |
| 4       | Mid          | Moderate       | Average consumers    |

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙋 Contributions

Pull requests are welcome! Feel free to fork the repo, add new features or improvements (e.g. elbow method, 3D clustering), and submit a PR.

```

---

Let me know if you'd like me to tailor this for the `.py` version or expand with extras like elbow method, PCA, or cluster profiling.
```
