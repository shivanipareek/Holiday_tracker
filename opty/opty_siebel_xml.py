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

CREATE_OPTY_DATA = """

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cus="http://siebel.com/CustomUI" xmlns:crm="http://www.siebel.com/xml/CRM%%20Opportunity%%20IO">
   <soapenv:Header/>
   <soapenv:Body>
      <cus:Receive_spcOpportunity_Input>
         <cus:OptyId></cus:OptyId>
         <cus:Login>%s</cus:Login>
         <cus:Dealer_spcCode>%s</cus:Dealer_spcCode>
         <crm:ListOfCrmOpportunityIo>
            <crm:Opportunity>
               <!--Optional:-->
               <crm:MarketingLeadId>%s</crm:MarketingLeadId>
               <!--Optional:-->
               <crm:OtherReason></crm:OtherReason>
               <!--Optional:-->
               <crm:BoomBoxId>%s</crm:BoomBoxId>
               <!--Optional:-->
               <crm:AccountName>%s</crm:AccountName>
               <crm:AccountId>%s</crm:AccountId>
               <crm:OpportunityName>%s</crm:OpportunityName>
               <crm:SalesStage>%s</crm:SalesStage>
               <crm:Status>%s</crm:Status>
               <!--Optional:-->
               <crm:Comments>%s</crm:Comments>
               <!--Optional:-->
               <crm:FinanceContract></crm:FinanceContract>
               <!--Optional:-->
               <crm:ServiceContract></crm:ServiceContract>
               <crm:EstimatedQuantity>%s</crm:EstimatedQuantity>
               <crm:Make>%s</crm:Make>
               <!--Optional:-->
               <crm:Model>%s</crm:Model>
               <!--Optional:-->
               <crm:EstimatedSellPrice></crm:EstimatedSellPrice>
               <crm:WinProbability>%s</crm:WinProbability>
               <!--Optional:-->
               <crm:DeliveryDate>%s</crm:DeliveryDate>
               <!--Optional:-->
               <crm:CloseDate></crm:CloseDate>
               <!--Optional:-->
               <crm:Reason></crm:Reason>
               <crm:DealerCode>%s</crm:DealerCode>
               <crm:SourceType>%s</crm:SourceType>
               <!--Optional:-->
               <crm:PrimaryPositionId>%s</crm:PrimaryPositionId>
               <!--Optional:-->
               <crm:SalesMethod></crm:SalesMethod>
               <!--Optional:-->
               <crm:PrimaryPartnerId></crm:PrimaryPartnerId>
               <!--Optional:-->
               <crm:ActualQuantity></crm:ActualQuantity>
               <!--Optional:-->
               <crm:ActualUnitPrice></crm:ActualUnitPrice>
               <!--Optional:-->
               <crm:IndustrySegment></crm:IndustrySegment>
               <!--Optional:-->
               <crm:ApplicationType></crm:ApplicationType>
               <!--Optional:-->
               <crm:ContractType></crm:ContractType>
               <!--Optional:-->
               <crm:CopaymentFlag></crm:CopaymentFlag>
               <!--Optional:-->
               <crm:ExpectedOrderDate>%s</crm:ExpectedOrderDate>
               <!--Optional:-->
               <crm:CreditCheck></crm:CreditCheck>
               <!--Optional:-->
               <crm:SalesMethodId></crm:SalesMethodId>
               <!--Optional:-->
               <crm:SalesStageId></crm:SalesStageId>
               <!--Optional:-->
               <crm:OpportunityType>%s</crm:OpportunityType>
               <!--Optional:-->
               <crm:AvgUnits>%s</crm:AvgUnits>
               <!--Optional:-->
               <crm:Demo></crm:Demo>
               <!--Optional:-->
               <crm:NewAccount></crm:NewAccount>
               <!--Optional:-->
               <crm:PlantVisit></crm:PlantVisit>
               <!--Optional:-->
               <crm:QuoteNum></crm:QuoteNum>
               <!--Optional:-->
               <crm:Quoted>%s</crm:Quoted>
               <!--Optional:-->
               <crm:Reason2>%s</crm:Reason2>
               <!--Optional:-->
               <crm:Reason1>%s</crm:Reason1>
               <!--Optional:-->
               <crm:Reason3>%s</crm:Reason3>
               <!--Optional:-->
               <crm:WalkAround></crm:WalkAround>
               <!--Optional:-->
               <crm:AccountType></crm:AccountType>
               <!--Optional:-->
               <crm:CustomerContacted></crm:CustomerContacted>
               <!--Optional:-->
               <crm:CustomerInterested></crm:CustomerInterested>
               <!--Optional:-->
               <crm:MeetDeliveryDate></crm:MeetDeliveryDate>
               <!--Optional:-->
               <crm:DemoCustomer></crm:DemoCustomer>
               <!--Optional:-->
               <crm:FinalSpecification></crm:FinalSpecification>
               <!--Optional:-->
               <crm:HotButtons></crm:HotButtons>
               <!--Optional:-->
               <crm:MackProduct></crm:MackProduct>
               <!--Optional:-->
               <crm:PlanonReturnVisit></crm:PlanonReturnVisit>
               <!--Optional:-->
               <crm:PlansOnaTruck></crm:PlansOnaTruck>
               <!--Optional:-->
               <crm:ProductDemostration></crm:ProductDemostration>
               <!--Optional:-->
               <crm:ProductSatisfy></crm:ProductSatisfy>
               <!--Optional:-->
               <crm:PurchaseLease></crm:PurchaseLease>
               <!--Optional:-->
               <crm:ProbableScore></crm:ProbableScore>
               <!--Optional:-->
               <crm:SelectPlant></crm:SelectPlant>
               <!--Optional:-->
               <crm:TypeofCustomer></crm:TypeofCustomer>
               <!--Optional:-->
               <crm:VisittothePlant></crm:VisittothePlant>
               <!--Optional:-->
               <crm:CRMOptyIdentifier></crm:CRMOptyIdentifier>
               <!--Optional:-->
               <crm:TurnInLeadId>%s</crm:TurnInLeadId>
               <!--Optional:-->
               <crm:CustomerBuyingStage></crm:CustomerBuyingStage>
               <!--Optional:-->
               <crm:CRMVRCFlag></crm:CRMVRCFlag>
               <!--Optional:-->
               <crm:BudgetQual></crm:BudgetQual>
               <!--Optional:-->
               <crm:AuthorityQual></crm:AuthorityQual>
               <!--Optional:-->
               <crm:NeedQual></crm:NeedQual>
               <!--Optional:-->
               <crm:TimeframeQual></crm:TimeframeQual>
               <!--Optional:-->
               <crm:ListOfOpportunity_Position>
                  <!--Zero or more repetitions:-->
                  <crm:Opportunity_Position IsPrimaryMVG="?">
                     <!--Optional:-->
                     <crm:Id>?</crm:Id>
                     <crm:Position>?</crm:Position>
                     <!--Optional:-->
                     <crm:PositionId>?</crm:PositionId>
                  </crm:Opportunity_Position>
               </crm:ListOfOpportunity_Position>
               <!--Optional:-->
               <crm:ListOfOpportunity_Organization>
                  <!--Zero or more repetitions:-->
                  <crm:Opportunity_Organization IsPrimaryMVG="?">
                     <crm:Organization>?</crm:Organization>
                     <crm:OrganizationId>?</crm:OrganizationId>
                  </crm:Opportunity_Organization>
               </crm:ListOfOpportunity_Organization>
               <!--Optional:-->
               <crm:ListOfOpportunity_Competitor>
                  <!--Zero or more repetitions:-->
               </crm:ListOfOpportunity_Competitor>
            </crm:Opportunity>
         </crm:ListOfCrmOpportunityIo>
      </cus:Receive_spcOpportunity_Input>
   </soapenv:Body>
</soapenv:Envelope>

"""

CREATE_OPTY_URL = "https://wsp-qa.it.volvo.com/BOOMBOX/eai_anon_enu/start.swe?SWEExtSource=SecureWebService&SWEExtCmd=Execute"

CREATE_OPTY_HEADER = {
        'Content-Type':'text/xml;charset=UTF-8',
        'SOAPAction': '"document/http://siebel.com/CustomUI:Receive_spcOpportunity"'
    }

OPTY_RESPONSE_XML = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:opty="http://35.161.1.92:8080/api/sync/opty/">
       <soapenv:Header/>
       <soapenv:Body>
          <opty:AudetemiOptyResponse>
             <opty:faultactor>%s</opty:faultactor>
             <opty:faultcode>%s</opty:faultcode>
             <opty:faultstring>%s</opty:faultstring>
          </opty:AudetemiOptyResponse>
       </soapenv:Body>
   </soapenv:Envelope>
"""
