# Performance Variance Model API

## Overview
Measures role-wise outcome variability and overall stability for all-rounders using Coefficient of Variation and Euclidean dispersion metrics.

## Run Instructions
1. Install dependencies:
   pip install r requirements.txt
2. Run server locally:
   uvicorn main:app reload
3. Run server for production deployment (Render):
   uvicorn main:app host 0.0.0.0 port $PORT
4. Interactive Docs: http://127.0.0.1:8000/docs
