---
title: "Protein Quantification"
weight: 10
draft: false
---

# Protein Quantification
![Version Badge](https://img.shields.io/badge/Version-0.1-blue)
![Validation Badge](https://img.shields.io/badge/Validation-Unvalidated-red)
![Date Badge](https://img.shields.io/badge/Released-2023--10--12-blue)
![License](https://img.shields.io/github/license/TCP-Lab/handbook)

This protocol can be used to quantify the amount of protein in a sample.
It is know as the Bradford Protein Assay.

## Contributors
- Creator: Luca Visentin - [0000-0003-2568-5694](https://orcid.org/0000-0003-2568-5694);

This protocol was adapted from an in-house version by Giorgia Chinigo' ([0000-0002-3772-178X](https://orcid.org/0000-0002-3772-178X)).

## License
This document is licensed under the 
[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

# General
## Scope of application
This protocol can be used to quantify the amount of protein in virtually all
solutions with a protein content.
The essay is very sensitive and particularly well suited for cell extracts.

## Disadvantages
This protocol provides wrong estimates for very concentrated samples.
It requires a calibration curve, so it needs titrated solutions of sample
proteins, like Albumin.
It does not quantify well unfolded proteins.
Strong detergents like Sodium Dodecyl Sulfate may interfere with the assay.

## Timeframe
The essay takes about two hours, all in one sitting.

## Inputs and outputs

### Input(s)
- Protein Sample Solution
  - Starting Material: Any protein suspension
  - Strain/Genotype: Any
  - Amount of Material: At least 100 μl for each sample.
  - Storage: No sample storage is required.

### Output(s)
Produces two tabular files: one with the absorbance of the calibration curve and
one with the recorded data of the samples.

# Required Equipment
This protocol requires:
- Micropipette of 1-10 μl with tips;
- Micropipette of 100-1000 μl with tips;
- Sonicator;
- Spectrophotometer with clean cuvettes, one cuvette per sample plus 6;
- High-speed centrifuge;
- Vortexer;
- Small Eppendorf vials;
- Crushed Ice and Ice box;

# Required Reagent
- Bovine serum albumin 1 mg/ml solution
  - Abbreviation: BSA
  - Required: Yes 
  - Recipe ID: [SOL-001](https://example.org/)
  - Required Amount: 10 μl
  - Modifications: None
  - Storage: Refrigerated at 4 C.
  - Potential Substitutions: None

- Coomassie Brilliant Blue R 250 solution
  - Abbreviation: CBlue
  - Manufacturer: Sigma Aldrich
  - Required: Yes
  - Required Amount: 1 ml per every sample (or every sample dilution) plus 5 ml.
  - Storage: Refrigerated at 4 C.
  - Potential Substitutions: None

# Methods
## Reagent preparation
Prepare 5 dilutions of BSA. In different eppendorf vials stored in a bath of 
crushed ice, combine the following:
- 10 ug/ml: 90 ul of distilled water and 10 ul of BSA (1mg/ml);
- 5 ug/ml: 50 ul of distilled water plus 50 ul of the previous solution;
- 2.5 ug/ml: 50 ul of distilled water plus 50 ul of the previous solution;
- 1.25 ug/ml: 50 ul of distilled water plus 50 ul of the previous solution;
- 0 ug/ml: 100 ul of distilled water. This sample will be referred to as the "blank".

Label the 0 ug/ml vial as "blank".
Label all other vials as `BSA - ` followed by the known concentration.

Store all prepared solutions at 4 C. Store BSA solutions for up to 12 hours.

## Sample preparation
No sample preparation is strictly necessary. If samples are expected to be highly
concentrated, prepare dilutions of each sample:
- x1: Add 100 ul of the sample;
- x0.5: Take 50 ul of the previous dilution and add 50 ul of distilled water;
- x0.25: Take 50 ul of the previous dilution and add 50 ul of distilled water;
- x0.125: Take 50 ul of the previous dilution and add 50 ul of distilled water;

Label all of these vials with the respective dilutions.
Store all prepared solutions at 4 C.

## Procedure
- Add 1 ml of CBlue to every sample dilution and every BSA dilutions as well as
  the blank solution.
- Close and vortex each vial to mix well.
- Turn on the spectrophotometer and set the wavelength to 595 nanometers;
- Move the blank solution to a cuvette and insert it in the spectrophotometer.
- Tare the spectrophotometer.
- Measure each sample and each BSA solution and write down the measured absorbance.
- Discard all measured samples.
- Fit a linear model on the BSA known concentrations.
- Compute concentrations based on this fitted line.

## Output Data
Record all measurements in a `.csv` file with the following columns:
- `sample_id`: The label on the sample. E.g., `BSA - 10 ug/ml`, `sample_x1`
- `absorbance`: The absorbance value for that sample.
- `computed_concentration`: The computed absorbance concentration.

If more sample metadata is available (e.g. sample ID of origin), add more
columns as needed to store all metadata information.

Name the file as `yyyy_mm_dd_computed_concentrations_<id>.csv` with a meaningful
identifier of the experiment in place of `<id>`.

## Necessary Data and Metadata
- Operator Metadata (name, orcid);
- Type and model of spectrophotometer;
- Output file name.

# Changelog
This section records all changes to this protocol:
- [2023-10-17] (Luca, Visentin) [1.0]: Released.

