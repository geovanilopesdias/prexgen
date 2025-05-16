from enum import Enum
from services import EscalarQuantity, UnitiesTable

class PhysicalConstants(Enum):
    EARTH_GRAVITY_ACCELERATION = EscalarQuantity(
        9.8, UnitiesTable.METER_PER_SECOND_SQUARE,
        'aceleração gravitacional', False
    )

    SPEED_OF_LIGHT = EscalarQuantity(
        299_792_458, UnitiesTable.METER_PER_SECOND,
        'velocidade da luz', False
    )

    ELECTRON_CHARGE = EscalarQuantity(
        1.602176634e-19, UnitiesTable.COULOMB,
        'carga do elétron', False
    )



