
from my_project.auth.service import technician_service
from my_project.auth.controller.general_controller import GeneralController


class TechnicianController(GeneralController):

    _service = technician_service

    def technicians_find_fundraising(self, technician_id : int):
        return self._service.technicians_find_fundraising(technician_id)

    def technician_find_coins_loading(self, technician_id: int):
        return self._service.technician_find_coins_loading(technician_id)

    def technician_find_product_loading(self, technician_id: int):
        return self._service.technician_find_product_loading(technician_id)
