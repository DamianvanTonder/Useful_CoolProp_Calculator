# _Useful CoolProp Calculator_
A command-line interface for calculating thermodynamic and transport properties of various fluids using the CoolProp library.

## _Overview_
This interactive calculator allows you to compute a wide range of thermophysical properties for over 120 pure fluids and mixtures. Properties include temperature, pressure, enthalpy, entropy, density, viscosity, thermal conductivity, and many more.

## _Features_
- 19 calculable properties including thermodynamic and transport properties
- 122+ supported substances ranging from common fluids like Water and Air to refrigerants and specialized chemicals
- SI units for all calculations
- Interactive command-line interface with user-friendly prompts

## _Requirements_
- Python 3.x
- CoolProp library

## _Installation_
Install the required dependency:

```bash
pip install CoolProp
```

## _Usage_
Run the Jupyter notebook or execute the Python script. The calculator will prompt you for:

1. Property to calculate (e.g., viscosity, density, temperature)
2. Known properties (two state variables for most calculations)
3. Values for the known properties
4. Substance name

### _Example_
```
COOLPROP CALCULATOR (SI UNITS)

I want to know: viscosity
for a given: T
at temperature[K] = 298.15
for a given: P
at pressure[Pa] = 101325
for the substance: Water

the viscosity[Pa.s] of Water at the given (T) and (P) = 0.001[Pa.s]
```

## _Available Properties_
- **T** - Temperature [K]
- **P** - Pressure [Pa]
- **H** - Enthalpy [J/kg]
- **S** - Entropy [J/kg.K]
- **D** - Density [kg/m³]
- **Q** - Quality [dimensionless]
- **V** - Specific volume [m³/kg]
- **U** - Internal energy [J/kg]
- **W** - Humidity ratio [water vapor/dry air]
- **G** - Gibbs free energy [J/kg]
- **A** - Helmholtz free energy [J/kg]
- **P_critical** - Critical pressure [Pa]
- **T_critical** - Critical temperature [K]
- **D_critical** - Critical density [kg/m³]
- **viscosity** - Dynamic viscosity [Pa.s]
- **conductivity** - Thermal conductivity [W/m.K]
- **Prandtl** - Prandtl number [dimensionless]
- **Phase** - Phase fraction [dimensionless]
- **sigma** - Surface tension [N/m]

## _Supported Substances_
The calculator supports 122+ substances including:

- **Common fluids**: Water, Air, Ammonia, Nitrogen, Oxygen
- **Hydrocarbons**: Methane, Ethane, Propane, Butane, Benzene, Toluene
- **Refrigerants**: R134a, R410A, R404A, R407C, R32, and many more
- **Alcohols**: Methanol, Ethanol
- **Noble gases**: Helium, Argon, Neon, Krypton, Xenon
- **Specialized fluids**: Siloxanes (D4, D5, D6, MM, MDM, etc.)

For the complete list, see the `substance` array in the code.

## _How It Works_
The calculator uses the CoolProp library's `PropsSI` function to compute thermophysical properties. You specify:

- The property you want to calculate
- Two known state variables (for most properties)
- Their values
- The substance

CoolProp then returns the requested property based on its equation of state database.

## _Notes_
- All inputs and outputs use **SI units**
- For critical properties (P_critical, T_critical, D_critical), special calculation methods are used
- Some property combinations may not be valid for all substances
- Ensure substance names match exactly (case-sensitive)

## _References_
- [CoolProp Documentation](http://www.coolprop.org/)
- [CoolProp on GitHub](https://github.com/CoolProp/CoolProp)

## _Contributing_
Feel free to submit issues or pull requests to improve the calculator's functionality or add new features.
