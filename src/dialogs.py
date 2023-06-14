import wx
import Auxiliares


def saved_successfully(unit_weight, total_weight, cutting_distance, folder):
    message = "Your code has been successfully generated!\n\n"
    message += "Unit Weight: " + Auxiliares.pesoString(unit_weight)
    message += "\nTotal weight: " + Auxiliares.pesoString(total_weight)
    message += "\nCutting distance: " + Auxiliares.converterDist(cutting_distance)
    message += "\nNote: Weight for steel parts"
    message += "\n\nThe G-code is in this folder:\n " + folder
    dlg = wx.MessageDialog(parent=None, message=message, caption="Saved code", style=wx.OK | wx.ICON_INFORMATION)
    dlg.ShowModal()
    dlg.Destroy()
