# -*- coding: utf-8 -*-
import math


def deg2grad(deg):
    """
    deg2grad(90.00) --> 100.0
    """

    return deg*(10/9)


def grad2deg(grad):
    """
    grad2deg(100.00) --> 90.0
    """

    return grad*(9/10)


def grad2rad(grad):
    """
    grad2rad(100.0) --> 1.5707963267948968
    """

    return grad*(9/10)*(math.pi/180)


def rad2grad(rad):
    """
    rad2grad(1.5707963267948968) --> 90.0
    """

    return rad*(10/9)*(180/math.pi)


# ======================== for 3


def decimal_deg2rad(decimal_deg):
    """
    decimal_deg(1.5707963267948968) --> 90.0
    """

    return None

def rad2decimal_deg(rad):
    """
    rad2decimal_deg(1.5707963267948968) --> 90.0
    """

    return None

# ======================== for 4

def decimal_deg2dms_deg(decimal_deg):
    """
    decimal_deg2dms_deg(1.0169722222222222) --> (1, 1, 1.1)
    """

    return None


def dms_deg2decimal_deg(dms_deg):
    """
    dms_deg2decimal_deg(1, 1, 1.1) --> (1.0169722222222222)
    """

    return None

# ======================== for 5
