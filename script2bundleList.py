import os
import re
import csv

print("starting")
def flatten (list_of_lists):
    flattened  = [val for sublist in list_of_lists  for val in sublist]
    return flattened

def assignCategory(custStrng):
    custStrng = custStrng[1:-1]
    if re.search("custevent", custStrng):
        if custStrng not in flatten(crmFields):
            crmFields.append(["","",custStrng])
    elif re.search("custentity", custStrng):
        if custStrng not in flatten(entityFields):
            entityFields.append(["","",custStrng])
    elif re.search("custitem", custStrng):
        if custStrng not in flatten(itemfields):
            itemfields.append(["","",custStrng])
    elif re.search("custitemnumber", custStrng):
        if custStrng not in flatten(itemNumberFields):
            itemNumberFields.append(["","",custStrng])
    elif re.search("custrecord", custStrng):
        if custStrng not in flatten(otherRecordSublistFields):
            otherRecordSublistFields.append(["","",custStrng])
    elif re.search("custbody", custStrng):
        if custStrng not in flatten(transactionBodyFields):
            transactionBodyFields.append(["","",custStrng])
    elif re.search("custcol", custStrng):
        if custStrng not in flatten(transactionLineItemOptionsFields):
            transactionLineItemOptionsFields.append(["","",custStrng])
    elif re.search("customlist", custStrng):
        if custStrng not in flatten(lists):
            lists.append(["","",custStrng])
    elif re.search("customrecord", custStrng):
        if custStrng not in flatten(records):
            records.append(["","",custStrng])
    elif re.search("customtransaction", custStrng):
        if custStrng not in flatten(transactions):
            transactions.append(["","",custStrng])

def addName(fields, fieldsFile, idColumn, nameColumn):
    with open(fieldsFile, newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if len(row)>=idColumn:
                status = True
                i=0
                while status == True and i<len(fields):
                    match = re.search(f"^{fields[i][-1]}$", row[idColumn])
                    if match:
                        fields[i].append(row[nameColumn])
                        status = False
                    i+=1

def addNameScripts(fields, fieldsFile, idColumn, nameColumn):
    indexPop =[]
    with open(fieldsFile, newline='',  encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if len(row)>=idColumn:
                status = True
                i=0
                length = len(fields["suiteScripts"])
                while status == True and i<length:
                    match = re.search(f"^{fields['suiteScripts'][i][-1].strip()}$", row[idColumn].strip())
                    if match:
                        fields[row[2]].append(["","",row[idColumn],row[nameColumn]])
                        if i not in indexPop:
                            indexPop.append(i)
                        status = False
                    i+=1
    indexPop.sort(reverse=True)
    for index in indexPop:
        fields["suiteScripts"].pop(index)

def addNameComplex(fields, fields1, fields2, fieldsFile1, fieldsFile2, idColumn, nameColumn):
    indexPop =[]
    if fieldsFile1:
        with open(fieldsFile1, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                if len(row)>=idColumn:
                    status = True
                    i = 0
                    while status == True and i<len(fields):
                        match = re.search(f"^{fields[i][-1]}$", row[idColumn])
                        if match:
                            fields1.append(["","",fields[i][-1],row[nameColumn]])
                            if i not in indexPop:
                                indexPop.append(i)
                            status = False
                        i+=1
    if fieldsFile2:                    
        with open(fieldsFile2, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                if len(row)>=idColumn:
                    status = True
                    i = 0
                    while status == True and i<len(fields):
                        match = re.search(f"^{fields[i][-1]}$", row[idColumn])
                        if match:
                            fields2.append(["","",fields[i][-1],row[nameColumn]])
                            if i not in indexPop:
                                indexPop.append(i)
                            status = False
                        i+=1
    indexPop.sort(reverse=True)              
    for index in indexPop:
        fields.pop(index)

#toCSV Variables
crmFields = []
entityFields = []
itemfields = []
itemNumberFields = []
otherRecordSublistFields = []
otherRecordFields = []
otherSubslistFields = []
transactionBodyFields = []
transactionLineItemOptionsFields = []
transactionLineFields = []
itemOptionsFields = []
lists = []
records = []
transactions = []
suiteScripts = {
    "suiteScripts": [],
    "Client": [],
    "Map/Reduce": [],
    "Mass Update": [],
    "Portlet": [],
    "RESTlet": [],
    "Scheduled": [],
    "Suitelet": [],
    "User Event": [],
    "Workflow Action": []
    }

#file Variables
crmFieldsFile = None
entityFieldsFile = None
itemFieldsFile = None
itemNumberFieldsFile = None
otherRecordFieldsFile = None
otherSublistFieldsFile = None
transactionBodyFieldsFile = None
transactionLineFieldsFile = None
itemOptionsFieldsFile = None
listsFile = None
recordsFile = None
transactionsFile = None
suiteScriptsFile = None

for root, directories, files in os.walk("."):
    for name in files:
        match = re.search("^CustomCRMFields[0-9]*.csv$", name)
        if match:
            crmFieldsFile = os.path.join(root, name)
        match = re.search("^CustomEntityFields[0-9]*.csv$", name)
        if match:
            entityFieldsFile = os.path.join(root, name)
        match = re.search("^CustomItemFields[0-9]*.csv$", name)
        if match:
            itemFieldsFile = os.path.join(root, name)
        match = re.search("^CustomItemNumberFields[0-9]*.csv$", name)
        if match:
            itemNumberFieldsFile = os.path.join(root, name)
        match = re.search("^OtherRecordFields[0-9]*.csv$", name)
        if match:
            otherRecordFieldsFile = os.path.join(root, name)
        match = re.search("^OtherSublistFields[0-9]*.csv$", name)
        if match:
            otherSublistFieldsFile = os.path.join(root, name)
        match = re.search("^TransactionBodyFields[0-9]*.csv$", name)
        if match:
            transactionBodyFieldsFile = os.path.join(root, name)
        match = re.search("^TransactionLineFields[0-9]*.csv$", name)
        if match:
            transactionLineFieldsFile = os.path.join(root, name)
        match = re.search("^ItemOptionsFields[0-9]*.csv$", name)
        if match:
            itemOptionsFieldsFile = os.path.join(root, name)
        match = re.search("^CustomLists[0-9]*.csv$", name)
        if match:
            listsFile = os.path.join(root, name)
        match = re.search("^RecordTypes[0-9]*.csv$", name)
        if match:
            recordsFile = os.path.join(root, name)
        match = re.search("^CustomTransactionTypes[0-9]*.csv$", name)
        if match:
            transactionsFile = os.path.join(root, name)
        match = re.search("^scriptSearch4BundlerListResults[0-9]*.csv$", name)
        if match:
            suiteScriptsFile = os.path.join(root, name)
        match = re.search(".js$", name)
        if match:
            suiteScripts["suiteScripts"].append(["","",name])
            with open(os.path.join(root, name), 'r') as file:
                text = file.read()
                matches = re.findall("'cust[a-z_]+'|\"cust[a-z_]+\"", text)
                for custStrng in matches:
                    assignCategory(custStrng)

#search names
if crmFieldsFile:
    addName(crmFields, crmFieldsFile, 3, 1)
if entityFieldsFile:
    addName(entityFields, entityFieldsFile, 3, 1)
if itemFieldsFile:
    addName(itemfields, itemFieldsFile, 3, 1)
if itemNumberFieldsFile:
    addName(itemNumberFields, itemNumberFieldsFile, 3, 1)
if otherRecordFieldsFile or otherSublistFieldsFile:
    addNameComplex(otherRecordSublistFields, otherRecordFields, otherSubslistFields, otherRecordFieldsFile, otherSublistFieldsFile, 3, 1)
if transactionBodyFieldsFile:
    addName(transactionBodyFields, transactionBodyFieldsFile, 3, 1)
if transactionLineFieldsFile:
    addName(transactionLineFields, transactionLineFieldsFile, 3, 1)
if itemOptionsFieldsFile:
    addName(itemOptionsFields, itemOptionsFieldsFile, 3, 1)
if transactionLineFieldsFile or itemOptionsFieldsFile:
    addNameComplex(transactionLineItemOptionsFields, transactionLineFields, itemOptionsFields, transactionLineFieldsFile, itemOptionsFieldsFile, 3, 1)
if listsFile:
    addName(lists, listsFile, 3, 1)
if recordsFile:
    addName(records, recordsFile, 2, 0)
if transactionsFile:
    addName(transactions, transactionsFile, 3, 1)
if suiteScriptsFile:
    addNameScripts(suiteScripts, suiteScriptsFile, 3, 1)

#write file
with open('bundleList.csv', 'w', newline='',  encoding="utf8") as csvfile:
    spamwriter = csv.writer(csvfile)
    if len(crmFields)>0 or len(entityFields)>0 or len(itemfields)>0 or len(itemNumberFields)>0 or len(otherRecordSublistFields)>0 or len(otherRecordFields)>0 or len(otherSubslistFields)>0 or len(transactionBodyFields)>0 or len(transactionLineItemOptionsFields)>0 or len(transactionLineFields)>0 or len(itemOptionsFields)>0:
        spamwriter.writerows([["Custom Fields"]])
    if len(crmFields)>0:
        spamwriter.writerows([["","CRM Fields"]])
        spamwriter.writerows(crmFields)
    if len(entityFields)>0:
        spamwriter.writerows([["","Entity Fields"]])
        spamwriter.writerows(entityFields)
    if len(itemfields)>0:
        spamwriter.writerows([["","item Fields"]])
        spamwriter.writerows(itemfields)
    if len(itemNumberFields)>0:
        spamwriter.writerows([["","Item Number Fields"]])
        spamwriter.writerows(itemNumberFields)
    
    if len(otherSubslistFields)==0 and len(otherRecordFields)==0:
        spamwriter.writerows([["","Other Record/Sublist Fields not founded"]])
        spamwriter.writerows(otherRecordSublistFields)
    else:
        if len(otherRecordFields)>0:
            spamwriter.writerows([["","Other Record Fields"]])
            spamwriter.writerows(otherRecordFields)
        if len(otherSubslistFields)>0:
            spamwriter.writerows([["","Other Sublist Fields"]])
            spamwriter.writerows(otherSubslistFields)
        if len(otherRecordSublistFields)>0:
            spamwriter.writerows([["","Other Sublist/Record Fields not founded, probably non bundable fields from custom records, suitelets, etc"]])
            spamwriter.writerows(otherRecordSublistFields)

    if len(transactionBodyFields)>0:
        spamwriter.writerows([["","Transaction Body Fields"]])
        spamwriter.writerows(transactionBodyFields)
        
    if len(transactionLineFields)==0 and len(itemOptionsFields)==0:
        spamwriter.writerows([["","Transaction Line Fields or Item Options not founded"]])
        spamwriter.writerows(transactionLineItemOptionsFields)
    else:
        if len(itemOptionsFields)>0:
            spamwriter.writerows([["","Transaction Item Options"]])
            spamwriter.writerows(itemOptionsFields)
        if len(transactionLineFields)>0:
            spamwriter.writerows([["","Transaction Line Fields"]])
            spamwriter.writerows(transactionLineFields)
        if len(transactionLineItemOptionsFields)>0:
            spamwriter.writerows([["","Transaction Line Fields or Item Options not founded"]])
            spamwriter.writerows(transactionLineItemOptionsFields)

    if len(lists)>0 or len(records)>0 or len(transactions)>0:
        spamwriter.writerows([["Custom List/Records"]])
    if len(lists)>0:
        spamwriter.writerows([["","Lists"]])
        spamwriter.writerows(lists)
    if len(records)>0:
        spamwriter.writerows([["","Records"]])
        spamwriter.writerows(records)
    if len(transactions)>0:
        spamwriter.writerows([["","Transactions"]])
        spamwriter.writerows(transactions)
    if len(suiteScripts["suiteScripts"])>0:
        spamwriter.writerows([["SuiteScripts"]])
        if not suiteScriptsFile:
            spamwriter.writerows(suiteScripts["suiteScripts"])
        else:
            if len(suiteScripts["Client"])>0:
                spamwriter.writerows([["","Client"]])
                spamwriter.writerows(suiteScripts["Client"])
            if len(suiteScripts["Map/Reduce"])>0:
                spamwriter.writerows([["","Map/Reduce"]])
                spamwriter.writerows(suiteScripts["Map/Reduce"])
            if len(suiteScripts["Mass Update"])>0:
                spamwriter.writerows([["","Mass Update"]])
                spamwriter.writerows(suiteScripts["Mass Update"])
            if len(suiteScripts["Portlet"])>0:
                spamwriter.writerows([["","Portlet"]])
                spamwriter.writerows(suiteScripts["Portlet"])
            if len(suiteScripts["RESTlet"])>0:
                spamwriter.writerows([["","RESTlet"]])
                spamwriter.writerows(suiteScripts["RESTlet"])
            if len(suiteScripts["Scheduled"])>0:
                spamwriter.writerows([["","Scheduled"]])
                spamwriter.writerows(suiteScripts["Scheduled"])
            if len(suiteScripts["Suitelet"])>0:
                spamwriter.writerows([["","Suitelet"]])
                spamwriter.writerows(suiteScripts["Suitelet"])
            if len(suiteScripts["User Event"])>0:
                spamwriter.writerows([["","User Event"]])
                spamwriter.writerows(suiteScripts["User Event"])
            if len(suiteScripts["Workflow Action"])>0:
                spamwriter.writerows([["","Workflow Action"]])
                spamwriter.writerows(suiteScripts["Workflow Action"])
            if len(suiteScripts["suiteScripts"])>0:
                spamwriter.writerows([["","Not founded scripts probably libraries or cs realated on code"]])
                spamwriter.writerows(suiteScripts["suiteScripts"])


"""
#EntityField custentity
#Itemfields custitem
#CRM Fields custevent
Custom Item Number Fields custitemnumber 
Other Record Fields 
custrecord
Other Sublist Fields 
Transaction Body Fields 
custbody
Transaction Line Fields  | Item Options 
custcol
Custom Lists 
customlist
Record Types 
customrecord
Custom Transaction Types 
customtransaction
Center Categories 
custcentercategory
Center Tabs 
custcentertab8
Centers
custcenter
KPI Scorecards 
custkpiscorecard
#######
no file cabinet
############
Custom Address Entry Forms |
custform
Advanced PDF/HTML Templates 
custtmpl 
Custom Entry Forms 
custform
Transaction Form
custform
SuiteScripts
"""