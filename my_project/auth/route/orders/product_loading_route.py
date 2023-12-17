
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import product_loading_controller
from my_project.auth.domain import ProductLoading

product_loading_bp = Blueprint('product_loading', __name__, url_prefix='/product_loading')


@product_loading_bp.get('/all')
def get_all_product_loading() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(product_loading_controller.find_all()), HTTPStatus.OK)


@product_loading_bp.get('/<int:product_loading_id>')
def get_gps(product_loading_id: int) -> Response:
    """
    Gets gps by ID.
    :return: Response object
    """
    return make_response(jsonify(product_loading_controller.find_by_id(product_loading_id)), HTTPStatus.OK)


@product_loading_bp.get('/<int:product_loading_id>/technician_has_product_loading')
def get_all_technician_from_product_loading(product_loading_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(product_loading_controller.product_loading_find_technician(product_loading_id)), HTTPStatus.OK)


@product_loading_bp.get('/get_product_loading_stats/<stats_type>')
def get_product_loading_stats(stats_type: str) -> Response:
    return make_response(jsonify(product_loading_controller.get_product_loading_stats(stats_type)), HTTPStatus.OK)


@product_loading_bp.post('')
def create_product_loading() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    product_loading = ProductLoading.create_from_dto(content)
    product_loading_controller.create(product_loading)
    return make_response(jsonify(product_loading.put_into_dto()), HTTPStatus.CREATED)


@product_loading_bp.put('/<int:product_loading_id>')
def update_product_loading(product_loading_id: int) -> Response:
    """
    Updates product_loading by ID.
    :return: Response object
    """
    content = request.get_json()
    product_loading = ProductLoading.create_from_dto(content)
    product_loading_controller.update(product_loading_id, product_loading)
    return make_response("product_loading updated", HTTPStatus.OK)


@product_loading_bp.patch('/<int:product_loading_id>')
def patch_product_loading(product_loading_id: int) -> Response:
    """
    Patches product_loading by ID.
    :return: Response object
    """
    content = request.get_json()
    product_loading_controller.patch(product_loading_id, content)
    return make_response("product_loading updated", HTTPStatus.OK)


@product_loading_bp.delete('/<int:product_loading_id>')
def delete_product_loading(product_loading_id: int) -> Response:
    """
    Deletes product_loading by ID.
    :return: Response object
    """
    product_loading_controller.delete(product_loading_id)
    return make_response("product_loading deleted", HTTPStatus.OK)
