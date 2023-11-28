
from my_project.auth.dao import fundraising_dao
from my_project.auth.service.general_service import GeneralService


class FundraisingService(GeneralService):

    _dao = fundraising_dao

    def fundraising_find_technician(self,fundraising_id : int):
        return self._dao.fundraising_find_technician(fundraising_id)
