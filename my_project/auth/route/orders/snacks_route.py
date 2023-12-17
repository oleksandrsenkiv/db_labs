
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import snacks_controller
from my_project.auth.domain import Snacks

snacks_bp = Blueprint('snacks', __name__, url_prefix='/snacks')


@snacks_bp.get('/all')
def get_all_snacks() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(snacks_controller.find_all()), HTTPStatus.OK)


@snacks_bp.get('/<int:snacks_id>/snacks_has_brands')
def get_all_snacks_from_brands(snacks_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(snacks_controller.snacks_find_brand(snacks_id)), HTTPStatus.OK)


@snacks_bp.get('/<int:snacks_id>/snacks_has_vm_menu')
def get_all_snack_availability_vm_menu_from_snacks(snacks_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(snacks_controller.snacks_find_snack_availability_vm_menu(snacks_id)), HTTPStatus.OK)


@snacks_bp.post('/create_db_from_snacks')
def create_db_from_snacks() -> Response:
    try:
        snacks_controller.create_db_from_snacks()
        return make_response(jsonify({"message": "db created successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@snacks_bp.post('')
def create_snacks() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    snacks = Snacks.create_from_dto(content)
    snacks_controller.create(snacks)
    return make_response(jsonify(snacks.put_into_dto()), HTTPStatus.CREATED)


@snacks_bp.post('/<int:snacks_id>/add_brand')
def add_snack_to_brand(snacks_id) -> Response:
    try:
        data = request.get_json()
        brand_id = data.get('brand_id')
        snacks_controller.add_brand_to_snack(snacks_id, brand_id)
        return make_response(jsonify({"message": "Brand added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@snacks_bp.post('/<int:snacks_id>/add_vending_availability')
def add_vending_availability(snacks_id) -> Response:
    try:
        data = request.get_json()
        vm_menu_id = data.get('vm_menu_id')
        snack_availability_id = data.get('snack_availability_id')
        snacks_controller.add_vm_menu_and_availability_to_snack(snacks_id, vm_menu_id, snack_availability_id)
        return make_response(jsonify({"message": "vending_machine and snack_availability added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@snacks_bp.post('/insert_no_name')
def insert_no_name_into_snacks() -> Response:
    try:
        snacks_controller.insert_ten_no_name_snacks()
        return make_response(jsonify({"message": "No name snacks added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@snacks_bp.post('/insert_into_snacks_has_brand')
def insert_into_sacks_has_brand() -> Response:
    try:
        data = request.get_json()
        brand_name = data.get('insert_brand_name')
        snack_name = data.get('insert_snack_name')
        snacks_controller.insert_in_snacks_has_brand(brand_name, snack_name)
        return make_response(jsonify({"message": "Brand added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@snacks_bp.get('/<int:snacks_id>')
def get_snacks(snacks_id: int) -> Response:
    """
    Gets snacks by ID.
    :return: Response object
    """
    return make_response(jsonify(snacks_controller.find_by_id(snacks_id)), HTTPStatus.OK)


@snacks_bp.put('/<int:snacks_id>')
def update_snacks(snacks_id: int) -> Response:
    """
    Updates snacks by ID.
    :return: Response object
    """
    content = request.get_json()
    snacks = Snacks.create_from_dto(content)
    snacks_controller.update(snacks_id, snacks)
    return make_response("Snacks updated", HTTPStatus.OK)


@snacks_bp.patch('/<int:snacks_id>')
def patch_snacks(snacks_id: int) -> Response:
    """
    Patches snacks by ID.
    :return: Response object
    """
    content = request.get_json()
    snacks_controller.patch(snacks_id, content)
    return make_response("Snacks updated", HTTPStatus.OK)


@snacks_bp.patch('/<int:snacks_id>/remove_brand')
def remove_brand_from_snack(snacks_id) -> Response:
    try:
        data = request.get_json()
        brand_id = data.get('brand_id')
        snacks_controller.remove_brand_from_snack(snacks_id, brand_id)
        return make_response(jsonify({"message": "Brand removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@snacks_bp.patch('/<int:snacks_id>/remove_vm_menu_and_availability')
def remove_vm_menu_and_availability_from_snack(snacks_id) -> Response:
    try:
        data = request.get_json()
        vm_menu_id = data.get('vm_menu_id')
        snack_availability_id = data.get('snack_availability_id')
        snacks_controller.remove_vm_menu_and_availability_from_snack(snacks_id, vm_menu_id, snack_availability_id)
        return make_response(jsonify({"message": "vm_menu and snack_availability removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@snacks_bp.delete('/<int:snacks_id>')
def delete_snacks(snacks_id: int) -> Response:
    """
    Deletes snacks by ID.
    :return: Response object
    """
    snacks_controller.delete(snacks_id)
    return make_response("Snacks deleted", HTTPStatus.OK)
