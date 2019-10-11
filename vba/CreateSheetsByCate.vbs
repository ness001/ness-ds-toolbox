Sub create_sheets()
Dim i, flag, last_row As Integer
Dim sheet As Worksheet
Dim filter_col As Integer


filter_col = InputBox("input filter column number! example:4")

if isnumeric(filter_col) =False Then
    exit Sub
end If

Application.DisplayAlerts = False
'''that's why you need for each not for i=xxx
For Each sheet In Sheets
    If sheet.Name <> Sheet1.Name Then
        sheet.Delete
    End If
Next

Application.DisplayAlerts = True

last_row = Sheet1.Range("a65536").End(xlUp).Row
'''create sheets, make flag=1 as the sheet already exists
For i = 2 To last_row
    flag = 0
    For Each sheet In Sheets
        If Cells(i, filter_col) = sheet.Name Then
            flag = 1
        End If
    Next
    
    If flag = 0 Then
        Sheets.Add after:=Sheets(Sheets.Count)
        Sheet1.Activate
        Sheets(Sheets.Count).Name = Cells(i, filter_col)
    End If
Next

'''copy the filtered data to newly created sheets
For i = 2 To Sheets.Count
    Sheet1.Range("a1:f" & last_row).AutoFilter field:=filter_col, Criteria1:=Sheets(i).Name
    Sheet1.Range("a1:f" & last_row).Copy Sheets(i).Range("a1")
Next

Sheet1.Range("a1:f" & last_row).AutoFilter

MsgBox ("Misson completed!")

End Sub
