# MCM2026 Problem B: Space Transportation System Analysis

## ? Overview

This repository contains the comprehensive mathematical modeling and analysis for **MCM2026 Problem B**, which addresses the transportation of 100 million metric tons of materials from Earth to the Moon starting from 2050.

## ? Problem Statement

Design and analyze optimal transportation strategies to move 100 million metric tons of lunar materials under three scenarios:
- **Scenario A**: Space Elevator only
- **Scenario B**: Traditional Rockets only  
- **Scenario C**: Hybrid approach combining both methods

Additionally, analyze how system failures and operational inefficiencies affect mission completion time and cost.

## ? Key Results Summary

### Scenario Comparison

| Scenario | Duration | Total Cost | Avg. Cost/kg | Status |
|----------|----------|-----------|-------------|--------|
| Space Elevator Only | ~186 years | $1.36 Trillion | $13.6/kg | Slowest, Cheapest |
| Traditional Rockets | ~109 years | $7.73 Trillion | $77/kg | Fastest, Most Expensive |
| **Hybrid (24% Rockets)** | **~132 years** | **$3.72 Trillion** | **$37/kg** | **Recommended** ? |

### Recommendation

The **Hybrid Strategy (24% Rocket utilization)** is optimal because it:
- ? Balances time-cost tradeoffs effectively
- ? Provides operational redundancy (dual transport modes)
- ? Mitigates single-point-of-failure risks
- ? Saves 54 years vs. elevator-only while reducing costs 52% vs. rockets-only

## ? Mathematical Models

### 1. Exponential Decay Model for Launch Cost Prediction
- **Form**: $y(t) = a \cdot e^{-b(t-1988)} + c$
- Applied to historical NASA data (1988-2025)
- Captures rapid cost reduction followed by asymptotic stabilization

### 2. Generalized Logistic Growth Model for Launch Rate
- **Form**: $N(t) = N_0 + \frac{K - N_0}{1 + e^{-r(t-t_{inf})}}$
- Parameters: N? = 80 launches/year, K = 7,300 launches/year
- Physical constraint: 10 global launch sites ¡Á 2 launches/day maximum
- Fitted R? > 0.95

### 3. Wright's Law (Learning Curve) for Rocket Cost
- **Form**: $C(m) = C_1 \cdot m^b$ where b = -0.322
- Represents ~20% cost reduction per doubling of cumulative production
- Calibrated starting cost: $114.7/kg in 2050

### 4. Pareto Optimization for Hybrid Strategy Selection
- Minimizes both duration and cost simultaneously
- Method: Normalized Euclidean distance to Utopia point
- Sweep: 51 hybrid configurations (0-100% rocket utilization)

## ? Failure Analysis (Task 2)

### Monte Carlo Simulation Results

| Scenario | Perfect Conditions | With Failures | Impact | Uncertainty |
|----------|-------------------|--------------|--------|-------------|
| Rockets | 109 years | 132 years | +21% | ¡À0.07 years |
| Space Elevator | 186 years | 200 years | +7.3% | ¡À6.0 years |
| Hybrid | 112 years | 104 years | -7% | ¡À2.2 years |

### Key Insights
- **Rocket System**: Vulnerable to fleet grounding (30-day investigation per major failure)
- **Space Elevator**: Catastrophic failures (micrometeorite impacts) requiring 2-year recovery are primary risk
- **Hybrid System**: Redundancy enables superior performance under faults through dynamic load balancing

## ? Repository Structure

```
MCM2026/
©À©¤©¤ README.md                    # This file
©À©¤©¤ Summary.md                   # Detailed problem summaries
©À©¤©¤ Solution.pdf                 # Complete written solution
©À©¤©¤ Code/                        # Jupyter notebooks with implementations
©¦   ©À©¤©¤ Task1.ipynb             # Main transportation model analysis
©¦   ©À©¤©¤ Task2.ipynb             # Failure analysis and Monte Carlo
©¦   ©À©¤©¤ Task3.ipynb             # Additional analysis
©¦   ©¸©¤©¤ Task4.ipynb             # Additional analysis
©À©¤©¤ Data/                        # Input data and datasets
©À©¤©¤ Preparation/                 # Research materials and background
©¦   ©¸©¤©¤ Models/                  # Reusable modeling modules
©¦       ©À©¤©¤ data_preprocessing.py
©¦       ©À©¤©¤ differential_equations.py
©¦       ©À©¤©¤ evaluation_methods.py
©¦       ©À©¤©¤ forecasting.py
©¦       ©À©¤©¤ graph_algorithms.py
©¦       ©À©¤©¤ machine_learning.py
©¦       ©À©¤©¤ optimization.py
©¦       ©À©¤©¤ plot_templates.py
©¦       ©À©¤©¤ regression.py
©¦       ©¸©¤©¤ statistical_tests.py
©À©¤©¤ img/                         # Figures and diagrams
©À©¤©¤ References/                  # Academic references
©¸©¤©¤ Modeling approach/           # Documentation of methodology
```

## ?? Technologies & Methods

- **Languages**: Python 3
- **Key Libraries**: 
  - scipy (curve fitting, optimization)
  - numpy (numerical computing)
  - pandas (data analysis)
  - matplotlib/seaborn (visualization)
- **Methods**:
  - Nonlinear curve fitting
  - Numerical integration
  - Multi-objective optimization (Pareto frontier)
  - Monte Carlo simulation
  - Time series forecasting
  - Sensitivity analysis

## ? Implementation Details

### Nonlinear Curve Fitting
Fitted exponential decay and logistic growth models to historical NASA launch cost and frequency data using `scipy.optimize.curve_fit`.

### Cost Accumulation
Integrated daily cost calculations over mission timeline using numerical methods to account for Wright's Law learning curve effects.

### Pareto Optimization
Generated 51 hybrid configurations and computed Pareto frontier by minimizing normalized Euclidean distance to utopia point.

### Failure Simulation
5,000 Monte Carlo iterations modeling:
- Poisson-distributed operational failures
- Binomial launch failure rates
- Dynamic load balancing between transportation modes

## ? Running the Code

1. **Setup Environment**
   ```bash
   pip install numpy scipy pandas matplotlib seaborn jupyter
   ```

2. **Run Notebooks**
   - Open Jupyter: `jupyter notebook`
   - Navigate to `Code/` directory
   - Run notebooks in order: Task1 ¡ú Task2 ¡ú Task3 ¡ú Task4

3. **Key Outputs**
   - Cost/time comparison charts
   - Pareto frontier visualization
   - Failure impact analysis
   - Sensitivity analysis plots

## ? Problem Context

This solution addresses the Chinese MCM2026 Problem B. The problem requires students to apply advanced mathematical modeling techniques to real-world space engineering challenges.

**Problem Source**: 2026_MCM_Problem_B.pdf

## ?? Authors

Team Solution for MCM2026 Problem B

## ? Contest Details

- **Contest**: Mathematical Contest in Modeling (MCM) 2026
- **Category**: Problem B - Space Transportation Systems
- **Date**: 2026
- **Solution Date**: February 2026

## ? How to Read This Repository

1. **Start with Summary.md** for quick overview of all tasks
2. **Review Solution.pdf** for complete written analysis
3. **Explore Code/** notebooks for implementation details
4. **Check Preparation/Models/** for reusable utility functions

## ? File Descriptions

- **Solution.pdf**: Complete formal solution document with all mathematics, results, and recommendations
- **Summary.md**: Concise summary of each task's problem, methodology, and findings
- **Task[1-4].ipynb**: Jupyter notebooks implementing each task's analysis and visualizations

## ? References

See `References/` folder for all academic papers and technical sources used in this analysis.

## ? Notes

- All monetary values in USD (unless otherwise specified)
- Timeline estimates assume operations beginning in 2050
- Cost projections account for Wright's Law learning curve effects
- Failure rates calibrated from historical aerospace data
