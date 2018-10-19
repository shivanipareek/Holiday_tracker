


COMPETITOR_HEADER = {'content-type': 'text/xml',
                     'SOAPAction': '"document/http://siebel.com/CustomUI:Receive_spcOpportunity"'}

# COMPETITOR_DATA = """
#
#     <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cus="http://siebel.com/CustomUI" xmlns:crm="http://www.siebel.com/xml/CRM%%20Opportunity%%20IO">
#         <soapenv:Header/>
#         <soapenv:Body>
#             <cus:Receive_spcOpportunity_Input>
#                 <cus:Login>%s</cus:Login>
#                 <cus:Dealer_spcCode>%s</cus:Dealer_spcCode>
#                 <crm:ListOfCrmOpportunityIo>
#                     <crm:Opportunity>
#                         <!--Optional:-->
#                         <crm:BoomBoxId>%s</crm:BoomBoxId>
#                         <!--Optional:-->
#                         <crm:SalesStage>%s</crm:SalesStage>
#                         <!--Optional:-->
#                         <crm:PrimaryPositionId>%s</crm:PrimaryPositionId>
#                         <!--Optional:-->
#                         <crm:Make>%s</crm:Make>
#                         <!--Optional:-->
#                         <crm:CRMOptyIdentifier></crm:CRMOptyIdentifier>
#                         <!--Optional:-->
#                         <crm:ListOfOpportunity_Position>
#                           <!--Zero or more repetitions:-->
#                         </crm:ListOfOpportunity_Position>
#                         <!--Optional:-->
#                         <crm:ListOfOpportunity_Organization>
#                           <!--Zero or more repetitions:-->
#                         </crm:ListOfOpportunity_Organization>
#                         <!--Optional:-->
#                         <crm:ListOfOpportunity_Competitor>
#                          <crm:Opportunity_Competitor IsPrimaryMVG="Y">
#                              <!--Optional:-->
#                              <crm:Name>%s</crm:Name>
#                              <!--Optional:-->
#                              <crm:EstQty>%s</crm:EstQty>
#                              <!--Optional:-->
#                              <crm:ComModel>%s</crm:ComModel>
#                              <!--Optional:-->
#                              <crm:CompetitorsPrice>%s</crm:CompetitorsPrice>
#                              <!--Optional:-->
#                              <crm:SalesType>%s</crm:SalesType>
#                              <!--Optional:-->
#                              <crm:ComComments>%s</crm:ComComments>
#                              <!--Optional:-->
#                           </crm:Opportunity_Competitor>
#                         </crm:ListOfOpportunity_Competitor>
#                     </crm:Opportunity>
#                 </crm:ListOfCrmOpportunityIo>
#             </cus:Receive_spcOpportunity_Input>
#         </soapenv:Body>
#     </soapenv:Envelope>
# """

COMPETITOR_DATA = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cus="http://siebel.com/CustomUI" xmlns:crm="http://www.siebel.com/xml/CRM%20Opportunity%20IO">
       <soapenv:Header/>
       <soapenv:Body>
          <cus:Receive_spcOpportunity_Input>
             <cus:Login>A239004</cus:Login>
             <cus:Dealer_spcCode>Macasa</cus:Dealer_spcCode>
             <crm:ListOfCrmOpportunityIo>
                <crm:Opportunity>
                   <!--Optional:-->
                   <crm:BoomBoxId>1-J81LI3</crm:BoomBoxId>
                   <!--Optional:-->
                   <crm:SalesStage>Identificada</crm:SalesStage>
                   <!--Optional:-->
                   <crm:Make>Renault</crm:Make>
                   <!--Optional:-->
                   <crm:CRMOptyIdentifier></crm:CRMOptyIdentifier>
                   <!--Optional:-->
                   <crm:ListOfOpportunity_Position>
                      <!--Zero or more repetitions:-->
                   </crm:ListOfOpportunity_Position>
                   <!--Optional:-->
                   <crm:ListOfOpportunity_Organization>
                      <!--Zero or more repetitions:-->
                   </crm:ListOfOpportunity_Organization>
                   <!--Optional:-->
                   <crm:ListOfOpportunity_Competitor>
                     <crm:Opportunity_Competitor IsPrimaryMVG="Y">
                         <crm:Name>MAN</crm:Name>
                           <!--Optional:-->
                         <crm:EstQty>10</crm:EstQty>
                         <!--Optional:-->
                      </crm:Opportunity_Competitor>
                   </crm:ListOfOpportunity_Competitor>
                </crm:Opportunity>
             </crm:ListOfCrmOpportunityIo>
          </cus:Receive_spcOpportunity_Input>
       </soapenv:Body>
    </soapenv:Envelope>
"""