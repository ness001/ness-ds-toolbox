'''like pandas split
Sub split()

Dim a As Variant

On Error Resume Next
For i = 2 To Sheet2.Range("a65536").End(xlUp).Row
a = Split(Sheet2.Range("a" & i), "-")
    Sheet2.Range("b" & i) = a(2) & "年 第" & a(3) & "周"

Next

End Sub

'''extract substring
''' example 20140808
Sub extract()
dim a as Range
Sheet1.Activate
last_row=Range("a65536").End(xlUp).Row
    For i = 2 To last_row
    a=range("a" &i)
        Range("b" & i) = DateSerial(Left(a, 4), Mid(a, 5, 2), Right(a, 2))
    Next

End Sub