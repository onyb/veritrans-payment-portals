from flask import Module, jsonify, request
from flask.views import MethodView

from core.api import API
from core.api.decorators import jsonp
from core.api.utils.RequestValidator import PaymentDataValidator

api = Module(
    __name__,
    url_prefix='/api'
)


def jsonify_status_code(*args, **kw):
    response = jsonify(*args, **kw)
    response.status_code = kw['code']
    return response


@api.route('/')
def index():
    """
    The root of the API returns an error
    """
    return jsonify_status_code(
        code=400,
        message='Room no 404: File not found. HTTP GET requests to API root are not allowed.'
    )


class Payments(MethodView):
    @jsonp
    def get(self):
        return jsonify_status_code(
            code=405,
            message='HTTP method GET is not allowed for this URL'
        )

    @jsonp
    def post(self):
        content = request.get_json(force=False, silent=True)
        if not content:
            return jsonify_status_code(
                code=400,
                message='Bad HTTP POST request'
            )
        else:
            if PaymentDataValidator.check_elements(content) and PaymentDataValidator.validator(content):
                return jsonify_status_code(
                    code=200,
                    message='HTTP POST request successful'
                )
            else:
                return jsonify_status_code(
                    code=400,
                    message='Bad HTTP POST request'
                )


class PaymentsList(MethodView):
    @jsonp
    def get(self):
        try:
            page = int(request.args.get('page', 1))
        except ValueError:
            page = 1

        if page < 1:
            page = 1

        try:
            limit = int(request.args.get('limit', 3))
        except ValueError:
            limit = 3

        cursor = API.mongo_client.db.payments.find(
            {}, {'_id': 0}
        ).sort(
            'rating', -1
        )

        count = cursor.count()

        data = list(
            cursor.skip(
                (page - 1) * limit
            ).limit(
                limit
            )
        )

        return jsonify(
            code=200,
            count=count,
            page=page,
            limit=limit,
            data=data
        )

    @jsonp
    def post(self):
        return jsonify_status_code(
            code=405,
            message='HTTP method POST is not allowed for this URL'
        )


class PaymentsCount(MethodView):
    @jsonp
    def get(self):
        count = API.mongo_client.db.payments.find().count()

        return jsonify(
            code=200,
            count=count
        )

    @jsonp
    def post(self):
        return jsonify_status_code(
            code=405,
            message='HTTP method POST is not allowed for this URL'
        )


class PaymentsSearch(MethodView):
    @jsonp
    def get(self):
        try:
            page = int(request.args.get('page', 1))
        except ValueError:
            page = 1

        if page < 1:
            page = 1

        try:
            limit = int(request.args.get('limit', 3))
        except ValueError:
            limit = 3

        name = request.args.get('name', None)

        if name:
            name_cursor = API.mongo_client.db.payments.find(
                {
                    '$text':
                        {
                            '$search': name
                        }
                },
                {
                    '_id': 0,
                    'search_score':
                        {
                            '$meta': 'textScore'
                        }
                }
            ).sort(
                [
                    (
                        'search_score', {'$meta': 'textScore'}
                    ),
                    (
                        'rating', -1
                    )
                ]
            )

            data = list(
                name_cursor.skip(
                    (page - 1) * limit
                ).limit(
                    limit
                )
            )

            count = name_cursor.count()
        else:
            count = 0
            data = []

        return jsonify(
            code=200,
            data=data,
            count=count,
            page=page,
            limit=limit
        )

    @jsonp
    def post(self):
        return jsonify_status_code(
            code=405,
            message='HTTP method POST is not allowed for this URL'
        )


Payments_view = Payments.as_view('payments')
api.add_url_rule(
    '/payments',
    view_func=Payments_view,
    methods=['GET', 'POST']
)

PaymentsList_view = PaymentsList.as_view('payments_list')
api.add_url_rule(
    '/payments/list',
    view_func=PaymentsList_view,
    methods=['GET', 'POST']
)

PaymentsCount_view = PaymentsCount.as_view('payments_count')
api.add_url_rule(
    '/payments/count',
    view_func=PaymentsCount_view,
    methods=['GET', 'POST']
)

PaymentsSearch_view = PaymentsSearch.as_view('payments_search')
api.add_url_rule(
    '/payments/search',
    view_func=PaymentsSearch_view,
    methods=['GET', 'POST']
)
