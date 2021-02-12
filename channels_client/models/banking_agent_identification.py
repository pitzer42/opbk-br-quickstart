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
from channels_client.models.cnpj import CNPJ  # noqa: F401,E501

class BankingAgentIdentification(CNPJ):
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
        'corporation_name': 'str',
        'group_name': 'str',
        'is_underestablishment': 'bool'
    }
    if hasattr(CNPJ, "swagger_types"):
        swagger_types.update(CNPJ.swagger_types)

    attribute_map = {
        'corporation_name': 'corporationName',
        'group_name': 'groupName',
        'is_underestablishment': 'isUnderestablishment'
    }
    if hasattr(CNPJ, "attribute_map"):
        attribute_map.update(CNPJ.attribute_map)

    def __init__(self, corporation_name=None, group_name=None, is_underestablishment=None, *args, **kwargs):  # noqa: E501
        """BankingAgentIdentification - a model defined in Swagger"""  # noqa: E501
        self._corporation_name = None
        self._group_name = None
        self._is_underestablishment = None
        self.discriminator = None
        self.corporation_name = corporation_name
        if group_name is not None:
            self.group_name = group_name
        if is_underestablishment is not None:
            self.is_underestablishment = is_underestablishment
        CNPJ.__init__(self, *args, **kwargs)

    @property
    def corporation_name(self):
        """Gets the corporation_name of this BankingAgentIdentification.  # noqa: E501


        :return: The corporation_name of this BankingAgentIdentification.  # noqa: E501
        :rtype: str
        """
        return self._corporation_name

    @corporation_name.setter
    def corporation_name(self, corporation_name):
        """Sets the corporation_name of this BankingAgentIdentification.


        :param corporation_name: The corporation_name of this BankingAgentIdentification.  # noqa: E501
        :type: str
        """
        if corporation_name is None:
            raise ValueError("Invalid value for `corporation_name`, must not be `None`")  # noqa: E501

        self._corporation_name = corporation_name

    @property
    def group_name(self):
        """Gets the group_name of this BankingAgentIdentification.  # noqa: E501


        :return: The group_name of this BankingAgentIdentification.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this BankingAgentIdentification.


        :param group_name: The group_name of this BankingAgentIdentification.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def is_underestablishment(self):
        """Gets the is_underestablishment of this BankingAgentIdentification.  # noqa: E501

        Indicador do Correspondente Bancário ser um Substabelecimento (são empresas  que foram contratadas por um correspondente bancário para prestar serviços. A empresa substabelecida é tratada como um correspondente do banco e tem praticamente os mesmos direitos e obrigações que possui o correspondente direto)  # noqa: E501

        :return: The is_underestablishment of this BankingAgentIdentification.  # noqa: E501
        :rtype: bool
        """
        return self._is_underestablishment

    @is_underestablishment.setter
    def is_underestablishment(self, is_underestablishment):
        """Sets the is_underestablishment of this BankingAgentIdentification.

        Indicador do Correspondente Bancário ser um Substabelecimento (são empresas  que foram contratadas por um correspondente bancário para prestar serviços. A empresa substabelecida é tratada como um correspondente do banco e tem praticamente os mesmos direitos e obrigações que possui o correspondente direto)  # noqa: E501

        :param is_underestablishment: The is_underestablishment of this BankingAgentIdentification.  # noqa: E501
        :type: bool
        """

        self._is_underestablishment = is_underestablishment

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
        if issubclass(BankingAgentIdentification, dict):
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
        if not isinstance(other, BankingAgentIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
