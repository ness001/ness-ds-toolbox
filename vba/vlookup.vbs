''' search for info with id number
Sub search_info()
On Error Resume Next
Sheet1.Range("d14").ClearContents

For i = 2 To Sheets.Count
    Sheet1.Range("d14") = Application.WorksheetFunction.VLookup(Sheet1.Range("d9"), Sheets(i).Range("a:h"), 5, 0)
    Sheet1.Range("d16") = Application.WorksheetFunction.VLookup(Sheet1.Range("d9"), Sheets(i).Range("a:h"), 6, 0)
    Sheet1.Range("d18") = Application.WorksheetFunction.VLookup(Sheet1.Range("d9"), Sheets(i).Range("a:h"), 3, 0)
    Sheet1.Range("d20") = Application.WorksheetFunction.VLookup(Sheet1.Range("d9"), Sheets(i).Range("a:h"), 8, 0)
    Sheet1.Range("d22") = Sheets(i).Name
    
    If Sheet1.Range("d14") <> "" Then
        Exit For
    End If
Next
End Sub