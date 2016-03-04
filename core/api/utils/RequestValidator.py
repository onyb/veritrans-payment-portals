class RequestValidator(object):
    REQUIRED = True
    OPTIONAL = False


class PaymentDataValidator(RequestValidator):
    __toplevel__ = {
        'name': str,
        'image': str,
        'description': str,
        'branding': bool,
        'rating': float,
        'setup_fee': bool,
        'transaction_fee': str,
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
                rating = float(data['setup_fee'])
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

        if type(data['transaction_fee']) is not PaymentDataValidator.__toplevel__['transaction_fee']:
            return False

        if type(data['how_to_url']) is not PaymentDataValidator.__toplevel__['how_to_url']:
            return False

        if type(data['currencies']) is not PaymentDataValidator.__toplevel__['currencies']:
            return False

        return True