Sub merge_sheets()

Dim end_sheet_num, i, sheet_last_row, summary_last_row, last_col_num As Integer
Dim table As Worksheet
Dim flag As Integer
flag = 0
Dim end_col_num As String
Dim start_sheet_num As Integer


start_sheet_num = InputBox("input starting sheet number! example:2")
end_col_letter = InputBox("input column boundary letter! example:f")
if isnumeric(start_sheet_num)=False or (start_sheet_num<1) Then
    exit Sub
end If

if isstring(end_col_letter)=False Then
    exit Sub
end If

''' create summary table
'''if flag=1 summary table exits
For Each table In Sheets
If table.Name = "summary" Then
flag = 1
End If
Next

If flag = 0 Then
Sheets.Add after:=Sheets(Sheets.Count), Count:=1
Sheets(Sheets.Count).Name = "summary"
Else
Sheets("summary").Range("a1:iv65536").ClearContents
End If

end_sheet_num = Sheets.Count

'''start merging data
'''copy fields

Sheets(start_sheet_num).Range("a1:" & end_col_letter & "1").Copy Sheets(end_sheet_num).Range("a1")

For i = start_sheet_num To end_sheet_num - 1

sheet_last_row = Sheets(i).Range("a65536").End(xlUp).Row

summary_last_row = Sheets(end_sheet_num).Range("a65536").End(xlUp).Row + 1

Sheets(i).Range("a2:" & end_col_letter & sheet_last_row).Copy Sheets(end_sheet_num).Range("a" & summary_last_row)

Next



End Sub

