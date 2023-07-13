# name-to-label-script
Writes a script to convert names to readable labels in Survey123 data.

## How to Use
Download the script, and place the XLSForm spreadsheet containing the configuration details for the survey in the same location. Next, change the file name in the `name-to-label-script.py` file, located near the top of the script.

```python
import pandas as pd

PROJECT_NAME = "[TYPE THE NAME OF THE XLSFORM HERE]"

d_df = pd.read_excel(PROJECT_NAME+'.xlsx', sheet_name = ['choices'])
df = d_df.get('choices')
```

In the terminal, navigate to the folder containing `name-to-label-script.py` and run `python name-to-label-script.py`. A file called `output.txt` should have been created in the folder.

Copy the contents of `output.txt` and open up the script used to process the Survey123 data. Paste the copied text near the top of the script.

```python
import datetime, os, math, glob
import arcgis
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection
import pyodbc, traceback, sys
import win32com.client

# paste contents here
def convert_to_labels(original_dict):
	output = {}
	exec('...')
	return output
```

Under where the dictionaries for the attributes are constructed, remove all preexisting procedures that convert names to labels. Instead, just call the `convert_to_labels` function on the original dictionary.
