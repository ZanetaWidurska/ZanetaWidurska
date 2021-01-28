# -*- coding: utf-8 -*-
import pytest

from angles import deg2grad, grad2deg
from angles import grad2rad, rad2grad
from angles import decimal_deg2rad, rad2decimal_deg
from angles import decimal_deg2dms_deg


def test_deg2grad():
    assert deg2grad(0) == 0
    assert deg2grad(45) == 50
    assert deg2grad(90) == 100
    assert deg2grad(135) == 150 
    assert deg2grad(180) == 200
    assert deg2grad(225) == 250
    assert deg2grad(270) == 300
    assert deg2grad(315) == 350
    assert deg2grad(360) == 400


def test_grad2deg():
    assert grad2deg(0) == 0
    assert grad2deg(50) == 45
    assert grad2deg(100) == 90
    assert grad2deg(150) == 135
    assert grad2deg(200) == 180
    assert grad2deg(250) == 225
    assert grad2deg(300) == 270
    assert grad2deg(350) == 315
    assert grad2deg(400) == 360


def test_grad2rad():
    assert pytest.approx(grad2rad(0)) == 0
    assert pytest.approx(grad2rad(50)) == 0.7853981633974484
    assert pytest.approx(grad2rad(100)) == 1.5707963267948968
    assert pytest.approx(grad2rad(150)) == 2.356194490192345
    assert pytest.approx(grad2rad(200)) == 3.1415926535897936
    assert pytest.approx(grad2rad(250)) == 3.926990816987242
    assert pytest.approx(grad2rad(300)) == 4.71238898038469
    assert pytest.approx(grad2rad(350)) == 5.497787143782139
    assert pytest.approx(grad2rad(400)) == 6.283185307179587


def test_rad2grad():
    assert pytest.approx(rad2grad(0)) == 0
    assert pytest.approx(rad2grad(0.7853981633974484)) == 50
    assert pytest.approx(rad2grad(1.5707963267948968)) == 100
    assert pytest.approx(rad2grad(2.356194490192345)) == 150
    assert pytest.approx(rad2grad(3.1415926535897936)) == 200
    assert pytest.approx(rad2grad(3.926990816987242)) == 250
    assert pytest.approx(rad2grad(4.71238898038469)) == 300
    assert pytest.approx(rad2grad(5.497787143782139)) == 350
    assert pytest.approx(rad2grad(6.283185307179587)) == 400


def test_decimal_deg2rad():
    assert pytest.approx(decimal_deg2rad(0)) == 0
    assert pytest.approx(decimal_deg2rad(45)) == 0.7853981633974484
    assert pytest.approx(decimal_deg2rad(90)) == 1.5707963267948968
    assert pytest.approx(decimal_deg2rad(135)) == 2.356194490192345
    assert pytest.approx(decimal_deg2rad(180)) == 3.1415926535897936
    assert pytest.approx(decimal_deg2rad(225)) == 3.926990816987242
    assert pytest.approx(decimal_deg2rad(270)) == 4.71238898038469
    assert pytest.approx(decimal_deg2rad(315)) == 5.497787143782139
    assert pytest.approx(decimal_deg2rad(360)) == 6.283185307179587


def test_rad2decimal_deg():
    assert pytest.approx(rad2decimal_deg(0)) == 0
    assert pytest.approx(rad2decimal_deg(0.7853981633974484)) == 45
    assert pytest.approx(rad2decimal_deg(1.5707963267948968)) == 90
    assert pytest.approx(rad2decimal_deg(2.356194490192345)) == 135
    assert pytest.approx(rad2decimal_deg(3.1415926535897936)) == 180
    assert pytest.approx(rad2decimal_deg(3.926990816987242)) == 225
    assert pytest.approx(rad2decimal_deg(4.71238898038469)) == 270
    assert pytest.approx(rad2decimal_deg(5.497787143782139)) == 315
    assert pytest.approx(rad2decimal_deg(6.283185307179587)) == 360


def test_decimal_deg2dms_deg():
    assert decimal_deg2dms_deg(1.0169722222222222)[:2] == (1, 1)
    assert pytest.approx(decimal_deg2dms_deg(1.0169722222222222)[2]) == 1.1


def test_dms_deg2decimal_deg():
    # correct for 5
    pass
