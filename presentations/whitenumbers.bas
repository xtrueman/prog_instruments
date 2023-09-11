Attribute VB_Name = "Module1"
Sub WhiteNumbers()
  Dim sld As Slide
  Dim shp As Shape
  Set sld = Application.ActiveWindow.View.Slide
  
  Set shp = sld.Shapes(3)

'Debug.Print "123"

  With shp.TextFrame.TextRange
    'For x = 1 To .Runs.Count
    For x = 1 To .Words.Count
       Set word = .Words(x)
       If IsNumeric(word) Then
         word.Font.Color.RGB = RGB(255, 255, 255)
       End If
    Next x
  End With
End Sub
