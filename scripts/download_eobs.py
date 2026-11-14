import cdsapi
from pathlib import Path

out = Path("data/raw/eobs")
out.mkdir(parents=True, exist_ok=True)

client = cdsapi.Client()
dataset = "insitu-gridded-observations-europe"

for var, short in [("minimum_temperature", "tn"),
                   ("maximum_temperature", "tx"),
                   ("precipitation_amount", "rr")]:
    target = out / f"eobs_{short}_ensmean_0.1deg_v34.0e.zip"
    if target.exists():          # no repite lo ya descargado
        continue
    client.retrieve(dataset, {
        "licence_type": "open_data_licence",
        "product_type": "ensemble_mean",
        "variable": [var],
        "grid_resolution": "0_1deg",
        "version": ["34_0e"],
    }).download(str(target))