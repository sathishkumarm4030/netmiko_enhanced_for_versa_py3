#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

device = {
    "ip": "10.91.127.194",
    "username": "Automated",
    "password": "Auto@12345",
    "device_type": "versa",
}

device2 = {
    "ip": "10.91.240.11",
    "username": "admin",
    "password": "versa123",
    "device_type": "versa",
}

commands = "move devices device CPE11-HKG-HYBRD-IPC00190 config orgs org-services IPC00190 class-of-service qos-policies Default-Policy rules LAN1-VRF-Internet-Default jkjkjk"

cmd2 = "show orgs org IPC00190 sessions sdwan detail | nomore| select source-port 2000"
net_connect = Netmiko(**device2)

print()
print(net_connect.find_prompt())
# print(net_connect.config_mode(config_command="configure private"))
# print(net_connect.check_config_mode())
# output = net_connect.send_config_set(commands, exit_config_mode=True, cmd_verify=False)
# output = net_connect.send_command_expect(commands, expect_string='%', strip_prompt=False, strip_command=False, cmd_verify=True)
# print(output)
# output += net_connect.commit(and_quit=True)
output = net_connect.send_command_expect(cmd2, expect_string='>', strip_prompt=True)
print(net_connect.global_cmd_verify)
print(output)
# print(net_connect.exit_config_mode())
# print(net_connect.check_config_mode())
# print(output)
print(net_connect.find_prompt())
net_connect.disconnect()
