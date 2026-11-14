# Motivation
Statistical Downscaling project.
HadGEM2-ES is a GCM that resolves the atmosphere in a ~140km grid resolution, the Pyrenees on that resolution seem like a gentle hill. Temperatures and rain given from this GCM have a systematic bias and the valleys and summits are can't be seen. 

Our objective is to downscale its resolution to a ~10km grid. The idea downscaling method used is the Multivariable Adaptative Constructed Analogs (MACA) method.
## Data
- HadGEM2-ES historical r1i1p1, daily tasmax/tasmin/pr, 1909–2005 (CMIP5, Copernicus CDS)
- E-OBS v34.0e, 0.1°, ensemble mean (reference observations)
Domain: 40–46°N, 5°W–6°E. See `data/README.md`.
## Method
1. Bias correction (quantile mapping, ±15-day moving window)
2. Constructed analogs at coarse scale
3. Apply analog weights to fine-scale E-OBS
4. Fine-scale bias correction
Calibration 1950–1980, validation 1981–2005.

## Reproduce
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/download_gcm.py
python scripts/download_eobs.py
then run notebooks/ in order.

## Status
Data acquisition done; bias correction in progress.