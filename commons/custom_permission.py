# /********************************************************************************
# * AUDETEMI INC. ("COMPANY") CONFIDENTIAL
# *_______________________________________
# *
# * Unpublished Copyright (c) 2015-2017 [AUDETEMI INC].
# * http://www.audetemi.com.
# * All Rights Reserved.
# *
# * NOTICE:  All information contained herein is, and remains the property of COMPANY. * The intellectual and #technical concepts contained herein are proprietary to COMPANY * and may be covered by U.S. and Foreign Patents, #patents in process, and are
# * protected by trade secret or copyright law.
# * Dissemination of this information or reproduction of this material is strictly
# * forbidden unless prior written permission is obtained from COMPANY.
# * Access to the source code contained herein is hereby forbidden to anyone except
# * current COMPANY employees, managers or contractors who have executed
# * Confidentiality and Non-disclosure agreements explicitly covering such access.
# *
# * The copyright notice above does not evidence any actual or intended publication or * disclosure of this source #code, which includes information that is confidential
# * and/or proprietary, and is a trade secret, of the COMPANY.
# *
# * ANY SUB-LICENSING, REPRODUCTION, REVERSE ENGINEERING, DECOMPILATION, MODIFICATION, * DISTRIBUTION, PUBLIC #PERFORMANCE, OR PUBLIC DISPLAY OF OR THROUGH USE OF THIS
# * SOURCE CODE WITHOUT THE EXPRESS WRITTEN CONSENT OF COMPANY IS STRICTLY PROHIBITED,
# * AND IN VIOLATION OF APPLICABLE LAWS AND INTERNATIONAL TREATIES.  THE RECEIPT OR
# * POSSESSION OF THIS SOURCE CODE AND/OR RELATED INFORMATION DOES NOT CONVEY OR IMPLY * ANY RIGHTS TO REPRODUCE, #DISCLOSE OR DISTRIBUTE ITS CONTENTS, OR TO MANUFACTURE,
# * USE, OR SELL ANYTHING THAT IT MAY DESCRIBE, IN WHOLE OR IN PART.
# */
import json
import logging
import urllib

from django.conf import settings
from django.http.multipartparser import parse_header
from django.utils import six
from rest_framework import renderers
from rest_framework.compat import SHORT_SEPARATORS, LONG_SEPARATORS, \
    INDENT_SEPARATORS
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser
from rest_framework.renderers import BaseRenderer, zero_as_none
from rest_framework.settings import api_settings
from rest_framework.utils import encoders

from commons.conf import URL_LIB_SAFE

logger = logging.getLogger('eguru')


def read_list_check(items):
    data = []
    for item in items:
        if isinstance(item, dict):
            check = read_dict_check(item)
            data.append(check)
        elif isinstance(item, list):
            check = read_list_check(item)
            data.append(check)
        elif item == '*':
            raise ParseError(
                'Invalid characters found, Please check input data.')
        else:
            data.append(urllib.quote(item, safe=URL_LIB_SAFE))
    return data


def read_dict_check(ele):
    data = {}
    for k1, v1 in ele.items():
        if isinstance(v1, dict):
            read_dict_check(v1)
            data.update({k1: data})
        elif isinstance(v1, list):
            read_list_check(v1)
            data.update({k1: data})
        elif v1 == "*":
            raise ParseError(
                'Invalid characters found, Please check input data.')
        else:
            data.update({k1: urllib.quote(v1, safe=URL_LIB_SAFE)})
    return data


def write_list_check(items):
    for item in items:
        if isinstance(item, dict):
            write_dict_check(item)
        elif isinstance(item, list):
            write_list_check(item)
        elif item == '*':
            raise ParseError(
                'Invalid characters found, Please check input data.')
    return


def write_dict_check(ele):
    for k1, v1 in ele.items():
        if isinstance(v1, dict):
            write_dict_check(v1)
        elif isinstance(v1, list):
            write_list_check(v1)
        elif v1 == "*":
            raise ParseError(
                'Invalid characters found, Please check input data.')
    return


class ReadJSONParser(BaseParser):
    """
    Parses JSON-serialized data.
    """

    media_type = 'application/json'
    renderer_class = renderers.JSONRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            json_data = json.loads(data)
            data = {}
            for k, v in json_data.items():
                if isinstance(v, dict):
                    check = read_dict_check(v)
                    data.update({k: check})
                elif isinstance(v, list):
                    check = read_list_check(v)
                    data.update({k: check})
                elif v == '*':
                    raise ParseError(
                        'Invalid characters found, Please check input data.')
                else:
                    if isinstance(v, str) or isinstance(v, unicode):
                        data.update({k: urllib.quote(v, safe=URL_LIB_SAFE)})
                    else:
                        data.update({k: v})
            logger.info(json.dumps(data))
            return data
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))
POSITION_UPDATED_SUCCESSFULLY = {
    "message": "Position Updated successfully.",
    "success_code": 13
}


class WriteJSONParser(BaseParser):
    """
    Parses JSON-serialized data.
    """

    media_type = 'application/json'
    renderer_class = renderers.JSONRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as JSON and returns the resulting data.
        """
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            json_data = json.loads(data)
            for k, v in json_data.items():
                if isinstance(v, dict):
                    write_dict_check(v)
                elif isinstance(v, list):
                    write_list_check(v)
                elif v == '*':
                    raise ParseError(
                        'Invalid characters found, Please check input data.')
            logger.info(json.dumps(json_data))
            return json_data
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % six.text_type(exc))


class CUSTOMJSONRenderer(BaseRenderer):
    """
    Renderer which serializes to JSON.
    """

    media_type = 'application/json'
    format = 'json'
    encoder_class = encoders.JSONEncoder
    ensure_ascii = not api_settings.UNICODE_JSON
    compact = api_settings.COMPACT_JSON

    # We don't set a charset because JSON is a binary encoding,
    # that can be encoded as utf-8, utf-16 or utf-32.
    # See: http://www.ietf.org/rfc/rfc4627.txt
    # Also: http://lucumr.pocoo.org/2013/7/19/application-mimetypes-and-encodings/
    charset = None

    def get_indent(self, accepted_media_type, renderer_context):
        if accepted_media_type:
            # If the media type looks like 'application/json; indent=4',
            # then pretty print the result.
            # Note that we coerce `indent=0` into `indent=None`.
            base_media_type, params = parse_header(
                accepted_media_type.encode('ascii'))
            try:
                return zero_as_none(max(min(int(params['indent']), 8), 0))
            except (KeyError, ValueError, TypeError):
                pass

        # If 'indent' is provided in the context, then pretty print the result.
        # E.g. If we're being called by the BrowsableAPIRenderer.
        return renderer_context.get('indent', None)

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into JSON, returning a bytestring.
        """
        if data is None:
            return bytes()

        renderer_context = renderer_context or {}
        indent = self.get_indent(accepted_media_type, renderer_context)

        if indent is None:
            separators = SHORT_SEPARATORS if self.compact else LONG_SEPARATORS
        else:
            separators = INDENT_SEPARATORS

        ret = json.dumps(
            data, cls=self.encoder_class,
            indent=indent, ensure_ascii=self.ensure_ascii,
            separators=separators
        )

        # On python 2.x json.dumps() returns bytestrings if ensure_ascii=True,
        # but if ensure_ascii=False, the return type is underspecified,
        # and may (or may not) be unicode.
        # On python 3.x json.dumps() returns unicode strings.
        if isinstance(ret, six.text_type):
            # We always fully escape \u2028 and \u2029 to ensure we output JSON
            # that is a strict javascript subset. If bytes were returned
            # by json.dumps() then we don't have these characters in any case.
            # See: http://timelessrepo.com/json-isnt-a-javascript-subset
            ret = ret.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
            return bytes(ret.encode('utf-8'))
        return ret
