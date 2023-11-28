
from .orders.snack_availability_service import SnackAvailabilityService
from .orders.snacks_service import SnacksService
from .orders.brand_service import BrandService
from .orders.coins_loading_service import CoinsLoadingService
from .orders.fundraising_service import FundraisingService
from .orders.technician_service import TechnicianService
from .orders.gps_service import GpsService
from .orders.vm_menu_service import VmMenuService
from .orders.vending_machine_service import VendingMachineService
from .orders.product_loading_service import ProductLoadingService


snack_availability_service = SnackAvailabilityService()
snacks_service = SnacksService()
brand_service = BrandService()
coins_loading_service = CoinsLoadingService()
fundraising_service = FundraisingService()
technician_service = TechnicianService()
gps_service = GpsService()
vm_menu_service = VmMenuService()
vending_machine_service = VendingMachineService()
product_loading_service = ProductLoadingService()
