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

class BankingAgent(object):
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
        'identification': 'BankingAgentIdentification',
        'locations': 'list[BankingAgentLocation]',
        'services': 'list[BankingAgentService]'
    }

    attribute_map = {
        'identification': 'identification',
        'locations': 'locations',
        'services': 'services'
    }

    def __init__(self, identification=None, locations=None, services=None):  # noqa: E501
        """BankingAgent - a model defined in Swagger"""  # noqa: E501
        self._identification = None
        self._locations = None
        self._services = None
        self.discriminator = None
        self.identification = identification
        self.locations = locations
        self.services = services

    @property
    def identification(self):
        """Gets the identification of this BankingAgent.  # noqa: E501


        :return: The identification of this BankingAgent.  # noqa: E501
        :rtype: BankingAgentIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this BankingAgent.


        :param identification: The identification of this BankingAgent.  # noqa: E501
        :type: BankingAgentIdentification
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

    @property
    def locations(self):
        """Gets the locations of this BankingAgent.  # noqa: E501

        Relação de informações referentes as localizações dos Correspondentes bancários.  # noqa: E501

        :return: The locations of this BankingAgent.  # noqa: E501
        :rtype: list[BankingAgentLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this BankingAgent.

        Relação de informações referentes as localizações dos Correspondentes bancários.  # noqa: E501

        :param locations: The locations of this BankingAgent.  # noqa: E501
        :type: list[BankingAgentLocation]
        """
        if locations is None:
            raise ValueError("Invalid value for `locations`, must not be `None`")  # noqa: E501

        self._locations = locations

    @property
    def services(self):
        """Gets the services of this BankingAgent.  # noqa: E501

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :return: The services of this BankingAgent.  # noqa: E501
        :rtype: list[BankingAgentService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this BankingAgent.

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :param services: The services of this BankingAgent.  # noqa: E501
        :type: list[BankingAgentService]
        """
        if services is None:
            raise ValueError("Invalid value for `services`, must not be `None`")  # noqa: E501

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
        if issubclass(BankingAgent, dict):
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
        if not isinstance(other, BankingAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
