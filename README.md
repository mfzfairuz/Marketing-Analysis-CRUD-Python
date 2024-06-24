# Marketing-Analytics-CRUD-Python
This Python-based tool is designed to help marketing teams gather, organize, and analyze data from Facebook Ad campaigns.

# Facebook Ads Marketing Analysis Tool

## Overview

This Python-based tool is designed to help marketing teams gather, organize, and analyze data from Facebook Ad campaigns. It provides a simple command-line interface to:

- **Create (C):**  Add new campaign data.
- **Read (R):** View and filter campaign data.
- **Update (U):** Modify existing campaign metrics.
- **Delete (D):** Remove campaigns.
- **Calculate KPIs:** Compute key performance indicators (CTR, CPC, ROAS) and provide recommendations.

## Features

- **User-Friendly Menu:** Easy navigation for creating, viewing, updating, and deleting campaign data.
- **Data Storage:** Stores campaign data in a list of dictionaries for organized access.
- **Tabular Data Display:** Presents campaign data in a clean, readable table format using the `tabulate` library.
- **KPI Calculation:** Calculates Click-Through Rate (CTR), Cost Per Click (CPC), Return on Ad Spend (ROAS), and Conversion Rate (CVR).
- **Performance Recommendations:** Offers actionable insights based on the calculated KPIs to improve campaign performance.
- **Error Handling:** Includes basic error handling to prevent crashes from invalid input.

## Installation and Usage

1. **Prerequisites:**
   - Ensure you have Python installed on your system.
   - Install the `tabulate` library:
     ```bash
     pip install tabulate
     ```

2. **Running the Script:**
   - Save the code in a file named `marketing_analysis.py`.
   - Open your terminal or command prompt.
   - Navigate to the directory where you saved the file.
   - Run the command:

     ```bash
     python marketing_analysis.py
     ```

3. **Using the Menu:**
   - Follow the on-screen instructions to create, view, update, or delete campaign data.
   - Choose the option to calculate KPIs to get insights and recommendations.

## Sample Data Input

When creating a campaign, you'll be prompted to enter:

- Ad Set ID
- Amount Spent
- Reach
- Total Clicks
- Landing Page Views
- Total Conversions
- Conversion Value

## Contributing

Contributions are welcome! If you'd like to enhance the tool or fix any issues, please fork the repository and submit a pull request.
