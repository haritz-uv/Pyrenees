from pathlib import Path
import cdsapi

out = Path("data/raw/gcm"); out.mkdir(parents=True, exist_ok=True)
periods = ["19091201-19191130", "19191201-19291130", "19291201-19391130",
           "19391201-19491130", "19491201-19591130", "19591201-19691130",
           "19691201-19791130", "19791201-19891130", "19891201-19991130",
           "19991201-20051130"]
c = cdsapi.Client()
for p in periods:
    target = out / f"hadgem2es_hist_{p}_N46W-5S40E6.zip"
    if target.exists():
        continue
    c.retrieve("projections-cmip5-daily-single-levels", {
        "experiment": "historical",
        "variable": ["maximum_2m_temperature_in_the_last_24_hours",
                     "minimum_2m_temperature_in_the_last_24_hours",
                     "mean_precipitation_flux"],
        "model": "hadgem2_es", "ensemble_member": "r1i1p1",
        "period": p, "area": [46, -5, 40, 6], "format": "zip",
    }).download(str(target))