from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import playsound
import time

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def volume_one():
    volume.SetMasterVolumeLevel(-55.0, None) #1%
    playsound.playsound("filepath")
def volume_two():
    volume.SetMasterVolumeLevel(-33.0, None) #10%
    playsound.playsound("filepath")
def volume_three():
    volume.SetMasterVolumeLevel(-24.0, None) #20%
    playsound.playsound("filepath")
def volume_four():
    volume.SetMasterVolumeLevel(-18.0, None) #30%
    playsound.playsound("filepath")
def volume_five():
    volume.SetMasterVolumeLevel(-14.0, None) #40%
    playsound.playsound("filepath")
def volume_six():
    volume.SetMasterVolumeLevel(-10.0, None) #50%

