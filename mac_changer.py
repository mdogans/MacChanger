import optparse
import subprocess
import re
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="New MAC address!")
    return parse_object.parse_args()
def change_mac(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not obtain MAC Address.")
        return None
def main():
    print("MAC Changer started.")
    (user_input, arguments) = get_user_input()

    current_mac = get_current_mac(user_input.interface)
    print(f"Current MAC Address: {current_mac}")

    change_mac(user_input.interface, user_input.mac_address)

    new_mac = get_current_mac(user_input.interface)

    if new_mac == user_input.mac_address:
        print(f"The MAC address for interface {user_input.interface} has been successfully changed to {user_input.mac_address}.")
    else:
        print("Could not change MAC Address.")


if __name__ == "__main__":
    main()
