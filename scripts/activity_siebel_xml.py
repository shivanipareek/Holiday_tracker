CREATE_ACTIVITY_HEADER = {
        'Content-Type':'text/xml;charset=UTF-8',
        'SOAPAction': '"document/http://siebel.com/CustomUI:Receive_spcActivity"'
    }


ACTIVITY_CREATE_DATA = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cus="http://siebel.com/CustomUI" xmlns:crm="http://www.siebel.com/xml/CRM%%20Activity%%20MoBox%%20IO">
       <soapenv:Header/>
       <soapenv:Body>
          <cus:Receive_spcActivity_Input>
             <cus:Login>A239004</cus:Login>
             <cus:Dealer_spcCode>%s</cus:Dealer_spcCode>
             <crm:ListOfCrmActivityMoboxIo>
                <!--Zero or more repetitions:-->
                <crm:Action>
                   <!--Optional:-->
                   <crm:TurnInLeadId>%s</crm:TurnInLeadId>
                   <!--Optional:-->
                   <crm:MarketingLeadId>%s</crm:MarketingLeadId>
                   <!--Optional:-->
                   <crm:BoomBoxId>%s</crm:BoomBoxId>
                   <!--Optional:-->
                   <crm:AccountId>%s</crm:AccountId>
                   <crm:Type>%s</crm:Type>
                   <crm:Status>%s</crm:Status>
                   <!--Optional:-->
                   <crm:Comment>%s</crm:Comment>
                   <!--Optional:-->
                   <crm:Description>%s</crm:Description>
                   <!--Optional:-->
                   <crm:PrimaryOwnedBy>%s</crm:PrimaryOwnedBy>
                   <!--Optional:-->
                   <crm:DoneFlg>%s</crm:DoneFlg>
                   <!--Optional:-->
                   <crm:OpportunityId>%s</crm:OpportunityId>
                   <!--Optional:-->
                   <crm:CRMActIdentifier>%s</crm:CRMActIdentifier>
                   <!--Optional:-->
                   <crm:SubType>%s</crm:SubType>
                   <!--Optional:-->
                   <crm:Proceed>%s</crm:Proceed>
                   <!--Optional:-->
                   <crm:ListOfAction_Employee>
                      <!--Zero or more repetitions:-->
                      <crm:Action_Employee IsPrimaryMVG="?">
                         <!--Optional:-->
                         <crm:OwnedById>?</crm:OwnedById>
                      </crm:Action_Employee>
                   </crm:ListOfAction_Employee>
                </crm:Action>
             </crm:ListOfCrmActivityMoboxIo>
          </cus:Receive_spcActivity_Input>
       </soapenv:Body>
    </soapenv:Envelope>
"""