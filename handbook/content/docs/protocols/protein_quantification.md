---
title: "Protein Quantification"
weight: 10
---

# Protein Quantification - Microplate
![Version Badge](https://img.shields.io/badge/Version-0.1-blue)
![Validation Badge](https://img.shields.io/badge/Validation-Unvalidated-red)
![Date Badge](https://img.shields.io/badge/Released-2023--10--12-blue)
![License](https://img.shields.io/github/license/TCP-Lab/handbook)

This protocol can be used to quantify the amount of protein in a sample.
It is know as the Bradford Protein Assay.

## Contributors
The following contributors have created this record:
- Luca Visentin - [0000-0003-2568-5694](https://orcid.org/0000-0003-2568-5694);

The following contributors have edited or reviewed this record:
- None

The following contributors have validated this record:
- None

## Provenance
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

## Generated data
Produces two tabular files: one with the absorbance of the calibration curve and
one with the recorded data of the samples.

# Materials
- Biological Source:
  - Starting Material: Any protein suspension
  - Strain/Genotype: Any
  - Amount of Material: At least $100 \mul$ to each test tube
  - Storage: No sample storage is required.

- Prepared Reagent: Phosphate-Buffered Saline Buffer
  - Name: Phosphate-Buffered Saline Buffer
  - Abbreviation: PBS
  - Required: Yes 
  - Recipe ID: [BUFF-001](https://example.org/)
  - Required Amount: At least 500 ml.
  - Modifications: Must be used cold, around 4 C.

- prepared reagent: bovine serum albumin 2mg/ml solution
  - Name: Bovine serum albumin 2mg/ml solution
  - Abbreviation: BSA
  - Required: Yes 
  - Recipe ID: [SOL-001](https://example.org/)
  - Required Amount: 10 ulu
  - Modifications: None

- Raw Reagent: RIPA Lysis Buffer
  - Name: Radio-Immunoprecipitation assay (RIPA) Lysis Buffer
  - Abbreviation: RIPA
  - Manufacturer: ThermoFisher Scientific
  - Required: Yes
  - Required Amount: 50 ul per MW6 well, 150 ul per p58 well.
  - Potential Substitutions: None

# Required Laboratory Equipment
This protocol requires:
- Micropipette of 1-50 ul with tips;
- Micropipette of 100-1000 ul with tips;
- Sonicator;
- Spectrophotometer with clean cuvettes, one cuvette per sample plus 6;
- High-speed centrifuge;
- Vortexer;
- Small Eppendorf vials;
- Ice;
- Ice bath;

# Methods

## Reagent preparation
Prepare PBS following the recipe. Store at 4 degrees Celsius for at least 5
hours before use. Always use cold PBS in all steps of the procedure.

Prepare 5 dilutions of BSA. In different eppendorf vials stored in a bath of 
crushed ice, combine the following:
- 10 ug: 90 ul of distilled water and 10 ul of BSA (2mg/ml);
- 5 ug: 50 ul of distilled water plus 50 ul of the previous solution;
- 2.5 ug: 50 ul of distilled water plus 50 ul of the previous solution;
- 1.25 ug: 50 ul of distilled water plus 50 ul of the previous solution;
- 0 ug: 100 ul of distidde water. This sample will be referred to as the "blank".

Store all prepared solutions at 4 C. Store BSA solutions for up to 12 hours.

## Sample preparation
If starting with plated cells, 

## Procedure
### Day 1
> *"Add 5 ul of reagent BBB to every sample. Pipette at least three time for 
through mixing. Incubate overnight at 4 degrees Celsius."*

### Day 2
> *"Take samples from incubator and vortex at high-speed in a high-speed centrifuge
for 3 minutes at 4000 RPM.
Remove surnatant by pipetting to vacuum.
Add 3 ul of reagent CCC to each sample. Incubate overnight."*

### Day 3
> *Do all other steps. Measure at spectrofotometer at wavelenght 400 nm.*

# Changelog
This section records all changes to this protocol:
- [2023-01-01] (Name, Surname): Changed ...
