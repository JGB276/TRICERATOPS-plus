import numpy as np
from pandas import read_csv
from astropy import constants
from pkg_resources import resource_filename

from .likelihoods import *
from .priors import *
from .funcs import stellar_relations, flux_relation, estimate_sdss_magnitudes

np.seterr(divide='ignore')

Msun = constants.M_sun.cgs.value
Rsun = constants.R_sun.cgs.value
Rearth = constants.R_earth.cgs.value
G = constants.G.cgs.value
au = constants.au.cgs.value
pi = np.pi
ln2pi = np.log(2*pi)

# load TESS limb darkening coefficients
LDC_FILE = resource_filename('triceratops', 'data/ldc_tess.csv')
ldc_T = read_csv(LDC_FILE)
ldc_T_Zs = np.array(ldc_T.Z, dtype=float)
ldc_T_Teffs = np.array(ldc_T.Teff, dtype=int)
ldc_T_loggs = np.array(ldc_T.logg, dtype=float)
ldc_T_u1s = np.array(ldc_T.aLSM, dtype=float)
ldc_T_u2s = np.array(ldc_T.bLSM, dtype=float)

# load Kepler limb darkening coefficients
LDC_FILE = resource_filename('triceratops', 'data/ldc_kepler.csv')
ldc_K = read_csv(LDC_FILE)
ldc_K_Zs = np.array(ldc_K.Z, dtype=float)
ldc_K_Teffs = np.array(ldc_K.Teff, dtype=int)
ldc_K_loggs = np.array(ldc_K.logg, dtype=float)
ldc_K_u1s = np.array(ldc_K.a, dtype=float)
ldc_K_u2s = np.array(ldc_K.b, dtype=float)

# load V band limb darkening coefficients
LDC_FILE = resource_filename('triceratops', 'data/ldc_V.csv')
ldc_V = read_csv(LDC_FILE)
ldc_V_Zs = np.array(ldc_V.Z, dtype=float)
ldc_V_Teffs = np.array(ldc_V.Teff, dtype=int)
ldc_V_loggs = np.array(ldc_V.logg, dtype=float)
ldc_V_u1s = np.array(ldc_V.aLSM, dtype=float)
ldc_V_u2s = np.array(ldc_V.bLSM, dtype=float)

# load J band limb darkening coefficients
LDC_FILE = resource_filename('triceratops', 'data/ldc_wirc.csv')
ldc_J = read_csv(LDC_FILE)
ldc_J_Zs = np.array(ldc_J.Z, dtype=float)
ldc_J_Teffs = np.array(ldc_J.Teff, dtype=int)
ldc_J_loggs = np.array(ldc_J.logg, dtype=float)
ldc_J_u1s = np.array(ldc_J.aLSM, dtype=float)
ldc_J_u2s = np.array(ldc_J.bLSM, dtype=float)

# load H band limb darkening coefficients
LDC_FILE = resource_filename('triceratops', 'data/ldc_H.csv')
ldc_H = read_csv(LDC_FILE)
ldc_H_Zs = np.array(ldc_H.Z, dtype=float)
ldc_H_Teffs = np.array(ldc_H.Teff, dtype=int)
ldc_H_loggs = np.array(ldc_H.logg, dtype=float)
ldc_H_u1s = np.array(ldc_H.aLSM, dtype=float)
ldc_H_u2s = np.array(ldc_H.bLSM, dtype=float)

# load K band limb darkening coefficients
LDC_FILE = resource_filename('triceratops', 'data/ldc_K.csv')
ldc_Kband = read_csv(LDC_FILE)
ldc_Kband_Zs = np.array(ldc_Kband.Z, dtype=float)
ldc_Kband_Teffs = np.array(ldc_Kband.Teff, dtype=int)
ldc_Kband_loggs = np.array(ldc_Kband.logg, dtype=float)
ldc_Kband_u1s = np.array(ldc_Kband.aLSM, dtype=float)
ldc_Kband_u2s = np.array(ldc_Kband.bLSM, dtype=float)

LDC_FILE = resource_filename('triceratops', 'data/ldc_sdss_g.csv')
ldc_gband = read_csv(LDC_FILE)
ldc_gband_Zs = np.array(ldc_gband.Z, dtype=float)
ldc_gband_Teffs = np.array(ldc_gband.Teff, dtype=int)
ldc_gband_loggs = np.array(ldc_gband.logg, dtype=float)
ldc_gband_u1s = np.array(ldc_gband.aLSM, dtype=float)
ldc_gband_u2s = np.array(ldc_gband.bLSM, dtype=float)

LDC_FILE = resource_filename('triceratops', 'data/ldc_sdss_r.csv')
ldc_rband = read_csv(LDC_FILE)
ldc_rband_Zs = np.array(ldc_rband.Z, dtype=float)
ldc_rband_Teffs = np.array(ldc_rband.Teff, dtype=int)
ldc_rband_loggs = np.array(ldc_rband.logg, dtype=float)
ldc_rband_u1s = np.array(ldc_rband.aLSM, dtype=float)
ldc_rband_u2s = np.array(ldc_rband.bLSM, dtype=float)

LDC_FILE = resource_filename('triceratops', 'data/ldc_sdss_i.csv')
ldc_iband = read_csv(LDC_FILE)
ldc_iband_Zs = np.array(ldc_iband.Z, dtype=float)
ldc_iband_Teffs = np.array(ldc_iband.Teff, dtype=int)
ldc_iband_loggs = np.array(ldc_iband.logg, dtype=float)
ldc_iband_u1s = np.array(ldc_iband.aLSM, dtype=float)
ldc_iband_u2s = np.array(ldc_iband.bLSM, dtype=float)

LDC_FILE = resource_filename('triceratops', 'data/ldc_sdss_g.csv')
ldc_zband = read_csv(LDC_FILE)
ldc_zband_Zs = np.array(ldc_zband.Z, dtype=float)
ldc_zband_Teffs = np.array(ldc_zband.Teff, dtype=int)
ldc_zband_loggs = np.array(ldc_zband.logg, dtype=float)
ldc_zband_u1s = np.array(ldc_zband.aLSM, dtype=float)
ldc_zband_u2s = np.array(ldc_zband.bLSM, dtype=float)

def lnZ_TTP(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Z: float, N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            external_lc_files: list = None,
            filt_lcs: list = None, lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the TTP scenario.
    Now supports up to four external light curves with different filters.
    Always runs in parallel if external light curves are provided.

    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
        external_lc_files (List[str]): List of external light curve file paths (up to 4).
        filt_lcs (List[str]): List of corresponding filters for external light curves.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)
    a = ((G*M_s*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    logg = np.log10(G*(M_s*Msun)/(R_s*Rsun)**2)
    # determine target star limb darkening coefficients
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s

    this_Z = ldc_Zs[np.argmin(np.abs(ldc_Zs-Z))]
    this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teff))] # get T_eff from the table that is most similar to the star's T_eff
    this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-logg))]
    mask = (
        (ldc_Zs == this_Z)
        & (ldc_Teffs == this_Teff)
        & (ldc_loggs == this_logg)
        )
    u1, u2 = ldc_u1s[mask], ldc_u2s[mask] # gets the coefficients from the table for the corresponding T, logg and Z vals.

    external_lcs = []
    if external_lc_files and filt_lcs:
        parallel = True  # Force parallel execution when external LCs are provided
        if len(external_lc_files) != len(filt_lcs):
            raise ValueError("Number of external LC files must match number of filters")
        if len(external_lc_files) > 4:
            raise ValueError("Maximum of 4 external light curves supported")

        for lc_file, filt in zip(external_lc_files, filt_lcs):
            ldc_map = {
                "J": (ldc_J_Zs, ldc_J_Teffs, ldc_J_loggs, ldc_J_u1s, ldc_J_u2s),
                "H": (ldc_H_Zs, ldc_H_Teffs, ldc_H_loggs, ldc_H_u1s, ldc_H_u2s),
                "K": (ldc_Kband_Zs, ldc_Kband_Teffs, ldc_Kband_loggs, ldc_Kband_u1s, ldc_Kband_u2s),
                "g": (ldc_gband_Zs, ldc_gband_Teffs, ldc_gband_loggs, ldc_gband_u1s, ldc_gband_u2s),
                "r": (ldc_rband_Zs, ldc_rband_Teffs, ldc_rband_loggs, ldc_rband_u1s, ldc_rband_u2s),
                "i": (ldc_iband_Zs, ldc_iband_Teffs, ldc_iband_loggs, ldc_iband_u1s, ldc_iband_u2s),
                "z": (ldc_zband_Zs, ldc_zband_Teffs, ldc_zband_loggs, ldc_zband_u1s, ldc_zband_u2s),
            }

            ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s = ldc_map[filt]

            this_Z_p = ldc_P_Zs[np.argmin(np.abs(ldc_P_Zs-Z))]
            this_Teff_p = ldc_P_Teffs[np.argmin(np.abs(ldc_P_Teffs-Teff))]
            this_logg_p = ldc_P_loggs[np.argmin(np.abs(ldc_P_loggs-logg))]
            mask_p = (
                (ldc_P_Zs == this_Z_p)
                & (ldc_P_Teffs == this_Teff_p)
                & (ldc_P_loggs == this_logg_p)
            )
            u1_p, u2_p = ldc_P_u1s[mask_p], ldc_P_u2s[mask_p]

            external_lc = np.loadtxt(lc_file)
            time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
            sigma_p = np.mean(fluxerr_p)
            lnsigma_p = np.log(sigma_p)
            exptime_p = np.min(np.diff(time_p))

            external_lcs.append({
                'time': time_p,
                'flux': flux_p,
                'sigma': sigma_p,
                'lnsigma': lnsigma_p,
                'exptime': exptime_p,
                'u1': u1_p,
                'u2': u2_p,
                'lnL': np.full(N, -np.inf)
            })

    # sample from prior distributions
    rps = sample_rp(np.random.rand(N), np.full(N, M_s), flatpriors)
    incs = sample_inc(np.random.rand(N))
    eccs = sample_ecc(np.random.rand(N), planet=True, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(R_s*Rsun)

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    Ptra = (rps*Rearth + R_s*Rsun)/a * e_corr

    # find instances with collisions
    coll = ((rps*Rearth + R_s*Rsun) > a*(1-eccs))

    lnL = np.full(N, -np.inf)

    if parallel:
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll == False)
        # calculate lnL for transiting systems
        a_arr = np.full(N, a)
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        companion_fluxratio = np.zeros(N)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_TP_p(
                    time, flux, sigma, rps[mask],
                    P_orb[mask], incs[mask], a_arr[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )

        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            ext_lc['lnL'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_TP_p(
                ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], rps[mask],
                P_orb[mask], incs[mask], a_arr[mask], R_s_arr[mask],
                u1_arr_p[mask], u2_arr_p[mask],
                eccs[mask], argps[mask],
                companion_fluxratio=companion_fluxratio[mask],
                exptime=ext_lc['exptime'], nsamples=nsamples
            )
            lnL = lnL + ext_lc['lnL']

    else:
        for i in range(N):
            if Ptra[i] <= 1.:
                inc_min = np.arccos(Ptra[i]) * 180./pi
            else:
                continue
            if (incs[i] >= inc_min) & (coll[i] == False):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_TP(
                    time, flux, sigma, rps[i],
                    P_orb[i], incs[i], a[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )

    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL + lnz_const )  # where does 600 come from?
        ))
    lnZ = np.log(Z)

    res = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': rps[idx],
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': np.zeros(N_samples),
        'R_EB': np.zeros(N_samples),
        'fluxratio_EB': np.zeros(N_samples),
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }

    # Add results for each external light curve
    for i, ext_lc in enumerate(external_lcs):
        # res[f'lnZ_p{idx+1}'] = np.log(np.mean(np.nan_to_num(np.exp(ext_lc['lnL'] + lnz_const))))
        res[f'u1_p{i+1}'] = np.full(N_samples, ext_lc['u1'])
        res[f'u2_p{i+1}'] = np.full(N_samples, ext_lc['u2'])

    return res


def lnZ_TEB(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Z: float, N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            external_lc_files: list = None,
            filt_lcs: list = None, lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the TEB scenario.
    Now supports up to four external light curves with different filters.

    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
        external_lc_files (List[str]): List of external light curve file paths (up to 4).
        filt_lcs (List[str]): List of corresponding filters for external light curves.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
        res_twin (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)
    logg = np.log10(G*(M_s*Msun)/(R_s*Rsun)**2)

    # determine target star limb darkening coefficients
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s

    this_Z = ldc_Zs[np.argmin(np.abs(ldc_Zs-Z))]
    this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teff))]
    this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-logg))]
    mask = (
        (ldc_Zs == this_Z)
        & (ldc_Teffs == this_Teff)
        & (ldc_loggs == this_logg)
        )
    u1, u2 = ldc_u1s[mask], ldc_u2s[mask]

    external_lcs = []
    if external_lc_files and filt_lcs:
        parallel = True  # Force parallel execution when external LCs are provided
        if len(external_lc_files) != len(filt_lcs):
            raise ValueError("Number of external LC files must match number of filters")
        if len(external_lc_files) > 4:
            raise ValueError("Maximum of 4 external light curves supported")

        for lc_file, filt in zip(external_lc_files, filt_lcs):
            ldc_map = {
                "J": (ldc_J_Zs, ldc_J_Teffs, ldc_J_loggs, ldc_J_u1s, ldc_J_u2s),
                "H": (ldc_H_Zs, ldc_H_Teffs, ldc_H_loggs, ldc_H_u1s, ldc_H_u2s),
                "K": (ldc_Kband_Zs, ldc_Kband_Teffs, ldc_Kband_loggs, ldc_Kband_u1s, ldc_Kband_u2s),
                "g": (ldc_gband_Zs, ldc_gband_Teffs, ldc_gband_loggs, ldc_gband_u1s, ldc_gband_u2s),
                "r": (ldc_rband_Zs, ldc_rband_Teffs, ldc_rband_loggs, ldc_rband_u1s, ldc_rband_u2s),
                "i": (ldc_iband_Zs, ldc_iband_Teffs, ldc_iband_loggs, ldc_iband_u1s, ldc_iband_u2s),
                "z": (ldc_zband_Zs, ldc_zband_Teffs, ldc_zband_loggs, ldc_zband_u1s, ldc_zband_u2s),
            }

            ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s = ldc_map[filt]

            this_Z_p = ldc_P_Zs[np.argmin(np.abs(ldc_P_Zs-Z))]
            this_Teff_p = ldc_P_Teffs[np.argmin(np.abs(ldc_P_Teffs-Teff))]
            this_logg_p = ldc_P_loggs[np.argmin(np.abs(ldc_P_loggs-logg))]
            mask_p = (
                (ldc_P_Zs == this_Z_p)
                & (ldc_P_Teffs == this_Teff_p)
                & (ldc_P_loggs == this_logg_p)
            )
            u1_p, u2_p = ldc_P_u1s[mask_p], ldc_P_u2s[mask_p]

            external_lc = np.loadtxt(lc_file)
            time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
            sigma_p = np.mean(fluxerr_p)
            lnsigma_p = np.log(sigma_p)
            exptime_p = np.min(np.diff(time_p))

            external_lcs.append({
                'time': time_p,
                'flux': flux_p,
                'sigma': sigma_p,
                'lnsigma': lnsigma_p,
                'exptime': exptime_p,
                'u1': u1_p,
                'u2': u2_p,
                'lnL': np.full(N, -np.inf),
                'lnL_twin': np.full(N, -np.inf),
                'filter': filt
            })

    # sample from prior distributions
    incs = sample_inc(np.random.rand(N))
    qs = sample_q(np.random.rand(N), M_s)
    eccs = sample_ecc(np.random.rand(N), planet=False, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate properties of the drawn EBs
    masses = qs*M_s
    radii, Teffs = stellar_relations(
        masses, np.full(N, R_s), np.full(N, Teff)
        )
    # calculate flux ratios in the TESS band
    fluxratios = (
        flux_relation(masses)
        / (flux_relation(masses) + flux_relation(np.array([M_s])))
        )

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = ((G*(M_s+masses)*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    Ptra = (radii*Rsun + R_s*Rsun)/a * e_corr
    a_twin = ((G*(M_s+masses)*Msun)/(4*pi**2)*(2*P_orb*86400)**2)**(1/3)
    Ptra_twin = (radii*Rsun + R_s*Rsun)/a_twin * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(R_s*Rsun)
    r_twin = a_twin*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b_twin = r_twin*np.cos(incs*pi/180)/(R_s*Rsun)

    # find instances with collisions
    coll = ((radii*Rsun + R_s*Rsun) > a*(1-eccs))
    coll_twin = ((2*R_s*Rsun) > a_twin*(1-eccs))

    lnL = np.full(N, -np.inf)
    lnL_twin = np.full(N, -np.inf)

    if parallel:
        # q < 0.95
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll == False) & (qs < 0.95)
        # calculate lnL for transiting systems
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        companion_fluxratio = np.zeros(N)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_EB_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    P_orb[mask], incs[mask], a[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )

        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            fluxratios_lc_band = (
                flux_relation(masses, filt=ext_lc['filter'])
                / (flux_relation(masses, filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
            )
            ext_lc['lnL'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_EB_p(
                ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], radii[mask], fluxratios_lc_band[mask],
                P_orb[mask], incs[mask], a[mask], R_s_arr[mask],
                u1_arr_p[mask], u2_arr_p[mask],
                eccs[mask], argps[mask],
                companion_fluxratio=companion_fluxratio[mask],
                exptime=ext_lc['exptime'], nsamples=nsamples
            )
            lnL = lnL + ext_lc['lnL']

        # q >= 0.95
        inc_min = np.full(N, 90.)
        inc_min[Ptra_twin <= 1.] = np.arccos(
            Ptra_twin[Ptra_twin <= 1.]
            ) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll_twin == False) & (qs >= 0.95)
        # calculate lnL for transiting systems
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        companion_fluxratio = np.zeros(N)
        lnL_twin[mask] = -0.5*ln2pi - lnsigma - lnL_EB_twin_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )

        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            fluxratios_lc_band = (
                flux_relation(masses, filt=ext_lc['filter'])
                / (flux_relation(masses, filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
            )
            ext_lc['lnL_twin'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_EB_twin_p(
                ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], radii[mask], fluxratios_lc_band[mask],
                2*P_orb[mask], incs[mask], a_twin[mask], R_s_arr[mask],
                u1_arr_p[mask], u2_arr_p[mask],
                eccs[mask], argps[mask],
                companion_fluxratio=companion_fluxratio[mask],
                exptime=ext_lc['exptime'], nsamples=nsamples
            )
            lnL_twin = lnL_twin + ext_lc['lnL_twin']

    else:
        for i in range(N):
            # q < 0.95
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if (incs[i] >= inc_min) & (qs[i] < 0.95) & (coll[i] == False):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_EB(
                    time, flux, sigma, radii[i], fluxratios[i],
                    P_orb[i], incs[i], a[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )
            # q >= 0.95 and 2xP_orb
            if Ptra_twin[i] <= 1:
                inc_min = np.arccos(Ptra_twin[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] >= 0.95)
                & (coll_twin[i] == False)):
                lnL_twin[i] = -0.5*ln2pi - lnsigma - lnL_EB_twin(
                    time, flux, sigma, radii[i], fluxratios[i],
                    2*P_orb[i], incs[i], a_twin[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )

    # results for q < 0.95
    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL + lnz_const )
        ))
    lnZ = np.log(Z)

    # Modify the result dictionaries to include information for each external light curve
    res = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }

    # results for q >= 0.95 and 2xP_orb
    N_samples = 1000
    idx = (-lnL_twin).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL_twin + lnz_const )
        ))
    lnZ = np.log(Z)

    res_twin = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': 2*P_orb[idx],
        'inc': incs[idx],
        'b': b_twin[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }

    # Add results for each external light curve
    for i, ext_lc in enumerate(external_lcs):
        # res[f'lnZ_p{idx+1}'] = np.log(np.mean(np.nan_to_num(np.exp(ext_lc['lnL'] + lnz_const))))
        # idx is redefined in the loop
        res[f'u1_p{i+1}'] = np.full(N_samples, ext_lc['u1'])
        res[f'u2_p{i+1}'] = np.full(N_samples, ext_lc['u2'])
        res[f'fluxratio_EB_p{i+1}'] = flux_relation(res['M_EB'], filt=ext_lc['filter']) / (flux_relation(res['M_EB'], filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))

        # res_twin[f'lnZ_p{idx+1}'] = np.log(np.mean(np.nan_to_num(np.exp(ext_lc['lnL_twin'] + lnz_const))))
        res_twin[f'u1_p{i+1}'] = np.full(N_samples, ext_lc['u1'])
        res_twin[f'u2_p{i+1}'] = np.full(N_samples, ext_lc['u2'])
        res_twin[f'fluxratio_EB_p{i+1}'] = flux_relation(res_twin['M_EB'], filt=ext_lc['filter']) / (flux_relation(res_twin['M_EB'], filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))

    return res, res_twin


def lnZ_PTP(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Z: float, plx: float, contrast_curve_file: str = None,
            filt: str = "TESS",
            N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            molusc_file: str = None, external_lc_files: list = None,
            filt_lcs: list = None, lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the PTP scenario.
    Now supports up to four external light curves with different filters.

    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        plx (float): Target star parallax [mas].
        contrast_curve_file (string): Path to contrast curve file.
        filt (string): Photometric filter of contrast curve. Options
                         are TESS, Vis, J, H, and K.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
        external_lc_files (List[str]): List of external light curve file paths (up to 4).
        filt_lcs (List[str]): List of corresponding filters for external light curves.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
    """
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(low=P_orb[0], high=P_orb[-1], size=N)
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)
    a = ((G*M_s*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    logg = np.log10(G*(M_s*Msun)/(R_s*Rsun)**2)

    if mission == "TESS":
        ldc_Zs, ldc_Teffs, ldc_loggs, ldc_u1s, ldc_u2s = ldc_T_Zs, ldc_T_Teffs, ldc_T_loggs, ldc_T_u1s, ldc_T_u2s
    else:
        ldc_Zs, ldc_Teffs, ldc_loggs, ldc_u1s, ldc_u2s = ldc_K_Zs, ldc_K_Teffs, ldc_K_loggs, ldc_K_u1s, ldc_K_u2s

    this_Z = ldc_Zs[np.argmin(np.abs(ldc_Zs-Z))]
    this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teff))]
    this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-logg))]
    mask = (ldc_Zs == this_Z) & (ldc_Teffs == this_Teff) & (ldc_loggs == this_logg)
    u1, u2 = ldc_u1s[mask], ldc_u2s[mask]

    external_lcs = []
    if external_lc_files and filt_lcs:
        parallel = True  # Force parallel execution when external LCs are provided
        if len(external_lc_files) != len(filt_lcs):
            raise ValueError("Number of external LC files must match number of filters")
        if len(external_lc_files) > 4:
            raise ValueError("Maximum of 4 external light curves supported")

        for lc_file, filt in zip(external_lc_files, filt_lcs):
            ldc_map = {
                "J": (ldc_J_Zs, ldc_J_Teffs, ldc_J_loggs, ldc_J_u1s, ldc_J_u2s),
                "H": (ldc_H_Zs, ldc_H_Teffs, ldc_H_loggs, ldc_H_u1s, ldc_H_u2s),
                "K": (ldc_Kband_Zs, ldc_Kband_Teffs, ldc_Kband_loggs, ldc_Kband_u1s, ldc_Kband_u2s),
                "g": (ldc_gband_Zs, ldc_gband_Teffs, ldc_gband_loggs, ldc_gband_u1s, ldc_gband_u2s),
                "r": (ldc_rband_Zs, ldc_rband_Teffs, ldc_rband_loggs, ldc_rband_u1s, ldc_rband_u2s),
                "i": (ldc_iband_Zs, ldc_iband_Teffs, ldc_iband_loggs, ldc_iband_u1s, ldc_iband_u2s),
                "z": (ldc_zband_Zs, ldc_zband_Teffs, ldc_zband_loggs, ldc_zband_u1s, ldc_zband_u2s),
            }

            ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s = ldc_map[filt]

            this_Z_p = ldc_P_Zs[np.argmin(np.abs(ldc_P_Zs-Z))]
            this_Teff_p = ldc_P_Teffs[np.argmin(np.abs(ldc_P_Teffs-Teff))]
            this_logg_p = ldc_P_loggs[np.argmin(np.abs(ldc_P_loggs-logg))]
            mask_p = (ldc_P_Zs == this_Z_p) & (ldc_P_Teffs == this_Teff_p) & (ldc_P_loggs == this_logg_p)
            u1_p, u2_p = ldc_P_u1s[mask_p], ldc_P_u2s[mask_p]

            external_lc = np.loadtxt(lc_file)
            time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
            sigma_p = np.mean(fluxerr_p)
            lnsigma_p = np.log(sigma_p)
            exptime_p = np.min(np.diff(time_p))

            external_lcs.append({
                'time': time_p,
                'flux': flux_p,
                'sigma': sigma_p,
                'lnsigma': lnsigma_p,
                'exptime': exptime_p,
                'u1': u1_p,
                'u2': u2_p,
                'lnL': np.full(N, -np.inf),
                'filter': filt
            })

    if molusc_file is None:
        qs_comp = sample_q_companion(np.random.rand(N), M_s)
    else:
        molusc_df = read_csv(molusc_file)
        molusc_a = molusc_df["semi-major axis(AU)"].values
        molusc_e = molusc_df["eccentricity"].values
        molusc_df2 = molusc_df[molusc_a*(1-molusc_e) > 10]
        qs_comp = molusc_df2["mass ratio"].values
        qs_comp[qs_comp < 0.1/M_s] = 0.1/M_s
        qs_comp = np.pad(qs_comp, (0, N - len(qs_comp)))

    masses_comp = qs_comp*M_s
    radii_comp, Teffs_comp = stellar_relations(masses_comp, np.full(N, R_s), np.full(N, Teff))
    fluxratios_comp = flux_relation(masses_comp) / (flux_relation(masses_comp) + flux_relation(np.array([M_s])))

    if molusc_file is None:
        if contrast_curve_file is None:
            delta_mags = 2.5*np.log10(fluxratios_comp/(1-fluxratios_comp))
            lnprior_companion = lnprior_bound_TP(M_s, plx, np.abs(delta_mags), np.array([2.2]), np.array([1.0]))
            lnprior_companion[lnprior_companion > 0.0] = 0.0
            lnprior_companion[delta_mags > 0.0] = -np.inf
        else:
            fluxratios_comp_cc = flux_relation(masses_comp, filt) / (flux_relation(masses_comp, filt) + flux_relation(np.array([M_s]), filt))
            delta_mags = 2.5*np.log10(fluxratios_comp_cc/(1-fluxratios_comp_cc))
            separations, contrasts = file_to_contrast_curve(contrast_curve_file)
            lnprior_companion = lnprior_bound_TP(M_s, plx, np.abs(delta_mags), separations, contrasts)
            lnprior_companion[lnprior_companion > 0.0] = 0.0
            lnprior_companion[delta_mags > 0.0] = -np.inf
    else:
        lnprior_companion = np.zeros(N)

    rps = sample_rp(np.random.rand(N), np.full(N, M_s), flatpriors)
    incs = sample_inc(np.random.rand(N))
    eccs = sample_ecc(np.random.rand(N), planet=True, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(R_s*Rsun)

    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    Ptra = (rps*Rearth + R_s*Rsun)/a * e_corr

    coll = ((rps*Rearth + R_s*Rsun) > a*(1-eccs))

    lnL = np.full(N, -np.inf)

    if parallel:
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        mask = (incs >= inc_min) & (coll == False) & (qs_comp != 0.0)
        a_arr = np.full(N, a)
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_TP_p(
                    time, flux, sigma, rps[mask],
                    P_orb[mask], incs[mask], a_arr[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[mask],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )
        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            fluxratios_lc_band = flux_relation(masses_comp, filt=ext_lc['filter']) / (flux_relation(masses_comp, filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
            ext_lc['lnL'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_TP_p(
                    ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], rps[mask],
                    P_orb[mask], incs[mask], a_arr[mask], R_s_arr[mask],
                    u1_arr_p[mask], u2_arr_p[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_lc_band[mask],
                    companion_is_host=False,
                    exptime=ext_lc['exptime'], nsamples=nsamples
                    )
            lnL = lnL + ext_lc['lnL']
    else:
        for i in range(N):
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (coll[i] == False) & (qs_comp[i] != 0.0)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_TP(
                    time, flux, sigma, rps[i],
                    P_orb[i], incs[i], a[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[i],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )

    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(np.exp(lnL + lnprior_companion + lnz_const)))
    lnZ = np.log(Z)

    res = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': rps[idx],
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': np.zeros(N_samples),
        'R_EB': np.zeros(N_samples),
        'M_comp': masses_comp[idx],
        'R_comp': radii_comp[idx],
        'fluxratio_EB': np.zeros(N_samples),
        'fluxratio_comp': fluxratios_comp[idx],
        'lnZ': lnZ
    }

    # Add results for each external light curve
    for i, ext_lc in enumerate(external_lcs):
        res[f'u1_p{i+1}'] = np.full(N_samples, ext_lc['u1'])
        res[f'u2_p{i+1}'] = np.full(N_samples, ext_lc['u2'])
        #res[f'fluxratio_EB_p{i+1}'] = np.zeros(N_samples)
        res[f'fluxratio_comp_p{i+1}'] = flux_relation(res["M_comp"], filt=ext_lc['filter']) / (flux_relation(res["M_comp"], filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))

    return res


def lnZ_PEB(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Z: float, plx: float, contrast_curve_file: str = None,
            filt: str = "TESS",
            N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            molusc_file: str = None, external_lc_files: list = None,
            filt_lcs: list = None, lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the PEB scenario.
    Now supports multiple external light curves with different filters.

    Args:
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        plx (float): Target star parallax [mas].
        contrast_curve_file (string): Path to contrast curve file.
        filt (string): Photometric filter of contrast curve. Options
                         are TESS, Vis, J, H, and K.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
        external_lc_files (List[str]): List of external light curve file paths.
        filt_lcs (List[str]): List of corresponding filters for external light curves.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
        res_twin (dict): Best-fit properties and marginal likelihood.
    """
    # Sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(low=P_orb[0], high=P_orb[-1], size=N)
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)
    logg = np.log10(G*(M_s*Msun)/(R_s*Rsun)**2)

    # Determine target star limb darkening coefficients
    if mission == "TESS":
        ldc_Zs, ldc_Teffs, ldc_loggs, ldc_u1s, ldc_u2s = ldc_T_Zs, ldc_T_Teffs, ldc_T_loggs, ldc_T_u1s, ldc_T_u2s
    else:
        ldc_Zs, ldc_Teffs, ldc_loggs, ldc_u1s, ldc_u2s = ldc_K_Zs, ldc_K_Teffs, ldc_K_loggs, ldc_K_u1s, ldc_K_u2s

    this_Z = ldc_Zs[np.argmin(np.abs(ldc_Zs-Z))]
    this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teff))]
    this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-logg))]
    mask = (ldc_Zs == this_Z) & (ldc_Teffs == this_Teff) & (ldc_loggs == this_logg)
    u1, u2 = ldc_u1s[mask], ldc_u2s[mask]

    external_lcs = []
    if external_lc_files and filt_lcs:
        parallel = True  # Force parallel execution when external LCs are provided
        if len(external_lc_files) != len(filt_lcs):
            raise ValueError("Number of external LC files must match number of filters")
        if len(external_lc_files) > 4:
            raise ValueError("Maximum of 4 external light curves supported")

        for lc_file, filt in zip(external_lc_files, filt_lcs):
            ldc_map = {
                "J": (ldc_J_Zs, ldc_J_Teffs, ldc_J_loggs, ldc_J_u1s, ldc_J_u2s),
                "H": (ldc_H_Zs, ldc_H_Teffs, ldc_H_loggs, ldc_H_u1s, ldc_H_u2s),
                "K": (ldc_Kband_Zs, ldc_Kband_Teffs, ldc_Kband_loggs, ldc_Kband_u1s, ldc_Kband_u2s),
                "g": (ldc_gband_Zs, ldc_gband_Teffs, ldc_gband_loggs, ldc_gband_u1s, ldc_gband_u2s),
                "r": (ldc_rband_Zs, ldc_rband_Teffs, ldc_rband_loggs, ldc_rband_u1s, ldc_rband_u2s),
                "i": (ldc_iband_Zs, ldc_iband_Teffs, ldc_iband_loggs, ldc_iband_u1s, ldc_iband_u2s),
                "z": (ldc_zband_Zs, ldc_zband_Teffs, ldc_zband_loggs, ldc_zband_u1s, ldc_zband_u2s),
            }

            ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s = ldc_map[filt]

            this_Z_p = ldc_P_Zs[np.argmin(np.abs(ldc_P_Zs-Z))]
            this_Teff_p = ldc_P_Teffs[np.argmin(np.abs(ldc_P_Teffs-Teff))]
            this_logg_p = ldc_P_loggs[np.argmin(np.abs(ldc_P_loggs-logg))]
            mask_p = (ldc_P_Zs == this_Z_p) & (ldc_P_Teffs == this_Teff_p) & (ldc_P_loggs == this_logg_p)
            u1_p, u2_p = ldc_P_u1s[mask_p], ldc_P_u2s[mask_p]

            external_lc = np.loadtxt(lc_file)
            time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
            sigma_p = np.mean(fluxerr_p)
            lnsigma_p = np.log(sigma_p)
            exptime_p = np.min(np.diff(time_p))

            external_lcs.append({
                'time': time_p,
                'flux': flux_p,
                'sigma': sigma_p,
                'lnsigma': lnsigma_p,
                'exptime': exptime_p,
                'u1': u1_p,
                'u2': u2_p,
                'lnL': np.full(N, -np.inf),
                'lnL_twin': np.full(N, -np.inf),
                'filter': filt
            })

    # sample from prior distributions
    incs = sample_inc(np.random.rand(N))
    qs = sample_q(np.random.rand(N), M_s)
    eccs = sample_ecc(np.random.rand(N), planet=False, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    if molusc_file is None:
        qs_comp = sample_q_companion(np.random.rand(N), M_s)
    else:
        molusc_df = read_csv(molusc_file)
        molusc_a = molusc_df["semi-major axis(AU)"].values
        molusc_e = molusc_df["eccentricity"].values
        molusc_df2 = molusc_df[molusc_a*(1-molusc_e) > 10]
        qs_comp = molusc_df2["mass ratio"].values
        qs_comp[qs_comp < 0.1/M_s] = 0.1/M_s
        qs_comp = np.pad(qs_comp, (0, N - len(qs_comp)))

    # calculate properties of the drawn EBs
    masses = qs*M_s
    radii, Teffs = stellar_relations(
        masses, np.full(N, R_s), np.full(N, Teff)
        )
    # calculate flux ratios in the TESS band
    fluxratios = (
        flux_relation(masses)
        / (flux_relation(masses) + flux_relation(np.array([M_s])))
        )

    # calculate properties of the drawn companions
    masses_comp = qs_comp*M_s
    radii_comp, Teffs_comp = stellar_relations(
        masses_comp, np.full(N, R_s), np.full(N, Teff)
        )
    # calculate flux ratios in the TESS band
    fluxratios_comp = (
        flux_relation(masses_comp)
        / (flux_relation(masses_comp) + flux_relation(np.array([M_s])))
        )

    # calculate priors for companions
    if molusc_file is None:
        if contrast_curve_file is None:
            delta_mags = 2.5*np.log10(
                    fluxratios_comp/(1-fluxratios_comp)
                    )
            lnprior_companion = lnprior_bound_EB(
                M_s, plx, np.abs(delta_mags),
                np.array([2.2]), np.array([1.0])
                )
            lnprior_companion[lnprior_companion > 0.0] = 0.0
            lnprior_companion[delta_mags > 0.0] = -np.inf
        else:
            # use flux ratio of contrast curve filter
            fluxratios_comp_cc = (
                flux_relation(masses_comp, filt)
                / (flux_relation(masses_comp, filt)
                    + flux_relation(np.array([M_s]), filt))
                )
            delta_mags = 2.5*np.log10(
                fluxratios_comp_cc/(1-fluxratios_comp_cc)
                )
            separations, contrasts = file_to_contrast_curve(
                contrast_curve_file
                )
            lnprior_companion = lnprior_bound_EB(
                M_s, plx, np.abs(delta_mags), separations, contrasts
                )
            lnprior_companion[lnprior_companion > 0.0] = 0.0
            lnprior_companion[delta_mags > 0.0] = -np.inf
    else:
        lnprior_companion = np.zeros(N)

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = ((G*(M_s+masses)*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    Ptra = (radii*Rsun + R_s*Rsun)/a * e_corr
    a_twin = ((G*(M_s+masses)*Msun)/(4*pi**2)*(2*P_orb*86400)**2)**(1/3)
    Ptra_twin = (radii*Rsun + R_s*Rsun)/a_twin * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(R_s*Rsun)
    r_twin = a_twin*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b_twin = r_twin*np.cos(incs*pi/180)/(R_s*Rsun)

    # find instances with collisions
    coll = ((radii*Rsun + R_s*Rsun) > a*(1-eccs))
    coll_twin = ((2*R_s*Rsun) > a_twin*(1-eccs))

    lnL = np.full(N, -np.inf)
    lnL_twin = np.full(N, -np.inf)

    if parallel:
        # q < 0.95
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        mask = ((incs >= inc_min) & (coll == False) & (qs < 0.95) & (qs_comp != 0.0))
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_EB_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    P_orb[mask], incs[mask], a[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[mask],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )
        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            fluxratios_lc_band = flux_relation(masses, filt=ext_lc['filter']) / (flux_relation(masses, filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
            fluxratios_comp_lc_band = flux_relation(masses_comp, filt=ext_lc['filter']) / (flux_relation(masses_comp, filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
            ext_lc['lnL'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_EB_p(
                    ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], radii[mask], fluxratios_lc_band[mask],
                    P_orb[mask], incs[mask], a[mask], R_s_arr[mask],
                    u1_arr_p[mask], u2_arr_p[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp_lc_band[mask],
                    companion_is_host=False,
                    exptime=ext_lc['exptime'], nsamples=nsamples
                    )
            lnL = lnL + ext_lc['lnL']

        # q >= 0.95
        inc_min = np.full(N, 90.)
        inc_min[Ptra_twin <= 1.] = np.arccos(Ptra_twin[Ptra_twin <= 1.]) * 180./pi
        mask = ((incs >= inc_min) & (coll_twin == False) & (qs >= 0.95) & (qs_comp != 0.0))
        lnL_twin[mask] = -0.5*ln2pi - lnsigma - lnL_EB_twin_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[mask],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )
        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            fluxratios_lc_band = flux_relation(masses, filt=ext_lc['filter']) / (flux_relation(masses, filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
            fluxratios_comp_lc_band = flux_relation(masses_comp, filt=ext_lc['filter']) / (flux_relation(masses_comp, filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
            ext_lc['lnL_twin'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_EB_twin_p(
                    ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], radii[mask], fluxratios_lc_band[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], R_s_arr[mask],
                    u1_arr_p[mask], u2_arr_p[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp_lc_band[mask],
                    companion_is_host=False,
                    exptime=ext_lc['exptime'], nsamples=nsamples
                    )
            lnL_twin = lnL_twin + ext_lc['lnL_twin']
    else:
        for i in range(N):
            # q < 0.95
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] < 0.95)
                & (coll[i] == False) & (qs_comp[i] != 0)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_EB(
                    time, flux, sigma, radii[i], fluxratios[i],
                    P_orb[i], incs[i], a[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[i],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )
            # q >= 0.95 and 2xP_orb
            if Ptra_twin[i] <= 1:
                inc_min = np.arccos(Ptra_twin[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] >= 0.95)
                & (coll_twin[i] == False) & (qs_comp[i] != 0)):
                lnL_twin[i] = -0.5*ln2pi - lnsigma - lnL_EB_twin(
                    time, flux, sigma, radii[i], fluxratios[i],
                    2*P_orb[i], incs[i], a_twin[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[i],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )

    # results for q < 0.95
    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    res = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'M_comp': masses_comp[idx],
        'R_comp': radii_comp[idx],
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': fluxratios_comp[idx],
        'lnZ': lnZ
    }

    # results for q >= 0.95 and 2xP_orb
    N_samples = 1000
    idx = (-lnL_twin).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL_twin + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    res_twin = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': 2*P_orb[idx],
        'inc': incs[idx],
        'b': b_twin[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'M_comp': masses_comp[idx],
        'R_comp': radii_comp[idx],
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': fluxratios_comp[idx],
        'lnZ': lnZ
    }

    # Add results for each external light curve
    # we probably don't want these. They should have an idx
    for i, ext_lc in enumerate(external_lcs):
        res[f'u1_p{i+1}'] = np.full(N_samples, ext_lc['u1'])
        res[f'u2_p{i+1}'] = np.full(N_samples, ext_lc['u2'])
        res[f'fluxratio_EB_p{i+1}'] = flux_relation(res['M_EB'], filt=ext_lc['filter']) / (flux_relation(res['M_EB'], filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
        res[f'fluxratio_comp_p{i+1}'] = flux_relation(res['M_comp'], filt=ext_lc['filter']) / (flux_relation(res['M_comp'], filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))

        res_twin[f'u1_p{i+1}'] = np.full(N_samples, ext_lc['u1'])
        res_twin[f'u2_p{i+1}'] = np.full(N_samples, ext_lc['u2'])
        res_twin[f'fluxratio_EB_p{i+1}'] = flux_relation(res_twin['M_EB'], filt=ext_lc['filter']) / (flux_relation(res_twin['M_EB'], filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))
        res_twin[f'fluxratio_comp_p{i+1}'] = flux_relation(res_twin['M_comp'], filt=ext_lc['filter']) / (flux_relation(res_twin['M_comp'], filt=ext_lc['filter']) + flux_relation(np.array([M_s]), filt=ext_lc['filter']))

    return res, res_twin


def lnZ_STP(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float, Z: float,
            plx: float, contrast_curve_file: str = None,
            filt: str = "TESS",
            N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            molusc_file: str = None, external_lc_files: list = None,
            filt_lcs: list = None, lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the STP scenario.
    Now supports multiple external light curves with different filters.

    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        plx (float): Target star parallax [mas].
        contrast_curve_file (string): contrast curve file.
        filt (string): Photometric filter of contrast curve. Options
                         are TESS, Vis, J, H, and K.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
        external_lc_files (List[str]): List of paths to external light curves (up to 4).
        filt_lcs (List[str]): List of photometric filters for external light curves.
            Options are J, H, K, g, r, i, and z.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)

    # sample from q prior distribution
    if molusc_file is None:
        qs_comp = sample_q_companion(np.random.rand(N), M_s)
    else:
        molusc_df = read_csv(molusc_file)
        molusc_a = molusc_df["semi-major axis(AU)"].values
        molusc_e = molusc_df["eccentricity"].values
        molusc_df2 = molusc_df[molusc_a*(1-molusc_e) > 10]
        qs_comp = molusc_df2["mass ratio"].values
        qs_comp[qs_comp < 0.1/M_s] = 0.1/M_s
        qs_comp = np.pad(qs_comp, (0, N - len(qs_comp)))

    # calculate properties of the drawn companions
    masses_comp = qs_comp*M_s
    radii_comp, Teffs_comp = stellar_relations(
        masses_comp, np.full(N, R_s), np.full(N, Teff)
        )
    loggs_comp = np.log10(G*(masses_comp*Msun)/(radii_comp*Rsun)**2)
    # calculate flux ratios in the TESS band
    fluxratios_comp = (
        flux_relation(masses_comp)
        / (flux_relation(masses_comp) + flux_relation(np.array([M_s])))
        )

    # calculate limb darkening ceofficients for companions
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
        ldc_at_Z = ldc_T[(ldc_Zs == ldc_Zs[np.abs(ldc_Zs - Z).argmin()])]
        Teffs_at_Z = np.array(ldc_at_Z.Teff, dtype=int)
        loggs_at_Z = np.array(ldc_at_Z.logg, dtype=float)
        u1s_at_Z = np.array(ldc_at_Z.aLSM, dtype=float)
        u2s_at_Z = np.array(ldc_at_Z.bLSM, dtype=float)
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s
        ldc_at_Z = ldc_K[(ldc_Zs == ldc_Zs[np.abs(ldc_Zs - Z).argmin()])]
        Teffs_at_Z = np.array(ldc_at_Z.Teff, dtype=int)
        loggs_at_Z = np.array(ldc_at_Z.logg, dtype=float)
        u1s_at_Z = np.array(ldc_at_Z.a, dtype=float)
        u2s_at_Z = np.array(ldc_at_Z.b, dtype=float)

    rounded_loggs_comp = np.round(loggs_comp/0.5) * 0.5
    rounded_loggs_comp[rounded_loggs_comp < 3.5] = 3.5
    rounded_loggs_comp[rounded_loggs_comp > 5.0] = 5.0
    rounded_Teffs_comp = np.round(Teffs_comp/250) * 250
    rounded_Teffs_comp[rounded_Teffs_comp < 3500] = 3500
    rounded_Teffs_comp[rounded_Teffs_comp > 10000] = 10000
    u1s_comp, u2s_comp = np.zeros(N), np.zeros(N)

    for i, (comp_Teff, comp_logg) in enumerate(
            zip(rounded_Teffs_comp, rounded_loggs_comp)
            ):
        mask = (Teffs_at_Z == comp_Teff) & (loggs_at_Z == comp_logg)
        u1s_comp[i], u2s_comp[i] = u1s_at_Z[mask], u2s_at_Z[mask]

    external_lcs = []
    if external_lc_files and filt_lcs:
        parallel = True
        if len(external_lc_files) != len(filt_lcs):
            raise ValueError("Number of external LC files must match number of filters")
        if len(external_lc_files) > 4:
            raise ValueError("Maximum of 4 external light curves supported")

        for lc_file, filt in zip(external_lc_files, filt_lcs):
            ldc_map = {
                "J": (ldc_J, ldc_J_Zs, ldc_J_Teffs, ldc_J_loggs, ldc_J_u1s, ldc_J_u2s),
                "H": (ldc_H, ldc_H_Zs, ldc_H_Teffs, ldc_H_loggs, ldc_H_u1s, ldc_H_u2s),
                "K": (ldc_Kband, ldc_Kband_Zs, ldc_Kband_Teffs, ldc_Kband_loggs, ldc_Kband_u1s, ldc_Kband_u2s),
                "g": (ldc_gband, ldc_gband_Zs, ldc_gband_Teffs, ldc_gband_loggs, ldc_gband_u1s, ldc_gband_u2s),
                "r": (ldc_rband, ldc_rband_Zs, ldc_rband_Teffs, ldc_rband_loggs, ldc_rband_u1s, ldc_rband_u2s),
                "i": (ldc_iband, ldc_iband_Zs, ldc_iband_Teffs, ldc_iband_loggs, ldc_iband_u1s, ldc_iband_u2s),
                "z": (ldc_zband, ldc_zband_Zs, ldc_zband_Teffs, ldc_zband_loggs, ldc_zband_u1s, ldc_zband_u2s),
            }

            ldc_P, ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s = ldc_map[filt]
            ldc_at_Z_p = ldc_P[(ldc_P_Zs == ldc_P_Zs[np.abs(ldc_P_Zs - Z).argmin()])]
            Teffs_at_Z_p = np.array(ldc_at_Z_p.Teff, dtype=int)
            loggs_at_Z_p = np.array(ldc_at_Z_p.logg, dtype=float)
            u1s_at_Z_p = np.array(ldc_at_Z_p.aLSM, dtype=float)
            u2s_at_Z_p = np.array(ldc_at_Z_p.bLSM, dtype=float)

            u1s_comp_p, u2s_comp_p = np.zeros(N), np.zeros(N)
            for i, (comp_Teff, comp_logg) in enumerate(zip(rounded_Teffs_comp, rounded_loggs_comp)):
                mask_p = (Teffs_at_Z_p == comp_Teff) & (loggs_at_Z_p == comp_logg)
                u1s_comp_p[i], u2s_comp_p[i] = u1s_at_Z_p[mask_p], u2s_at_Z_p[mask_p]

            external_lc = np.loadtxt(lc_file)
            time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
            sigma_p = np.mean(fluxerr_p)
            lnsigma_p = np.log(sigma_p)
            exptime_p = np.min(np.diff(time_p))

            fluxratios_comp_lc_band = (
                flux_relation(masses_comp, filt=filt)
                / (flux_relation(masses_comp, filt=filt) + flux_relation(np.array([M_s]), filt=filt))
            )

            external_lcs.append({
                'time': time_p,
                'flux': flux_p,
                'sigma': sigma_p,
                'lnsigma': lnsigma_p,
                'exptime': exptime_p,
                'u1s_comp': u1s_comp_p,
                'u2s_comp': u2s_comp_p,
                'fluxratios': fluxratios_comp_lc_band,
                'lnL': np.full(N, -np.inf),
                'filter': filt
            })

    # calculate priors for companions
    if molusc_file is None:
        if contrast_curve_file is None:
            delta_mags = 2.5*np.log10(
                    fluxratios_comp/(1-fluxratios_comp)
                    )
            lnprior_companion = lnprior_bound_TP(
                M_s, plx, np.abs(delta_mags),
                np.array([2.2]), np.array([1.0])
                )
            lnprior_companion[lnprior_companion > 0.0] = 0.0
            lnprior_companion[delta_mags > 0.0] = -np.inf
        else:
            # use flux ratio of contrast curve filter
            fluxratios_comp_cc = (
                flux_relation(masses_comp, filt)
                / (flux_relation(masses_comp, filt)
                    + flux_relation(np.array([M_s]), filt))
                )
            delta_mags = 2.5*np.log10(fluxratios_comp_cc/(1-fluxratios_comp_cc))
            separations, contrasts = file_to_contrast_curve(
                contrast_curve_file
                )
            lnprior_companion = lnprior_bound_TP(
                M_s, plx, np.abs(delta_mags), separations, contrasts
                )
            lnprior_companion[lnprior_companion > 0.0] = 0.0
            lnprior_companion[delta_mags > 0.0] = -np.inf
    else:
        lnprior_companion = np.zeros(N)

    # sample from prior distributions
    rps = sample_rp(np.random.rand(N), masses_comp, flatpriors)
    incs = sample_inc(np.random.rand(N))
    eccs = sample_ecc(np.random.rand(N), planet=True, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = ((G*masses_comp*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    Ptra = (rps*Rearth + radii_comp*Rsun)/a * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(radii_comp*Rsun)

    # find instances with collisions
    coll = ((rps*Rearth + radii_comp*Rsun) > a*(1-eccs))
    lnL = np.full(N, -np.inf)

    if parallel:
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll == False) & (qs_comp != 0.0)
        # calculate lnL for transiting systems
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_TP_p(
                    time, flux, sigma, rps[mask],
                    P_orb[mask], incs[mask], a[mask], radii_comp[mask],
                    u1s_comp[mask], u2s_comp[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[mask],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )

        for ext_lc in external_lcs:
            ext_lc['lnL'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_TP_p(
                ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], rps[mask],
                P_orb[mask], incs[mask], a[mask], radii_comp[mask],
                ext_lc['u1s_comp'][mask], ext_lc['u2s_comp'][mask],
                eccs[mask], argps[mask],
                companion_fluxratio=ext_lc['fluxratios'][mask],
                companion_is_host=True,
                exptime=ext_lc['exptime'], nsamples=nsamples
            )
            lnL = lnL + ext_lc['lnL']
    else:
        for i in range(N):
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (coll[i] == False)
                & (qs_comp[i] != 0.0)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_TP(
                    time, flux, sigma, rps[i],
                    P_orb[i], incs[i], a[i], radii_comp[i],
                    u1s_comp[i], u2s_comp[i],
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[i],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )

    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    res = {
        'M_s': masses_comp[idx],
        'R_s': radii_comp[idx],
        'u1': u1s_comp[idx],
        'u2': u2s_comp[idx],
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': rps[idx],
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': np.zeros(N_samples),
        'R_EB': np.zeros(N_samples),
        'M_comp': np.full(N_samples, M_s),
        'R_comp': np.full(N_samples, R_s),
        'fluxratio_EB': np.zeros(N_samples),
        'fluxratio_comp': fluxratios_comp[idx],
        'lnZ': lnZ
    }

    # Add results for each external light curve
    for i, ext_lc in enumerate(external_lcs):
        res[f'u1_p{i+1}'] = ext_lc['u1s_comp'][idx]
        res[f'u2_p{i+1}'] = ext_lc['u2s_comp'][idx]
        res[f'fluxratio_EB_p{i+1}'] = np.zeros(N_samples)
        res[f'fluxratio_comp_p{i+1}'] = ext_lc['fluxratios'][idx]

    return res


def lnZ_SEB(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Z: float, plx: float, contrast_curve_file: str = None,
            filt: str = "TESS",
            N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            molusc_file: str = None, external_lc_files: list = None,
            filt_lcs: list = None, lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the SEB scenario.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        plx (float): Target star parallax [mas].
        contrast_curve_file (string): Path to contrast curve file.
        filt (string): Photometric filter of contrast curve. Options
                         are TESS, Vis, J, H, and K.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        external_lc_files (List[str]): List of paths to external light curves (up to 4).
        filt_lcs (List[str]): List of photometric filters for external light curves.
            Options are J, H, K, g, r, i, and z.
        nsamples (int): Sampling rate for supersampling.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
        res_twin (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)

    # sample from prior distributions
    incs = sample_inc(np.random.rand(N))
    qs = sample_q(np.random.rand(N), M_s)
    eccs = sample_ecc(np.random.rand(N), planet=False, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))
    if molusc_file is None:
        qs_comp = sample_q_companion(np.random.rand(N), M_s)
    else:
        molusc_df = read_csv(molusc_file)
        molusc_a = molusc_df["semi-major axis(AU)"].values
        molusc_e = molusc_df["eccentricity"].values
        molusc_df2 = molusc_df[molusc_a*(1-molusc_e) > 10]
        qs_comp = molusc_df2["mass ratio"].values
        qs_comp[qs_comp < 0.1/M_s] = 0.1/M_s
        qs_comp = np.pad(qs_comp, (0, N - len(qs_comp)))

    # calculate properties of the drawn companions
    masses_comp = qs_comp*M_s
    radii_comp, Teffs_comp = stellar_relations(
        masses_comp, np.full(N, R_s), np.full(N, Teff)
        )
    loggs_comp = np.log10(G*(masses_comp*Msun)/(radii_comp*Rsun)**2)
    # calculate flux ratios in the TESS band
    fluxratios_comp = (
        flux_relation(masses_comp)
        / (flux_relation(masses_comp) + flux_relation(np.array([M_s])))
        )

    # calculate limb darkening ceofficients for companions
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
        ldc_at_Z = ldc_T[(ldc_Zs == ldc_Zs[np.abs(ldc_Zs - Z).argmin()])]
        Teffs_at_Z = np.array(ldc_at_Z.Teff, dtype=int)
        loggs_at_Z = np.array(ldc_at_Z.logg, dtype=float)
        u1s_at_Z = np.array(ldc_at_Z.aLSM, dtype=float)
        u2s_at_Z = np.array(ldc_at_Z.bLSM, dtype=float)
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s
        ldc_at_Z = ldc_K[(ldc_Zs == ldc_Zs[np.abs(ldc_Zs - Z).argmin()])]
        Teffs_at_Z = np.array(ldc_at_Z.Teff, dtype=int)
        loggs_at_Z = np.array(ldc_at_Z.logg, dtype=float)
        u1s_at_Z = np.array(ldc_at_Z.a, dtype=float)
        u2s_at_Z = np.array(ldc_at_Z.b, dtype=float)

    rounded_loggs_comp = np.round(loggs_comp/0.5) * 0.5
    rounded_loggs_comp[rounded_loggs_comp < 3.5] = 3.5
    rounded_loggs_comp[rounded_loggs_comp > 5.0] = 5.0
    rounded_Teffs_comp = np.round(Teffs_comp/250) * 250
    rounded_Teffs_comp[rounded_Teffs_comp < 3500] = 3500
    rounded_Teffs_comp[rounded_Teffs_comp > 13000] = 13000
    u1s_comp, u2s_comp = np.zeros(N), np.zeros(N)
    u1s_comp_p, u2s_comp_p = np.zeros(N), np.zeros(N) # this is for the external_lc data

    for i, (comp_Teff, comp_logg) in enumerate(
            zip(rounded_Teffs_comp, rounded_loggs_comp)
            ):
        mask = (Teffs_at_Z == comp_Teff) & (loggs_at_Z == comp_logg)
        u1s_comp[i], u2s_comp[i] = u1s_at_Z[mask], u2s_at_Z[mask]

    # calculate properties of the drawn EBs
    masses = qs*masses_comp
    radii, Teffs = stellar_relations(masses, radii_comp, Teffs_comp)
    # calculate flux ratios in the TESS band
    fluxratios = (
        flux_relation(masses)
        / (flux_relation(masses) + flux_relation(np.array([M_s])))
        )

    # external light curve code
    # need ldc_P, ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s. Done
    # need for i, (comp_Teff, comp_logg) in enumerate. Done
    # need fluxratios_lc_band. Done
    # meed fluxratios_comp_lc_band. Done
    external_lcs = []
    if external_lc_files and filt_lcs:
        parallel = True
        if len(external_lc_files) != len(filt_lcs):
            raise ValueError("Number of external LC files must match number of filters")
        if len(external_lc_files) > 4:
            raise ValueError("Maximum of 4 external light curves supported")

        for lc_file, filt in zip(external_lc_files, filt_lcs):
            ldc_map = {
                "J": (ldc_J, ldc_J_Zs, ldc_J_Teffs, ldc_J_loggs, ldc_J_u1s, ldc_J_u2s),
                "H": (ldc_H, ldc_H_Zs, ldc_H_Teffs, ldc_H_loggs, ldc_H_u1s, ldc_H_u2s),
                "K": (ldc_Kband, ldc_Kband_Zs, ldc_Kband_Teffs, ldc_Kband_loggs, ldc_Kband_u1s, ldc_Kband_u2s),
                "g": (ldc_gband, ldc_gband_Zs, ldc_gband_Teffs, ldc_gband_loggs, ldc_gband_u1s, ldc_gband_u2s),
                "r": (ldc_rband, ldc_rband_Zs, ldc_rband_Teffs, ldc_rband_loggs, ldc_rband_u1s, ldc_rband_u2s),
                "i": (ldc_iband, ldc_iband_Zs, ldc_iband_Teffs, ldc_iband_loggs, ldc_iband_u1s, ldc_iband_u2s),
                "z": (ldc_zband, ldc_zband_Zs, ldc_zband_Teffs, ldc_zband_loggs, ldc_zband_u1s, ldc_zband_u2s),
            }

            ldc_P, ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s = ldc_map[filt]
            ldc_at_Z_p = ldc_P[(ldc_P_Zs == ldc_P_Zs[np.abs(ldc_P_Zs - Z).argmin()])]
            Teffs_at_Z_p = np.array(ldc_at_Z_p.Teff, dtype=int)
            loggs_at_Z_p = np.array(ldc_at_Z_p.logg, dtype=float)
            u1s_at_Z_p = np.array(ldc_at_Z_p.aLSM, dtype=float)
            u2s_at_Z_p = np.array(ldc_at_Z_p.bLSM, dtype=float)

            u1s_comp_p, u2s_comp_p = np.zeros(N), np.zeros(N)
            for i, (comp_Teff, comp_logg) in enumerate(zip(rounded_Teffs_comp, rounded_loggs_comp)):
                mask_p = (Teffs_at_Z_p == comp_Teff) & (loggs_at_Z_p == comp_logg)
                u1s_comp_p[i], u2s_comp_p[i] = u1s_at_Z_p[mask_p], u2s_at_Z_p[mask_p]

            external_lc = np.loadtxt(lc_file)
            time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
            sigma_p = np.mean(fluxerr_p)
            lnsigma_p = np.log(sigma_p)
            exptime_p = np.min(np.diff(time_p))

            fluxratios_lc_band = (
                flux_relation(masses, filt=filt)
                / (flux_relation(masses, filt=filt) + flux_relation(np.array([M_s]), filt=filt))
                )

            fluxratios_comp_lc_band = (
                flux_relation(masses_comp, filt=filt)
                / (flux_relation(masses_comp, filt=filt) + flux_relation(np.array([M_s]), filt=filt))
            )

            external_lcs.append({
                'time': time_p,
                'flux': flux_p,
                'sigma': sigma_p,
                'lnsigma': lnsigma_p,
                'exptime': exptime_p,
                'u1s_comp': u1s_comp_p,
                'u2s_comp': u2s_comp_p,
                'fluxratios': fluxratios_lc_band,
                'fluxratios_comp': fluxratios_comp_lc_band,
                'lnL': np.full(N, -np.inf),
                'lnL_twin': np.full(N, -np.inf),
                'filter': filt
            })

    # calculate priors for companions
    if molusc_file is None:
        if contrast_curve_file is None:
            # use TESS/Vis band flux ratios
            delta_mags = 2.5*np.log10(
                (fluxratios_comp/(1-fluxratios_comp))
                + (fluxratios/(1-fluxratios))
                )
            lnprior_companion = lnprior_bound_EB(
                M_s, plx, np.abs(delta_mags),
                np.array([2.2]), np.array([1.0])
                )
            lnprior_companion[lnprior_companion > 0.0] = 0.0
            lnprior_companion[delta_mags > 0.0] = -np.inf
        else:
            # use flux ratio of contrast curve filter
            fluxratios_cc = (
                flux_relation(masses, filt)
                / (flux_relation(masses, filt)
                    + flux_relation(np.array([M_s]), filt))
                )
            fluxratios_comp_cc = (
                flux_relation(masses_comp, filt)
                / (flux_relation(masses_comp, filt)
                    + flux_relation(np.array([M_s]), filt))
                )
            delta_mags = 2.5*np.log10(
                (fluxratios_comp_cc/(1-fluxratios_comp_cc))
                + (fluxratios_cc/(1-fluxratios_cc))
                )
            separations, contrasts = file_to_contrast_curve(
                contrast_curve_file
                )
            lnprior_companion = lnprior_bound_EB(
                M_s, plx, np.abs(delta_mags), separations, contrasts
                )
            lnprior_companion[lnprior_companion > 0.0] = 0.0
            lnprior_companion[delta_mags > 0.0] = -np.inf
    else:
        lnprior_companion = np.zeros(N)

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = (
        (G*(masses_comp+masses)*Msun)/(4*pi**2)*(P_orb*86400)**2
        )**(1/3)
    Ptra = (radii*Rsun + radii_comp*Rsun)/a * e_corr
    a_twin = (
        (G*(masses_comp+masses)*Msun)/(4*pi**2)*(2*P_orb*86400)**2
        )**(1/3)
    Ptra_twin = (radii*Rsun + radii_comp*Rsun)/a_twin * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(radii_comp*Rsun)
    r_twin = a_twin*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b_twin = r_twin*np.cos(incs*pi/180)/(radii_comp*Rsun)

    # find instances with collisions
    coll = ((radii*Rsun + radii_comp*Rsun) > a*(1-eccs))
    coll_twin = ((2*radii_comp*Rsun) > a_twin*(1-eccs))

    lnL = np.full(N, -np.inf)
    lnL_twin = np.full(N, -np.inf)

    if parallel:
        # q < 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = ((incs >= inc_min) & (coll == False)
            & (qs < 0.95) & (qs_comp != 0.0))
        # calculate lnL for transiting systems
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_EB_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    P_orb[mask], incs[mask], a[mask], radii_comp[mask],
                    u1s_comp[mask], u2s_comp[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[mask],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )
        for ext_lc in external_lcs:
            ext_lc['lnL'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_EB_p(
                    ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], radii[mask], ext_lc['fluxratios'][mask],
                    P_orb[mask], incs[mask], a[mask], radii_comp[mask],
                    ext_lc['u1s_comp'][mask], ext_lc['u2s_comp'][mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=ext_lc['fluxratios_comp'][mask],
                    companion_is_host=True,
                    exptime=ext_lc['exptime'], nsamples=nsamples
                    )
            lnL = lnL + ext_lc['lnL']

        # q >= 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra_twin <= 1.] = np.arccos(
            Ptra_twin[Ptra_twin <= 1.]
            ) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = ((incs >= inc_min) & (coll_twin == False)
            & (qs >= 0.95) & (qs_comp != 0.0))
        # calculate lnL for transiting systems
        lnL_twin[mask] = -0.5*ln2pi - lnsigma - lnL_EB_twin_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], radii_comp[mask],
                    u1s_comp[mask], u2s_comp[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[mask],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )
        for ext_lc in external_lcs:
            ext_lc['lnL_twin'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_EB_twin_p(
                    ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], radii[mask], ext_lc['fluxratios'][mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], radii_comp[mask],
                    ext_lc['u1s_comp'][mask], ext_lc['u2s_comp'][mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=ext_lc['fluxratios_comp'][mask],
                    companion_is_host=True,
                    exptime=ext_lc['exptime'], nsamples=nsamples
                    )
            lnL_twin = lnL_twin + ext_lc['lnL_twin']
    else:
        for i in range(N):
            # q < 0.95
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] < 0.95)
                & (coll[i] == False) & (qs_comp[i] != 0.0)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_EB(
                    time, flux, sigma, radii[i], fluxratios[i],
                    P_orb[i], incs[i], a[i], radii_comp[i],
                    u1s_comp[i], u2s_comp[i],
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[i],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )
            # q >= 0.95 and 2xP_orb
            if Ptra_twin[i] <= 1:
                inc_min = np.arccos(Ptra_twin[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] >= 0.95)
                & (coll_twin[i] == False) & (qs_comp[i] != 0.0)):
                lnL_twin[i] = -0.5*ln2pi - lnsigma - lnL_EB_twin(
                    time, flux, sigma, radii[i], fluxratios[i],
                    2*P_orb[i], incs[i], a_twin[i], radii_comp[i],
                    u1s_comp[i], u2s_comp[i],
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[i],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )


    # results for q < 0.95
    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    res = {
        'M_s': masses_comp[idx],
        'R_s': radii_comp[idx],
        'u1': u1s_comp[idx],
        'u2': u2s_comp[idx],
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'M_comp': np.full(N_samples, M_s),
        'R_comp': np.full(N_samples, R_s),
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': fluxratios_comp[idx],
        'lnZ': lnZ
        }

    # Add results for each external light curve
    for i, ext_lc in enumerate(external_lcs):
        res[f'u1_p{i+1}'] = ext_lc['u1s_comp'][idx]
        res[f'u2_p{i+1}'] = ext_lc['u2s_comp'][idx]
        res[f'fluxratio_EB_p{i+1}'] = ext_lc['fluxratios'][idx]
        res[f'fluxratio_comp_p{i+1}'] = ext_lc['fluxratios_comp'][idx]

    # results for q >= 0.95 and 2xP_orb
    N_samples = 1000
    idx = (-lnL_twin).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL_twin + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    res_twin = {
        'M_s': masses_comp[idx],
        'R_s': radii_comp[idx],
        'u1': u1s_comp[idx],
        'u2': u2s_comp[idx],
        'P_orb': 2*P_orb[idx],
        'inc': incs[idx],
        'b': b_twin[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'M_comp': np.full(N_samples, M_s),
        'R_comp': np.full(N_samples, R_s),
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': fluxratios_comp[idx],
        'lnZ': lnZ
        }

    # Add results for each external light curve
    # idx is different from the previous idx
    for i, ext_lc in enumerate(external_lcs):
        res_twin[f'u1_p{i+1}'] = ext_lc['u1s_comp'][idx]
        res_twin[f'u2_p{i+1}'] = ext_lc['u2s_comp'][idx]
        res_twin[f'fluxratio_EB_p{i+1}'] = ext_lc['fluxratios'][idx]
        res_twin[f'fluxratio_comp_p{i+1}'] = ext_lc['fluxratios_comp'][idx]

    return res, res_twin


def lnZ_DTP(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Z: float, Bmag: float, Vmag: float,
            gmag: float, rmag: float, imag: float, zmag: float,
            Tmag: float, Jmag: float, Hmag: float,
            Kmag: float, trilegal_fname: str,
            contrast_curve_file: str = None, filt: str = "TESS",
            N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            external_lc_files: list = None,
            filt_lcs: list = None, lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the DTP scenario.
    Now supports up to four external light curves with different filters.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        Tmag (float): Target star TESS magnitude.
        Jmag (float): Target star J magnitude.
        Hmag (float): Target star H magnitude.
        Kmag (float): Target star K magnitude.
        trilegal_fname (string): File containing trilegal query results.
        contrast_curve_file (string): Contrast curve file.
        filt (string): Photometric filter of contrast curve. Options
                         are TESS, Vis, J, H, and K.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
        external_lc_files (List[str]): List of external light curve file paths (up to 4).
        filt_lcs (List[str]): List of corresponding filters for external light curves.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)
    a = ((G*M_s*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    logg = np.log10(G*(M_s*Msun)/(R_s*Rsun)**2)
    # determine target star limb darkening coefficients
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s

    this_Z = ldc_Zs[np.argmin(np.abs(ldc_Zs-Z))]
    this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teff))]
    this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-logg))]
    mask = (
        (ldc_Zs == this_Z)
        & (ldc_Teffs == this_Teff)
        & (ldc_loggs == this_logg)
        )
    u1, u2 = ldc_u1s[mask], ldc_u2s[mask]

    # determine background star population properties
    (Tmags_comp, masses_comp, loggs_comp, Teffs_comp, Zs_comp,
        Jmags_comp, Hmags_comp, Kmags_comp, gmags_comp, rmags_comp, imags_comp, zmags_comp) = (
        trilegal_results(trilegal_fname, Tmag)
        )
    delta_mags = Tmag - Tmags_comp
    delta_Jmags = Jmag - Jmags_comp
    delta_Hmags = Hmag - Hmags_comp
    delta_Kmags = Kmag - Kmags_comp
    fluxratios_comp = 10**(delta_mags/2.5) / (1 + 10**(delta_mags/2.5))

    delta_mags_map = {
                    "delta_TESSmags":delta_mags,
                    "delta_Jmags":delta_Jmags,
                    "delta_Hmags":delta_Hmags,
                    "delta_Kmags":delta_Hmags,
                    }

    # Check if the TIC returns nans for griz mags
    no_sdss_mags = (np.isnan(gmag)) and (np.isnan(rmag)) and \
        (np.isnan(imag)) and (np.isnan(zmag))

    # if we are using sdss filters, but the magnitude of the target in these filters is unknown
    if external_lc_files and any(filt in ['g', 'r', 'i', 'z'] for filt in filt_lcs) and no_sdss_mags:
        print('Warning: no sdss magnitudes available from TIC. Using empirical relations to estimate g, r, i, z mags')
        gmag, rmag, imag, zmag = estimate_sdss_magnitudes(Bmag, Vmag, Jmag)
        print("Using gmag, rmag, imag, zmag: ", gmag, rmag, imag, zmag)

    # if we are using sdss filters, compute the delta sdss mags
    if external_lc_files and any(filt in ['g', 'r', 'i', 'z'] for filt in filt_lcs):
        delta_gmags = gmag - gmags_comp
        delta_rmags = rmag - rmags_comp
        delta_imags = imag - imags_comp
        delta_zmags = zmag - zmags_comp

        #add to delta mags dictionary
        delta_mags_map['delta_gmags'] = delta_gmags
        delta_mags_map['delta_rmags'] = delta_rmags
        delta_mags_map['delta_imags'] = delta_imags
        delta_mags_map['delta_zmags'] = delta_zmags

    external_lcs = []
    if external_lc_files and filt_lcs:
        parallel = True  # Force parallel execution when external LCs are provided
        if len(external_lc_files) != len(filt_lcs):
            raise ValueError("Number of external LC files must match number of filters")
        if len(external_lc_files) > 4:
            raise ValueError("Maximum of 4 external light curves supported")

        for lc_file, filt in zip(external_lc_files, filt_lcs):
            ldc_map = {
                "J": (ldc_J_Zs, ldc_J_Teffs, ldc_J_loggs, ldc_J_u1s, ldc_J_u2s),
                "H": (ldc_H_Zs, ldc_H_Teffs, ldc_H_loggs, ldc_H_u1s, ldc_H_u2s),
                "K": (ldc_Kband_Zs, ldc_Kband_Teffs, ldc_Kband_loggs, ldc_Kband_u1s, ldc_Kband_u2s),
                "g": (ldc_gband_Zs, ldc_gband_Teffs, ldc_gband_loggs, ldc_gband_u1s, ldc_gband_u2s),
                "r": (ldc_rband_Zs, ldc_rband_Teffs, ldc_rband_loggs, ldc_rband_u1s, ldc_rband_u2s),
                "i": (ldc_iband_Zs, ldc_iband_Teffs, ldc_iband_loggs, ldc_iband_u1s, ldc_iband_u2s),
                "z": (ldc_zband_Zs, ldc_zband_Teffs, ldc_zband_loggs, ldc_zband_u1s, ldc_zband_u2s),
            }

            ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s = ldc_map[filt]

            this_Z_p = ldc_P_Zs[np.argmin(np.abs(ldc_P_Zs-Z))]
            this_Teff_p = ldc_P_Teffs[np.argmin(np.abs(ldc_P_Teffs-Teff))]
            this_logg_p = ldc_P_loggs[np.argmin(np.abs(ldc_P_loggs-logg))]
            mask_p = (
                (ldc_P_Zs == this_Z_p)
                & (ldc_P_Teffs == this_Teff_p)
                & (ldc_P_loggs == this_logg_p)
            )
            u1_p, u2_p = ldc_P_u1s[mask_p], ldc_P_u2s[mask_p]

            external_lc = np.loadtxt(lc_file)
            time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
            sigma_p = np.mean(fluxerr_p)
            lnsigma_p = np.log(sigma_p)
            exptime_p = np.min(np.diff(time_p))

            delta_mags_p = delta_mags_map[f"delta_{filt}mags"]
            fluxratios_comp_lc_band = 10**(delta_mags_p/2.5) / (1 + 10**(delta_mags_p/2.5))

            external_lcs.append({
                'time': time_p,
                'flux': flux_p,
                'sigma': sigma_p,
                'lnsigma': lnsigma_p,
                'exptime': exptime_p,
                'u1': u1_p,
                'u2': u2_p,
                'fluxratios': fluxratios_comp_lc_band,
                'lnL': np.full(N, -np.inf)
            })

    N_comp = Tmags_comp.shape[0]
    # draw random sample of background stars
    idxs = np.random.randint(0, N_comp-1, N)

    # calculate priors for companions
    if contrast_curve_file is None:
        # use TESS/Vis band flux ratios
        delta_mags = 2.5*np.log10(
                fluxratios_comp[idxs]/(1-fluxratios_comp[idxs])
                )
        lnprior_companion = np.full(
            N, np.log10((N_comp/0.1) * (1/3600)**2 * 2.2**2)
            )
        lnprior_companion[lnprior_companion > 0.0] = 0.0
        lnprior_companion[delta_mags > 0.0] = -np.inf
    else:
        if filt == "J":
            delta_mags = delta_Jmags[idxs]
        elif filt == "H":
            delta_mags = delta_Hmags[idxs]
        elif filt == "K":
            delta_mags = delta_Kmags[idxs]
        else:
            delta_mags = delta_mags[idxs]
        separations, contrasts = file_to_contrast_curve(
            contrast_curve_file
            )
        lnprior_companion = lnprior_background(
            N_comp, np.abs(delta_mags), separations, contrasts
            )
        lnprior_companion[lnprior_companion > 0.0] = 0.0
        lnprior_companion[delta_mags > 0.0] = -np.inf

    # sample from R_p and inc prior distributions
    rps = sample_rp(np.random.rand(N), np.full(N, M_s), flatpriors)
    incs = sample_inc(np.random.rand(N))
    eccs = sample_ecc(np.random.rand(N), planet=True, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(R_s*Rsun)

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    Ptra = (rps*Rearth + R_s*Rsun)/a * e_corr

    # find instances with collisions
    coll = ((rps*Rearth + R_s*Rsun) > a*(1-eccs))

    lnL = np.full(N, -np.inf)

    if parallel:
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll == False)
        # calculate lnL for transiting systems
        a_arr = np.full(N, a)
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_TP_p(
                    time, flux, sigma, rps[mask],
                    P_orb[mask], incs[mask], a_arr[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[idxs[mask]],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )

        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            ext_lc['lnL'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_TP_p(
                ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], rps[mask],
                P_orb[mask], incs[mask], a_arr[mask], R_s_arr[mask],
                u1_arr_p[mask], u2_arr_p[mask],
                eccs[mask], argps[mask],
                companion_fluxratio=ext_lc['fluxratios'][idxs[mask]],
                companion_is_host=False,
                exptime=ext_lc['exptime'], nsamples=nsamples
            )
            lnL = lnL + ext_lc['lnL']

    else:
        for i in range(N):
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if (incs[i] >= inc_min) & (coll[i] == False):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_TP(
                    time, flux, sigma, rps[i],
                    P_orb[i], incs[i], a[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[idxs[i]],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )

    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp( lnL + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    res = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': rps[idx],
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': np.zeros(N_samples),
        'R_EB': np.zeros(N_samples),
        'M_comp': masses_comp[idxs[idx]],
        'R_comp': np.zeros(N_samples), # not provided by Trilegal
        'fluxratio_EB': np.zeros(N_samples),
        'fluxratio_comp': fluxratios_comp[idxs[idx]],
        'lnZ': lnZ
    }

    # Add results for each external light curve
    for i, ext_lc in enumerate(external_lcs):
        res[f'u1_p{i+1}'] = np.full(N_samples, ext_lc['u1'])
        res[f'u2_p{i+1}'] = np.full(N_samples, ext_lc['u2'])
        res[f'fluxratio_comp_p{i+1}'] = ext_lc['fluxratios'][idxs[idx]]

    return res


def lnZ_DEB(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Z: float, Bmag: float, Vmag: float,
            gmag: float, rmag: float, imag: float, zmag: float,
            Tmag: float, Jmag: float, Hmag: float,
            Kmag: float, trilegal_fname: str,
            contrast_curve_file: str = None, filt: str = "TESS",
            N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            external_lc_files: list = None,
            filt_lcs: list = None, lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the DEB scenario.
    Now supports up to four external light curves with different filters.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        Tmag (float): Target star TESS magnitude.
        Jmag (float): Target star J magnitude.
        Hmag (float): Target star H magnitude.
        Kmag (float): Target star K magnitude.
        trilegal_fname (string): File containing trilegal query results.
        contrast_curve_file (string): Path to contrast curve file.
        filt (string): Photometric filter of contrast curve. Options
                         are TESS, Vis, J, H, and K.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
        external_lc_files (List[str]): List of external light curve file paths (up to 4).
        filt_lcs (List[str]): List of corresponding filters for external light curves.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
        res_twin (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)
    logg = np.log10(G*(M_s*Msun)/(R_s*Rsun)**2)
    # determine target star limb darkening coefficients
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s

    this_Z = ldc_Zs[np.argmin(np.abs(ldc_Zs-Z))]
    this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teff))]
    this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-logg))]
    mask = (
        (ldc_Zs == this_Z)
        & (ldc_Teffs == this_Teff)
        & (ldc_loggs == this_logg)
        )
    u1, u2 = ldc_u1s[mask], ldc_u2s[mask]

    # sample from inc and q prior distributions
    incs = sample_inc(np.random.rand(N))
    qs = sample_q(np.random.rand(N), M_s)
    eccs = sample_ecc(np.random.rand(N), planet=False, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate properties of the drawn EBs
    masses = qs*M_s
    radii, Teffs = stellar_relations(
        masses, np.full(N, R_s), np.full(N, Teff)
        )
    # calculate flux ratios in the TESS band
    fluxratios = (
        flux_relation(masses)
        / (flux_relation(masses) + flux_relation(np.array([M_s])))
        )

    # determine background star population properties
    (Tmags_comp, masses_comp, loggs_comp, Teffs_comp, Zs_comp,
        Jmags_comp, Hmags_comp, Kmags_comp, gmags_comp, rmags_comp, imags_comp, zmags_comp) = (
        trilegal_results(trilegal_fname, Tmag)
        )
    delta_mags = Tmag - Tmags_comp
    delta_Jmags = Jmag - Jmags_comp
    delta_Hmags = Hmag - Hmags_comp
    delta_Kmags = Kmag - Kmags_comp
    fluxratios_comp = 10**(delta_mags/2.5) / (1 + 10**(delta_mags/2.5))

    delta_mags_map = {
                    "delta_TESSmags":delta_mags,
                    "delta_Jmags":delta_Jmags,
                    "delta_Hmags":delta_Hmags,
                    "delta_Kmags":delta_Hmags,
                    }

    # Check if the TIC returns nans for griz mags
    no_sdss_mags = (np.isnan(gmag)) and (np.isnan(rmag)) and \
        (np.isnan(imag)) and (np.isnan(zmag))

    # if we are using sdss filters, but the magnitude of the target in these filters is unknown
    if external_lc_files and any(filt in ['g', 'r', 'i', 'z'] for filt in filt_lcs) and no_sdss_mags:
        print('Warning: no sdss magnitudes available from TIC. Using empirical relations to estimate g, r, i, z mags')
        gmag, rmag, imag, zmag = estimate_sdss_magnitudes(Bmag, Vmag, Jmag)
        print("Using gmag, rmag, imag, zmag: ", gmag, rmag, imag, zmag)

    # if we are using sdss filters, compute the delta sdss mags
    if external_lc_files and any(filt in ['g', 'r', 'i', 'z'] for filt in filt_lcs):
        delta_gmags = gmag - gmags_comp
        delta_rmags = rmag - rmags_comp
        delta_imags = imag - imags_comp
        delta_zmags = zmag - zmags_comp

        #add to delta mags dictionary
        delta_mags_map['delta_gmags'] = delta_gmags
        delta_mags_map['delta_rmags'] = delta_rmags
        delta_mags_map['delta_imags'] = delta_imags
        delta_mags_map['delta_zmags'] = delta_zmags

    external_lcs = []
    if external_lc_files and filt_lcs:
        parallel = True  # Force parallel execution when external LCs are provided
        if len(external_lc_files) != len(filt_lcs):
            raise ValueError("Number of external LC files must match number of filters")
        if len(external_lc_files) > 4:
            raise ValueError("Maximum of 4 external light curves supported")

        for lc_file, filt in zip(external_lc_files, filt_lcs):
            ldc_map = {
                "J": (ldc_J_Zs, ldc_J_Teffs, ldc_J_loggs, ldc_J_u1s, ldc_J_u2s),
                "H": (ldc_H_Zs, ldc_H_Teffs, ldc_H_loggs, ldc_H_u1s, ldc_H_u2s),
                "K": (ldc_Kband_Zs, ldc_Kband_Teffs, ldc_Kband_loggs, ldc_Kband_u1s, ldc_Kband_u2s),
                "g": (ldc_gband_Zs, ldc_gband_Teffs, ldc_gband_loggs, ldc_gband_u1s, ldc_gband_u2s),
                "r": (ldc_rband_Zs, ldc_rband_Teffs, ldc_rband_loggs, ldc_rband_u1s, ldc_rband_u2s),
                "i": (ldc_iband_Zs, ldc_iband_Teffs, ldc_iband_loggs, ldc_iband_u1s, ldc_iband_u2s),
                "z": (ldc_zband_Zs, ldc_zband_Teffs, ldc_zband_loggs, ldc_zband_u1s, ldc_zband_u2s),
            }

            ldc_P_Zs, ldc_P_Teffs, ldc_P_loggs, ldc_P_u1s, ldc_P_u2s = ldc_map[filt]

            this_Z_p = ldc_P_Zs[np.argmin(np.abs(ldc_P_Zs-Z))]
            this_Teff_p = ldc_P_Teffs[np.argmin(np.abs(ldc_P_Teffs-Teff))]
            this_logg_p = ldc_P_loggs[np.argmin(np.abs(ldc_P_loggs-logg))]
            mask_p = (
                (ldc_P_Zs == this_Z_p)
                & (ldc_P_Teffs == this_Teff_p)
                & (ldc_P_loggs == this_logg_p)
            )
            u1_p, u2_p = ldc_P_u1s[mask_p], ldc_P_u2s[mask_p]

            external_lc = np.loadtxt(lc_file)
            time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
            sigma_p = np.mean(fluxerr_p)
            lnsigma_p = np.log(sigma_p)
            exptime_p = np.min(np.diff(time_p))

            fluxratios_lc_band = (
                flux_relation(masses, filt = filt)
                / (flux_relation(masses, filt = filt) + flux_relation(np.array([M_s]), filt = filt))
                )
            delta_mags_p = delta_mags_map[f"delta_{filt}mags"]
            fluxratios_comp_lc_band = 10**(delta_mags_p/2.5) / (1 + 10**(delta_mags_p/2.5))
            external_lcs.append({
                'time': time_p,
                'flux': flux_p,
                'sigma': sigma_p,
                'lnsigma': lnsigma_p,
                'exptime': exptime_p,
                'u1': u1_p,
                'u2': u2_p,
                'fluxratios':fluxratios_lc_band,
                'fluxratios_comp': fluxratios_comp_lc_band,
                'lnL': np.full(N, -np.inf),
                'lnL_twin': np.full(N, -np.inf)
            })

    N_comp = Tmags_comp.shape[0]
    # draw random sample of background stars
    idxs = np.random.randint(0, N_comp-1, N)

    # calculate priors for companions
    if contrast_curve_file is None:
        # use TESS/Vis band flux ratios
        delta_mags = 2.5*np.log10(
                fluxratios_comp[idxs]/(1-fluxratios_comp[idxs])
                )
        lnprior_companion = np.full(
            N, np.log10((N_comp/0.1) * (1/3600)**2 * 2.2**2)
            )
        lnprior_companion[lnprior_companion > 0.0] = 0.0
        lnprior_companion[delta_mags > 0.0] = -np.inf
    else:
        if filt == "J":
            delta_mags = delta_Jmags[idxs]
        elif filt == "H":
            delta_mags = delta_Hmags[idxs]
        elif filt == "K":
            delta_mags = delta_Kmags[idxs]
        else:
            delta_mags = delta_mags[idxs]
        separations, contrasts = file_to_contrast_curve(
            contrast_curve_file
            )
        lnprior_companion = lnprior_background(
            N_comp, np.abs(delta_mags), separations, contrasts
            )
        lnprior_companion[lnprior_companion > 0.0] = 0.0
        lnprior_companion[delta_mags > 0.0] = -np.inf

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = ((G*(M_s+masses)*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    Ptra = (radii*Rsun + R_s*Rsun)/a * e_corr
    a_twin = ((G*(M_s+masses)*Msun)/(4*pi**2)*(2*P_orb*86400)**2)**(1/3)
    Ptra_twin = (radii*Rsun + R_s*Rsun)/a_twin * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(R_s*Rsun)
    r_twin = a_twin*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b_twin = r_twin*np.cos(incs*pi/180)/(R_s*Rsun)

    # find instances with collisions
    coll = ((radii*Rsun + R_s*Rsun) > a*(1-eccs))
    coll_twin = ((2*R_s*Rsun) > a_twin*(1-eccs))

    lnL = np.full(N, -np.inf)
    lnL_twin = np.full(N, -np.inf)

    if parallel:
        # q < 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll == False) & (qs < 0.95)
        # calculate lnL for transiting systems
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_EB_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    P_orb[mask], incs[mask], a[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[idxs[mask]],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )

        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            ext_lc['lnL'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_EB_p(
                ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], radii[mask],
                ext_lc['fluxratios'][mask],
                P_orb[mask], incs[mask], a[mask], R_s_arr[mask],
                u1_arr_p[mask], u2_arr_p[mask],
                eccs[mask], argps[mask],
                companion_fluxratio=ext_lc['fluxratios_comp'][idxs[mask]],
                companion_is_host=False,
                exptime=ext_lc['exptime'], nsamples=nsamples
            )
            lnL = lnL + ext_lc['lnL']

        # q >= 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra_twin <= 1.] = np.arccos(
            Ptra_twin[Ptra_twin <= 1.]
            ) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll_twin == False) & (qs >= 0.95)
        # calculate lnL for transiting systems
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        lnL_twin[mask] = -0.5*ln2pi - lnsigma - lnL_EB_twin_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[idxs[mask]],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )

        for ext_lc in external_lcs:
            u1_arr_p = np.full(N, ext_lc['u1'])
            u2_arr_p = np.full(N, ext_lc['u2'])
            ext_lc['lnL_twin'][mask] = -0.5*ln2pi - ext_lc['lnsigma'] - lnL_EB_twin_p(
                ext_lc['time'], ext_lc['flux'], ext_lc['sigma'], radii[mask],
                ext_lc['fluxratios'][mask],
                2*P_orb[mask], incs[mask], a_twin[mask], R_s_arr[mask],
                u1_arr_p[mask], u2_arr_p[mask],
                eccs[mask], argps[mask],
                companion_fluxratio=ext_lc['fluxratios_comp'][idxs[mask]],
                companion_is_host=False,
                exptime=ext_lc['exptime'], nsamples=nsamples
            )
            lnL_twin = lnL_twin + ext_lc['lnL_twin']

    else:
        for i in range(N):
            # q < 0.95
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if (incs[i] >= inc_min) & (qs[i] < 0.95) & (coll[i] == False):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_EB(
                    time, flux, sigma, radii[i], fluxratios[i],
                    P_orb[i], incs[i], a[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[idxs[i]],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )
            # q >= 0.95 and 2xP_orb
            if Ptra_twin[i] <= 1:
                inc_min = np.arccos(Ptra_twin[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] >= 0.95)
                & (coll_twin[i] == False)):
                lnL_twin[i] = -0.5*ln2pi - lnsigma - lnL_EB_twin(
                    time, flux, sigma, radii[i], fluxratios[i],
                    2*P_orb[i], incs[i], a_twin[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[idxs[i]],
                    companion_is_host=False,
                    exptime=exptime, nsamples=nsamples
                    )

    # results for q < 0.95
    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    res = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'M_comp':masses_comp[idxs[idx]],
        'R_comp': np.zeros(N_samples), # not provided by Trilegal
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': fluxratios_comp[idxs[idx]],
        'lnZ': lnZ
        }

    # Add results for each external light curve
    for i, ext_lc in enumerate(external_lcs):
        res[f'u1_p{i+1}'] = np.full(N_samples, u1)
        res[f'u2_p{i+1}'] = np.full(N_samples, u2)
        res[f'fluxratio_EB_p{i+1}'] = ext_lc['fluxratios'][idx]
        res[f'fluxratio_comp_p{i+1}'] = ext_lc['fluxratios_comp'][idxs[idx]]

    # results for q >= 0.95 and 2xP_orb
    N_samples = 1000
    idx = (-lnL_twin).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL_twin + lnprior_companion + lnz_const)
            )
        )
    lnZ = np.log(Z)

    res_twin = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': 2*P_orb[idx],
        'inc': incs[idx],
        'b': b_twin[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'M_comp':masses_comp[idxs[idx]],
        'R_comp': np.zeros(N_samples), # not provided by Trilegal
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': fluxratios_comp[idxs[idx]],
        'lnZ': lnZ
        }

    # Add results for each external light curve
    # idx is different from the previous idx
    for i, ext_lc in enumerate(external_lcs):
        res_twin[f'u1_p{i+1}'] = np.full(N_samples, u1)
        res_twin[f'u2_p{i+1}'] = np.full(N_samples, u2)
        res_twin[f'fluxratio_EB_p{i+1}'] = ext_lc['fluxratios'][idx]
        res_twin[f'fluxratio_comp_p{i+1}'] = ext_lc['fluxratios_comp'][idxs[idx]]

    return res, res_twin


def lnZ_BTP(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Bmag: float, Vmag: float,
            gmag: float, rmag: float, imag: float, zmag: float,
            Tmag: float, Jmag: float, Hmag: float, Kmag: float,
            trilegal_fname: str,
            contrast_curve_file: str = None, filt: str = "TESS",
            N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            external_lc_file: str = None,
            filt_lc: str = "J", lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the BTP scenario.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Tmag (float): Target star TESS magnitude.
        Jmag (float): Target star J magnitude.
        Hmag (float): Target star H magnitude.
        Kmag (float): Target star K magnitude.
        trilegal_fname (string): File containing trilegal query results.
        contrast_curve_file (string): Path to contrast curve file.
        filt (string): Photometric filter of contrast curve. Options
                         are TESS, Vis, J, H, and K.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)

    # determine background star population properties
    (Tmags_comp, masses_comp, loggs_comp, Teffs_comp, Zs_comp,
        Jmags_comp, Hmags_comp, Kmags_comp, gmags_comp, rmags_comp, imags_comp, zmags_comp) = (
        trilegal_results(trilegal_fname, Tmag)
        )
    radii_comp = np.sqrt(G*masses_comp*Msun / 10**loggs_comp) / Rsun
    delta_mags = Tmag - Tmags_comp
    delta_Jmags = Jmag - Jmags_comp
    delta_Hmags = Hmag - Hmags_comp
    delta_Kmags = Kmag - Kmags_comp
    fluxratios_comp = 10**(delta_mags/2.5) / (1 + 10**(delta_mags/2.5))

    # checks if the TIC returns nans for griz mags
    no_sdss_mags = (np.isnan(gmag)) and (np.isnan(rmag)) and \
        (np.isnan(imag)) and (np.isnan(zmag))


    if (external_lc_file != None) and (filt_lc in ['g', 'r', 'i', 'z']) and (no_sdss_mags):
          print(f'Warnning: no sdss magnitudes available from TIC. Using empirical relations to estimate {filt_lc} mag')
          gmag, rmag, imag, zmag = estimate_sdss_magnitudes(Bmag, Vmag, Jmag)
          print("Using gmag, rmag, imag, zmag: ", gmag, rmag, imag, zmag)
          delta_gmags = gmag - gmags_comp
          delta_rmags = rmag - rmags_comp
          delta_imags = imag - imags_comp
          delta_zmags = zmag - zmags_comp

    if (external_lc_file != None):
        if filt_lc == "J":
            fluxratios_comp_lc_band = 10**(delta_Jmags/2.5) / (1 + 10**(delta_Jmags/2.5))

        elif filt_lc == "H":
            fluxratios_comp_lc_band = 10**(delta_Hmags/2.5) / (1 + 10**(delta_Hmags/2.5))

        elif filt_lc == "K":
            fluxratios_comp_lc_band = 10**(delta_Kmags/2.5) / (1 + 10**(delta_Kmags/2.5))

        elif filt_lc == "g":
            fluxratios_comp_lc_band = 10**(delta_gmags/2.5) / (1 + 10**(delta_gmags/2.5))

        elif filt_lc == "r":
            fluxratios_comp_lc_band = 10**(delta_rmags/2.5) / (1 + 10**(delta_rmags/2.5))

        elif filt_lc == "i":
            fluxratios_comp_lc_band = 10**(delta_imags/2.5) / (1 + 10**(delta_imags/2.5))

        elif filt_lc == "z":
            fluxratios_comp_lc_band = 10**(delta_zmags/2.5) / (1 + 10**(delta_zmags/2.5))

    N_comp = Tmags_comp.shape[0]
    # determine limb darkening coefficients of background stars
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s

    if (external_lc_file != None):

        if filt_lc == "J":
            ldc_P_Zs = ldc_J_Zs
            ldc_P_Teffs = ldc_J_Teffs
            ldc_P_loggs = ldc_J_loggs
            ldc_P_u1s = ldc_J_u1s
            ldc_P_u2s = ldc_J_u2s

        elif filt_lc == "H":
            ldc_P_Zs = ldc_H_Zs
            ldc_P_Teffs = ldc_H_Teffs
            ldc_P_loggs = ldc_H_loggs
            ldc_P_u1s = ldc_H_u1s
            ldc_P_u2s = ldc_H_u2s

        elif filt_lc == "K":
            ldc_P_Zs = ldc_Kband_Zs
            ldc_P_Teffs = ldc_Kband_Teffs
            ldc_P_loggs = ldc_Kband_loggs
            ldc_P_u1s = ldc_Kband_u1s
            ldc_P_u2s = ldc_Kband_u2s

        elif filt_lc == "g":
            ldc_P_Zs = ldc_gband_Zs
            ldc_P_Teffs = ldc_gband_Teffs
            ldc_P_loggs = ldc_gband_loggs
            ldc_P_u1s = ldc_gband_u1s
            ldc_P_u2s = ldc_gband_u2s

        elif filt_lc == "r":
            ldc_P_Zs = ldc_rband_Zs
            ldc_P_Teffs = ldc_rband_Teffs
            ldc_P_loggs = ldc_rband_loggs
            ldc_P_u1s = ldc_rband_u1s
            ldc_P_u2s = ldc_rband_u2s

        elif filt_lc == "i":
            ldc_P_Zs = ldc_iband_Zs
            ldc_P_Teffs = ldc_iband_Teffs
            ldc_P_loggs = ldc_iband_loggs
            ldc_P_u1s = ldc_iband_u1s
            ldc_P_u2s = ldc_iband_u2s

        elif filt_lc == "z":
            ldc_P_Zs = ldc_zband_Zs
            ldc_P_Teffs = ldc_zband_Teffs
            ldc_P_loggs = ldc_zband_loggs
            ldc_P_u1s = ldc_zband_u1s
            ldc_P_u2s = ldc_zband_u2s

    u1s_comp, u2s_comp = np.zeros(N_comp), np.zeros(N_comp)
    u1s_comp_p, u2s_comp_p = np.zeros(N_comp), np.zeros(N_comp) # this is for the external_lc data

    for i in range(N_comp):
        this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teffs_comp[i]))]
        this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-loggs_comp[i]))]
        mask1 = (ldc_Teffs == this_Teff) & (ldc_loggs == this_logg)
        these_Zs = ldc_Zs[mask1]
        this_Z = these_Zs[np.argmin(np.abs(these_Zs-Zs_comp[i]))]
        mask = (
            (ldc_Zs == this_Z)
            & (ldc_Teffs == this_Teff)
            & (ldc_loggs == this_logg)
            )
        u1s_comp[i], u2s_comp[i] = ldc_u1s[mask], ldc_u2s[mask]

    if (external_lc_file != None):
        external_lc = np.loadtxt(external_lc_file)
        time_p, flux_p, fluxerr_p = external_lc[:,0], external_lc[:,1], external_lc[:,2]
        sigma_p = np.mean(fluxerr_p)
        lnsigma_p = np.log(sigma_p)
        exptime_p = np.min(np.diff(time_p))
        lnL_external_lc = np.full(N, -np.inf)

    if (external_lc_file != None):
        for i in range(N_comp):
            this_Teff_p = ldc_P_Teffs[np.argmin(np.abs(ldc_P_Teffs-Teffs_comp[i]))]
            this_logg_p = ldc_P_loggs[np.argmin(np.abs(ldc_P_loggs-loggs_comp[i]))]
            mask1_p = (ldc_P_Teffs == this_Teff_p) & (ldc_P_loggs == this_logg_p)
            these_Zs_p = ldc_P_Zs[mask1_p]
            this_Z_p = these_Zs_p[np.argmin(np.abs(these_Zs_p-Zs_comp[i]))]
            mask_p = (
                (ldc_P_Zs == this_Z_p)
                & (ldc_P_Teffs == this_Teff_p)
                & (ldc_P_loggs == this_logg_p)
                )
            u1s_comp_p[i], u2s_comp_p[i] = ldc_P_u1s[mask_p], ldc_P_u2s[mask_p]


    # draw random sample of background stars
    idxs = np.random.randint(0, N_comp, N)

    # calculate priors for companions
    if contrast_curve_file is None:
        if (external_lc_file != None):
            print(f"Using {filt_lc} band flux ratios for lnprior_companion")
            delta_mags = 2.5*np.log10(
                fluxratios_comp_lc_band[idxs]/(1-fluxratios_comp_lc_band[idxs])
                )
        else:
            # use TESS/Vis band flux ratios
            delta_mags = 2.5*np.log10(
                fluxratios_comp[idxs]/(1-fluxratios_comp[idxs])
                )
        lnprior_companion = np.full(
            N, np.log10((N_comp/0.1) * (1/3600)**2 * 2.2**2)
            )
        lnprior_companion[lnprior_companion > 0.0] = 0.0
        lnprior_companion[delta_mags > 0.0] = -np.inf
    else:
        if filt == "J":
            delta_mags = delta_Jmags[idxs]
        elif filt == "H":
            delta_mags = delta_Hmags[idxs]
        elif filt == "K":
            delta_mags = delta_Kmags[idxs]
        else:
            delta_mags = delta_mags[idxs]
        separations, contrasts = file_to_contrast_curve(
            contrast_curve_file
            )
        lnprior_companion = lnprior_background(
            N_comp, np.abs(delta_mags), separations, contrasts
            )
        lnprior_companion[lnprior_companion > 0.0] = 0.0
        lnprior_companion[delta_mags > 0.0] = -np.inf

    # sample from inc and R_p prior distributions
    rps = sample_rp(np.random.rand(N), masses_comp[idxs], flatpriors)
    incs = sample_inc(np.random.rand(N))
    eccs = sample_ecc(np.random.rand(N), planet=True, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = ((G*masses_comp[idxs]*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    Ptra = (rps*Rearth + radii_comp[idxs]*Rsun)/a * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(radii_comp[idxs]*Rsun)

    # find instances with collisions
    coll = ((rps*Rearth + radii_comp[idxs]*Rsun) > a*(1-eccs))

    lnL = np.full(N, -np.inf)

    if parallel:
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (
            (incs >= inc_min)
            & (coll == False)
            & (loggs_comp[idxs] >= 3.5)
            & (Teffs_comp[idxs] <= 10000)
            )
        # calculate lnL for transiting systems
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_TP_p(
                    time, flux, sigma, rps[mask],
                    P_orb[mask], incs[mask], a[mask], radii_comp[idxs[mask]],
                    u1s_comp[idxs[mask]], u2s_comp[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[idxs[mask]],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )
        if (external_lc_file != None):
            lnL_external_lc[mask] = -0.5*ln2pi - lnsigma_p - lnL_TP_p(
                    time_p, flux_p, sigma_p, rps[mask],
                    P_orb[mask], incs[mask], a[mask], radii_comp[idxs[mask]],
                    u1s_comp_p[idxs[mask]], u2s_comp_p[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp_lc_band[idxs[mask]],
                    companion_is_host=True,
                    exptime=exptime_p, nsamples=nsamples
                    )
            lnL = lnL+lnL_external_lc
    else:
        for i in range(N):
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (loggs_comp[idxs[i]] >= 3.5)
                    & (Teffs_comp[idxs[i]] <= 10000) & (coll[i] == False)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_TP(
                    time, flux, sigma, rps[i],
                    P_orb[i], incs[i], a[i], radii_comp[idxs[i]],
                    u1s_comp[idxs[i]], u2s_comp[idxs[i]],
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[idxs[i]],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )

    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    if (external_lc_file != None):
        idx_p = (-lnL_external_lc).argsort()[:N_samples]
        Z_p = np.mean(np.nan_to_num(
            np.exp(lnL_external_lc + lnprior_companion + lnz_const )  # where does 600 come from?
            ))
        lnZ_p = np.log(Z_p)
        res = {
            'M_s': masses_comp[idxs[idx]],
            'R_s': radii_comp[idxs[idx]],
            'u1': u1s_comp[idxs[idx]],
            'u2': u2s_comp[idxs[idx]],
            'u1_p': u1s_comp_p[idxs[idx]],
            'u2_p': u2s_comp_p[idxs[idx]],
            'P_orb': P_orb[idx],
            'inc': incs[idx],
            'b': b[idx],
            'R_p': rps[idx],
            'ecc': eccs[idx],
            'argp': argps[idx],
            'M_EB': np.zeros(N_samples),
            'R_EB': np.zeros(N_samples),
            'fluxratio_EB': np.zeros(N_samples),
            'fluxratio_comp': fluxratios_comp[idxs[idx]],
            'fluxratio_EB_p': np.zeros(N_samples),
            'fluxratio_comp_p': fluxratios_comp_lc_band[idxs[idx]],
            'lnZ': lnZ,
            'lnZ_p': lnZ_p
            }
    else:
        res = {
            'M_s': masses_comp[idxs[idx]],
            'R_s': radii_comp[idxs[idx]],
            'u1': u1s_comp[idxs[idx]],
            'u2': u2s_comp[idxs[idx]],
            'P_orb': P_orb[idx],
            'inc': incs[idx],
            'b': b[idx],
            'R_p': rps[idx],
            'ecc': eccs[idx],
            'argp': argps[idx],
            'M_EB': np.zeros(N_samples),
            'R_EB': np.zeros(N_samples),
            'fluxratio_EB': np.zeros(N_samples),
            'fluxratio_comp': fluxratios_comp[idxs[idx]],
            'lnZ': lnZ
            }
    return res


def lnZ_BEB(time: np.ndarray, flux: np.ndarray, sigma: float,
            P_orb: float, M_s: float, R_s: float, Teff: float,
            Bmag: float, Vmag: float, gmag: float,
            rmag: float, imag: float, zmag: float,
            Tmag: float, Jmag:float, Hmag: float, Kmag: float,
            trilegal_fname: str,
            contrast_curve_file: str = None, filt: str = "TESS",
            N: int = 1000000, parallel: bool = False,
            mission: str = "TESS", flatpriors: bool = False,
            exptime: float = 0.00139, nsamples: int = 20,
            external_lc_file: str = None,
            filt_lc: str = "J", lnz_const: int = 600):
    """
    Calculates the marginal likelihood of the BEB scenario.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        M_s (float): Target star mass [Solar masses].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Tmag (float): Target star TESS magnitude.
        Jmag (float): Target star J magnitude.
        Hmag (float): Target star H magnitude.
        Kmag (float): Target star K magnitude.
        trilegal_fname (string): File containing trilegal query results.
        contrast_curve_file (string): Path to contrast curve file.
        filt (string): Photometric filter of contrast curve. Options
                         are TESS, Vis, J, H, and K.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
        res_twin (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)

    # sample from prior distributions
    incs = sample_inc(np.random.rand(N))
    qs = sample_q(np.random.rand(N), M_s)
    qs_comp = sample_q_companion(np.random.rand(N), M_s)
    eccs = sample_ecc(np.random.rand(N), planet=False, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # determine background star population properties
    (Tmags_comp, masses_comp, loggs_comp, Teffs_comp, Zs_comp,
        Jmags_comp, Hmags_comp, Kmags_comp, gmags_comp, rmags_comp, imags_comp, zmags_comp) = (
        trilegal_results(trilegal_fname, Tmag)
        )
    radii_comp = np.sqrt(G*masses_comp*Msun / 10**loggs_comp) / Rsun
    delta_mags = Tmag - Tmags_comp
    delta_Jmags = Jmag - Jmags_comp
    delta_Hmags = Hmag - Hmags_comp
    delta_Kmags = Kmag - Kmags_comp
    fluxratios_comp = 10**(delta_mags/2.5) / (1 + 10**(delta_mags/2.5))
    fluxratios_comp_J = 10**(delta_Jmags/2.5) / (1 + 10**(delta_Jmags/2.5))
    fluxratios_comp_H = 10**(delta_Hmags/2.5) / (1 + 10**(delta_Hmags/2.5))
    fluxratios_comp_K = 10**(delta_Kmags/2.5) / (1 + 10**(delta_Kmags/2.5))

    # checks if the TIC returns nans for griz mags
    no_sdss_mags = (np.isnan(gmag)) and (np.isnan(rmag)) and \
        (np.isnan(imag)) and (np.isnan(zmag))


    if (external_lc_file != None) and (filt_lc in ['g', 'r', 'i', 'z']) and (no_sdss_mags):
          print(f'Warnning: no sdss magnitudes available from TIC. Using empirical relations to estimate {filt_lc} mag')
          gmag, rmag, imag, zmag = estimate_sdss_magnitudes(Bmag, Vmag, Jmag)
          print("Using gmag, rmag, imag, zmag: ", gmag, rmag, imag, zmag)
          delta_gmags = gmag - gmags_comp
          delta_rmags = rmag - rmags_comp
          delta_imags = imag - imags_comp
          delta_zmags = zmag - zmags_comp

          fluxratios_comp_g = 10**(delta_gmags/2.5) / (1 + 10**(delta_gmags/2.5))
          fluxratios_comp_r = 10**(delta_rmags/2.5) / (1 + 10**(delta_rmags/2.5))
          fluxratios_comp_i = 10**(delta_imags/2.5) / (1 + 10**(delta_imags/2.5))
          fluxratios_comp_z = 10**(delta_zmags/2.5) / (1 + 10**(delta_zmags/2.5))


    N_comp = Tmags_comp.shape[0]
    # determine limb darkening coefficients of background stars
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s

    if (external_lc_file != None):

        if filt_lc == "J":
            ldc_P_Zs = ldc_J_Zs
            ldc_P_Teffs = ldc_J_Teffs
            ldc_P_loggs = ldc_J_loggs
            ldc_P_u1s = ldc_J_u1s
            ldc_P_u2s = ldc_J_u2s

        elif filt_lc == "H":
            ldc_P_Zs = ldc_H_Zs
            ldc_P_Teffs = ldc_H_Teffs
            ldc_P_loggs = ldc_H_loggs
            ldc_P_u1s = ldc_H_u1s
            ldc_P_u2s = ldc_H_u2s

        elif filt_lc == "K":
            ldc_P_Zs = ldc_Kband_Zs
            ldc_P_Teffs = ldc_Kband_Teffs
            ldc_P_loggs = ldc_Kband_loggs
            ldc_P_u1s = ldc_Kband_u1s
            ldc_P_u2s = ldc_Kband_u2s

        elif filt_lc == "g":
            ldc_P_Zs = ldc_gband_Zs
            ldc_P_Teffs = ldc_gband_Teffs
            ldc_P_loggs = ldc_gband_loggs
            ldc_P_u1s = ldc_gband_u1s
            ldc_P_u2s = ldc_gband_u2s

        elif filt_lc == "r":
            ldc_P_Zs = ldc_rband_Zs
            ldc_P_Teffs = ldc_rband_Teffs
            ldc_P_loggs = ldc_rband_loggs
            ldc_P_u1s = ldc_rband_u1s
            ldc_P_u2s = ldc_rband_u2s

        elif filt_lc == "i":
            ldc_P_Zs = ldc_iband_Zs
            ldc_P_Teffs = ldc_iband_Teffs
            ldc_P_loggs = ldc_iband_loggs
            ldc_P_u1s = ldc_iband_u1s
            ldc_P_u2s = ldc_iband_u2s

        elif filt_lc == "z":
            ldc_P_Zs = ldc_zband_Zs
            ldc_P_Teffs = ldc_zband_Teffs
            ldc_P_loggs = ldc_zband_loggs
            ldc_P_u1s = ldc_zband_u1s
            ldc_P_u2s = ldc_zband_u2s

    u1s_comp, u2s_comp = np.zeros(N_comp), np.zeros(N_comp)
    u1s_comp_p, u2s_comp_p = np.zeros(N_comp), np.zeros(N_comp)

    for i in range(N_comp):
        this_Teff = ldc_Teffs[np.argmin(
            np.abs(ldc_Teffs-Teffs_comp[i])
            )]
        this_logg = ldc_loggs[np.argmin(
            np.abs(ldc_loggs-loggs_comp[i])
            )]
        mask1 = (ldc_Teffs == this_Teff) & (ldc_loggs == this_logg)
        these_Zs = ldc_Zs[mask1]
        this_Z = these_Zs[np.argmin(np.abs(these_Zs-Zs_comp[i]))]
        mask = (
            (ldc_Zs == this_Z)
            & (ldc_Teffs == this_Teff)
            & (ldc_loggs == this_logg)
            )
        u1s_comp[i], u2s_comp[i] = ldc_u1s[mask], ldc_u2s[mask]

    if (external_lc_file != None):
        external = np.loadtxt(external_lc_file)
        time_p, flux_p, fluxerr_p = external[:,0], external[:,1], external[:,2]
        sigma_p = np.mean(fluxerr_p)
        lnsigma_p = np.log(sigma_p)
        exptime_p = np.min(np.diff(time_p))
        lnL_external = np.full(N, -np.inf)
        lnL_external_twin = np.full(N, -np.inf)

    if (external_lc_file != None):
        for i in range(N_comp):
            this_Teff_p = ldc_P_Teffs[np.argmin(np.abs(ldc_P_Teffs-Teffs_comp[i]))]
            this_logg_p = ldc_P_loggs[np.argmin(np.abs(ldc_P_loggs-loggs_comp[i]))]
            mask1_p = (ldc_P_Teffs == this_Teff_p) & (ldc_P_loggs == this_logg_p)
            these_Zs_p = ldc_P_Zs[mask1_p]
            this_Z_p = these_Zs_p[np.argmin(np.abs(these_Zs_p-Zs_comp[i]))]
            mask_p = (
                (ldc_P_Zs == this_Z_p)
                & (ldc_P_Teffs == this_Teff_p)
                & (ldc_P_loggs == this_logg_p)
                )
            u1s_comp_p[i], u2s_comp_p[i] = ldc_P_u1s[mask_p], ldc_P_u2s[mask_p]

    # draw random sample of background stars
    idxs = np.random.randint(0, N_comp, N)

    # calculate properties of the drawn EBs
    masses = qs*masses_comp[idxs]
    radii, Teffs = stellar_relations(
        masses, radii_comp[idxs], Teffs_comp[idxs]
        )
    # calculate EB flux ratios in the TESS band
    fluxratios_comp_bound = (
        flux_relation(masses_comp[idxs])
        / (
            flux_relation(masses_comp[idxs])
            + flux_relation(np.array([M_s]))
            )
        )
    distance_correction = fluxratios_comp[idxs]/fluxratios_comp_bound
    fluxratios = (
        flux_relation(masses)
        / (flux_relation(masses) + flux_relation(np.array([M_s])))
        * distance_correction
        )


    if (external_lc_file != None):

        # calculate EB flux ratios in the J band (for external)
        fluxratios_comp_bound_lc_band = (
            flux_relation(masses_comp[idxs], filt=filt_lc)
            / (
                flux_relation(masses_comp[idxs], filt=filt_lc)
                + flux_relation(np.array([M_s]), filt=filt_lc)
                )
            )

        if filt_lc == "J":
            flux_term = fluxratios_comp_J
        elif filt_lc == "H":
            flux_term = fluxratios_comp_H
        elif filt_lc == "K":
            flux_term = fluxratios_comp_K
        elif filt_lc == "g":
            flux_term = fluxratios_comp_g
        elif filt_lc == "r":
            flux_term = fluxratios_comp_r
        elif filt_lc == "i":
            flux_term = fluxratios_comp_i
        elif filt_lc == "z":
            flux_term = fluxratios_comp_z

        distance_correction_lc_band = flux_term[idxs]/fluxratios_comp_bound_lc_band
        fluxratios_lc_band = (
            flux_relation(masses, filt=filt_lc)
            / (flux_relation(masses, filt=filt_lc) + flux_relation(np.array([M_s]), filt=filt_lc))
            * distance_correction_lc_band
            )

    # calculate EB flux ratios in the contrast curve filter
    if filt == "J":
        fluxratios_comp_cc = fluxratios_comp_J[idxs]
    elif filt == "H":
        fluxratios_comp_cc = fluxratios_comp_H[idxs]
    elif filt == "K":
        fluxratios_comp_cc = fluxratios_comp_K[idxs]
    else:
        fluxratios_comp_cc = fluxratios_comp[idxs]

    fluxratios_comp_bound_cc = (
        flux_relation(masses_comp[idxs], filt)
        / (
            flux_relation(masses_comp[idxs], filt)
            + flux_relation(np.array([M_s]), filt)
            )
        )
    distance_correction_cc = fluxratios_comp_cc/fluxratios_comp_bound_cc
    fluxratios_cc = (
        flux_relation(masses, filt)
        / (flux_relation(masses, filt)
            + flux_relation(np.array([M_s]), filt))
        * distance_correction_cc
        )

    # calculate priors for companions
    if contrast_curve_file is None:
        if (external_lc_file != None):
            print(f"Using {filt_lc} band flux ratios for lnprior_companion")
            delta_mags = 2.5*np.log10(
                (flux_term[idxs]/(1-flux_term[idxs]))
                + (fluxratios_lc_band/(1-fluxratios_lc_band))
                )
        else:
            # use TESS/Vis band flux ratios
            delta_mags = 2.5*np.log10(
                (fluxratios_comp[idxs]/(1-fluxratios_comp[idxs]))
                + (fluxratios/(1-fluxratios))
                )
        lnprior_companion = np.full(
            N, np.log10((N_comp/0.1) * (1/3600)**2 * 2.2**2)
            )
        lnprior_companion[lnprior_companion > 0.0] = 0.0
        lnprior_companion[delta_mags > 0.0] = -np.inf
    else:
        # use contrast curve filter flux ratios
        delta_mags = 2.5*np.log10(
            (fluxratios_comp_cc/(1-fluxratios_comp_cc))
            + (fluxratios_cc/(1-fluxratios_cc))
            )
        separations, contrasts = file_to_contrast_curve(
            contrast_curve_file
            )
        lnprior_companion = lnprior_background(
            N_comp, np.abs(delta_mags), separations, contrasts
            )
        lnprior_companion[lnprior_companion > 0.0] = 0.0
        lnprior_companion[delta_mags > 0.0] = -np.inf

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = (
        (G*(masses_comp[idxs]+masses)*Msun)/(4*pi**2)*(P_orb*86400)**2
        )**(1/3)
    Ptra = (radii*Rsun + radii_comp[idxs]*Rsun)/a * e_corr
    a_twin = (
        (G*(masses_comp[idxs]+masses)*Msun)/(4*pi**2)*(2*P_orb*86400)**2
        )**(1/3)
    Ptra_twin = (radii*Rsun + radii_comp[idxs]*Rsun)/a_twin * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(radii_comp[idxs]*Rsun)
    r_twin = a_twin*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b_twin = r_twin*np.cos(incs*pi/180)/(radii_comp[idxs]*Rsun)

    # find instances with collisions
    coll = ((radii*Rsun + radii_comp[idxs]*Rsun) > a*(1-eccs))
    coll_twin = ((2*radii_comp[idxs]*Rsun) > a_twin*(1-eccs))

    lnL = np.full(N, -np.inf)
    lnL_twin = np.full(N, -np.inf)

    if parallel:
        # q < 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (
            (incs >= inc_min)
            & (coll_twin == False)
            & (qs < 0.95)
            & (loggs_comp[idxs] >= 3.5)
            & (Teffs_comp[idxs] <= 10000)
            )
        # calculate lnL for transiting systems
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_EB_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    P_orb[mask], incs[mask], a[mask], radii_comp[idxs[mask]],
                    u1s_comp[idxs[mask]], u2s_comp[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[idxs[mask]],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )
        if (external_lc_file != None):
            lnL_external[mask] = -0.5*ln2pi - lnsigma_p - lnL_EB_p(
                    time_p, flux_p, sigma_p, radii[mask], fluxratios_lc_band[mask],
                    P_orb[mask], incs[mask], a[mask], radii_comp[idxs[mask]],
                    u1s_comp_p[idxs[mask]], u2s_comp_p[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=flux_term[idxs[mask]],
                    companion_is_host=True,
                    exptime=exptime_p, nsamples=nsamples
                    )
            lnL = lnL+lnL_external
        # q >= 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra_twin <= 1.] = np.arccos(
            Ptra_twin[Ptra_twin <= 1.]
            ) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (
            (incs >= inc_min)
            & (coll_twin == False)
            & (qs >= 0.95)
            & (loggs_comp[idxs] >= 3.5)
            & (Teffs_comp[idxs] <= 10000)
            )
        # calculate lnL for transiting systems
        lnL_twin[mask] = -0.5*ln2pi - lnsigma - lnL_EB_twin_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], radii_comp[idxs[mask]],
                    u1s_comp[idxs[mask]], u2s_comp[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=fluxratios_comp[idxs[mask]],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )
        if (external_lc_file != None):
            lnL_external_twin[mask] = -0.5*ln2pi - lnsigma_p - lnL_EB_twin_p(
                    time_p, flux_p, sigma_p, radii[mask], fluxratios_lc_band[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], radii_comp[idxs[mask]],
                    u1s_comp_p[idxs[mask]], u2s_comp_p[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=flux_term[idxs[mask]],
                    companion_is_host=True,
                    exptime=exptime_p, nsamples=nsamples
                    )
            lnL_twin = lnL_twin + lnL_external_twin
    else:
        for i in range(N):
            # q < 0.95
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] < 0.95)
                    & (loggs_comp[idxs[i]] >= 3.5)
                    & (Teffs_comp[idxs[i]] <= 10000)
                    & (coll[i] == False)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_EB(
                    time, flux, sigma, radii[i], fluxratios[i],
                    P_orb[i], incs[i], a[i], radii_comp[idxs[i]],
                    u1s_comp[idxs[i]], u2s_comp[idxs[i]],
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[idxs[i]],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )
            # q >= 0.95 and 2xP_orb
            if Ptra_twin[i] <= 1:
                inc_min = np.arccos(Ptra_twin[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] >= 0.95)
                    & (loggs_comp[idxs[i]] >= 3.5)
                    & (Teffs_comp[idxs[i]] <= 10000)
                    & (coll_twin[i] == False)):
                lnL_twin[i] = -0.5*ln2pi - lnsigma - lnL_EB_twin(
                    time, flux, sigma, radii[i], fluxratios[i],
                    2*P_orb[i], incs[i], a_twin[i], radii_comp[idxs[i]],
                    u1s_comp[idxs[i]], u2s_comp[idxs[i]],
                    eccs[i], argps[i],
                    companion_fluxratio=fluxratios_comp[idxs[i]],
                    companion_is_host=True,
                    exptime=exptime, nsamples=nsamples
                    )

    # results for q < 0.95
    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    if (external_lc_file != None):
        idx_p = (-lnL_external).argsort()[:N_samples]
        Z_p = np.mean(np.nan_to_num(
            np.exp(lnL_external + lnprior_companion + lnz_const )  # where does 600 come from?
            ))
        lnZ_p = np.log(Z_p)
        res = {
            'M_s': masses_comp[idxs[idx]],
            'R_s': radii_comp[idxs[idx]],
            'u1': u1s_comp[idxs[idx]],
            'u2': u2s_comp[idxs[idx]],
            'u1_p': u1s_comp_p[idxs[idx]],
            'u2_p': u2s_comp_p[idxs[idx]],
            'P_orb': P_orb[idx],
            'inc': incs[idx],
            'b': b[idx],
            'R_p': np.zeros(N_samples),
            'ecc': eccs[idx],
            'argp': argps[idx],
            'M_EB': masses[idx],
            'R_EB': radii[idx],
            'fluxratio_EB': fluxratios[idx],
            'fluxratio_comp': fluxratios_comp[idxs[idx]],
            'fluxratio_EB_p': fluxratios_lc_band[idx],
            'fluxratio_comp_p': flux_term[idxs[idx]],
            'lnZ': lnZ,
            'lnZ_p': lnZ_p
            }
    else:
        res = {
            'M_s': masses_comp[idxs[idx]],
            'R_s': radii_comp[idxs[idx]],
            'u1': u1s_comp[idxs[idx]],
            'u2': u2s_comp[idxs[idx]],
            'P_orb': P_orb[idx],
            'inc': incs[idx],
            'b': b[idx],
            'R_p': np.zeros(N_samples),
            'ecc': eccs[idx],
            'argp': argps[idx],
            'M_EB': masses[idx],
            'R_EB': radii[idx],
            'fluxratio_EB': fluxratios[idx],
            'fluxratio_comp': fluxratios_comp[idxs[idx]],
            'lnZ': lnZ
            }
    # results for q >= 0.95 and 2xP_orb
    N_samples = 1000
    idx = (-lnL_twin).argsort()[:N_samples]
    Z = np.mean(
        np.nan_to_num(
            np.exp(lnL_twin + lnprior_companion + lnz_const )
            )
        )
    lnZ = np.log(Z)

    if (external_lc_file != None):
        idx_p = (-lnL_external_twin).argsort()[:N_samples]
        Z_p = np.mean(np.nan_to_num(
            np.exp(lnL_external_twin + lnprior_companion + lnz_const )  # where does 600 come from?
            ))
        lnZ_p = np.log(Z_p)
        res_twin = {
            'M_s': masses_comp[idxs[idx]],
            'R_s': radii_comp[idxs[idx]],
            'u1': u1s_comp[idxs[idx]],
            'u2': u2s_comp[idxs[idx]],
            'u1_p': u1s_comp_p[idxs[idx]],
            'u2_p': u2s_comp_p[idxs[idx]],
            'P_orb': 2*P_orb[idx],
            'inc': incs[idx],
            'b': b_twin[idx],
            'R_p': np.zeros(N_samples),
            'ecc': eccs[idx],
            'argp': argps[idx],
            'M_EB': masses[idx],
            'R_EB': radii[idx],
            'fluxratio_EB': fluxratios[idx],
            'fluxratio_comp': fluxratios_comp[idxs[idx]],
            'fluxratio_EB_p': fluxratios_lc_band[idx],
            'fluxratio_comp_p': flux_term[idxs[idx]],
            'lnZ': lnZ,
            'lnZ_p': lnZ_p
            }
    else:
        res_twin = {
            'M_s': masses_comp[idxs[idx]],
            'R_s': radii_comp[idxs[idx]],
            'u1': u1s_comp[idxs[idx]],
            'u2': u2s_comp[idxs[idx]],
            'P_orb': 2*P_orb[idx],
            'inc': incs[idx],
            'b': b_twin[idx],
            'R_p': np.zeros(N_samples),
            'ecc': eccs[idx],
            'argp': argps[idx],
            'M_EB': masses[idx],
            'R_EB': radii[idx],
            'fluxratio_EB': fluxratios[idx],
            'fluxratio_comp': fluxratios_comp[idxs[idx]],
            'lnZ': lnZ
            }
    return res, res_twin


def lnZ_NTP_unknown(time: np.ndarray, flux: np.ndarray, sigma: float,
                    P_orb: float, Tmag: float, trilegal_fname: str,
                    N: int = 1000000, parallel: bool = False,
                    mission: str = "TESS", flatpriors: bool = False,
                    exptime: float = 0.00139, nsamples: int = 20):
    """
    Calculates the marginal likelihood of the NTP scenario for
    a star of unknown properties.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        Tmag (float): Target star TESS magnitude.
        trilegal_fname (string): File containing trilegal query results.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)

    # determine properties of possible stars
    (Tmags_nearby, masses_nearby, loggs_nearby, Teffs_nearby,
        Zs_nearby, Jmags_nearby, Hmags_nearby, Kmags_nearby, _, _, _, _) = (
        trilegal_results(trilegal_fname, Tmag)
        )
    mask = (Tmag-1 < Tmags_nearby) & (Tmags_nearby < Tmag+1)
    Tmags_possible = Tmags_nearby[mask]
    masses_possible = masses_nearby[mask]
    loggs_possible = loggs_nearby[mask]
    Teffs_possible = Teffs_nearby[mask]
    Zs_possible = Zs_nearby[mask]
    radii_possible = np.sqrt(
        G*masses_possible*Msun / 10**loggs_possible
        ) / Rsun
    N_possible = Tmags_possible.shape[0]
    # determine limb darkening coefficients of background stars
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s
    u1s_possible = np.zeros(N_possible)
    u2s_possible = np.zeros(N_possible)
    for i in range(N_possible):
        this_Teff = ldc_Teffs[np.argmin(
            np.abs(ldc_Teffs-Teffs_possible[i])
            )]
        this_logg = ldc_loggs[np.argmin(
            np.abs(ldc_loggs-loggs_possible[i])
            )]
        mask1 = (ldc_Teffs == this_Teff) & (ldc_loggs == this_logg)
        these_Zs = ldc_Zs[mask1]
        this_Z = these_Zs[np.argmin(np.abs(these_Zs-Zs_possible[i]))]
        mask = (
            (ldc_Zs == this_Z)
            & (ldc_Teffs == this_Teff)
            & (ldc_loggs == this_logg)
            )
        u1s_possible[i], u2s_possible[i] = ldc_u1s[mask], ldc_u2s[mask]
    # draw random sample of background stars
    if N_possible > 0:
        idxs = np.random.randint(0, N_possible, N)
    # if there aren't enough similar stars, don't do the calculation
    else:
        res = {
            'M_s': 0,
            'R_s': 0,
            'u1': 0,
            'u2': 0,
            'P_orb': 0,
            'inc': 0,
            'R_p': 0,
            'ecc': 0,
            'argp': 0,
            'M_EB': 0,
            'R_EB': 0,
            'fluxratio_EB': 0,
            'fluxratio_comp': 0,
            'lnZ': -np.inf
        }
        return res

    # sample from inc and R_p prior distributions
    rps = sample_rp(np.random.rand(N), masses_possible[idxs], flatpriors)
    incs = sample_inc(np.random.rand(N))
    eccs = sample_ecc(np.random.rand(N), planet=True, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = (
        (G*masses_possible[idxs]*Msun)/(4*pi**2)*(P_orb*86400)**2
        )**(1/3)
    Ptra = (rps*Rearth + radii_possible[idxs]*Rsun)/a * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(radii_possible[idxs]*Rsun)

    # find instances with collisions
    coll = ((rps*Rearth + radii_possible[idxs]*Rsun) > a*(1-eccs))

    lnL = np.full(N, -np.inf)
    if parallel:
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (
            (incs >= inc_min)
            & (coll == False)
            & (loggs_possible[idxs] >= 3.5)
            & (Teffs_possible[idxs] <= 10000)
            )
        # calculate lnL for transiting systems
        companion_fluxratio = np.zeros(N)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_TP_p(
                    time, flux, sigma, rps[mask],
                    P_orb[mask], incs[mask], a[mask],
                    radii_possible[idxs[mask]],
                    u1s_possible[idxs[mask]],
                    u2s_possible[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )
    else:
        for i in range(N):
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (loggs_possible[idxs[i]] >= 3.5)
                    & (Teffs_possible[idxs[i]] <= 10000)
                    & (coll[i] == False)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_TP(
                    time, flux, sigma, rps[i],
                    P_orb[i], incs[i], a[i], radii_possible[idxs[i]],
                    u1s_possible[idxs[i]], u2s_possible[idxs[i]],
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )

    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL+600)
        ))
    lnZ = np.log(Z)
    res = {
        'M_s': masses_possible[idxs[idx]],
        'R_s': radii_possible[idxs[idx]],
        'u1': u1s_possible[idxs[idx]],
        'u2': u2s_possible[idxs[idx]],
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': rps[idx],
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': np.zeros(N_samples),
        'R_EB': np.zeros(N_samples),
        'fluxratio_EB': np.zeros(N_samples),
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }
    return res


def lnZ_NEB_unknown(time: np.ndarray, flux: np.ndarray, sigma: float,
                    P_orb: float, Tmag: float, trilegal_fname: str,
                    N: int = 1000000, parallel: bool = False,
                    mission: str = "TESS", flatpriors: bool = False,
                    exptime: float = 0.00139, nsamples: int = 20):
    """
    Calculates the marginal likelihood of the NEB scenario for a star
    of unknown properties.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        Tmag (float): Target star TESS magnitude.
        trilegal_fname (string): File containing trilegal query results.
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
        res_twin (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)

    # sample from prior distributions
    incs = sample_inc(np.random.rand(N))
    qs = sample_q(np.random.rand(N), 1.0)
    eccs = sample_ecc(np.random.rand(N), planet=False, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # determine properties of possible stars
    (Tmags_nearby, masses_nearby, loggs_nearby, Teffs_nearby,
        Zs_nearby, Jmags_nearby, Hmags_nearby, Kmags_nearby, _, _, _, _) = (
        trilegal_results(trilegal_fname, Tmag)
        )
    mask = (Tmag-1 < Tmags_nearby) & (Tmags_nearby < Tmag+1)
    Tmags_possible = Tmags_nearby[mask]
    masses_possible = masses_nearby[mask]
    loggs_possible = loggs_nearby[mask]
    Teffs_possible = Teffs_nearby[mask]
    Zs_possible = Zs_nearby[mask]
    radii_possible = np.sqrt(
        G*masses_possible*Msun / 10**loggs_possible
        ) / Rsun
    N_possible = Tmags_possible.shape[0]
    # determine limb darkening coefficients of background stars
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s
    u1s_possible = np.zeros(N_possible)
    u2s_possible = np.zeros(N_possible)
    for i in range(N_possible):
        this_Teff = ldc_Teffs[np.argmin(
            np.abs(ldc_Teffs-Teffs_possible[i])
            )]
        this_logg = ldc_loggs[np.argmin(
            np.abs(ldc_loggs-loggs_possible[i])
            )]
        mask1 = (ldc_Teffs == this_Teff) & (ldc_loggs == this_logg)
        these_Zs = ldc_Zs[mask1]
        this_Z = these_Zs[np.argmin(np.abs(these_Zs-Zs_possible[i]))]
        mask = (
            (ldc_Zs == this_Z)
            & (ldc_Teffs == this_Teff)
            & (ldc_loggs == this_logg)
            )
        u1s_possible[i], u2s_possible[i] = ldc_u1s[mask], ldc_u2s[mask]
    # draw random sample of background stars
    if N_possible > 0:
        idxs = np.random.randint(0, N_possible, N)
    # if there aren't enough similar stars, don't do the calculation
    else:
        res = {
            'M_s': 0,
            'R_s': 0,
            'u1': 0,
            'u2': 0,
            'P_orb': 0,
            'inc': 0,
            'b': 0,
            'R_p': 0,
            'ecc': 0,
            'argp': 0,
            'M_EB': 0,
            'R_EB': 0,
            'fluxratio_EB': 0,
            'fluxratio_comp': 0,
            'lnZ': -np.inf
        }
        return res

    # calculate properties of the drawn EBs
    masses = qs*masses_possible[idxs]
    radii, Teffs = stellar_relations(
        masses, radii_possible[idxs], Teffs_possible[idxs]
        )
    # calculate flux ratios in the TESS band
    fluxratios = (
        flux_relation(masses)
        / (flux_relation(masses) + flux_relation(masses_possible[idxs]))
        )

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = (
        (G*(masses_possible[idxs]+masses)*Msun)/(4*pi**2)
        * (P_orb*86400)**2
        )**(1/3)
    Ptra = (radii*Rsun + radii_possible[idxs]*Rsun)/a * e_corr
    a_twin = (
        (G*(masses_possible[idxs]+masses)*Msun)/(4*pi**2)
        * (2*P_orb*86400)**2
        )**(1/3)
    Ptra_twin = (radii*Rsun + radii_possible[idxs]*Rsun)/a_twin * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(radii_possible[idxs]*Rsun)
    r_twin = a_twin*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b_twin = r_twin*np.cos(incs*pi/180)/(radii_possible[idxs]*Rsun)

    # find instances with collisions
    coll = ((radii*Rsun + radii_possible[idxs]*Rsun) > a*(1-eccs))
    coll_twin = ((2*radii_possible[idxs]*Rsun) > a_twin*(1-eccs))

    lnL = np.full(N, -np.inf)
    lnL_twin = np.full(N, -np.inf)
    if parallel:
        # q < 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (
            (incs >= inc_min)
            & (coll == False)
            & (qs < 0.95)
            & (loggs_possible[idxs] >= 3.5)
            & (Teffs_possible[idxs] <= 10000)
            )
        # calculate lnL for transiting systems
        companion_fluxratio = np.zeros(N)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_EB_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    P_orb[mask], incs[mask], a[mask],
                    radii_possible[idxs[mask]],
                    u1s_possible[idxs[mask]], u2s_possible[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )
        # q >= 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra_twin <= 1.] = np.arccos(
            Ptra_twin[Ptra_twin <= 1.]
            ) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (
            (incs >= inc_min)
            & (coll == False)
            & (qs >= 0.95)
            & (loggs_possible[idxs] >= 3.5)
            & (Teffs_possible[idxs] <= 10000)
            )
        # calculate lnL for transiting systems
        companion_fluxratio = np.zeros(N)
        lnL_twin[mask] = -0.5*ln2pi - lnsigma - lnL_EB_twin_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask],
                    radii_possible[idxs[mask]],
                    u1s_possible[idxs[mask]], u2s_possible[idxs[mask]],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )
    else:
        for i in range(N):
            # q < 0.95
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] < 0.95)
                    & (loggs_possible[idxs[i]] >= 3.5)
                    & (Teffs_possible[idxs[i]] <= 10000)
                    & (coll[i] == False)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_EB(
                    time, flux, sigma, radii[i], fluxratios[i],
                    P_orb[i], incs[i], a[i], radii_possible[idxs[i]],
                    u1s_possible[idxs[i]], u2s_possible[idxs[i]],
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )
            # q >= 0.95 and 2xP_orb
            if Ptra_twin[i] <= 1:
                inc_min = np.arccos(Ptra_twin[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] >= 0.95)
                    & (loggs_possible[idxs[i]] >= 3.5)
                    & (Teffs_possible[idxs[i]] <= 10000)
                    & (coll_twin[i] == False)):
                lnL_twin[i] = -0.5*ln2pi - lnsigma - lnL_EB_twin(
                    time, flux, sigma, radii[i], fluxratios[i],
                    2*P_orb[i], incs[i], a_twin[i], radii_possible[idxs[i]],
                    u1s_possible[idxs[i]], u2s_possible[idxs[i]],
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )

    # results for q < 0.95
    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL+600)
        ))
    lnZ = np.log(Z)
    res = {
        'M_s': masses_possible[idxs[idx]],
        'R_s': radii_possible[idxs[idx]],
        'u1': u1s_possible[idxs[idx]],
        'u2': u2s_possible[idxs[idx]],
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }
    # results for q >= 0.95 and 2xP_orb
    N_samples = 1000
    idx = (-lnL_twin).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL_twin+600)
        ))
    lnZ = np.log(Z)
    res_twin = {
        'M_s': masses_possible[idxs[idx]],
        'R_s': radii_possible[idxs[idx]],
        'u1': u1s_possible[idxs[idx]],
        'u2': u2s_possible[idxs[idx]],
        'P_orb': 2*P_orb[idx],
        'inc': incs[idx],
        'b': b_twin[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }
    return res, res_twin


def lnZ_NTP_evolved(time: np.ndarray, flux: np.ndarray, sigma: float,
                    P_orb: float, R_s: float, Teff: float, Z: float,
                    N: int = 1000000, parallel: bool = False,
                    mission: str = "TESS", flatpriors: bool = False,
                    exptime: float = 0.00139, nsamples: int = 20):
    """
    Calculates the marginal likelihood of the NTP scenario for
    subgiant stars.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)
    logg = 3.0
    M_s = (10**logg)*(R_s*Rsun)**2 / G / Msun
    # determine target star limb darkening coefficients
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s
    this_Z = ldc_Zs[np.argmin(np.abs(ldc_Zs-Z))]
    this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teff))]
    this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-logg))]
    mask = (
        (ldc_Zs == this_Z)
        & (ldc_Teffs == this_Teff)
        & (ldc_loggs == this_logg)
        )
    u1, u2 = ldc_u1s[mask], ldc_u2s[mask]

    # sample from inc and R_p prior distributions
    rps = sample_rp(np.random.rand(N), np.full(N, M_s), flatpriors)
    incs = sample_inc(np.random.rand(N))
    eccs = sample_ecc(np.random.rand(N), planet=True, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = ((G*M_s*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    Ptra = (rps*Rearth + R_s*Rsun)/a * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(R_s*Rsun)

    # find instances with collisions
    coll = ((rps*Rearth + R_s*Rsun) > a*(1-eccs))

    lnL = np.full(N, -np.inf)
    if parallel:
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll == False)
        # calculate lnL for transiting systems
        a_arr = np.full(N, a)
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        companion_fluxratio = np.zeros(N)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_TP_p(
                    time, flux, sigma, rps[mask],
                    P_orb[mask], incs[mask], a_arr[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )
    else:
        for i in range(N):
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if (incs[i] >= inc_min) & (coll[i] == False):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_TP(
                    time, flux, sigma, rps[i],
                    P_orb[i], incs[i], a[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )

    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL+600)
        ))
    lnZ = np.log(Z)
    res = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': rps[idx],
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': np.zeros(N_samples),
        'R_EB': np.zeros(N_samples),
        'fluxratio_EB': np.zeros(N_samples),
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }
    return res


def lnZ_NEB_evolved(time: np.ndarray, flux: np.ndarray, sigma: float,
                    P_orb: float, R_s: float, Teff: float, Z: float,
                    N: int = 1000000, parallel: bool = False,
                    mission: str = "TESS", flatpriors: bool = False,
                    exptime: float = 0.00139, nsamples: int = 20):
    """
    Calculates the marginal likelihood of the NEB scenario
    for subgiant stars.
    Args:
        time (numpy array): Time of each data point
                            [days from transit midpoint].
        flux (numpy array): Normalized flux of each data point.
        sigma (float): Normalized flux uncertainty.
        P_orb (float): Orbital period [days].
        R_s (float): Target star radius [Solar radii].
        Teff (float): Target star effective temperature [K].
        Z (float): Target star metallicity [dex].
        N (int): Number of draws for MC.
        parallel (bool): Whether or not to simulate light curves
                         in parallel.
        mission (str): TESS, Kepler, or K2.
        flatpriors (bool): Assume flat Rp and Porb planet priors?
        exptime (float): Exposure time of observations [days].
        nsamples (int): Sampling rate for supersampling.
    Returns:
        res (dict): Best-fit properties and marginal likelihood.
        res_twin (dict): Best-fit properties and marginal likelihood.
    """
    # sample orbital periods if range is given
    if type(P_orb) not in [float,int]:
        P_orb = np.random.uniform(
            low=P_orb[0], high=P_orb[-1], size=N
            )
    else:
        P_orb = np.full(N, P_orb)

    lnsigma = np.log(sigma)
    logg = 3.0
    M_s = (10**logg)*(R_s*Rsun)**2 / G / Msun
    # determine target star limb darkening coefficients
    if mission == "TESS":
        ldc_Zs = ldc_T_Zs
        ldc_Teffs = ldc_T_Teffs
        ldc_loggs = ldc_T_loggs
        ldc_u1s = ldc_T_u1s
        ldc_u2s = ldc_T_u2s
    else:
        ldc_Zs = ldc_K_Zs
        ldc_Teffs = ldc_K_Teffs
        ldc_loggs = ldc_K_loggs
        ldc_u1s = ldc_K_u1s
        ldc_u2s = ldc_K_u2s
    this_Z = ldc_Zs[np.argmin(np.abs(ldc_Zs-Z))]
    this_Teff = ldc_Teffs[np.argmin(np.abs(ldc_Teffs-Teff))]
    this_logg = ldc_loggs[np.argmin(np.abs(ldc_loggs-logg))]
    mask = (
        (ldc_Zs == this_Z)
        & (ldc_Teffs == this_Teff)
        & (ldc_loggs == this_logg)
        )
    u1, u2 = ldc_u1s[mask], ldc_u2s[mask]

    # sample from inc and q prior distributions
    incs = sample_inc(np.random.rand(N))
    qs = sample_q(np.random.rand(N), 1.0)
    eccs = sample_ecc(np.random.rand(N), planet=False, P_orb=np.mean(P_orb))
    argps = sample_w(np.random.rand(N))

    # calculate properties of the drawn EBs
    masses = qs*M_s
    radii, Teffs = stellar_relations(
        masses, np.full(N, R_s), np.full(N, Teff)
        )
    fluxratios = (
        flux_relation(masses)
        / (flux_relation(masses) + flux_relation(np.array([M_s])))
        )

    # calculate transit probability for each instance
    e_corr = (1+eccs*np.sin(argps*pi/180))/(1-eccs**2)
    a = ((G*(M_s+masses)*Msun)/(4*pi**2)*(P_orb*86400)**2)**(1/3)
    Ptra = (radii*Rsun + R_s*Rsun)/a * e_corr
    a_twin = ((G*(M_s+masses)*Msun)/(4*pi**2)*(2*P_orb*86400)**2)**(1/3)
    Ptra_twin = (R_s*Rsun + R_s*Rsun)/a_twin * e_corr

    # calculate impact parameter
    r = a*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b = r*np.cos(incs*pi/180)/(R_s*Rsun)
    r_twin = a_twin*(1-eccs**2)/(1+eccs*np.sin(argps*np.pi/180))
    b_twin = r_twin*np.cos(incs*pi/180)/(R_s*Rsun)

    # find instances with collisions
    coll = ((radii*Rsun + R_s*Rsun) > a*(1-eccs))
    coll_twin = ((2*R_s*Rsun) > a_twin*(1-eccs))

    lnL = np.full(N, -np.inf)
    lnL_twin = np.full(N, -np.inf)
    if parallel:
        # q < 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra <= 1.] = np.arccos(Ptra[Ptra <= 1.]) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll == False) & (qs < 0.95)
        # calculate lnL for transiting systems
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        companion_fluxratio = np.zeros(N)
        lnL[mask] = -0.5*ln2pi - lnsigma - lnL_EB_p(
                    time, flux, sigma, radii[mask], fluxratios[mask],
                    P_orb[mask], incs[mask], a[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )
        # q >= 0.95
        # find minimum inclination each planet can have while transiting
        inc_min = np.full(N, 90.)
        inc_min[Ptra_twin <= 1.] = np.arccos(
            Ptra_twin[Ptra_twin <= 1.]
            ) * 180./pi
        # filter out systems that do not transit or have a collision
        mask = (incs >= inc_min) & (coll_twin == False) & (qs >= 0.95)
        # calculate lnL for transiting systems
        R_s_arr = np.full(N, R_s)
        u1_arr = np.full(N, u1)
        u2_arr = np.full(N, u2)
        companion_fluxratio = np.zeros(N)
        lnL_twin[mask] = -0.5*ln2pi - lnsigma - lnL_EB_twin_p(
                    time, flux, sigma, R_s, fluxratios[mask],
                    2*P_orb[mask], incs[mask], a_twin[mask], R_s_arr[mask],
                    u1_arr[mask], u2_arr[mask],
                    eccs[mask], argps[mask],
                    companion_fluxratio=companion_fluxratio[mask],
                    exptime=exptime, nsamples=nsamples
                    )
    else:
        for i in range(N):
            # q < 0.95
            if Ptra[i] <= 1:
                inc_min = np.arccos(Ptra[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] < 0.95)
                    & (coll[i] == False)):
                lnL[i] = -0.5*ln2pi - lnsigma - lnL_EB(
                    time, flux, sigma, radii[i], fluxratios[i],
                    P_orb[i], incs[i], a[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )
            # q >= 0.95 and 2xP_orb
            if Ptra_twin[i] <= 1:
                inc_min = np.arccos(Ptra_twin[i]) * 180/pi
            else:
                continue
            if ((incs[i] >= inc_min) & (qs[i] >= 0.95)
                    & (coll_twin[i] == False)):
                lnL_twin[i] = -0.5*ln2pi - lnsigma - lnL_EB_twin(
                    time, flux, sigma, R_s, fluxratios[i],
                    2*P_orb[i], incs[i], a_twin[i], R_s, u1, u2,
                    eccs[i], argps[i],
                    exptime=exptime, nsamples=nsamples
                    )

    # results for q < 0.95
    N_samples = 1000
    idx = (-lnL).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL + 600)
        ))
    lnZ = np.log(Z)
    res = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': P_orb[idx],
        'inc': incs[idx],
        'b': b[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': radii[idx],
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }
    # results for q >= 0.95 and 2xP_orb
    N_samples = 1000
    idx = (-lnL_twin).argsort()[:N_samples]
    Z = np.mean(np.nan_to_num(
        np.exp(lnL_twin+600)
        ))
    lnZ = np.log(Z)
    res_twin = {
        'M_s': np.full(N_samples, M_s),
        'R_s': np.full(N_samples, R_s),
        'u1': np.full(N_samples, u1),
        'u2': np.full(N_samples, u2),
        'P_orb': 2*P_orb[idx],
        'inc': incs[idx],
        'b': b_twin[idx],
        'R_p': np.zeros(N_samples),
        'ecc': eccs[idx],
        'argp': argps[idx],
        'M_EB': masses[idx],
        'R_EB': np.full(N_samples, R_s),
        'fluxratio_EB': fluxratios[idx],
        'fluxratio_comp': np.zeros(N_samples),
        'lnZ': lnZ
    }
    return res, res_twin
