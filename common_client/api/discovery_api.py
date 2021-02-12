# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.2
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from common_client.api_client import ApiClient


class DiscoveryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_outage(self, **kwargs):  # noqa: E501
        """a descrição referente ao código de status retornado pelas APIs  # noqa: E501

        a descrição referente ao código de status retornado pelas APIs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_outage(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseDiscoveryOutageList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_outage_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_outage_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_outage_with_http_info(self, **kwargs):  # noqa: E501
        """a descrição referente ao código de status retornado pelas APIs  # noqa: E501

        a descrição referente ao código de status retornado pelas APIs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_outage_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseDiscoveryOutageList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_outage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/outages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDiscoveryOutageList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_status(self, **kwargs):  # noqa: E501
        """a descrição referente ao código de status retornado pelas APIs  # noqa: E501

         descrição referente ao código de status retornado pelas APIs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseDiscoveryStatusList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_status_with_http_info(self, **kwargs):  # noqa: E501
        """a descrição referente ao código de status retornado pelas APIs  # noqa: E501

         descrição referente ao código de status retornado pelas APIs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseDiscoveryStatusList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseDiscoveryStatusList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
