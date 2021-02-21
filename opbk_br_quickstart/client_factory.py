from enum import Enum
import yaml

from admin_client.configuration import Configuration as AdminConfiguration
from admin_client.api_client import ApiClient as AdminApiClient
from admin_client.api import MetricsApi

from common_client.configuration import Configuration as CommonConfiguration
from common_client.api_client import ApiClient as CommonApiClient
from common_client.api import DiscoveryApi

from channels_client.configuration import Configuration as ChannelsConfiguration
from channels_client.api_client import ApiClient as ChannelsApiClient
from channels_client.api import ChannelsApi

from products_and_services_client.configuration import Configuration as ProductsAndServicesConfiguration
from products_and_services_client.api_client import ApiClient as ProductsAndServicesApiClient
from products_and_services_client.api import AccountsApi
from products_and_services_client.api import CreditCardsApi
from products_and_services_client.api import FinancingsApi
from products_and_services_client.api import InvoiceFinancingsApi
from products_and_services_client.api import LoansApi
from products_and_services_client.api import UnarrangedAccountOverdraftApi


CONFIG_FILE = 'opbk_config.yml'
VERSION_KEY = 'version'
FAMILY_KEY = 'api_family'


class ApiFamily(Enum):
    COMMON = 'common'
    ADMIN = 'admin'
    CHANNELS = 'channels'
    PRODUCTS_SERVICES = 'products_services'


class CommonApiFamily(Enum):
    DISCOVERY = 'discovery'


class AdminApiFamily(Enum):
    METRICS = 'metrics'


class ChannelsApiFamily(Enum):
    CHANNELS = 'channels'


class ProductsServicesApiFamily(Enum):
    ACCOUNTS = 'accounts'
    CREDIT_CARD = 'credit_card'
    FINANCINGS = 'financings'
    INVOICE_FINANCINGS = 'invoice_financings'
    LOANS = 'loans'
    UNARRANGED_ACCOUNT_OVERDRAFTT = 'unarranged_account_overdraft'


CLIENT_MAP = {
    AdminApiFamily.METRICS: (AdminConfiguration, AdminApiClient, MetricsApi),
    CommonApiFamily.DISCOVERY: (CommonConfiguration, CommonApiClient, DiscoveryApi),
    ChannelsApiFamily.CHANNELS: (ChannelsConfiguration, ChannelsApiClient, ChannelsApi),
    ProductsServicesApiFamily.ACCOUNTS: (ProductsAndServicesConfiguration, ProductsAndServicesApiClient, AccountsApi),
    ProductsServicesApiFamily.CREDIT_CARD: (ProductsAndServicesConfiguration, ProductsAndServicesApiClient, AccountsApi),
    ProductsServicesApiFamily.FINANCINGS: (ProductsAndServicesConfiguration, ProductsAndServicesApiClient, FinancingsApi),
    ProductsServicesApiFamily.INVOICE_FINANCINGS: (ProductsAndServicesConfiguration, ProductsAndServicesApiClient, InvoiceFinancingsApi),
    ProductsServicesApiFamily.LOANS: (ProductsAndServicesConfiguration, ProductsAndServicesApiClient, LoansApi),
    ProductsServicesApiFamily.UNARRANGED_ACCOUNT_OVERDRAFTT: (ProductsAndServicesConfiguration, ProductsAndServicesApiClient, UnarrangedAccountOverdraftApi),
}


def create_client(host, api_family, api_type):
    host = _get_host(host, api_family)
    return _create_api(host, *CLIENT_MAP[api_type])



def _get_host(host, api_family):
    with open(CONFIG_FILE) as config_file:
        content = config_file.read()
        config = yaml.load(content)
        version = config[VERSION_KEY]
        family = config[FAMILY_KEY][api_family.value]
        return host + family + version


def _create_api(host, config_class, client_class, api_class):
    config = config_class()
    config.host = host
    client = client_class(config)
    return api_class(client)
