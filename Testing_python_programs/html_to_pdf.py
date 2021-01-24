import requests

url = "https://indiagosolar.in"
apiKey = "qY3mfrk4agXooY3JMfn8JI7EhdKExPxBIB1aAErkWTx9GeLNJk5jlBkzvKHPUeGr"
linkRequests = "https://api.html2pdf.app/v1/generate?url={0}&apiKey={1}".format(url, apiKey)

result = requests.get(linkRequests).content

with open("document.pdf", "wb") as handler:
    handler.write(result)