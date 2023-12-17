
from .orders.sanck_availability_dao import SnackAvailabilityDAO
from .orders.snacks_dao import SnacksDAO
from .orders.brand_dao import BrandDAO
from .orders.coins_loading_dao import CoinsLoadingDAO
from .orders.fundraising_dao import FundraisingDAO
from .orders.gps_dao import GpsDAO
from .orders.technician_dao import TechnicianDAO
from .orders.vm_menu_dao import VmMenuDAO
from .orders.vending_machine_dao import VendingMachineDAO
from .orders.product_loading_dao import ProductLoadingDAO


snack_availability_dao = SnackAvailabilityDAO()
snacks_dao = SnacksDAO()
brand_dao = BrandDAO()
coins_loading_dao = CoinsLoadingDAO()
fundraising_dao = FundraisingDAO()
gps_dao = GpsDAO()
technician_dao = TechnicianDAO()
vm_menu_dao = VmMenuDAO()
vending_machine_dao = VendingMachineDAO()
product_loading_dao = ProductLoadingDAO()
