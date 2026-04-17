from dataclasses import dataclass, field


class ErrorMetaMayorACero(Exception):
    """
    Se usa cuando la meta del ahorro es menor o igual que 0
    """
    def __init__(self, ahorro):
        super().__init__(f"Error: la meta de ahorro {ahorro.meta} ingresada debe ser mayor a 0")


class ErrorPlazoMayorACero(Exception):
    """
    Se usa cuando el plazo del ahorro es igual o menor que 0
    """
    def __init__(self, ahorro):
        super().__init__( f"Error: el plazo {ahorro.plazo} ingresado debe ser mayor a 0")


class ErrorAbonoSuperaMeta(Exception):
    """
    Se usa cuando el abono extra supera la meta de ahorro
    """
    def __init__(self, ahorro):
        super().__init__( f"Error: El extra {ahorro.extra} ingresado supera la meta de ahorro {ahorro.meta}")


class ErrorMesExtraFueraDelRango(Exception):
    """
    Se usa cuando el mes donde se hace el abono extra es mayor que la meta del ahorro programado
    """
    def __init__(self, ahorro): 
        super().__init__( f"Error: el mes extra ingresado {ahorro.mes_extra} debe estar entre 1 y el plazo {ahorro.plazo}")


class ErrorAbonoExtraMenorAcero(Exception):
    """
    Se usa cuando el abono extra es menor que 0
    """
    def __init__(self, ahorro):
        super().__init__(f"Error: abono {ahorro.extra} ingresado debe ser mayor que 0")
        
        
        
@dataclass
class Ahorro: 
    """
    Documentacion Ahorro

    :ivar tasa: La tasa de interés mensual valor constante
    :vartype tasa: float

    :param meta: La meta a la cual se desea llegar
    :type meta: float

    :param plazo: El plazo en meses para alcanzar la meta
    :type plazo: int

    :param extra: El monto extra que se desea aportar en un mes específico
    :type extra: float

    :param mes_extra: El mes en el que se hará el aporte extra
    :type mes_extra: int

    :return: El monto que se debe ahorrar cada mes para alcanzar la meta
    :rtype: float
    """
    tasa: float = field(default=0.0075, init=False)
    meta: float
    plazo: int
    extra: float
    mes_extra: int

    


@dataclass
class AhorroProgramado: 
    def calcular_ahorro(self, ahorro: Ahorro) -> float:
        """
        Método principal que calcula la cuota mensual necesaria
        para alcanzar la meta de ahorro.
        """

        self._validar_datos(ahorro)

        if ahorro.meta == 0:
            return 0

        if ahorro.extra == ahorro.meta:
            return 0

        valor_futuro_extra = self._calcular_valor_futuro_extra(ahorro)
        factor_anualidad = self._calcular_factor_anualidad(ahorro)

        cuota_mensual = (ahorro.meta - valor_futuro_extra) / factor_anualidad

        return round(cuota_mensual, 2)

    def _validar_datos(self, ahorro: Ahorro):
        """
        Realiza todas las validaciones de los datos ingresados
        antes de ejecutar el cálculo financiero.
        """

        if ahorro.meta < 0:
            raise ErrorMetaMayorACero(ahorro)

        if ahorro.plazo <= 0:
            raise ErrorPlazoMayorACero(ahorro)

        if ahorro.extra < 0:
            raise ErrorAbonoExtraMenorAcero(ahorro)

        if ahorro.extra > ahorro.meta:
            raise ErrorAbonoSuperaMeta(ahorro)

        if ahorro.mes_extra < 0 or ahorro.mes_extra > ahorro.plazo:
            raise ErrorMesExtraFueraDelRango(ahorro)

    def _calcular_valor_futuro_extra(self, ahorro: Ahorro) -> float:
        """
        Calcula el valor futuro del abono extra considerando
        el número de meses restantes hasta el final del plazo.
        """

        meses_restantes = ahorro.plazo - ahorro.mes_extra

        valor_futuro_extra = ahorro.extra * (1 + ahorro.tasa) ** meses_restantes

        return valor_futuro_extra

    def _calcular_factor_anualidad(self, ahorro: Ahorro) -> float:
        """
        Calcula el factor financiero correspondiente
        a una anualidad ordinaria con interés compuesto.
        """

        factor = ((1 + ahorro.tasa) ** ahorro.plazo - 1) / ahorro.tasa

        return factor