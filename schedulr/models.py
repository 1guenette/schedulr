# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
Created on Sep 16, 2016

@author: shshankm
'''
from pdfminer import pdfparser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from posix import lstat
import re
from _ast import Str
from fileinput import filename
import datetime
from django.core.files import File
from django.db import models
from django.utils import timezone

# Create your models here.
#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#    def __str__(self):
#        return self.question_text
#    def was_published_recently(self):
#        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
#    def __str__(self):
#        return self.choice_text
#########################################--------MAIN--------###########################################
class pdfParse(models.Model):
    filepath = '/home/phoenx/geo.pdf'
    pdfFile = open(filepath, "rb")
    
    def __str__(self):
        return self.seqStringfirst

    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)


    counter = 0
    lst = []
    for page in PDFPage.get_pages(pdfFile):
        interpreter.process_page(page)
        counter = counter+1
    pdfFile.close()


    ##################################################################
    #PUTS ALL DATA INTO A STRING FORMAT

    pdfText = sio.getvalue()

    dateOutput = re.findall("[a-zA-Z]{3}, +[a-zA-Z]{3} +[0-9]{2}", pdfText)
    if(len(dateOutput) < 4):
        dateOutput = re.findall("[a-zA-Z]{3}, +[0-9]{1,2} +[0-9]{1,2}", pdfText)
    if(len(dateOutput) < 4):
        dateOutput = re.findall("[a-zA-Z]{3}, +[0-9]{1,2} +[0-9]{1,2}", pdfText)

    if(len(dateOutput) < 4):
        dateOutput = re.findall("(January|Feburary|March|April|May|June|July|August|September|October|December){1,8} +[0-9]{1,2}", pdfText)

    #    print("One last try: BruteForce Searching for all and any matching dates"


    assignmentOutput = re.findall("[0-9]{1,2}.[0-9]{1,2}-[0-9]{1,2}.[0-9]{1,2}",pdfText)

    if(len(assignmentOutput) < 4):
        assignmentOutput = re.findall("[Fourm]{4} +[0-9]{3,4}",pdfText)

    if(len(assignmentOutput) < 4):
        assignmentOutput = re.findall("[a-zA-Z]{1,8} +[0-9].[0-9]{1,2}|-[0-9]{1,2}.[0-9]{1,2}|[a-zA-Z]{1,8} +[0-9]{1,2}", pdfText)

    #    if(len(assignmentOutput) < 4):
    #        print("No assignments Avalable, please check PDF entered or Enter the format of the date ")

    #    if(len(assignmentOutput) < 4 & len(dateOutput) < 4):
    #        print("Could not find any proper matching assignment, will still create a reminder for the date recieved")


        #print "dateOutput: "+dateOutput
    #    for objDate in dateOutput:
    #        print(objDate)

    #    for objassgn in assignmentOutput[3:]:
    #        print(objassgn)

    secondColumn = False;
    for obj2Date in dateOutput:
        startIdx = 0
        if(len(obj2Date) > 2):
            startIdx = 0
        else:
            startIdx = 8
        if(len(obj2Date) > 2):
    #           print("Date is Alpha only!! output might differ")
            break
        elif (int(obj2Date[startIdx:]) > 21):
    #           print("date is present in the Last column")
            secondColumn = True
            break
        else:
    #           print("date is present in the First column")
            break

    #    print("\n\n Printing: \n")
    #return self.toStr(dateOutput, assignmentOutput)

    seqStringfirst = []

    copyDateList = dateOutput
    copyAssignmentList = assignmentOutput[2:len(assignmentOutput)-2]


    copyDateList.reverse()
    copyAssignmentList.reverse()

    counter = 0

    #############Check for values#############

    while(counter < len(copyDateList)):
        dateString = ""
        assignString = ""

        seqStringfirst += "Assignment: "+copyDateList.pop()+" Due On:"+copyAssignmentList.pop()
        seqStringfirst += "</br> </br>"
        counter = counter + 1

    #return seqStringfirst
