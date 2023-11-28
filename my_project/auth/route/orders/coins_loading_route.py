
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import coins_loading_controller
from my_project.auth.domain import CoinsLoading

coins_loading_bp = Blueprint('coins_loading', __name__, url_prefix='/coins_loading')


@coins_loading_bp.get('/all')
def get_all_coins_loading() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(coins_loading_controller.find_all()), HTTPStatus.OK)


@coins_loading_bp.get('/<int:coins_loading_id>/technician_has_coins_loading')
def get_all_coins_loading_from_technician(coins_loading_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(coins_loading_controller.coins_loading_find_technician(coins_loading_id)), HTTPStatus.OK)

@coins_loading_bp.post('')
def create_coins_loading() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    coins_loading = CoinsLoading.create_from_dto(content)
    coins_loading_controller.create(coins_loading)
    return make_response(jsonify(coins_loading.put_into_dto()), HTTPStatus.CREATED)


@coins_loading_bp.get('/<int:coins_loading_id>')
def get_coins_loading(coins_loading_id: int) -> Response:
    """
    Gets coins_loading by ID.
    :return: Response object
    """
    return make_response(jsonify(coins_loading_controller.find_by_id(coins_loading_id)), HTTPStatus.OK)


@coins_loading_bp.put('/<int:coins_loading_id>')
def update_coins_loading(coins_loading_id: int) -> Response:
    """
    Updates coins_loading by ID.
    :return: Response object
    """
    content = request.get_json()
    coins_loading = CoinsLoading.create_from_dto(content)
    coins_loading_controller.update(coins_loading_id, coins_loading)
    return make_response("coins_loading updated", HTTPStatus.OK)


@coins_loading_bp.patch('/<int:coins_loading_id>')
def patch_coins_loading(coins_loading_id: int) -> Response:
    """
    Patches coins_loading by ID.
    :return: Response object
    """
    content = request.get_json()
    coins_loading_controller.patch(coins_loading_id, content)
    return make_response("coins_loading updated", HTTPStatus.OK)


@coins_loading_bp.delete('/<int:coins_loading_id>')
def delete_coins_loading(coins_loading_id: int) -> Response:
    """
    Deletes coins_loading by ID.
    :return: Response object
    """
    coins_loading_controller.delete(coins_loading_id)
    return make_response("coins_loading deleted", HTTPStatus.OK)
