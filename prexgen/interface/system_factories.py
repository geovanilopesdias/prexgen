from enum import Enum
from problems import *

class SystemFactories(Enum):
    AVERAGE_SPEED = AverageSpeed.FACTORIES
    UVRM = Uvrm.FACTORIES
    MECH_ENERGY_CONS = MechanicalEnergyConservation.FACTORIES
    CONCENTRATION = Concentration.FACTORIES
