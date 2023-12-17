
from my_project.auth.service import coins_loading_service
from my_project.auth.controller.general_controller import GeneralController


class CoinsLoadingController(GeneralController):

    _service = coins_loading_service

    def coins_loading_find_technician(self, coins_loading_id: int):
        return self._service.coins_loading_find_technician(coins_loading_id)
