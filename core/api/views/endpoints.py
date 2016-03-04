from flask import Module, jsonify, request
from flask.views import MethodView

from core.api.utils.RequestValidator import PaymentDataValidator

from core.api.decorators import jsonp

from core.api import API

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
        message='Room no 404: File not found'
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

        payments = list(
            API.mongo_client.db.payments.find()
        )

        return jsonify(
            code=200,
            count=len(payments),
            data=payments
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
