# Player Prop Pricing + Backtest

🏀 NBA Odds Data Pipeline & Analysis

This project builds a data pipeline and analytics framework for NBA betting markets, designed to transform raw sportsbook data into structured insights. Using The Odds API, it ingests live odds (head-to-head matchups, player props, and other markets), processes the data into clean, comparable formats, and runs analyses to uncover differences across sportsbooks.

The core goals are:

▫️Data Ingestion: Automating the collection of NBA odds data across multiple bookmakers.

▫️Data Engineering: Parsing and flattening complex JSON responses into structured datasets ready for analysis.

▫️Market Analysis: Identifying line discrepancies and opportunities, such as where one sportsbook offers significantly better odds than another.

▫️Future Expansion: Laying the foundation for predictive modeling of player performance and expected line values.

🎯 Real-World Applications

▫️For Bettors & Analysts: Quickly compare odds across DraftKings, FanDuel, and others to “shop” for the best line or detect arbitrage opportunities.

▫️For Sportsbooks: Benchmark pricing against competitors, spot inefficiencies in real time, and strengthen risk management.

▫️For Data Science: Build predictive models of player props (points, rebounds, assists) and simulate game outcomes against market lines.

💡 Why It Matters

Sports betting markets move fast and are highly competitive. By developing this system, I’ve shown the ability to:

-Engineer robust pipelines that handle external APIs and messy, real-world data.

-Apply statistical and analytical reasoning to complex market structures.

-Translate raw data into actionable insights, the same way sportsbooks must constantly monitor competitors and adjust pricing.

In short, this project demonstrates end-to-end skills in data engineering, sports analytics, and applied problem solving — the very skills that power real-world sportsbook operations.

🔑 Quick Start (run the demo)
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. How to run:
     notebooks/player_prop_demo.ipynb in Jupyter and Run → Run All Cells,
   Or run headlessly:
     jupyter nbconvert --ExecutePreprocessor.timeout=600 --to notebook --execute notebooks/player_prop_demo.ipynb --output notebooks/player_prop_demo.ran.ipynb
