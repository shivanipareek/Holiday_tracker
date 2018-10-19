CONTACT_HEADER = {
    'Content-Type': 'text/xml;charset=UTF-8',
    'SOAPAction'  : '"document/http://siebel.com/CustomUI:Receive_spcContact"'
                }

CONTACT_DATA = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cus="http://siebel.com/CustomUI" xmlns:crm="http://www.siebel.com/xml/CRM%%20MoBox%%20Contact%%20IO">
       <soapenv:Header/>
       <soapenv:Body>
          <cus:Receive_spcContact_Input>
             <cus:Login>%s</cus:Login>
             <cus:Dealer_spcCode>%s</cus:Dealer_spcCode>
             <crm:ListOfCrmMoboxContactIo>
                <!--Zero or more repetitions:-->
                <crm:Contact>
                   <!--Optional:-->
                   <crm:BoomBoxId>%s</crm:BoomBoxId>
                   <!--Optional:-->
                   <crm:AccountId>%s</crm:AccountId>
                   <!--Optional:-->
                   <crm:CellularPhone>%s</crm:CellularPhone>
                   <!--Optional:-->
                   <crm:EmailAddress>%s</crm:EmailAddress>
                   <crm:FirstName>%s</crm:FirstName>
                   <!--Optional:-->
                   <crm:JobTitle>%s</crm:JobTitle>
                   <crm:LastName>%s</crm:LastName>
                   <!--Optional:-->
                   <crm:WorkPhone>?</crm:WorkPhone>
                   <!--Optional:-->
                   <crm:CRMConIdentifier>?</crm:CRMConIdentifier>
                   <!--Optional:-->
                   <crm:CRMContactDMU>%s</crm:CRMContactDMU>
                   <!--Optional:-->
                   <crm:CRMContactsHobby>%s</crm:CRMContactsHobby>
                   <!--Optional:-->
                   <crm:ListOfContact_Account>
                      <!--Zero or more repetitions:-->
                      <crm:Contact_Account>
                         <crm:Account>?</crm:Account>
                         <!--Optional:-->
                         <crm:AccountRowId>?</crm:AccountRowId>
                      </crm:Contact_Account>
                   </crm:ListOfContact_Account>
                   <!--Optional:-->
                   <crm:ListOfContact_Position>
                      <!--Zero or more repetitions:-->
                      <crm:Contact_Position IsPrimaryMVG="?">
                         <crm:PositionName>?</crm:PositionName>
                         <!--Optional:-->
                         <crm:PositionId>?</crm:PositionId>
                      </crm:Contact_Position>
                   </crm:ListOfContact_Position>
                   <!--Optional:-->
                   <crm:ListOfContact_Organization>
                      <!--Zero or more repetitions:-->
                      <crm:Contact_Organization IsPrimaryMVG="?">
                         <crm:Organization>?</crm:Organization>
                         <crm:OrganizationId>?</crm:OrganizationId>
                      </crm:Contact_Organization>
                   </crm:ListOfContact_Organization>
                </crm:Contact>
             </crm:ListOfCrmMoboxContactIo>
             <cus:Primary>?</cus:Primary>
          </cus:Receive_spcContact_Input>
       </soapenv:Body>
    </soapenv:Envelope>
"""
