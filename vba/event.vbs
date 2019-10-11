'''hightlight the row you selected
''' in worksheet or workbook
'''Private Sub Workbook_SheetSelectionChange(ByVal Sh As Object, ByVal Target As Range)
Private Sub Worksheet_SelectionChange(ByVal Target As Range)
Cells.Interior.Pattern = xlNone
Selection.EntireRow.Interior.Color = 65535
End Sub


'''automatically refresh pivot table
''' in your worksheet
Private Sub Worksheet_Activate()
ActiveWorkbook.RefreshAll
End Sub

'''backup data before saving
'''in your workbook
Private Sub Workbook_BeforeSave(ByVal SaveAsUI As Boolean, Cancel As Boolean)
file_name = Format(Now(), "yyyy-mm-dd-hhmm")
ActiveWorkbook.SaveCopyAs Filename:="D:\backup\" & file_name & ".xls"
End Sub
