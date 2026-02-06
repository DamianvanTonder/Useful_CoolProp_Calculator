# _Usage Guide - CoolProp Calculator_

## _Table of Contents_
1. [Getting Started](#getting-started)
2. [CLI Interface Guide](#cli-interface-guide)
3. [Jupyter Notebook Guide](#jupyter-notebook-guide)
4. [Programming Examples](#programming-examples)
5. [Common Use Cases](#common-use-cases)
6. [Troubleshooting](#troubleshooting)

## _Getting Started_
### _Installation_

1. Install Python (3.8 or higher)
   ```bash
   python --version  # Check your version
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Verify installation
   ```bash
   python -c "import CoolProp; print('CoolProp installed!')"
   ```

## _CLI Interface Guide_
### _Starting the Calculator_
```bash
python coolprop_calculator_improved.py
```

### _Menu Options_
[1] Single Property Calculation
- Calculate one property from two known values
- Most common use case
- Example: Find density given temperature and pressure

[2] All Properties at State Point
- Get comprehensive thermodynamic data
- Useful for detailed analysis
- Shows all calculable properties at once

[3] Critical Properties
- Quick reference for critical temperature, pressure, and density
- Important for phase behavior understanding

[4] Triple Point Properties
- Access triple point data
- Useful for low-temperature applications

[7] View Calculation History
- See your recent calculations
- Helpful for reviewing work

[8] Export History
- Save calculations to file
- Formats: JSON or CSV

[9] List Available Substances
- Quick reference of common substances
- Full list available in CoolProp docs

[10] Property Reference Guide
- Detailed property descriptions
- Units and symbols

### _Example Workflow_
```
1. Select option [1] - Single Property Calculation
2. Choose property to calculate: D (Density)
3. Enter substance: Water
4. First input - Property: T, Value: 298.15
5. Second input - Property: P, Value: 101325
6. View result and additional properties
```

## _Jupyter Notebook Guide_
### _Launching the Notebook_
```bash
jupyter notebook ENHANCED_COOLPROP_CALCULATOR.ipynb
```

### _Notebook Sections_
#### _1. Interactive Calculator_
- Use dropdown menus to select properties
- Instant calculation with widgets
- Auto-updates as you change values

#### _2. Property Plotter_
- Visualize how properties change with temperature
- Adjustable pressure levels
- Export-quality plots

#### _3. T-S Diagram Generator_
- Create Temperature-Entropy diagrams
- Multiple isobars
- Identify phase regions

#### _4. Property Tables_
- Generate comprehensive data tables
- Export to CSV for use in other tools
- Customize temperature and pressure ranges

#### _5. Phase Envelope_
- Visualize saturation curves
- Identify critical point
- Understand phase behavior

#### _6. Comparison Tool_
- Compare multiple substances
- Side-by-side bar charts
- Useful for fluid selection

## _Programming Examples_
### _Basic Property Calculation_
```python
from coolprop_calculator_improved import CoolPropCalculator

calc = CoolPropCalculator()

# Water density at 25°C and atmospheric pressure
result = calc.calculate_property(
    output_prop='D',
    input1_prop='T',
    input1_value=298.15,  # K
    input2_prop='P',
    input2_value=101325,  # Pa
    substance='Water'
)

print(f"Density: {result['output_value']:.2f} kg/m³")
# Output: Density: 997.05 kg/m³
```

### _Get All Properties_
```python
# Get comprehensive state data
all_props = calc.get_all_properties(
    input1_prop='T',
    input1_value=373.15,  # 100°C
    input2_prop='P',
    input2_value=101325,
    substance='Water'
)

# Access specific properties
enthalpy = all_props['properties']['H']['value']
entropy = all_props['properties']['S']['value']
```

### _Batch Processing_
```python
# Process multiple calculations efficiently
batch_calcs = [
    {
        'output_prop': 'D',
        'input1_prop': 'T',
        'input1_value': 273.15,
        'input2_prop': 'P',
        'input2_value': 101325,
        'substance': 'Water'
    },
    {
        'output_prop': 'D',
        'input1_prop': 'T',
        'input1_value': 373.15,
        'input2_prop': 'P',
        'input2_value': 101325,
        'substance': 'Water'
    }
]

results = calc.batch_calculate(batch_calcs)

for r in results:
    print(f"T={r['input1_value']}K: ρ={r['output_value']:.2f} kg/m³")
```

### _Property Table Generation_
```python
import numpy as np

# Create table over temperature range
temps = np.linspace(273.15, 373.15, 11)  # 0-100°C
pressures = [101325]  # Atmospheric

table = calc.create_state_point_table('Water', temps, pressures)

# table is a list of dictionaries
for row in table:
    print(f"T={row['T']:.2f}K, ρ={row['D']:.2f} kg/m³")
```

## _Common Use Cases_
### _1. HVAC System Design_

```python
# R410A refrigerant properties for AC system
calc = CoolPropCalculator()

# Evaporator conditions
evap_temp = 278.15  # 5°C
evap_pressure = 5e5  # Pa

evap_enthalpy = calc.calculate_property(
    'H', 'T', evap_temp, 'Q', 1.0, 'R410A'
)

print(f"Evaporator outlet enthalpy: {evap_enthalpy['output_value']/1000:.2f} kJ/kg")
```

### _2. Steam Power Cycle Analysis_
```python
# Rankine cycle - find turbine outlet properties
turbine_inlet_T = 773.15  # 500°C
turbine_inlet_P = 10e6    # 10 MPa
turbine_outlet_P = 10e3   # 10 kPa

# Inlet enthalpy
h1 = calc.calculate_property('H', 'T', turbine_inlet_T, 'P', turbine_inlet_P, 'Water')

# Inlet entropy (for isentropic process)
s1 = calc.calculate_property('S', 'T', turbine_inlet_T, 'P', turbine_inlet_P, 'Water')

# Outlet properties (isentropic expansion)
h2s = calc.calculate_property('H', 'S', s1['output_value'], 'P', turbine_outlet_P, 'Water')

print(f"Isentropic enthalpy drop: {(h1['output_value']-h2s['output_value'])/1000:.2f} kJ/kg")
```

### _3. Cryogenic Storage_
```python
# Liquid nitrogen storage
LN2_temp = 77.15  # K
LN2_pressure = 101325  # Pa

density = calc.calculate_property('D', 'T', LN2_temp, 'P', LN2_pressure, 'Nitrogen')
latent_heat = calc.calculate_property('H', 'T', LN2_temp, 'Q', 1, 'Nitrogen')

print(f"LN2 Density: {density['output_value']:.2f} kg/m³")
```

### _4. Chemical Process Design_
```python
# Compare different heat transfer fluids
fluids = ['Water', 'Ethanol', 'Toluene']
temp = 350  # K
pressure = 101325  # Pa

print("\nHeat Transfer Fluid Comparison at 350K:")
print(f"{'Fluid':<12} {'Density':>12} {'Viscosity':>12} {'Th.Cond.':>12}")

for fluid in fluids:
    try:
        rho = calc.calculate_property('D', 'T', temp, 'P', pressure, fluid)
        mu = calc.calculate_property('viscosity', 'T', temp, 'P', pressure, fluid)
        k = calc.calculate_property('conductivity', 'T', temp, 'P', pressure, fluid)
        
        print(f"{fluid:<12} {rho['output_value']:12.2f} {mu['output_value']:12.6f} {k['output_value']:12.4f}")
    except:
        print(f"{fluid:<12} {'Error':>12}")
```

## _Troubleshooting_
### _Common Errors_
1. "Substance not found"
```python
# Solution: Check spelling and capitalization
# Correct: 'Water'
# Wrong: 'water', 'WATER', 'H2O'
```

2. "PropsSI error: Two-phase state"
```python
# This happens when you're in the two-phase region
# Solution: Use quality (Q) as one input for two-phase states
result = calc.calculate_property('H', 'T', 373.15, 'Q', 0.5, 'Water')
# Q=0 is saturated liquid, Q=1 is saturated vapor, 0<Q<1 is mixture
```

3. "Invalid property combination"
```python
# Some property pairs don't uniquely define a state
# Solution: Use standard pairs like (T,P), (P,H), (T,Q), (P,Q)
```

4. Import errors
```python
# If CoolProp import fails:
pip install --upgrade CoolProp

# If matplotlib/pandas fail:
pip install --upgrade matplotlib pandas
```

### _Performance Tips_
1. Batch calculations - Use `batch_calculate()` instead of loops
2. Cache results - Store frequently used values
3. Limit precision - Don't calculate more decimal places than needed
4. Pre-check ranges - Verify temperature/pressure are in valid ranges

### _Getting Help_
1. Check property combinations are valid
2. Verify substance name spelling
3. Ensure values are in SI units
4. Review CoolProp documentation for substance-specific limitations
5. Check calculation history for patterns in errors

## _Best Practices_
### _1. Always Use SI Units_
- Temperature: Kelvin (K)
- Pressure: Pascal (Pa)
- Don't convert unless displaying to user

### _2. Handle Errors Gracefully_
```python
try:
    result = calc.calculate_property(...)
    if result['status'] == 'success':
        # Use result
    else:
        print(f"Calculation failed: {result['error']}")
except Exception as e:
    print(f"Error: {e}")
```

### _3. Document Your Calculations_
```python
# Use meaningful variable names
water_density_at_STP = calc.calculate_property('D', 'T', 273.15, 'P', 101325, 'Water')

# Add comments for context
# Calculate density at standard conditions (0°C, 1 atm)
```

### _4. Export Important Results_
```python
# Save calculations for later reference
calc.export_history('my_calculations.json')
```
