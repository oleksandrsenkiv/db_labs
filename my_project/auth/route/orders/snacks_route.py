
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


@snacks_bp.delete('/<int:snacks_id>')
def delete_snacks(snacks_id: int) -> Response:
    """
    Deletes snacks by ID.
    :return: Response object
    """
    snacks_controller.delete(snacks_id)
    return make_response("Snacks deleted", HTTPStatus.OK)
