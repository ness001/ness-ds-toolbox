''' diable automation of function calculation
application.calculation =xlCalculationManual
' your code
'range("a1:b1").calculate
application.calculation=xlCalculationAutomatic


''' disable screen updating
application.screenupdating= FALSE
' your code
application.screenupdating=True


'''disable alerts
application.DisplayAlerts =False
'sheet1.delete
application.DisplayAlerts =True


''' use batch assignment rather than cell by cell
dim X() as Variant
x=sheet1.range("c1:c10").value
sheet.range("b1:b10").value=x
