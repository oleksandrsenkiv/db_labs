
from my_project.auth.service import vending_machine_service
from my_project.auth.controller.general_controller import GeneralController


class VendingMachineController(GeneralController):

    _service = vending_machine_service
