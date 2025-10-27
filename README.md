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

## Installation

```bash
git clone https://github.com/<yourusername>/NeuralNetFinance.git
cd NeuralNetFinance
python -m venv venv
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
