
from .orders.snack_availability_controller import SnackAvailabilityController
from .orders.snacks_controller import SnacksController
from .orders.brand_controller import BrandController
from .orders.coins_loading_controller import CoinsLoadingController
from .orders.fundraising_controller import FundraisingController
from .orders.gps_controller import GpsController
from .orders.technician_controller import TechnicianController
from .orders.vm_menu_controller import VmMenuController
from .orders.vending_machine_controller import VendingMachineController
from .orders.product_loading_controller import ProductLoadingController


snack_availability_controller = SnackAvailabilityController()
snacks_controller = SnacksController()
brand_controller = BrandController()
fundraising_controller = FundraisingController()
coins_loading_controller = CoinsLoadingController()
gps_controller = GpsController()
technician_controller = TechnicianController()
vm_menu_controller = VmMenuController()
vending_machine_controller = VendingMachineController()
product_loading_controller = ProductLoadingController()
