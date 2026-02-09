- # MCM 2026 Problem B: Space Transportation System Analysis

  ## Overview

  This repository contains the comprehensive mathematical modeling and analysis for MCM 2026 Problem B, which addresses the transportation of 100 million metric tons of materials from Earth to the Moon starting from 2050.

  ## Problem Statement

  Design and analyze optimal transportation strategies to move 100 million metric tons of lunar materials under three scenarios:
  * Scenario A: Space Elevator only
  * Scenario B: Traditional Rockets only
  * Scenario C: Hybrid approach combining both methods

  Additionally, the project analyzes how system failures and operational inefficiencies affect mission completion time and cost.

  ---

  ## Key Results Summary

  ### Scenario Comparison

  | Scenario                 | Duration       | Total Cost         | Avg. Cost/kg | Status                  |
  | :----------------------- | :------------- | :----------------- | :----------- | :---------------------- |
  | Space Elevator Only      | ~186 years     | $1.36 Trillion     | $13.6/kg     | Slowest, Cheapest       |
  | Traditional Rockets      | ~109 years     | $7.73 Trillion     | $77/kg       | Fastest, Most Expensive |
  | **Hybrid (24% Rockets)** | **~132 years** | **$3.72 Trillion** | **$37/kg**   | **Recommended**         |

  ### Recommendation

  The Hybrid Strategy (24% Rocket utilization) is optimal because it:
  * Balances time-cost tradeoffs effectively.
  * Provides operational redundancy through dual transport modes.
  * Mitigates single-point-of-failure risks.
  * Saves 54 years compared to the elevator-only scenario while reducing costs by 52% compared to the rockets-only scenario.

  ---

  ## Mathematical Models

  ### 1. Exponential Decay Model for Launch Cost Prediction
  * Formula: $y(t)=a \cdot e^{-b(t-1988)}+c$
  * Applied to historical NASA data (1988-2025).
  * Captures rapid cost reduction followed by asymptotic stabilization.

  ### 2. Generalized Logistic Growth Model for Launch Rate
  * Formula: $N(t)=N_{0}+\frac{K-N_{0}}{1+e^{-r(t-t_{inf})}}$
  * Parameters: $N_{0}=80$ launches/year, $K=7,300$ launches/year.
  * Physical constraint: 10 global launch sites with a maximum of 2 launches/day.
  * Fitted $R^{2}>0.95$ .

  ### 3. Wright's Law (Learning Curve) for Rocket Cost
  * Formula: $C(m)=C_{1} \cdot m^{b}$ where $b=-0.322$ .
  * Represents approximately 20% cost reduction per doubling of cumulative production.
  * Calibrated starting cost: $114.7/kg in 2050.

  ### 4. Pareto Optimization for Hybrid Strategy Selection
  * Minimizes both duration and cost simultaneously.
  * Method: Normalized Euclidean distance to the Utopia point.
  * Sweep: 51 hybrid configurations (0-100% rocket utilization).

  ---

  ## Failure Analysis (Task 2)

  ### Monte Carlo Simulation Results

  | Scenario       | Perfect Conditions | With Failures | Impact | Uncertainty      |
  | :------------- | :----------------- | :------------ | :----- | :--------------- |
  | Rockets        | 109 years          | 132 years     | +21%   | $\pm 0.07$ years |
  | Space Elevator | 186 years          | 200 years     | +7.3%  | $\pm 6.0$ years  |
  | Hybrid         | 112 years          | 104 years     | -7%    | $\pm 2.2$ years  |

  ### Key Insights
  * Rocket System: Highly vulnerable to fleet grounding (30-day investigation period per major failure).
  * Space Elevator: Primary risks involve catastrophic failures (e.g., micrometeorite impacts) requiring 2-year recovery periods.
  * Hybrid System: Redundancy enables superior performance under fault conditions through dynamic load balancing.

  ---

  ## Repository Structure

  MCM2026/
  ├── README.md                    # This file
  ├── Summary.md                   # Detailed problem summaries
  ├── Solution.pdf                 # Complete written solution
  ├── Code/                        # Jupyter notebooks with implementations
  │   ├── Task1.ipynb             # Main transportation model analysis
  │   ├── Task2.ipynb             # Failure analysis and Monte Carlo
  │   ├── Task3.ipynb             # Additional analysis
  │   └── Task4.ipynb             # Additional analysis
  ├── Data/                        # Input data and datasets
  ├── Preparation/                 # Research materials and background
  │   └── Models/                  # Reusable modeling modules
  │       ├── data_preprocessing.py
  │       ├── differential_equations.py
  │       ├── evaluation_methods.py
  │       ├── forecasting.py
  │       ├── graph_algorithms.py
  │       ├── machine_learning.py
  │       ├── optimization.py
  │       ├── plot_templates.py
  │       ├── regression.py
  │       └── statistical_tests.py
  ├── img/                         # Figures and diagrams
  ├── References/                  # Academic references
  └── Modeling approach/           # Documentation of methodology

  ---

  ## Technologies & Methods

  * Languages: Python 3
  * Key Libraries: scipy (curve fitting, optimization), numpy (numerical computing), pandas (data analysis), matplotlib/seaborn (visualization).
  * Methods: Nonlinear curve fitting, numerical integration, multi-objective optimization (Pareto frontier), Monte Carlo simulation, time series forecasting, and sensitivity analysis.

  ## Implementation Details

  ### Nonlinear Curve Fitting
  We fitted exponential decay and logistic growth models to historical NASA launch cost and frequency data using scipy.optimize.curve_fit.

  ### Cost Accumulation
  We integrated daily cost calculations over the mission timeline using numerical methods to account for Wright's Law learning curve effects.

  ### Pareto Optimization
  We generated 51 hybrid configurations and computed the Pareto frontier by minimizing the normalized Euclidean distance to the utopia point.

  ### Failure Simulation
  We performed 5,000 Monte Carlo iterations modeling Poisson-distributed operational failures, Binomial launch failure rates, and dynamic load balancing between transportation modes.

  ## Running the Code

  1. Setup Environment:
     pip install numpy scipy pandas matplotlib seaborn jupyter

  2. Run Notebooks:
     * Open Jupyter: jupyter notebook
     * Navigate to the Code/ directory.
     * Run notebooks in order: Task1, Task2, Task3, Task4.

  ## Problem Context

  This solution addresses the MCM 2026 Problem B. The problem requires applying advanced mathematical modeling techniques to real-world space engineering challenges.

  * Problem Source: 2026_MCM_Problem_B.pdf
  * Contest: Mathematical Contest in Modeling (MCM) 2026
  * Date: February 2026

  ## Notes

  * All monetary values are in USD.
  * Timeline estimates assume operations begin in 2050.
  * Cost projections account for Wright's Law learning curve effects.
  * Failure rates are calibrated from historical aerospace data.
