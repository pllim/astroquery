# Licensed under a 3-clause BSD style license - see LICENSE.rst
# Hanno Rein 2013
# hanno@hanno-rein.de

from xml.etree import ElementTree as ET
from astropy.tests.helper import pytest
from astropy.tests.helper import remote_data
from ... import open_exoplanet_catalogue as oec

@remote_data
def test_function():

    cata = oec.get_catalogue()
    kepler67b = cata.find(".//planet[name='Kepler-67 b']")
    assert kepler67b.findtext('name') == "Kepler-67 b"
    assert kepler67b.findtext('discoverymethod') == "transit"

    kepler67 = cata.find(".//system[name='Kepler-67']")
    assert kepler67.findvalue('distance') == 1107
