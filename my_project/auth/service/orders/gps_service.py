
from my_project.auth.dao import gps_dao
from my_project.auth.service.general_service import GeneralService


class GpsService(GeneralService):

    _dao = gps_dao
