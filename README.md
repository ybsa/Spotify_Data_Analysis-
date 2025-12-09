# 🎵 Spotify Data Analysis

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![License](https://img.shields.io/badge/License-Apache%202.0-red)

A comprehensive data analysis project exploring trends in Spotify track data, including release patterns, popularity distribution, track duration evolution, and explicit content analysis.

---

## 📊 Key Findings

| Metric | Value |
|--------|-------|
| **Total Tracks Analyzed** | 7,800+ |
| **Unique Artists** | 4,000+ |
| **Year Range** | 1957 - 2024 |
| **Avg Popularity Score** | ~35/100 |

### Highlights

- 📈 **Release Trends**: Significant increase in track releases in recent years
- ⏱️ **Duration Shifts**: Modern tracks tend to be shorter than older ones
- 🔞 **Explicit Content**: Clear upward trend in explicit content percentage
- 🎤 **Artist Concentration**: A small group of artists dominate track output

---

## 🗂️ Project Structure

```
📁 Spotify_Data_Analysis/
├── 📁 Data/                    # Processed data files
├── 📁 Raw_Data/                # Original source CSV files
├── 📁 Report/
│   └── 📄 Spotify_Findings_Report.pdf   # Final analysis report
├── 📓 Spotify_Analysis.ipynb   # Main analysis notebook
├── 🐍 etl_pipeline.py          # ETL data processing script
├── 📋 requirements.txt         # Python dependencies
├── 📄 LICENSE
└── 📄 README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Jupyter Notebook / JupyterLab

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Spotify_Data_Analysis.git
   cd Spotify_Data_Analysis
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the ETL pipeline** (if starting from raw data)

   ```bash
   python etl_pipeline.py
   ```

4. **Open and run the analysis notebook**

   ```bash
   jupyter notebook Spotify_Analysis.ipynb
   ```

---

## 📈 Analysis Overview

The analysis covers:

1. **Release Trends Over Time**
   - Track count by year
   - Peak release years identification

2. **Popularity Distribution**
   - Score distribution analysis
   - Mean and variance metrics

3. **Track Duration Trends**
   - Average duration by year
   - Temporal evolution analysis

4. **Explicit Content Analysis**
   - Yearly explicit content percentage
   - Trend identification

5. **Top Artists Analysis**
   - Most prolific artists
   - Track count rankings

---

## 📄 Output Report

The final PDF report is generated automatically and saved to:

```
Report/Spotify_Findings_Report.pdf
```

---

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib & Seaborn** - Data visualization
- **SQLite** - Data storage during ETL
- **Jupyter Notebook** - Interactive analysis environment

---

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

<p align="center">
  Made with ❤️ and 🎵
</p>
