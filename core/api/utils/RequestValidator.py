from core.api import API
import validators


class RequestValidator(object):
    REQUIRED = True
    OPTIONAL = False


class PaymentDataValidator(RequestValidator):
    __toplevel__ = {
        'id': str,
        'name': str,
        'image': str,
        'description': str,
        'branding': bool,
        'rating': float,
        'setup_fee': bool,
        'transaction_fees': str,
        'how_to_url': str,
        'currencies': str
    }

    @staticmethod
    def check_elements(data: dict) -> bool:
        for key in data:
            if key not in PaymentDataValidator.__toplevel__:
                return False

        for key, value in PaymentDataValidator.__toplevel__.items():
            if value is RequestValidator.REQUIRED and key not in data:
                return False

        return True

    @staticmethod
    def validator(data: dict) -> bool:
        if type(data['id']) is not PaymentDataValidator.__toplevel__['id']:
            return False

        if type(data['name']) is not PaymentDataValidator.__toplevel__['name']:
            return False

        if type(data['image']) is not PaymentDataValidator.__toplevel__['image']:
            return False

        if type(data['description']) is not PaymentDataValidator.__toplevel__['description']:
            return False

        if type(data['branding']) is not PaymentDataValidator.__toplevel__['branding']:
            try:
                branding = int(data['branding'])
            except ValueError:
                return False
            else:
                if branding == 0:
                    data['branding'] = False
                elif branding == 1:
                    data['branding'] = True
                else:
                    return False

        if type(data['rating']) is not PaymentDataValidator.__toplevel__['rating']:
            try:
                rating = float(data['rating'])
            except ValueError:
                return False
            else:
                data['rating'] = rating

        if type(data['setup_fee']) is not PaymentDataValidator.__toplevel__['setup_fee']:
            try:
                setup_fee = int(data['setup_fee'])
            except ValueError:
                return False
            else:
                if setup_fee == 0:
                    data['setup_fee'] = False
                elif setup_fee == 1:
                    data['setup_fee'] = True
                else:
                    return False

        if type(data['transaction_fees']) is not PaymentDataValidator.__toplevel__['transaction_fees']:
            return False

        if type(data['how_to_url']) is not PaymentDataValidator.__toplevel__['how_to_url']:
            return False
        else:
            if not validators.url(data['how_to_url']):
                return False

        if type(data['currencies']) is PaymentDataValidator.__toplevel__['currencies']:
            data['currencies'] = [each.strip() for each in data['currencies'].split(',')]
        else:
            return False

        if API.mongo_client.db.payments.find().count() == 0:
            API.mongo_client.db.payments.create_index(
                [
                    ('name', 'text')
                ]
            )

        API.mongo_client.db.payments.insert_one(
            data
        )

        return True
