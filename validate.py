from opbk_br_quickstart.client_factory import create_client, Participants, ApiFamily, AdminApiFamily,CommonApiFamily, ChannelsApiFamily, ProductsServicesApiFamily


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


def validate_participant(participant):

    print(header)
    print(participant.value.upper())
    print(header)

    validate_client(create_client(
        ApiFamily.ADMIN,
        AdminApiFamily.METRICS,
        participant))
    
    validate_client(create_client(
        ApiFamily.COMMON,
        CommonApiFamily.DISCOVERY,
        participant))
    
    validate_client(create_client(
        ApiFamily.CHANNELS,
        ChannelsApiFamily.CHANNELS,
        participant))

    for product_service_api_family in ProductsServicesApiFamily:
        validate_client(create_client(
            ApiFamily.PRODUCTS_SERVICES,
            product_service_api_family,
            participant))


def validate_client(client):
    for method in list_api_methods(client):
        print(method.__name__)
        try:
            method()
            print('ok')
        except Exception as e:
            print(e)
        print(separator)

for participant in Participants:
    validate_participant(participant)
