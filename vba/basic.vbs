''' sheet
dim sheet as worksheet
for each sheet in sheets/worksheets
    
next
' sheet properties
sheets.Count
' select
sheets(1).select ' 1 st
sheet1.select ' name in vba project window
sheets('sheet_name).select
' add 
Sheets.Add after:=Sheets(sheets.Count), Count:=3
sheet1.name=range("a1")

'copy
Sheet1.Copy after:=Sheets(sheets.Count), Count:=3
'delete
application.DisplayAlerts =False
sheet1.delete
application.DisplayAlerts =True


''' cell
'properties
range("a1").row/column

' the last row
last_row=sheet1.range("a65535").end(xlup).row

'[c1]
'cells(3,1)
sheet1.range("c1").value=100
range("c1:f10").clearcontents
range("a1").offset(2,3)=1 ' d3=1
range("a1").resize(1,3).merge
range("c1:10").copy range("b1:10")


''' workbooks
ActiveWorkbook.Sheets(1).Range("a1") = 10
'open
Workbooks.Open ("/Users/ness001/learn/cluster/code_data/andy.xlsx")

'add
workbooks.add

'save
ActiveWorkbook.SaveAs FileName:="/Users/ness001/Downloads/abc.xlsx"

'close
ActiveWorkbook.close


''' row
range("a1").entirerow.delete`