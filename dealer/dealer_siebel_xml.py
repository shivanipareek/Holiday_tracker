DEALER_RESPONSE_XML = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:deal="http://35.161.1.92:8080/api/sync/dealer/">
       <soapenv:Header/>
       <soapenv:Body>
          <deal:AudetemiDealerResponse>
             <deal:faultactor>%s</deal:faultactor>
             <deal:faultcode>%s</deal:faultcode>
             <deal:faultstring>%s</deal:faultstring>
          </deal:AudetemiDealerResponse>
       </soapenv:Body>
   </soapenv:Envelope>
"""
