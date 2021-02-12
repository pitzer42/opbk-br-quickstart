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

class ElectronicChannelService(object):
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
        'name': 'str',
        'code': 'str',
        'additional_info': 'str'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, name=None, code=None, additional_info=None):  # noqa: E501
        """ElectronicChannelService - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._code = None
        self._additional_info = None
        self.discriminator = None
        self.name = name
        self.code = code
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def name(self):
        """Gets the name of this ElectronicChannelService.  # noqa: E501

        Nome dos Serviços efetivamente prestados pelo Canal de Atendimento  # noqa: E501

        :return: The name of this ElectronicChannelService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ElectronicChannelService.

        Nome dos Serviços efetivamente prestados pelo Canal de Atendimento  # noqa: E501

        :param name: The name of this ElectronicChannelService.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def code(self):
        """Gets the code of this ElectronicChannelService.  # noqa: E501

        Código dos Serviços efetivamente prestados pelo Canal de Atendimento  # noqa: E501

        :return: The code of this ElectronicChannelService.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ElectronicChannelService.

        Código dos Serviços efetivamente prestados pelo Canal de Atendimento  # noqa: E501

        :param code: The code of this ElectronicChannelService.  # noqa: E501
        :type: str
        """
        self._code = code

    @property
    def additional_info(self):
        """Gets the additional_info of this ElectronicChannelService.  # noqa: E501

        Texto livre para complementar informação relativa ao Serviço disponível, quando for selecionada a opção 'OUTROS_PRODUTOS_SERVICOS'  # noqa: E501

        :return: The additional_info of this ElectronicChannelService.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this ElectronicChannelService.

        Texto livre para complementar informação relativa ao Serviço disponível, quando for selecionada a opção 'OUTROS_PRODUTOS_SERVICOS'  # noqa: E501

        :param additional_info: The additional_info of this ElectronicChannelService.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

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
        if issubclass(ElectronicChannelService, dict):
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
        if not isinstance(other, ElectronicChannelService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
