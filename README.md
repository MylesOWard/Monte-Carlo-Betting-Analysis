# Monte-Carlo-Betting-Analysis
### Stochastic Betting Strategies with Python

This repository is a small research toolkit for simulating and comparing **stochastic betting strategies** under a roulette-like game with a slight house edge (**win probability ≈ 0.49**). This is signifiantly lower than the real-world house edge in roulette or typical fruit machines. The repository focuses on **bankroll dynamics**, **probability of ruin**, and **distributional outcomes** using Monte Carlo simulation. The code is designed to be easily modifed, allowing different variations of house edge, stake and bankroll to be investegated.

The project is organized as reusable core logic in `src/` (RNG utilities, strategy implementations, simulation runner, and metrics) plus a short notebook series that explains each strategy and visualizes results.

---

## Project Overview

Progression systems can “feel” profitable because they often produce many small wins — until a losing streak creates a large drawdown or total ruin. This repo explores that trade-off by simulating strategies under identical assumptions and measuring:

- **Ruin probability** (how often bankroll hits zero / busts)
- **Final bankroll distributions** (skew, tails, dispersion)
- **Mean vs median outcomes** (typical vs “average” results)

### Strategies covered

| Strategy | Rule | Intuition | Main risk |
|:--|:--|:--|:--|
| **Simple / Flat** | Bet a constant stake each round | Baseline reference model | Slow drift under negative EV |
| **Martingale** | Double after each loss; reset after a win | “Recover losses quickly” | Exponential stake growth → bankroll blowups |
| **D’Alembert** | Increase stake by 1 unit after loss; decrease by 1 after win | “Smoother recovery” | Still negative EV; ruin remains possible |

---

## Notebook Series

All notebooks include narrative explanation plus plots from both **single-path** and **Monte Carlo** simulations.

| # | Notebook | Focus |
|:--|:--|:--|
| 01 | [`01_simple_bettor.ipynb`](notebooks/01_simple_bettor.ipynb) | Baseline flat betting + bankroll evolution + Monte Carlo outcome distribution |
| 02 | [`02_martingale_bettor.ipynb`](notebooks/02_martingale_bettor.ipynb) | Martingale dynamics (many small gains vs occasional large losses) + ruin behavior |
| 03 | [`03_d’alembert_bettor.ipynb`](notebooks/03_d’alembert_bettor.ipynb) | Linear progression variant + comparison to Martingale-style variance |
| 04 | [`04_strategy_comparison.ipynb`](notebooks/04_strategy_comparison.ipynb) | Head-to-head Monte Carlo comparison: ruin rate + distributions + mean/median outcomes |

The comparison notebook evaluates all three strategies under identical parameters and summarizes **ruin rate** and final-wealth statistics.

---

## Repository Structure

- `notebooks/` — walkthrough notebooks (strategy-by-strategy + final comparison)
- `src/` — reusable simulation code
  - `rng.py` — seeding + roulette-like trial helper
  - `runner.py` — Monte Carlo runner (`run_simulation`)
  - `metrics.py` — summary / reporting helpers
  - `strategies/` — strategy implementations (simple, martingale, d’alembert)
- `tests/` — unit tests for core logic (where applicable)

---


