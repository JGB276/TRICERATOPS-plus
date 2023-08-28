from urllib.request import urlopen
from bs4 import BeautifulSoup
from astropy.io import fits
import numpy as np

def segment_ID(str_segment):

    if len(str_segment) == 0:
        return "0000"
    elif len(str_segment) == 1:
        return "000"+str_segment
    elif len(str_segment) == 2:
        return "00"+str_segment
    elif len(str_segment) == 3:
        return "0"+str_segment
    elif len(str_segment) == 4:
        return str_segment

def find_url(ID, sector):

    url = "https://archive.stsci.edu/missions/tess/tid/"

    if len(str(sector)) == 1:
        str1 = "s000"+str(sector)
    elif len(str(sector)) == 2:
        str1 = "s00"+str(sector)

    str2 = segment_ID(str(ID)[-16:-12])
    str3 = segment_ID(str(ID)[-12:-8])
    str4 = segment_ID(str(ID)[-8:-4])
    str5 = segment_ID(str(ID)[-4:])

    url += str1+"/"+str2+"/"+str3+"/"+str4+"/"+str5+"/"

    urlpath = urlopen(url)
    string = urlpath.read().decode('utf-8')
    soup = BeautifulSoup(string, 'html.parser')
    for link in soup.find_all('a'):
        if (link.get('href')[-9:]) == "s_lc.fits":
            url += link.get('href')

    return url

def get_aperture(ID, sector):

    fits_file = find_url(ID, sector)

    with fits.open(fits_file, mode="readonly") as hdulist:
        aperture = hdulist[2].data

    ap_pixels = np.argwhere(aperture == np.max(aperture))
    ap_pixels[:,0] += hdulist[2].header["CRVAL2P"]
    ap_pixels[:,1] += hdulist[2].header["CRVAL1P"]
    ap_pixels = np.flip(ap_pixels, axis=1)

    return ap_pixels

# To get list of apertures for all sectors, run the following lines
#
# aps = []
# these_sectors = [...] # list or array of ints
# this_ID = ... # int
# for sector in these_sectors:
#     ap = get_aperture(this_ID, sector)
#     aps.append(ap)
