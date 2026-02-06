# _User Guide - CoolProp Calculator_
Complete guide to using the CoolProp Calculator for thermophysical property calculations.

## _Table of Contents_
1. [Getting Started](#getting-started)
2. [Interactive Menu Overview](#interactive-menu-overview)
3. [Feature Guide](#feature-guide)
4. [Property Reference](#property-reference)
5. [Example Workflows](#example-workflows)
6. [Programmatic Usage](#programmatic-usage)
7. [Tips and Best Practices](#tips-and-best-practices)
8. [Output Precision](#output-precision)

## _Getting Started_
### _Launching the Calculator_
```bash
# Interactive mode (recommended)
python coolprop_calculator.py

# Simple mode
python coolprop_calculator.py --simple
```

### _Main Menu_
When you launch the calculator, you'll see:
```
==============================================================
  ENHANCED COOLPROP CALCULATOR
==============================================================

[1] Single Property Calculation
[2] All Properties at State Point
[3] Critical Properties
[4] Triple Point Properties
[5] Batch Calculations
[6] Property Table Generator
[7] List Available Substances
[8] Property Reference Guide
[0] Exit
```

## _Interactive Menu Overview_
### _[1] Single Property Calculation_
Calculate one specific property given two known properties.

Example: Find the density of water at 300 K and 101325 Pa

1. Select option `1`
2. Enter output property: `D` (Density)
3. Enter substance: `Water`
4. Enter first input property: `T` (Temperature)
5. Enter value: `300` (in Kelvin)
6. Enter second input property: `P` (Pressure)
7. Enter value: `101325` (in Pascal)

Result:
```
============================================================
Result: Density
Value:  9.965326583930e+02 kg/m³
============================================================
```

### _[2] All Properties at State Point_
Get all available thermophysical properties at once.

Use case: Complete thermodynamic analysis at a specific state
Example: All properties of R134a at 300 K and 500000 Pa

1. Select option `2`
2. Enter substance: `R134a`
3. First property: `T`, Value: `300`
4. Second property: `P`, Value: `500000`

Output: Complete property table with ~20 different properties

### _[3] Critical Properties_
Display critical point data for any substance.

Example: Critical properties of Water
```
Critical Properties for Water:
  Temperature: 647.0960000000 K
  Pressure:    2.206400000000e+07 Pa
  Density:     322.0000000000 kg/m³
```

### _[4] Triple Point Properties_
Get triple point temperature and pressure.

Example: Triple point of Carbon Dioxide
```
Triple Point for CarbonDioxide:
  Temperature: 216.5920000000 K
  Pressure:    5.184961117599e+05 Pa
```

### _[5] Batch Calculations_
Process multiple property calculations in sequence without restarting.

Use case: Calculate multiple properties or compare different substances quickly
Example Workflow:
1. Select option `5`
2. For each calculation, enter:
   - Substance name
   - Output property
   - First input property and value
   - Second input property and value
3. Type `done` when finished
4. View all results at once

Output Example:
```
======================================================================
Processing 3 calculations...
======================================================================

1. Water: H = 4.179070831600e+06 J/kg
2. R134a: D = 4.726338492100e+00 kg/m³
3. Ammonia: S = 5.938402761000e+03 J/kg·K
```

### _[6] Property Table Generator_
Create comprehensive property tables across temperature and pressure ranges.

Use case: Generate data for plotting, analysis, or external applications
Features:
- Custom temperature and pressure ranges with adjustable step sizes
- Displays T, P, H, S, and D for each state point
- Shows first 20 rows on screen
- Option to export complete table to CSV

Example:
```
Substance: Water
Temperature range: 300 K to 400 K, step 10 K
Pressure range: 100000 Pa to 500000 Pa, step 100000 Pa

Generates: 11 temps × 5 pressures = 55 data points
```

Output Format:
```
========================================================================================================================
Property Table for Water
========================================================================================================================
           T (K)                 P (Pa)              H (J/kg)           S (J/kg·K)             D (kg/m³)
------------------------------------------------------------------------------------------------------------------------
   300.00000000     1.000000000000e+05     1.130159082031e+05     3.933336937500e+02     9.965326583930e+02
   300.00000000     2.000000000000e+05     1.132187500000e+05     3.926148437500e+02     9.975302734375e+02
...
```

### _[7] List Available Substances_
View the complete list of 100+ available substances organized by category.

### _[8] Property Reference Guide_
Complete table of all available properties with units and descriptions.

## _Feature Guide_
### _Understanding Property Codes_

| Code | Property | Unit | Common Use |
|------|----------|------|------------|
| `T` | Temperature | K | State variable |
| `P` | Pressure | Pa | State variable |
| `D` | Density | kg/m³ | Mass per volume |
| `H` | Enthalpy | J/kg | Energy content |
| `S` | Entropy | J/kg·K | Disorder/heat capacity |
| `Q` | Quality | - | Vapor fraction (0-1) |
| `C` | Cp | J/kg·K | Specific heat (const P) |
| `CVMASS` | Cv | J/kg·K | Specific heat (const V) |
| `V` | Specific Volume | m³/kg | Volume per mass |

### _Input Requirements_
Two independent properties are required to define a thermodynamic state:
- Valid: T + P, T + D, P + H, P + S, T + Q
- Invalid: T + T, P + P (same property twice)

Common Combinations:
- `T` + `P` - Most common for superheated vapor/compressed liquid
- `P` + `Q` - Saturated mixtures (Q between 0 and 1)
- `P` + `H` - Common in refrigeration cycles
- `T` + `Q` - Saturated conditions at known temperature

### _Unit System_
All inputs and outputs use SI units:
- Temperature: Kelvin (K)
- Pressure: Pascal (Pa)
- Energy: Joules (J)
- Mass: Kilograms (kg)

Quick conversions:
- °C to K: Add 273.15
- bar to Pa: Multiply by 100,000
- kJ to J: Multiply by 1,000
- MPa to Pa: Multiply by 1,000,000

## _Property Reference_
### _Thermodynamic Properties_
- Temperature (T) - Absolute temperature in Kelvin
- Pressure (P) - Absolute pressure in Pascal
- Density (D) - Mass per unit volume
- Enthalpy (H) - Total heat content per unit mass
- Entropy (S) - Measure of thermal disorder
- Internal Energy (U) - Microscopic energy per unit mass
- Quality (Q) - Vapor mass fraction (0 = saturated liquid, 1 = saturated vapor)

### _Transport Properties_
- Viscosity - Resistance to flow (dynamic viscosity)
- Thermal Conductivity - Heat transfer capability
- Prandtl Number - Ratio of momentum to thermal diffusivity

### _Derived Properties_
- Specific Heat (C, CVMASS) - Heat capacity at constant pressure/volume
- Speed of Sound - Propagation velocity of pressure waves
- Surface Tension - Interface energy between liquid and vapor

## _Example Workflows_

### _Example 1: Refrigeration Cycle Analysis_
Scenario: Analyze R134a in a vapor-compression cycle
```
State 1 (Evaporator exit): T = 280 K, Q = 1 (saturated vapor)
State 2 (Compressor exit): P = 1,000,000 Pa, S = (from State 1)
State 3 (Condenser exit): T = 320 K, Q = 0 (saturated liquid)
State 4 (Expansion valve exit): H = (from State 3), P = (from State 1)
```

Use option [2] for each state to get complete property tables.

### _Example 2: Steam Power Plant_
Scenario: Water/steam properties at various cycle points
```
Boiler: P = 10,000,000 Pa, T = 600 K → Calculate H, S
Turbine exit: P = 10,000 Pa, S = (isentropic from boiler)
Condenser: P = 10,000 Pa, Q = 0 → Calculate H
```

### _Example 3: Gas Pipeline Design_
Scenario: Natural gas (use Methane) flow properties
```
Inlet: T = 288 K, P = 5,000,000 Pa
Calculate: D, viscosity, speed_sound
```

Use these for Reynolds number, pressure drop calculations.

## _Programmatic Usage_
### _Basic Script Usage_
```python
from coolprop_calculator import CoolPropCalculator

calc = CoolPropCalculator()

# Single calculation
result = calc.calculate_property(
    output_prop='D',
    input1_prop='T',
    input1_value=300,
    input2_prop='P',
    input2_value=101325,
    substance='Water'
)

print(f"Density: {result['output_value']:.12e} kg/m³")
# Output: Density: 9.965326583930e+02 kg/m³
```

### _Batch Processing_
```python
calculations = [
    {'output_prop': 'D', 'input1_prop': 'T', 'input1_value': 300,
     'input2_prop': 'P', 'input2_value': 101325, 'substance': 'Water'},
    {'output_prop': 'H', 'input1_prop': 'T', 'input1_value': 350,
     'input2_prop': 'P', 'input2_value': 101325, 'substance': 'Water'},
]

results = calc.batch_calculate(calculations)
```

### _Get All Properties_
```python
props = calc.get_all_properties(
    input1_prop='T',
    input1_value=300,
    input2_prop='P',
    input2_value=101325,
    substance='Air'
)

for prop, data in props['properties'].items():
    print(f"{data['name']}: {data['value']} {data['unit']}")
```

### _Critical Properties_
```python
crit = calc.get_critical_properties('CarbonDioxide')
print(f"Critical Temperature: {crit['T_critical']} K")
print(f"Critical Pressure: {crit['P_critical']} Pa")
```

## _Tips and Best Practices_
### _1. Substance Names_
- Use exact CoolProp names (case-sensitive)
- Common: `Water`, `Air`, `CarbonDioxide` (not `CO2`)
- Refrigerants: `R134a`, `R410A`, `R32`, `R1234yf`
- 100+ substances available - check menu option [7] for complete list
- Categories include: pure fluids, hydrocarbons, HFCs, HFOs, blends, alcohols, aromatics, siloxanes

### _2. Valid State Points_
- Ensure your inputs define a physically realizable state
- Check against critical and triple point properties
- Quality (Q) only valid in two-phase region (0 ≤ Q ≤ 1)

### _3. Unit Conversions_
**Temperature:**
- Room temperature: ~293 K (20°C)
- Water boiling: 373 K (100°C)

Pressure:
- Atmospheric: 101,325 Pa (1.01325 bar)
- 10 bar: 1,000,000 Pa

### _4. Error Handling_
If you get an error:
1. Verify substance name spelling
2. Check that state point is valid (not below triple point, etc.)
3. Ensure two different properties are specified
4. Confirm units are in SI

### _5. Batch Processing_
- Use option [5] for multiple related calculations
- More efficient than repeating single calculations
- Results displayed together for easy comparison
- Perfect for comparing properties across different substances or states

### _6. Property Tables_
- CSV export option available for all generated tables
- Choose appropriate temperature and pressure step sizes
- Smaller steps = more data points but longer generation time
- Tables show first 20 rows on screen, save to CSV for complete data
- Perfect for creating plots or importing into other analysis tools

## _Common Use Cases_
### _HVAC Design_
- Refrigerant property analysis
- Psychrometric calculations with humid air
- Heat exchanger design data

### _Process Engineering_
- Steam cycle optimization
- Cryogenic system design
- Chemical process simulations

### _Research & Education_
- Thermodynamics homework/labs
- Experimental data validation
- Phase diagram exploration

## _Output Precision_
The calculator provides high-precision output suitable for engineering and scientific applications:

### _Precision Levels_
Scientific Notation (12 decimal places):
- Most properties use `.12e` format
- Example: `9.965326583930e+02` kg/m³
- Perfect for energy values, pressures, and derived properties

Fixed Decimal (10 decimal places):
- Temperatures: `.10f` format
- Example: `647.0960000000` K
- Densities: `.10f` format
- Example: `322.0000000000` kg/m³

Fixed Decimal (8 decimal places):
- Property table temperatures use `.8f` format
- Example: `300.00000000` K

### _Why High Precision?_
1. Engineering Accuracy - Critical for thermodynamic cycle calculations where small errors compound
2. Research Applications - Needed for validating experimental data and models
3. Numerical Stability - Prevents round-off errors in iterative calculations
4. Comparative Analysis - Enables detection of small differences between similar states

### _Using High Precision Data_
For Reports:
```python
# Round to appropriate significant figures
result = 9.965326583930e+02
print(f"Density: {result:.2f} kg/m³")  # Output: 996.53 kg/m³
```

For Calculations:
```python
# Use full precision for intermediate calculations
h1 = 4.179070831600e+06  # J/kg
h2 = 4.182391562100e+06  # J/kg
delta_h = h2 - h1  # Accurate difference
```

For CSV Export:
- Tables maintain full precision
- Import into Excel, MATLAB, Python for further analysis
- No loss of accuracy in data pipeline

## _Troubleshooting_
"Invalid property" error:
- Check property code spelling (case-sensitive)
- Use uppercase letters: `T`, `P`, `D` not `t`, `p`, `d`

"Calculation failed" error:
- State point may be invalid
- Check substance name
- Verify units are in SI

Empty results:
- Some properties not available for all substances
- Try a different substance or state point

## _Support_
For issues or questions:
- Check [CoolProp documentation](http://www.coolprop.org/)
- Open an issue on GitHub
- Consult the property reference guide (menu option 8)
