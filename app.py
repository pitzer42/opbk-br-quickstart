from opbk_br_quickstart.client_factory import create_client, Participants, CommonApiFamily, AdminApiFamily, ChannelsApiFamily, ProductsServicesApiFamily, ApiFamily


def find_product_checking_account(company):
    for personal_account in company.personal_accounts:
        if personal_account.type == 'CONTA_DEPOSITO_A_VISTA':
            return personal_account


def find_internet_ted_service_fee(account):
    fees = account.fees.priority_services
    for fee in fees:
        if 'TED_INTERNET' in fee.code:
            return fee


def get_price_distribution(fee):
    distribution = []
    for price_range in fee.prices:
        pair = price_range.customers.rate, price_range.value
        distribution.append(pair)
    return distribution


for participant in Participants:
    client = create_client(
        ApiFamily.PRODUCTS_SERVICES,
        ProductsServicesApiFamily.ACCOUNTS,
        participant)

    response = client.get_personal_accounts()

    print(participant.value)

    for company in response.data.brand.companies:
        checking_account = find_product_checking_account(company)
        if checking_account:
            ted_service_fee = find_internet_ted_service_fee(checking_account)
            price_distribution = get_price_distribution(ted_service_fee)
            print(price_distribution)
