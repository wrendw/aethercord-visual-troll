import os
import ctypes
import dearpygui.dearpygui as dpg

os.system('')

ctypes.windll.kernel32.SetConsoleTitleW("com.squirrel.Discord.Discord")

ascii_art = r"""
   _____          __  .__                                         .___
  /  _  \   _____/  |_|  |__   ___________   ____  ___________  __| _/
 /  /_\  \_/ __ \   __\  |  \_/ __ \_  __ \_/ ___\/  _ \_  __ \/ __ |
/    |    \  ___/|  | |   Y  \  ___/|  | \/\  \__(  <_> )  | \/ /_/ |
\____|__  /\___  >__| |___|  /\___  >__|    \___  >____/|__|  \____ |
        \/     \/          \/     \/            \/                 \/
Build x64
Created by Cypher (wcypher on discord) | https://github.com/LOOF-sys
discord:
"""

green_text = "\033[92m"  
reset_text = "\033[0m"    

print(green_text + ascii_art + reset_text)

dpg.create_context()

with dpg.window(label="v1.92.2 PUBLIC - Created by Cypher (wcypher on discord) | https://github.com/LOOF-sys", 
                width=795, height=600, no_close=True, no_resize=True):

    with dpg.tab_bar():
        with dpg.tab(label="Core State"):
            dpg.add_text("Build Type: RELEASE", color=(0, 255, 0))
            dpg.add_text("Supported Node Versions: (Dynamic Versions)", color=(255, 255, 255))
            dpg.add_text("VoiceNode: Valid", color=(0, 255, 0))
            dpg.add_text("Hooks: Success", color=(0, 255, 0))
            dpg.add_checkbox(label="Toggle Console Window", default_value=True)

        with dpg.tab(label="Encoder"):
            dpg.add_text("Encoder Configuration", color=(255, 255, 255))
            dpg.add_slider_float(label="vUnits", default_value=1.000, min_value=0.000, max_value=10.0, width=600)
            dpg.add_slider_float(label="Exploit dB", default_value=1.000, min_value=0.000, max_value=69.280, width=600)
            dpg.add_slider_int(label="Bitrate", default_value=64000, min_value=16000, max_value=128000, width=600)
            dpg.add_checkbox(label="Encoder Information")
            dpg.add_checkbox(label="Enable VBR", default_value=True)
            dpg.add_checkbox(label="CELT Mode", default_value=True)
            dpg.add_checkbox(label="Bitrate Locked", default_value=True)
            dpg.add_checkbox(label="Voice Encoder")
            dpg.add_checkbox(label="Discord Encoder")
            dpg.add_checkbox(label="Close Packet Line")

        with dpg.tab(label="Decoder"):
            dpg.add_text("Decoder Configuration", color=(255, 255, 255))
            dpg.add_checkbox(label="Decoder Information")
            dpg.add_checkbox(label="Descriptive Decoder")
            dpg.add_checkbox(label="Disable Float Decoder")
            dpg.add_checkbox(label="Packet Information")
            dpg.add_checkbox(label="Check For Priority Speaker")
            dpg.add_checkbox(label="Disable Limiter usage")
            dpg.add_spacer(height=10)
            dpg.add_text("Specify User Decoder", color=(255, 255, 255))
            dpg.add_slider_int(label="Index", default_value=0, min_value=0, max_value=100, width=600)
            dpg.add_button(label="Clear User Decoder Instances", width=200)
            dpg.add_checkbox(label="Isolate User Sound")
            dpg.add_spacer(height=10)
            dpg.add_text("Tamper User Volume", color=(255, 255, 255))
            dpg.add_slider_float(label="dB", default_value=0.00, min_value=-100.00, max_value=100.00, width=600)
            
        with dpg.tab(label="Debugger"):
            dpg.add_button(label="Show Debug Info", width=110)
            
        with dpg.tab(label="Audio"):
            dpg.add_text("These features are deprecated and should not be used", color=(255, 0, 0))
            dpg.add_text("Stereo Diff", color=(255, 255, 255))
            dpg.add_slider_float(label="%", default_value=0.000, min_value=-0.000, max_value=1000.000, width=600)
            dpg.add_checkbox(label="L/R", default_value=True)
            dpg.add_spacer(height=10)
            dpg.add_text("Stereo Delay", color=(255, 255, 255))
            dpg.add_slider_int(label="FS", default_value=0, min_value=0, max_value=500, width=600)
            dpg.add_checkbox(label="L/R", default_value=True)
            dpg.add_spacer(height=10)
            dpg.add_checkbox(label="Bass Expander")
            dpg.add_slider_float(label="BX Threshold", default_value=2.000, min_value=-0.000, max_value=1000.000, width=600)
            dpg.add_slider_float(label="BX Minimum", default_value=0.500, min_value=-0.000, max_value=1000.000, width=600)
            
        with dpg.tab(label="History"):
            dpg.add_text("Developer: Cypher (wcypher) -> Aethercord was created in May of 2024", color=(0, 255, 0))
            dpg.add_text("1st User: Morty (doom8648) -> Started using around August of 2024", color=(255, 255, 255))
            dpg.add_text("2nd User: CZ V2 (knowntemptation) -> Started using around August of 2024", color=(255, 255, 255))
            dpg.add_text("3rd User: Ascend/Lucifer (ncjxzkjcnjwfnew) -> Started using around August of 2024", color=(255, 255, 255))
            dpg.add_text("4th User: Yurei (oracledsc) -> Started using around September of 2024", color=(255, 255, 255))
            dpg.add_text("All other users are buyers or after its free -> September 27th•", color=(255, 255, 255))
            
        with dpg.tab(label="Local User"):
            dpg.add_input_text(label="Token changer (disabled)", width=400)
            dpg.add_button(label="Reload Token", width=110)

        with dpg.tab(label="Lua"):
            dpg.add_button(label="Execute", width=100)
            dpg.add_spacer(height=10)
            dpg.add_input_text(tag="lua_editor", label="--- Editor", multiline=True, width=770, height=500)

dpg.create_viewport(title="Aethercord", width=797, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()