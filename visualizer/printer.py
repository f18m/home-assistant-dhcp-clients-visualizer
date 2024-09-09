from dhcp_leases import Lease, DhcpLeases

leases = DhcpLeases('/usr/share/hassio/addons/data/core_dhcp_server/dhcpd.lease')
curr = leases.get_current()  # Returns only the currently valid dhcp leases as dict
                      # The key of the dict is the device mac address and the
                      # Value is a Lease object

print("Current DHCP clients:")
for mac in curr:
    x = curr[mac]
    print(f"{x.ip} ({x.mac}), hostname={x.hostname}")
