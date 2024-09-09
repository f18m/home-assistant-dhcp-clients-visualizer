from dhcp_leases import Lease, DhcpLeases

leases = DhcpLeases('/usr/share/hassio/addons/data/core_dhcp_server/dhcpd.lease')
leases.get()  # Returns the leases as a list of Lease objects
leases.get_current()  # Returns only the currently valid dhcp leases as dict
                      # The key of the dict is the device mac address and the
                      # Value is a Lease object

for mac in leases.get_current():
    print(mac)
