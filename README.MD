# World Happiness Report Dashboard

An interactive Dash web application that visualizes and analyzes the World Happiness Report data. The app allows users to explore happiness scores across different countries and years using dynamic graphs and filters.

## 📸 Screenshots
*(Add screenshots or a GIF showcasing your app here)*

## ✨ Features
- **Interactive visualizations**: Explore happiness scores through dynamic charts and graphs.
- **Filters & Selections**: Select countries, regions, years, or specific factors to analyze trends.
- **Comparisons**: Compare different countries based on happiness indicators.
- **Data Insights**: Get key statistics and rankings directly from the dataset.

## 📊 Dataset
The app uses the **World Happiness Report**, a dataset that measures global happiness based on factors such as GDP per capita, social support, life expectancy, freedom, generosity, and corruption perception.

- **Source**: [World Happiness Report](https://worldhappiness.report/)
- **Columns Include**:
  - Country
  - Year
  - Happiness Score
  - GDP per Capita
  - Social Support
  - Life Expectancy
  - Freedom to Make Life Choices
  - Generosity
  - Perceptions of Corruption

## 🚀 Installation & Usage
### **1. Clone the repository**
```bash
git clone https://github.com/MrIsCM/World-Happiness-Report.git
```

### **2. Create a virtual environment and activate it (optional but recommended)**
```bash
conda create --name WHR_Dashboard
conda activate WRH_Dashboard
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Dash app**
```bash
python app.py
```
Then, open your browser and go to `http://127.0.0.1:8050/` to access the dashboard.

## 📂 Project Structure
```
world-happiness-dash/
│-- app.py             # Main application file
|-- color_themes.py    # Aux functions file
│-- Data/              # Folder for dataset (xlsx file)
│-- Images/            # Folder for the images
│-- requirements.txt   # Dependencies
│-- README.md          # Project documentation
```

## 🛠 Technologies Used
- **Dash** for building the interactive web app.
- **Plotly** for visualizations.
- **Pandas** for data manipulation.
- **Python** as the main programming language.

## 🔮 Future Improvements
- Host the app online for public access.
- Automate data extraction

## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository, create a new branch, and submit a pull request.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🚀 **Enjoy exploring happiness trends worldwide!**


