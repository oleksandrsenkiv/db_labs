
from my_project.auth.dao import vending_machine_dao
from my_project.auth.service.general_service import GeneralService


class VendingMachineService(GeneralService):

    _dao = vending_machine_dao
