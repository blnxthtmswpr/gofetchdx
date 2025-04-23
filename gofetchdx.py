#
# Copyright (c) 2025 blnxthtmswpr
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#
#
# gofetchdx - the sequel to gofetch, my neofetch alternative
# Based mostly on the code of gofetch, plus ChatGPT helped a little...



# importing stuff
import platform
import distro
import os
import psutil

my_system = platform.uname()

if {my_system.system} == {'Linux'}:
    my_distro = distro.name()
    if {my_distro} == {'Fedora Linux Asahi Remix'}:
        print("\n")
        print("    @             @ ")
        print("    @             @ ")
        print("\n")
        print("      @         @")
        print("       @@@@@@@@@")
        print("\n")
        print(" Hello fellow Asahi user! :3")
    else:
        # big thanks to ascii.co.uk for the ascii art
        print("\n")
        print("        _nnnn_        ")
        print("       dGGGGMMb")
        print("      @p~qp~~qMb")
        print("      M|@||@) M|")
        print("      @,----,JM|")
        print("     JS^|__,  qKL")
        print("\nCertified Linux System\n")


if {my_system.system} == {'Darwin'}:
    print("\n")
    print("     ,:,")
    print("     --")
    print(",---,,,---")
    print("|        ,")
    print("|       ( ")
    print("(___,,___,")
    print("\nCertified macOS System\n")


if {my_system.system} == {'FreeBSD'}:
    print("\n")
    print("  ```                        `")
    print(" s` `.....---.......--.```   -|")
    print(" +o   .--`          y:`      +.")
    print("  yo`:.            :o      `+-")
    print("   y/               -|`   -o|")
    print("  .-_________________::/sy+:.")
    print("\nCertified FreeBSD System\n")


# define a little something here

def get_desktop_environment():
    desktop_env = os.environ.get("XDG_CURRENT_DESKTOP")
    if not desktop_env:
        desktop_env = os.environ.get("DESKTOP_SESSION")
    if not desktop_env:
        # fallback for GNOME
        if os.environ.get("GNOME_DESKTOP_SESSION_ID"):
            desktop_env = "GNOME"
        # fallback for KDE
        elif os.environ.get("KDE_FULL_SESSION"):
            desktop_env = "KDE"
    return desktop_env or "Unknown"


# getting system info
print(f"\nSystem: {my_system.system}")
print(f"Release: {my_system.release}")
print(f"System Version: {my_system.version}")
if {my_system.system} == {'Linux'}:
    print("Distro:", distro.name(), distro.version())
if {my_system.system} == {'Linux'}:
    print("DE: ", get_desktop_environment())
print(f"PC Name: {my_system.node}")
print(f"Processor: {my_system.processor}")

