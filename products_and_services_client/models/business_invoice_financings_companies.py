# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.2
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from products_and_services_client.models.company import Company  # noqa: F401,E501

class BusinessInvoiceFinancingsCompanies(Company):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'business_invoice_financings': 'list[BusinessInvoiceFinancings]'
    }
    if hasattr(Company, "swagger_types"):
        swagger_types.update(Company.swagger_types)

    attribute_map = {
        'business_invoice_financings': 'businessInvoiceFinancings'
    }
    if hasattr(Company, "attribute_map"):
        attribute_map.update(Company.attribute_map)

    def __init__(self, business_invoice_financings=None, *args, **kwargs):  # noqa: E501
        """BusinessInvoiceFinancingsCompanies - a model defined in Swagger"""  # noqa: E501
        self._business_invoice_financings = None
        self.discriminator = None
        self.business_invoice_financings = business_invoice_financings
        Company.__init__(self, *args, **kwargs)

    @property
    def business_invoice_financings(self):
        """Gets the business_invoice_financings of this BusinessInvoiceFinancingsCompanies.  # noqa: E501

        Lista de Modalidades de Direitos Creditórios Descontados  # noqa: E501

        :return: The business_invoice_financings of this BusinessInvoiceFinancingsCompanies.  # noqa: E501
        :rtype: list[BusinessInvoiceFinancings]
        """
        return self._business_invoice_financings

    @business_invoice_financings.setter
    def business_invoice_financings(self, business_invoice_financings):
        """Sets the business_invoice_financings of this BusinessInvoiceFinancingsCompanies.

        Lista de Modalidades de Direitos Creditórios Descontados  # noqa: E501

        :param business_invoice_financings: The business_invoice_financings of this BusinessInvoiceFinancingsCompanies.  # noqa: E501
        :type: list[BusinessInvoiceFinancings]
        """
        if business_invoice_financings is None:
            raise ValueError("Invalid value for `business_invoice_financings`, must not be `None`")  # noqa: E501

        self._business_invoice_financings = business_invoice_financings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BusinessInvoiceFinancingsCompanies, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BusinessInvoiceFinancingsCompanies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
