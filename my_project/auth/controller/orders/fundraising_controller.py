
from my_project.auth.service import fundraising_service
from my_project.auth.controller.general_controller import GeneralController


class FundraisingController(GeneralController):

    _service = fundraising_service

    def fundraising_find_technician(self, fundraising_id : int):
        return self._service.fundraising_find_technician(fundraising_id)
