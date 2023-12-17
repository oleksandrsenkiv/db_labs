from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Gps


class GpsDAO(GeneralDAO):
    _domain_type = Gps
