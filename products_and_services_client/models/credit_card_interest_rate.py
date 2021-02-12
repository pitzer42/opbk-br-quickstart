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

class CreditCardInterestRate(object):
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
        'code': 'str',
        'additional_info': 'str'
    }

    attribute_map = {
        'code': 'code',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, code=None, additional_info=None):  # noqa: E501
        """CreditCardInterestRate - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._additional_info = None
        self.discriminator = None
        self.code = code
        self.additional_info = additional_info

    @property
    def code(self):
        """Gets the code of this CreditCardInterestRate.  # noqa: E501

        Lista de outras operações de crédito  # noqa: E501

        :return: The code of this CreditCardInterestRate.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreditCardInterestRate.

        Lista de outras operações de crédito  # noqa: E501

        :param code: The code of this CreditCardInterestRate.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = ["SAQUE_A_CREDITO", "PAGAMENTOS_CONTAS", "OUTROS"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def additional_info(self):
        """Gets the additional_info of this CreditCardInterestRate.  # noqa: E501

        Campo Texto para descrever outras operações de crédito marcadas como 'OUTROS'. Se o campo 'code' vier selecionado com 'OUTROS' é obrigatório o preenchimento do additionalInfo  # noqa: E501

        :return: The additional_info of this CreditCardInterestRate.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CreditCardInterestRate.

        Campo Texto para descrever outras operações de crédito marcadas como 'OUTROS'. Se o campo 'code' vier selecionado com 'OUTROS' é obrigatório o preenchimento do additionalInfo  # noqa: E501

        :param additional_info: The additional_info of this CreditCardInterestRate.  # noqa: E501
        :type: str
        """
        if additional_info is None:
            raise ValueError("Invalid value for `additional_info`, must not be `None`")  # noqa: E501

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
        if issubclass(CreditCardInterestRate, dict):
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
        if not isinstance(other, CreditCardInterestRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
