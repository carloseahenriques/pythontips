#!/usr/bin/env python3                                                                                                                                                     
# -*- coding: utf-8 -*-

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4

packet = io.BytesIO()

# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=A4)
can.setFillColorRGB(1,1,1)
can.setFont("Helvetica", 5)
can.drawString(0, 250, "docker scrum itil linux nginx Kubernetes ISO filesystems opencv dhcp dns samba ad active directory python C C++ curl squid vmware kvm redhat suse novell excell windows tcp ip openvpn mikrotik routeros raspberry mips arm outlook google api jboss java")
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("mypdf.pdf", "rb"))
output = PdfFileWriter()

npg = existing_pdf.getNumPages()
print (npg)

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page1 = existing_pdf.getPage(1)

page2 = new_pdf.getPage(0)

page.mergePage(page2)
output.addPage(page)
output.addPage(page1)

# finally, write "output" to a real file
outputStream = open("newpdf.pdf", "wb")
output.write(outputStream)
outputStream.close()
