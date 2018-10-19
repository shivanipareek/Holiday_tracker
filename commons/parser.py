
from django.utils import six
from django.utils.xmlutils import SimplerXMLGenerator
import StringIO
from django.utils.encoding import force_text
from rest_framework.renderers import BaseRenderer

class XMLRenderer(BaseRenderer):
    """
    Renderer which serializes to XML.
    """

    media_type = 'application/xml'
    format = 'xml'
    charset = 'utf-8'
    item_tag_name = 'list-item'
    root_tag_name = ''
    end_tag_name = ''

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ''

        stream = StringIO.StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement(self.root_tag_name, {})

        self._to_xml(xml, data)

        xml.endElement(self.end_tag_name)
        xml.endDocument()
        final_xml = stream.getvalue()
        new_xml = ""
        xu = ""
        if "&lt" or "&gt" in final_xml:
            if "&lt" in final_xml:
                xu = final_xml.replace("&lt;","<")
            if "&gt" in final_xml:
                new_xml = xu.replace("&gt;",">")
            if "<>" or "</>" in final_xml:
                new_xml = new_xml.replace("<>", "")
                new_xml = new_xml.replace("</>", "")
            return new_xml

        return final_xml

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement(self.item_tag_name, {})
                self._to_xml(xml, item)
                xml.endElement(self.item_tag_name)

        elif isinstance(data, dict):
            for key, value in six.iteritems(data):
                xml.startElement(key, {})
                self._to_xml(xml, value)
                xml.endElement(key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(force_text(data))
