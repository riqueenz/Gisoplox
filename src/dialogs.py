import wx
import Auxiliares
from translate import translate


def saved_successfully(unit_weight, total_weight, cutting_distance, folder):
    message = translate("Your code has been successfully generated!")+"\n\n"
    message += translate("Unit Weight")+": " + Auxiliares.pesoString(unit_weight)
    message += "\n"+translate("Total weight")+": " + Auxiliares.pesoString(total_weight)
    message += "\n"+translate("Cutting distance")+": " + Auxiliares.converterDist(cutting_distance)
    message += "\n"+translate("Note: Weight for steel parts")
    message += "\n\n"+translate("The G-code is in this folder")+":\n " + folder
    dlg = wx.MessageDialog(parent=None, message=message, caption=translate("Saved code"), style=wx.OK | wx.ICON_INFORMATION)
    dlg.ShowModal()
    dlg.Destroy()
