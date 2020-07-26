#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name:       Text to PDF converter
Created by: Christian Morán
e-mail:     christianrmoran86@gmail.com
More code:  http://github.com/chrisrm86

##########################################################
"""
from fpdf import FPDF

def convert_to_pdf():
    print("Convert txt to PDF")
    text_filename = input("Text file name: ")
    pdf_filename = input("PDF file name: ")
    print('1 - Justify')
    print('2 - Center')
    print('3 - Right')
    alignment = str(input('Choose Alignment: '))
    if alignment == '1':
        align = 'J'
    elif alignment == '2':
        align = 'C'
    elif alignment == '3':
        align = 'R'
    else:
        print("Invalid option")
        return convert_to_pdf()

    pdf_file = FPDF()
    pdf_file.add_page()
    pdf_file.set_font("Arial", size=10)
    text_file = open('{}.txt'.format(text_filename), "r")
    for x in text_file:
        pdf_file.cell(200, 10, txt=x, ln=1, align = align)

    pdf_file.output("{}.pdf".format(pdf_filename))
    print('File: {} successfully created'.format(pdf_filename))

convert_to_pdf()
print('Press Enter/Intro to exit.')
input()