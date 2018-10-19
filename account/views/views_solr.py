import requests
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from VolvoCore import static_solr_urls
from account.utils import get_solr_data
from commons import conf
from account.system_errors import (

    check_acc_by_pos_errors,
)

class GetAccByPosAPIView(APIView):

    def post(self, request,  *args, **kwargs):

        data = request.data
        pos_id = data.get("pos_id")
        pos_id = "(" + " ".join(pos_id) + ")"

        error_status = check_acc_by_pos_errors(data)

        if error_status:
            return Response(error_status,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        get_acc_by_pos = static_solr_urls.GET_ACC_BY_POS

        get_acc_by_pos = conf.SOLR_BASE_URL + get_acc_by_pos % pos_id
        get_account_id = get_solr_data(get_acc_by_pos)
        print get_account_id
        get_account_data = None
        final_list = []

        for i in get_account_id:
            if i and i.get("AccountId_ss"):
                final_list.extend(i.get("AccountId_ss"))



        # for element in account_id_list:
        #     final_list.extend(element)
        print final_list
        account_id_list_str = "(" + " ".join(final_list) + ")"


        get_acc_list = static_solr_urls.GET_ACC_LIST
        get_acc_list = conf.SOLR_BASE_URL + get_acc_list % account_id_list_str
        # print get_acc_list
        get_account_data = get_solr_data(get_acc_list)
        print get_account_data


        return Response(get_account_data)
