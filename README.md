# _Useful CoolProp Calculator_
A comprehensive, feature-rich thermophysical property calculator with multiple interfaces, visualization capabilities, and batch processing support.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CoolProp](https://img.shields.io/badge/CoolProp-6.0+-green.svg)](http://www.coolprop.org/)

## _Features_
### _Multiple Interfaces_
- Interactive Menu-Driven CLI - Easy-to-use command-line interface
- Jupyter Notebook - Rich visualizations and interactive widgets
- Batch Processing - Process multiple calculations at once
- Data Export - JSON and CSV export capabilities

### _Advanced Calculations_
- Single Property Calculation - Calculate any property from two known state variables
- All Properties at State Point - Get comprehensive thermodynamic data
- Critical & Triple Point Properties - Easy access to reference properties
- Property Tables - Generate comprehensive property tables
- Comparison Tools - Compare multiple substances side-by-side

### _Visualizations (Jupyter Notebook)_
- Property vs Temperature Plots - Visualize property trends
- T-S Diagrams - Temperature-Entropy diagrams with isobars
- Phase Envelopes - P-T saturation curves
- Comparative Analysis - Bar charts and multi-substance comparisons

## _Quick Start_
### _Installation_
```bash
# Install required packages
pip install CoolProp numpy matplotlib pandas ipywidgets

# For Jupyter notebook support
pip install jupyter
```

### _Usage_
#### _Command Line Interface_
```bash
# Run the enhanced CLI
python coolprop_calculator_improved.py

# Run in simple mode (original style)
python coolprop_calculator_improved.py --simple
```

#### _Jupyter Notebook_
```bash
# Launch Jupyter
jupyter notebook ENHANCED_COOLPROP_CALCULATOR.ipynb
```

## _Examples_

### _Example 1: Single Property Calculation_
```python
from coolprop_calculator_improved import CoolPropCalculator

calc = CoolPropCalculator()

# Calculate density of water at 300K and 101325 Pa
result = calc.calculate_property(
    output_prop='D',
    input1_prop='T',
    input1_value=300,
    input2_prop='P',
    input2_value=101325,
    substance='Water'
)

print(f"Density: {result['output_value']:.2f} kg/m³")
```

### _Example 2: Get All Properties_
```python
# Get all available properties at a state point
results = calc.get_all_properties(
    input1_prop='T',
    input1_value=298.15,
    input2_prop='P',
    input2_value=101325,
    substance='Water'
)

for prop, data in results['properties'].items():
    print(f"{data['name']}: {data['value']:.4e} {data['unit']}")
```

### _Example 3: Batch Processing_
```python
# Process multiple calculations
calculations = [
    {'output_prop': 'D', 'input1_prop': 'T', 'input1_value': 300, 
     'input2_prop': 'P', 'input2_value': 101325, 'substance': 'Water'},
    {'output_prop': 'H', 'input1_prop': 'T', 'input1_value': 350, 
     'input2_prop': 'P', 'input2_value': 200000, 'substance': 'Water'},
]

results = calc.batch_calculate(calculations)
```

### _Example 4: Export Data_
```python
# Export calculation history
calc.export_history('calculations.json', format='json')
calc.export_history('calculations.csv', format='csv')
```

## _Available Properties_

| Code | Property | Unit |
|------|----------|------|
| T | Temperature | K |
| P | Pressure | Pa |
| D | Density | kg/m³ |
| H | Enthalpy | J/kg |
| S | Entropy | J/kg·K |
| U | Internal Energy | J/kg |
| G | Gibbs Free Energy | J/kg |
| A | Helmholtz Free Energy | J/kg |
| V | Specific Volume | m³/kg |
| Q | Quality | - |
| C | Specific Heat (const P) | J/kg·K |
| CVMASS | Specific Heat (const V) | J/kg·K |
| viscosity | Dynamic Viscosity | Pa·s |
| conductivity | Thermal Conductivity | W/m·K |
| Prandtl | Prandtl Number | - |
| surface_tension | Surface Tension | N/m |
| speed_sound | Speed of Sound | m/s |

## _Supported Substances_
The calculator supports 122+ substances including:

### _Common Fluids_
Water, Air, Nitrogen, Oxygen, Hydrogen, Helium, Argon, CO₂, Ammonia

### _Hydrocarbons_
Methane, Ethane, Propane, n-Butane, n-Pentane, n-Hexane, n-Heptane, Benzene, Toluene

### _Refrigerants_
R134a, R410A, R404A, R407C, R32, R1234yf, R22, R290, and many more

### _Specialized Fluids_
Siloxanes (D4, D5, D6, MM, MDM, etc.), Various esters and organic compounds

[See full list in CoolProp documentation](http://www.coolprop.org/fluid_properties/PurePseudoPure.html)

## _Visualization Examples_

The Jupyter notebook includes:
1. Interactive Property Calculator - Dropdown menus and sliders
2. Property vs Temperature Plots - Line graphs showing trends
3. T-S Diagrams - Phase diagrams with multiple isobars
4. Phase Envelopes - Saturation curves
5. Multi-Substance Comparisons - Bar charts
6. Property Tables - Pandas DataFrames

## _Advanced Features_
### _Property Table Generation_
Generate comprehensive tables across temperature and pressure ranges:
```python
table = calc.create_state_point_table(
    substance='Water',
    temps=[300, 320, 340, 360],
    pressures=[1e5, 5e5, 1e6]
)
```

### _Critical Properties_
Quick access to critical point data:
```python
critical = calc.get_critical_properties('Water')
print(f"Critical Temperature: {critical['T_critical']} K")
print(f"Critical Pressure: {critical['P_critical']} Pa")
```

### _Calculation History_
All calculations are automatically tracked:
```python
# View recent calculations
for calc in calculator.calculation_history[-5:]:
    print(calc)
```

## _Contributing_
Contributions are welcome! Areas for improvement:
- Additional plot types
- More visualization options
- GUI interface
- Web-based interface
- Additional property calculations
- Performance optimizations

## _References_
- [CoolProp Documentation](http://www.coolprop.org/)
- [CoolProp GitHub](https://github.com/CoolProp/CoolProp)
- [Property Calculation Guide](http://www.coolprop.org/coolprop/HighLevelAPI.html)
