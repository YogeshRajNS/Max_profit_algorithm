# 🏗️ Max Profit Calculator - Mars Land Development

A dynamic programming solution visualizer built with Streamlit that solves the **Max Profit Problem** for optimal property development on Mars Land.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Problem Statement

Mr. X owns a large strip of land in Mars Land with infinite land capacity. He can develop the land by building Theatres, Pubs, or Commercial Parks. Each property type has different construction times and generates earnings per time unit once operational.

**Key Constraints:**
- Only one property can be developed at a time (no parallel construction)
- Buildings start earning money immediately after construction completes
- Given `n` time units, determine the optimal mix of properties to maximize total earnings

This application solves this optimization problem using dynamic programming and displays all possible solutions that achieve maximum profit.

## ✨ Features

- **Dynamic Programming Algorithm**: Efficiently calculates optimal building strategies
- **Multiple Solutions**: Finds all possible combinations that achieve maximum profit
- **Interactive UI**: Clean, dark-themed interface with real-time calculations
- **Detailed Results**: Shows all optimal solutions with building breakdowns
- **Responsive Design**: Wide layout optimized for desktop viewing
- **Test Case Validation**: Verified against official problem test cases

## 📜 Problem Rules & Constraints

1. **Infinite Land**: Land capacity is unlimited
2. **Sequential Construction**: Only one property can be developed at a time (no parallel construction)
3. **Immediate Earnings**: Buildings start earning money immediately after construction completes
4. **Time Constraint**: Given `n` time units, maximize total earnings
5. **Earnings Formula**: Each operational building earns money per time unit it's active

## 🏢 Property Types

| Property | Build Time | Capacity | Earning/Unit | Efficiency | Land Required |
|----------|------------|----------|--------------|------------|---------------|
| 🎭 Theatre | 5 units | 8 Auditoriums | $1,500 | $300/time | 2×1 |
| 🍺 Pub | 4 units | 1 Dance Floor | $1,000 | $250/time | 1×1 |
| 🏢 Commercial Park | 10 units | 6 Commercial Spaces | $2,000 | $200/time | 3×1 |

**Note:** Earnings are generated per time unit once the building is operational (after construction completes).

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/YogeshRajNS/Max_profit_algorithm.git
cd Max_profit_algorithm
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install streamlit
```

## 💻 Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Using the Calculator

1. **View Property Details**: The top section displays all three property types with their specifications
2. **Enter Time Units**: Input the total time units available (n) in the left panel
3. **Calculate**: Click "📊 Calculate Maximum Profit" button
4. **View Results**: 
   - See the maximum achievable earnings
   - View number of optimal solutions
   - Examine each solution's property breakdown (T, P, C counts)
   - Check total time units used by each solution

### Output Format

Solutions are displayed in the format:
- **T**: Number of Theatres
- **P**: Number of Pubs  
- **C**: Number of Commercial Parks

Example: `T:2 P:1 C:0` means 2 Theatres, 1 Pub, and 0 Commercial Parks

## 🧮 Algorithm Explanation

The application implements a **dynamic programming** solution to solve this resource allocation optimization problem.

### Algorithm Details

**State Definition:**
- `dp[t]` = maximum profit achievable by using exactly `t` time units for construction

**Recurrence Relation:**
For each time unit `t`, we consider three options:
1. Build a Theatre (takes 5 units)
2. Build a Pub (takes 4 units)  
3. Build a Commercial Park (takes 10 units)

**Profit Calculation:**
```
profit = dp[t - build_time] + (n - t) × earning_per_unit
```

Where:
- `dp[t - build_time]` = profit from previous constructions
- `(n - t)` = remaining operational time after construction completes
- The building earns money for all remaining time units after it's built

**Solution Tracking:**
- Maintains all combinations (T, P, C counts) that achieve the optimal profit
- Allows finding multiple solutions when they exist

### Complexity Analysis
- **Time Complexity**: O(n × 3) = O(n) where n is the total time units
- **Space Complexity**: O(n) for DP array and solution tracking

### Example Walkthrough (n = 7)

```
t=0: dp[0] = 0 (no time used, no profit)
t=4: Build Pub → dp[4] = 0 + (7-4)×1000 = $3,000
t=5: Build Theatre → dp[5] = 0 + (7-5)×1500 = $3,000
...
Maximum: $3,000 (achieved by either 1 Theatre or 1 Pub)
```

## 📁 Project Structure

```
max-profit-calculator/
│
├── max_profit_algorithm.py     # Main Streamlit application
├── README.md           # This file
└── requirements.txt    # Python dependencies (optional)
```

## 🎨 Customization

### Modifying Property Types

Edit the logic in `max_profit_all_solutions()` function:

```python
# Commercial Park (Time: 10, Profit: 2000)
if t >= 10 and dp[t-10] != -1:
    profit = dp[t-10] + (n - t) * 2000
```

### Changing Theme Colors

Modify the CSS in the `st.markdown()` section:

```css
.highlight {
    color: #facc15;  /* Change highlight color */
}
```

## 📊 Example Results & Test Cases

### Test Case 1: n = 7 time units
**Maximum Earnings**: $3,000

**Optimal Solutions**:
- Solution 1: T:1 P:0 C:0 (1 Theatre)
- Solution 2: T:0 P:1 C:0 (1 Pub)

### Test Case 2: n = 8 time units
**Maximum Earnings**: $4,500

**Optimal Solution**:
- Solution 1: T:1 P:0 C:0 (1 Theatre)

### Test Case 3: n = 13 time units
**Maximum Earnings**: $16,500

**Optimal Solution**:
- Solution 1: T:2 P:0 C:0 (2 Theatres)

### Additional Example: n = 12 time units
**Maximum Profit**: $18,000

**Multiple Optimal Solutions**:
- 2 Theatres + 1 Pub (5+5+4 = 14 units used, earn from t=5, t=10, t=14)
- Other combinations may exist

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- None at the moment

## 🔮 Future Enhancements

-  Add visualization of construction timeline and earnings graph
-  Export results to CSV/PDF format
-  Show step-by-step DP table computation
-  Add interactive property comparison charts
-  Support for custom property types and parameters
-  Animation showing building construction sequence
-  Profit breakdown per time unit visualization
-  Compare efficiency metrics across solutions

## 👤 Author

**Yogesh Raj NS** - [@YogeshRajNS](https://github.com/YogeshRajNS)

Project Link: [https://github.com/YogeshRajNS/Max_profit_algorithm](https://github.com/YogeshRajNS/Max_profit_algorithm)

## 🙏 Acknowledgments

- Problem based on **"Max Profit Problem"** interview assignment
- Built with [Streamlit](https://streamlit.io/)
- Solution uses classic dynamic programming optimization techniques
- Inspired by resource allocation and scheduling problems in operations research

---

⭐ If you found this project helpful, please consider giving it a star!
