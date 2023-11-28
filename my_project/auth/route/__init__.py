"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.snack_availability_route import snack_availability_bp
    from .orders.brand_route import brand_bp
    from .orders.snacks_route import snacks_bp
    from .orders.fundraising_route import fundraising_bp
    from .orders.coins_loading_route import coins_loading_bp
    from .orders.technician_route import technician_bp
    from .orders.gps_route import gps_bp
    from .orders.vm_menu_route import vm_menu_bp
    from .orders.vending_machine_route import vending_machine_bp
    from .orders.product_loading_route import product_loading_bp

    app.register_blueprint(snack_availability_bp)
    app.register_blueprint(brand_bp)
    app.register_blueprint(snacks_bp)
    app.register_blueprint(fundraising_bp)
    app.register_blueprint(coins_loading_bp)
    app.register_blueprint(technician_bp)
    app.register_blueprint(gps_bp)
    app.register_blueprint(vm_menu_bp)
    app.register_blueprint(vending_machine_bp)
    app.register_blueprint(product_loading_bp)

