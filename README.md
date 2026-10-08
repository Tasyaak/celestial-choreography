# Celestial Choreography

Numerical computation and visualization of periodic solutions to the planar gravitational $N$-body problem

The project explores the motion of gravitationally interacting bodies in two dimensions, including both choreographic solutions, where bodies follow the same trajectory with phase shifts, and more general periodic configurations with distinct trajectories

## Features

- Fourier-based representation of periodic trajectories
- Variational formulation using the action functional
- Automatic differentiation and numerical optimization with `JAX`
- Analysis of symmetries, periodicity, and orbital stability
- Visualization of trajectories and animations with `Matplotlib` and `Manim`

## Installation

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/)

```bash
git clone https://github.com/Tasyaak/celestial-choreography.git
cd celestial-choreography
uv sync
```

## Project Structure

- `src/celestial/` — physical models and numerical algorithms
- `scripts/` — orbit computation and validation
- `notebooks/` — numerical experiments and analysis
- `scenes/` — Manim animations
- `data/` — initial conditions and computed trajectories
- `tests/` — numerical and physical consistency tests

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
![JAX](https://img.shields.io/badge/JAX-333333?style=flat-square)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)
![Manim](https://img.shields.io/badge/Manim-222222?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)