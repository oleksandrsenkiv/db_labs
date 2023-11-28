
from my_project.auth.service import gps_service
from my_project.auth.controller.general_controller import GeneralController


class GpsController(GeneralController):

    _service = gps_service
