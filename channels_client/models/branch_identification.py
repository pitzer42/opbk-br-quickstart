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

class BranchIdentification(object):
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
        'type': 'str',
        'code': 'str',
        'check_digit': 'str',
        'name': 'str',
        'related_branch': 'str',
        'opening_date': 'str'
    }

    attribute_map = {
        'type': 'type',
        'code': 'code',
        'check_digit': 'checkDigit',
        'name': 'name',
        'related_branch': 'relatedBranch',
        'opening_date': 'openingDate'
    }

    def __init__(self, type=None, code=None, check_digit=None, name=None, related_branch=None, opening_date=None):  # noqa: E501
        """BranchIdentification - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._code = None
        self._check_digit = None
        self._name = None
        self._related_branch = None
        self._opening_date = None
        self.discriminator = None
        self.type = type
        self.code = code
        self.check_digit = check_digit
        self.name = name
        if related_branch is not None:
            self.related_branch = related_branch
        if opening_date is not None:
            self.opening_date = opening_date

    @property
    def type(self):
        """Gets the type of this BranchIdentification.  # noqa: E501

         > Tipo da dependência, segundo a regulamentação do Bacen,  na Resolução Nº 4072, de 26 de abril de 2012: Dependência de instituições financeiras e demais instituições, autorizadas a funcionar pelo Banco Central do Brasil, destinada à prática das atividades para as quais a instituição esteja regularmente habilitada.  * `AGENCIA`: Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória;  * `POSTO_ATENDIMENTO`: Posto de Atendimento é a dependência subordinada a agência  ou à sede da instituição financeira, destinada ao atendimento ao público no exercício de uma ou mais de suas atividades, podendo ser fixo ou móvel. Segundo Art.15. Os Postos de Atendimento Bancário (PAB), Postos Avançados de Atendimento (PAA), Postos de Atendimento Transitórios (PAT), Postos de Compra de Ouro (PCO), Postos de Atendimento Cooperativo (PAC), Postos de Atendimento de Microcrédito (PAM), Postos Bancários de Arrecadação e Pagamento (PAP) e os Postos de Câmbio atualmente em funcionamento serão considerados PA.  * `POSTO_ATENDIMENTO_ELETRONICO`: Posto de Atendimento Eletrônico é a dependência constituída por um ou mais terminais de autoatendimento, subordinada a agência ou à sede da instituição, destinada à prestação de serviços por meio eletrônico, podendo ser fixo ou móvel, permanente ou transitório  * `UNIDADE_ADMINISTRATIVA_DESMEMBRADA `: Unidade Administrativa Desmembrada (UAD) segundo a Resolução 4072 , BCB, 2012, no Art. 8º \"... é dependência destinada à execução de atividades administrativas da instituição, vedado o atendimento ao público\"  # noqa: E501

        :return: The type of this BranchIdentification.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BranchIdentification.

         > Tipo da dependência, segundo a regulamentação do Bacen,  na Resolução Nº 4072, de 26 de abril de 2012: Dependência de instituições financeiras e demais instituições, autorizadas a funcionar pelo Banco Central do Brasil, destinada à prática das atividades para as quais a instituição esteja regularmente habilitada.  * `AGENCIA`: Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória;  * `POSTO_ATENDIMENTO`: Posto de Atendimento é a dependência subordinada a agência  ou à sede da instituição financeira, destinada ao atendimento ao público no exercício de uma ou mais de suas atividades, podendo ser fixo ou móvel. Segundo Art.15. Os Postos de Atendimento Bancário (PAB), Postos Avançados de Atendimento (PAA), Postos de Atendimento Transitórios (PAT), Postos de Compra de Ouro (PCO), Postos de Atendimento Cooperativo (PAC), Postos de Atendimento de Microcrédito (PAM), Postos Bancários de Arrecadação e Pagamento (PAP) e os Postos de Câmbio atualmente em funcionamento serão considerados PA.  * `POSTO_ATENDIMENTO_ELETRONICO`: Posto de Atendimento Eletrônico é a dependência constituída por um ou mais terminais de autoatendimento, subordinada a agência ou à sede da instituição, destinada à prestação de serviços por meio eletrônico, podendo ser fixo ou móvel, permanente ou transitório  * `UNIDADE_ADMINISTRATIVA_DESMEMBRADA `: Unidade Administrativa Desmembrada (UAD) segundo a Resolução 4072 , BCB, 2012, no Art. 8º \"... é dependência destinada à execução de atividades administrativas da instituição, vedado o atendimento ao público\"  # noqa: E501

        :param type: The type of this BranchIdentification.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["AGENCIA", "POSTO_ATENDIMENTO", "POSTO_ATENDIMENTO_ELETRONICO", "UNIDADE_ADMINISTRATIVA_DESMEMBRADA"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def code(self):
        """Gets the code of this BranchIdentification.  # noqa: E501

        Código identificador da dependência  # noqa: E501

        :return: The code of this BranchIdentification.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BranchIdentification.

        Código identificador da dependência  # noqa: E501

        :param code: The code of this BranchIdentification.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def check_digit(self):
        """Gets the check_digit of this BranchIdentification.  # noqa: E501

        Dígito verificador do código da dependência  # noqa: E501

        :return: The check_digit of this BranchIdentification.  # noqa: E501
        :rtype: str
        """
        return self._check_digit

    @check_digit.setter
    def check_digit(self, check_digit):
        """Sets the check_digit of this BranchIdentification.

        Dígito verificador do código da dependência  # noqa: E501

        :param check_digit: The check_digit of this BranchIdentification.  # noqa: E501
        :type: str
        """
        if check_digit is None:
            raise ValueError("Invalid value for `check_digit`, must not be `None`")  # noqa: E501

        self._check_digit = check_digit

    @property
    def name(self):
        """Gets the name of this BranchIdentification.  # noqa: E501

        Nome da dependência  # noqa: E501

        :return: The name of this BranchIdentification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BranchIdentification.

        Nome da dependência  # noqa: E501

        :param name: The name of this BranchIdentification.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def related_branch(self):
        """Gets the related_branch of this BranchIdentification.  # noqa: E501

        Código da agência vinculada ao Posto de Atendimento - se aplicável  # noqa: E501

        :return: The related_branch of this BranchIdentification.  # noqa: E501
        :rtype: str
        """
        return self._related_branch

    @related_branch.setter
    def related_branch(self, related_branch):
        """Sets the related_branch of this BranchIdentification.

        Código da agência vinculada ao Posto de Atendimento - se aplicável  # noqa: E501

        :param related_branch: The related_branch of this BranchIdentification.  # noqa: E501
        :type: str
        """

        self._related_branch = related_branch

    @property
    def opening_date(self):
        """Gets the opening_date of this BranchIdentification.  # noqa: E501

        Data de abertura da dependência (uma string com data conforme especificação RFC-3339. p.ex. 2014-03-19)  # noqa: E501

        :return: The opening_date of this BranchIdentification.  # noqa: E501
        :rtype: str
        """
        return self._opening_date

    @opening_date.setter
    def opening_date(self, opening_date):
        """Sets the opening_date of this BranchIdentification.

        Data de abertura da dependência (uma string com data conforme especificação RFC-3339. p.ex. 2014-03-19)  # noqa: E501

        :param opening_date: The opening_date of this BranchIdentification.  # noqa: E501
        :type: str
        """

        self._opening_date = opening_date

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
        if issubclass(BranchIdentification, dict):
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
        if not isinstance(other, BranchIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
