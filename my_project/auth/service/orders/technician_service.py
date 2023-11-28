
from my_project.auth.dao import technician_dao
from my_project.auth.service.general_service import GeneralService


class TechnicianService(GeneralService):

    _dao = technician_dao

    def technicians_find_fundraising(self, technician_id: int):
        return self._dao.technicians_find_fundraising(technician_id)

    def technician_find_coins_loading(self, technician_id: int):
        return self._dao.technician_find_coins_loading(technician_id)

    def technician_find_product_loading(self, technician_id: int):
        return self._dao.technician_find_product_loading(technician_id)
