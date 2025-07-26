import time
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL, GUID
from comtypes.client import CreateObject
from pycaw.pycaw import AudioUtilities
from pycaw.api.mmdeviceapi import IMMDeviceEnumerator

running = True

CLSID_MMDeviceEnumerator = GUID('{BCDE0395-E52F-467C-8E3D-C4579291692E}')
PKEY_Device_FriendlyName = GUID('{a45c254e-df1c-4efd-8020-67d146a850e0}')

def get_default_audio_device_name():
    enumerator = CreateObject(CLSID_MMDeviceEnumerator, interface=IMMDeviceEnumerator)
    device = enumerator.GetDefaultAudioEndpoint(0, 1)  # eRender, eMultimedia
    props = device.OpenPropertyStore(0)
    count = props.GetCount()

    for i in range(count):
        key = props.GetAt(i)
        prop = props.GetValue(key)
        if (key.fmtid == PKEY_Device_FriendlyName and key.pid == 14):
            return prop.GetValue()
    return "Unknown Device"


def set_arc_volume(percent):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        process = session.Process
        if process and "Arc" in process.name():
            volume.SetMasterVolume(percent / 100, None)


def monitor():
    last_device = None
    while True:
        current_device = get_default_audio_device_name()
        if current_device != last_device:
            last_device = current_device

        if "Earphones" in current_device:
            set_arc_volume(15)
        elif "Speaker" in current_device:
            set_arc_volume(60)
        else:
            set_arc_volume(40)

        time.sleep(5)


if __name__ == "__main__":
    monitor()
