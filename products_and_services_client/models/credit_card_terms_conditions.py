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

class CreditCardTermsConditions(object):
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
        'minimum_fee_rate': 'str',
        'additional_info': 'str',
        'elegibility_criteria_info': 'str',
        'closing_process_info': 'str'
    }

    attribute_map = {
        'minimum_fee_rate': 'minimumFeeRate',
        'additional_info': 'additionalInfo',
        'elegibility_criteria_info': 'elegibilityCriteriaInfo',
        'closing_process_info': 'closingProcessInfo'
    }

    def __init__(self, minimum_fee_rate=None, additional_info=None, elegibility_criteria_info=None, closing_process_info=None):  # noqa: E501
        """CreditCardTermsConditions - a model defined in Swagger"""  # noqa: E501
        self._minimum_fee_rate = None
        self._additional_info = None
        self._elegibility_criteria_info = None
        self._closing_process_info = None
        self.discriminator = None
        self.minimum_fee_rate = minimum_fee_rate
        if additional_info is not None:
            self.additional_info = additional_info
        self.elegibility_criteria_info = elegibility_criteria_info
        self.closing_process_info = closing_process_info

    @property
    def minimum_fee_rate(self):
        """Gets the minimum_fee_rate of this CreditCardTermsConditions.  # noqa: E501

        Percentual para pagamento mínimo sobre o saldo devedor da fatura.  # noqa: E501

        :return: The minimum_fee_rate of this CreditCardTermsConditions.  # noqa: E501
        :rtype: str
        """
        return self._minimum_fee_rate

    @minimum_fee_rate.setter
    def minimum_fee_rate(self, minimum_fee_rate):
        """Sets the minimum_fee_rate of this CreditCardTermsConditions.

        Percentual para pagamento mínimo sobre o saldo devedor da fatura.  # noqa: E501

        :param minimum_fee_rate: The minimum_fee_rate of this CreditCardTermsConditions.  # noqa: E501
        :type: str
        """
        if minimum_fee_rate is None:
            raise ValueError("Invalid value for `minimum_fee_rate`, must not be `None`")  # noqa: E501

        self._minimum_fee_rate = minimum_fee_rate

    @property
    def additional_info(self):
        """Gets the additional_info of this CreditCardTermsConditions.  # noqa: E501

        Campo aberto para detalhamento de taxas de juros  # noqa: E501

        :return: The additional_info of this CreditCardTermsConditions.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CreditCardTermsConditions.

        Campo aberto para detalhamento de taxas de juros  # noqa: E501

        :param additional_info: The additional_info of this CreditCardTermsConditions.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def elegibility_criteria_info(self):
        """Gets the elegibility_criteria_info of this CreditCardTermsConditions.  # noqa: E501

        Informação sobre as condições e critérios de elegibilidade do emissor do cartão. Pode ser informada a URL referente ao endereço onde constam as condições informadas.  # noqa: E501

        :return: The elegibility_criteria_info of this CreditCardTermsConditions.  # noqa: E501
        :rtype: str
        """
        return self._elegibility_criteria_info

    @elegibility_criteria_info.setter
    def elegibility_criteria_info(self, elegibility_criteria_info):
        """Sets the elegibility_criteria_info of this CreditCardTermsConditions.

        Informação sobre as condições e critérios de elegibilidade do emissor do cartão. Pode ser informada a URL referente ao endereço onde constam as condições informadas.  # noqa: E501

        :param elegibility_criteria_info: The elegibility_criteria_info of this CreditCardTermsConditions.  # noqa: E501
        :type: str
        """
        if elegibility_criteria_info is None:
            raise ValueError("Invalid value for `elegibility_criteria_info`, must not be `None`")  # noqa: E501

        self._elegibility_criteria_info = elegibility_criteria_info

    @property
    def closing_process_info(self):
        """Gets the closing_process_info of this CreditCardTermsConditions.  # noqa: E501

        Descrição dos procedimentos para encerramento da conta de pagamento pós paga. Pode ser informada a URL referente ao endereço onde constam as condições informadas.  # noqa: E501

        :return: The closing_process_info of this CreditCardTermsConditions.  # noqa: E501
        :rtype: str
        """
        return self._closing_process_info

    @closing_process_info.setter
    def closing_process_info(self, closing_process_info):
        """Sets the closing_process_info of this CreditCardTermsConditions.

        Descrição dos procedimentos para encerramento da conta de pagamento pós paga. Pode ser informada a URL referente ao endereço onde constam as condições informadas.  # noqa: E501

        :param closing_process_info: The closing_process_info of this CreditCardTermsConditions.  # noqa: E501
        :type: str
        """
        if closing_process_info is None:
            raise ValueError("Invalid value for `closing_process_info`, must not be `None`")  # noqa: E501

        self._closing_process_info = closing_process_info

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
        if issubclass(CreditCardTermsConditions, dict):
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
        if not isinstance(other, CreditCardTermsConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
