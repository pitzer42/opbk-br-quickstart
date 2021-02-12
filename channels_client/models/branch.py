# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.2
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Branch(object):
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
        'identification': 'BranchIdentification',
        'postal_addresses': 'BranchPostalAddress',
        'availability': 'BranchAvailability',
        'phones': 'list[BranchPhone]',
        'services': 'list[BranchService]'
    }

    attribute_map = {
        'identification': 'identification',
        'postal_addresses': 'postalAddresses',
        'availability': 'availability',
        'phones': 'phones',
        'services': 'services'
    }

    def __init__(self, identification=None, postal_addresses=None, availability=None, phones=None, services=None):  # noqa: E501
        """Branch - a model defined in Swagger"""  # noqa: E501
        self._identification = None
        self._postal_addresses = None
        self._availability = None
        self._phones = None
        self._services = None
        self.discriminator = None
        self.identification = identification
        if postal_addresses is not None:
            self.postal_addresses = postal_addresses
        self.availability = availability
        if phones is not None:
            self.phones = phones
        self.services = services

    @property
    def identification(self):
        """Gets the identification of this Branch.  # noqa: E501


        :return: The identification of this Branch.  # noqa: E501
        :rtype: BranchIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this Branch.


        :param identification: The identification of this Branch.  # noqa: E501
        :type: BranchIdentification
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

    @property
    def postal_addresses(self):
        """Gets the postal_addresses of this Branch.  # noqa: E501


        :return: The postal_addresses of this Branch.  # noqa: E501
        :rtype: BranchPostalAddress
        """
        return self._postal_addresses

    @postal_addresses.setter
    def postal_addresses(self, postal_addresses):
        """Sets the postal_addresses of this Branch.


        :param postal_addresses: The postal_addresses of this Branch.  # noqa: E501
        :type: BranchPostalAddress
        """

        self._postal_addresses = postal_addresses

    @property
    def availability(self):
        """Gets the availability of this Branch.  # noqa: E501


        :return: The availability of this Branch.  # noqa: E501
        :rtype: BranchAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this Branch.


        :param availability: The availability of this Branch.  # noqa: E501
        :type: BranchAvailability
        """
        if availability is None:
            raise ValueError("Invalid value for `availability`, must not be `None`")  # noqa: E501

        self._availability = availability

    @property
    def phones(self):
        """Gets the phones of this Branch.  # noqa: E501

        Lista de telefones da Dependência  # noqa: E501

        :return: The phones of this Branch.  # noqa: E501
        :rtype: list[BranchPhone]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this Branch.

        Lista de telefones da Dependência  # noqa: E501

        :param phones: The phones of this Branch.  # noqa: E501
        :type: list[BranchPhone]
        """

        self._phones = phones

    @property
    def services(self):
        """Gets the services of this Branch.  # noqa: E501

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :return: The services of this Branch.  # noqa: E501
        :rtype: list[BranchService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Branch.

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :param services: The services of this Branch.  # noqa: E501
        :type: list[BranchService]
        """
        self._services = services

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
        if issubclass(Branch, dict):
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
        if not isinstance(other, Branch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
