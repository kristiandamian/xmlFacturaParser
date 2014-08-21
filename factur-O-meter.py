# -*- coding: cp1252 -*-


from xml.dom import minidom
from xml.dom.minidom import parseString
import glob

def parseXML():
    for file in GetXML():
        xmldoc = minidom.parse(file)
        itemlist = xmldoc.getElementsByTagName('cfdi:Comprobante')
        fact=Factura()

        for s in itemlist :
            try:
                fact.Folio=s.attributes['folio'].value
            except:
                fact.Folio=""
            fact.LugarExpedicion=s.attributes['LugarExpedicion'].value
            fact.Total=s.attributes['total'].value
            
        itemlist = xmldoc.getElementsByTagName('cfdi:Receptor')
        for s in itemlist :
            fact.RFC=s.attributes['rfc'].value
            fact.Nombre= s.attributes['nombre'].value
        AgregoArchivo(fact)

def GetXML():
    files=[]
    for file in glob.glob("xml/*.xml"):
        files.append(file)
        print file
    return files

def AgregoArchivo(factura):
    SEPARADOR=";"
    with open('FacturasCaro.csv', 'a') as the_file:
            the_file.write(factura.Folio.encode('utf8'))
            the_file.write(SEPARADOR)
            the_file.write(factura.RFC.encode('utf8') )            
            the_file.write(SEPARADOR)
            the_file.write(factura.Nombre.encode('utf8') )
            the_file.write(SEPARADOR)
            the_file.write(factura.LugarExpedicion.encode('utf8') )
            the_file.write(SEPARADOR)
            the_file.write(factura.Total)
            the_file.write(SEPARADOR)
            the_file.write('\n')

class Factura:
    Folio=""
    LugarExpedicion=""
    Nombre=""
    RFC=""
    Total=""


if __name__ == "__main__":
    parseXML()
