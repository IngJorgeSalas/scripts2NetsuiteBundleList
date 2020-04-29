# scripts2NetsuiteBundleList
when working with large projects in netsuite, tracking the items to put in a bundle becomes complicated, this software creates a bundle list from a bunch of scripts

only searches for fields records and scripts
it goes through subfolders
# Instructions
1. is recommended copy the scripts to analyze to a new folder.
2. put the exe file on the folder with the scripts
3.(optional) to add the name/description to the output file, export the list of fields and records from netsuite and add them to the folder, the file name must follow the next rules

Crm Fields = CustomCRMFields#.csv
Entity Fields = CustomEntityFields#.csv
Item Fields = CustomItemFields#.csv
Item Number Fields = CustomItemNumberFields#.csv
Other Record Fields = OtherRecordFields#.csv
Other Sublist Fields = OtherSublistFields#.csv
Transaction Body Fields = TransactionBodyFields#.csv
Transaction Line Fields = TransactionLineFields#.csv
Item Options Fields = ItemOptionsFields#.csv
records = RecordTypes#.csv
transactions = CustomTransactionTypes#.csv
Suite Scripts = scriptSearch4BundlerListResults#.csv

there are some list that natively can’t be exported, as record types, to export them the next button can be injected, only is needed change the url from appendFormDataToURL to the desired one. After push the button the list will be downloaded
<input type='button' style='' class='rndbuttoninpt bntBgT' value='Export - CSV' id='export' name='export' onclick='document.forms['footer_actions_form'].elements.csv.value='Export';document.forms['footer_actions_form'].elements.OfficeXML.value='F';document.location.replace(appendFormDataToURL('/app/common/custom/custrecords.csv')); document.forms['footer_actions_form'].elements.csv.value='HTML'; ; return false;' onmousedown='this.setAttribute('_mousedown','T'); setButtonDown(true, false, this);' onmouseup='this.setAttribute('_mousedown','F'); setButtonDown(false, false, this);' onmouseout='if(this.getAttribute('_mousedown')=='T') setButtonDown(false, false, this);' onmouseover='if(this.getAttribute('_mousedown')=='T') setButtonDown(true, false, this);' _mousedown='F'>

to export the list of scripts is necessary use a saved search without filters and with the columns Name, Script Type and Script File in that order

4. execute the exe

[img]ad[/img]
