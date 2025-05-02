# TRICERATOPS+

A tool for vetting and validating TESS Objects of Interest.

## Installation

To install TRICERATOPS+, follow these steps:

1. Download the repository:
   ```bash
   git clone https://github.com/JGB276/TRICERATOPS-plus.git
   ```

2. Navigate to the main directory:
   ```bash
   cd TRICERATOPS-plus-main
   ```

3. Install the package:
   ```bash
   pip install .
   ```
   
  ## Overview

TRICERATOPS+ extends the functionality of the original TRICERATOPS package with enhanced capabilities for incorporating ground-based light curves into the analysis pipeline.

## Key Differences

The primary enhancement is in the `.calc_probs()` function, which now supports two additional arguments:

1. `external_lc_files`: A list of file paths (as strings) pointing to ground-based light curve data
2. `filt_lcs`: A list of strings specifying the photometric filters used for each light curve

## File Format Requirements

TRICERATOPS+ expects ground-based light curve files to be in `.txt` format with three columns:

| Column | Content | Notes |
|--------|---------|-------|
| 1 | Time from mid-transit (days) | No column header |
| 2 | Relative flux values | No column header |
| 3 | Relative flux error values | No column header |

## Supported Filters

The `filt_lcs` argument accepts the following photometric filter designations:

- `"g"` - SDSS g-band
- `"r"` - SDSS r-band
- `"i"` - SDSS i-band
- `"z"` - SDSS z-band
- `"J"` - NIR J-band
- `"H"` - NIR H-band
- `"K"` - NIR K-band

## Tutorials

Check out in the "examples" folder TOI4155_01_example.ipynb and TOI4051_01_example.ipynb, which demonstrate how to use TRICERATOPS+
