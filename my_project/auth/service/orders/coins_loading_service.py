
from my_project.auth.dao import coins_loading_dao
from my_project.auth.service.general_service import GeneralService


class CoinsLoadingService(GeneralService):

    _dao = coins_loading_dao

    def coins_loading_find_technician(self, coins_loading_id: int):
        return self._dao.coins_loading_find_technician(coins_loading_id)
