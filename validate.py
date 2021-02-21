from opbk_br_quickstart.client_factory import create_client, ApiFamily, AdminApiFamily,CommonApiFamily, ChannelsApiFamily, ProductsServicesApiFamily
from participant_endpoints import get_endpoints


separator = '----------------------------------------------'
header = '===================================================='


def list_api_methods(client):

    def filter_in(text):
        filter_out_words = ['__', 'api_client', 'with_http_info']
        for word in filter_out_words:
            if word in text:
                return False
        return True

    methods = []
    for attr in dir(client):
        if filter_in(attr):
            method = getattr(client, attr)
            methods.append(method)

    return methods


def validate_participant(participant, host):

    print(header)
    print(participant)
    print(header)

    validate_client(create_client(
        host,
        ApiFamily.ADMIN,
        AdminApiFamily.METRICS))
    
    validate_client(create_client(
        host,
        ApiFamily.COMMON,
        CommonApiFamily.DISCOVERY))
    
    validate_client(create_client(
        host,
        ApiFamily.CHANNELS,
        ChannelsApiFamily.CHANNELS))

    for product_service_api_family in ProductsServicesApiFamily:
        validate_client(create_client(
            host,
            ApiFamily.PRODUCTS_SERVICES,
            product_service_api_family))


def validate_client(client):
    for method in list_api_methods(client):
        print(method.__name__)
        try:
            method()
            print('ok')
        except Exception as e:
            print(e)
        print(separator)

for participant, endpoint in get_endpoints().items():
    validate_participant(participant, endpoint)
