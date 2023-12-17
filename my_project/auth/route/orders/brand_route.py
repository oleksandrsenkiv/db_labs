
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import brand_controller
from my_project.auth.domain import Brand

brand_bp = Blueprint('brand', __name__, url_prefix='/brand')


@brand_bp.get('/all')
def get_all_brand() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(brand_controller.find_all()), HTTPStatus.OK)


@brand_bp.post('')
def create_brand() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.create(brand)
    return make_response(jsonify(brand.put_into_dto()), HTTPStatus.CREATED)


@brand_bp.post('/<int:brand_id>/add_snack')
def add_snack_to_brand(brand_id) -> Response:
    try:
        data = request.get_json()
        snacks_id = data.get('snacks_id')
        brand_controller.add_snacks_to_brand(brand_id, snacks_id)
        return make_response(jsonify({"message": "Snack added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@brand_bp.post('/add_brand')
def add_brand() -> Response:
    try:
        data = request.get_json()
        brand_name = data.get('brand_name')
        brand_controller.add_brand(brand_name)
        return make_response(jsonify({"message": "Brand added successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@brand_bp.get('/<int:brand_id>')
def get_brand(brand_id: int) -> Response:
    """
    Gets brand by ID.
    :return: Response object
    """
    return make_response(jsonify(brand_controller.find_by_id(brand_id)), HTTPStatus.OK)


@brand_bp.get('/<int:brand_id>/snacks_has_brands')
def get_all_brands_from_snacks(brand_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(brand_controller.brand_find_snacks(brand_id)), HTTPStatus.OK)


@brand_bp.put('/<int:brand_id>')
def update_brand(brand_id: int) -> Response:
    """
    Updates brand by ID.
    :return: Response object
    """
    content = request.get_json()
    brand = Brand.create_from_dto(content)
    brand_controller.update(brand_id, brand)
    return make_response("Brand updated", HTTPStatus.OK)


@brand_bp.patch('/<int:brand_id>')
def patch_brand(brand_id: int) -> Response:
    """
    Patches brand by ID.
    :return: Response object
    """
    content = request.get_json()
    brand_controller.patch(brand_id, content)
    return make_response("Brand updated", HTTPStatus.OK)


@brand_bp.patch('/<int:brand_id>/remove_snack')
def remove_snack_from_brand(brand_id) -> Response:
    try:
        data = request.get_json()
        snacks_id = data.get('snacks_id')
        brand_controller.remove_snack_from_brand(brand_id, snacks_id)
        return make_response(jsonify({"message": "Snack removed successfully"}), HTTPStatus.OK)

    except Exception as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)


@brand_bp.delete('/<int:brand_id>')
def delete_brand(brand_id: int) -> Response:
    """
    Deletes brand by ID.
    :return: Response object
    """
    brand_controller.delete(brand_id)
    return make_response("Brand deleted", HTTPStatus.OK)
