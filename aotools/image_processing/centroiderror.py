"""
Functions to calculate the centre of gravity error in a number of noise cases

Mainly taken from Rousset, "Wave-front Sensors" in Adaptive Optics for Astronomy, edited by Francois Roddier
"""

import numpy

def cog_shotnoise(n_photons, N_T, N_D):
    """
    Args:
        n_photons (int): Number of photo-electrons 
        N_T (float): Image FWHM  in detector pixels
        N_D (float): FWHM of aperture diffraction pattern in detector pixels 

    Returns:
        float: noise in radians of phase squared
    """

    noise = ((numpy.pi ** 2) / 2) * (1. / n_photons) * (N_T / N_D) ** 2

    return noise


def cog_readnoise(n_photons, e_readnoise, N_S, N_D):
    """

    Args:
        n_photons (int): Number of photo-electrons
        e_readnoise (float): Read noise in counts squared
        N_S (float): Total number of pixels used for calculation
        N_D (float): FWHM of aperture diffraction pattern in detector pixels

    Returns:
        float: noise in radians of phase squared
    """

    noise = ((numpy.pi ** 2) / 3) * (e_readnoise / (n_photons ** 2)) * (N_S ** 4) / (N_D ** 2)

    return noise

