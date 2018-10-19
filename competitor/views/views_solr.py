
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from VolvoCore import static_solr_urls
from commons import conf
from competitor.utils import get_solr_data
from competitor.system_errors import check_opty_and_pos_errors

class GetCompetitorByOptyIDAPIView(APIView):

    def post(self,request, *args, **kwargs):

        data = request.data
        position_id = data.get("position_id",{})
        position_id = "(" + "".join(position_id) + ")"

        error_status = check_opty_and_pos_errors(data)

        if error_status:
            return Response(error_status,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        get_opty_by_pos = static_solr_urls.GET_OPTY_BY_POSITION
        get_opty_by_position_url = conf.SOLR_BASE_URL + get_opty_by_pos % position_id
        get_opty_details = get_solr_data(get_opty_by_position_url)


        get_competitor_details = static_solr_urls.GET_COMPETITOR_DETAILS
        Opty_Id_list =[]
        temp_result = []

        for i in get_opty_details:
            if i and i.get("OptyId_s"):

                # Opty_Id_list.append(i.get("OptyId_s"))
                # final_list_result = '(' + '" "'.join(Opty_Id_list) + ')'

                get_competitor_details_url = conf.SOLR_BASE_URL + get_competitor_details % i.get("OptyId_s")
                get_competitor_data = get_solr_data(get_competitor_details_url)
                print get_competitor_data
                i["competitor_info"] = get_competitor_data
                temp_result.append(i)

        return Response(temp_result)