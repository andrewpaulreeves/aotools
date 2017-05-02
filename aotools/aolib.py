"""
A library of useful functions to be used for analysis of AO systems
"""

def fitting_error(subap_diameter, r0, dm_constant=0.14):
    """
    Fitting error calculation (from Hardy)
    
    This is dependent on the diameter of each sub-apture and the atmospheric
    turbulence strength. It also differs for different DM types, which is set by a 
    constant. For a continuous phase sheet, this value is quoted at 0.14 rad^2 by Hardy. 
    This is the default value here.
    
    Parameters: 
        subap_diameter (float): Size of each sub-aperture in metres
        r0 (float): Atmospheric fried parameter in metres
        dm_constant (float): DM constant describing DM performance. Default is 0.14
    Returns:
        float: fitting_error in radians
    """

    fitting_error = dm_constant * (subap_diameter/r0)**(5./3)

    return fitting_error