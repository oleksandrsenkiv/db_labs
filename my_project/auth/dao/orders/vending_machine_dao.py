from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import VendingMachine


class VendingMachineDAO(GeneralDAO):
    _domain_type = VendingMachine
