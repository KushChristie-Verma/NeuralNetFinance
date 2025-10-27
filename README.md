# NeuralNetFinance
Predict next-day S&P 500 direction using a simple feedforward neural network (PyTorch).

---

## Overview
This project trains a neural network on historical SPY data to predict whether the next day's return will be positive or negative.

**Key features:**
- Feature engineering with lagged returns, moving averages, and volatility
- Two-layer MLP trained on daily price data (PyTorch)
- Evaluation with accuracy metrics and a simple backtest

---

## Data & Label
- Asset: S&P500 ETF (SPY)
- Horizon: Predict next day
- Target definition: $y_t = (close_{t+1} / close_t) - 1$

---

## Features (v1)
- % returns over past 1, 5, 10, 20 days
- Volatility: rolling std over past 10, 20 days
- 20 Day momentum
- Vol changes: current vol over last 20 day avg vol
- Crossover momentum

---

## Method
**Test/Train/Validate**
- Test data 2015-2021
- Validate data 2022-2023
- Test data 2024-2025

**Models**
- Baseline 0: Risk-free return
- Baseline 1: Linear regression
- Model 2: Neural network

---

## Backtest
- Converting predictions into positions
- Metrics: Sharpe ratio, max drawdown

---

## Installation

```bash
git clone https://github.com/KushChristie-Verma/NeuralNetFinance.git
cd NeuralNetFinance
python -m venv venv
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
