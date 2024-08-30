import scapy.all as scapy

def scan_network(ip_range, timeout=5, retries=5):
    devices = []
    for _ in range(retries):
        arp_request = scapy.ARP(pdst=ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=timeout, verbose=False)[0]
        
        for element in answered_list:
            device = {
                'ip': element[1].psrc,
                'mac': element[1].hwsrc
            }
            if device not in devices:
                devices.append(device)
    return devices

def scan_multiple_subnets(subnets):
    all_devices = []
    for subnet in subnets:
        print(f"Scanning subnet: {subnet}")
        devices = scan_network(subnet)
        all_devices.extend(devices)
    
    return all_devices

def mark_attendance(connected_devices, student_devices):
    attendance = {}
    for student, mac in student_devices.items():
        attendance[student] = 'Present' if mac in connected_devices else 'Absent'
    return attendance

def main():
    subnets = [
        "172.20.7.0/24", 
        "172.20.1.0/24", 
        "172.20.13.0/24", 
        "172.20.15.0/24"
    ]  # Add more subnets if needed
    connected_devices = scan_multiple_subnets(subnets)

    print("\nConnected devices across subnets:")
    for device in connected_devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")

    # Replace with actual MAC addresses of student devices
    student_devices = {
        'Your Device': 'ba:07:29:e8:c7:f0',
        'student 1' : '4e:27:f6:83:67:ea'
        # Add more student devices here
    }

    connected_mac_addresses = [device['mac'] for device in connected_devices]
    attendance = mark_attendance(connected_mac_addresses, student_devices)

    print("\nAttendance Report:")
    for student, status in attendance.items():
        print(f"{student}: {status}")

if __name__ == "__main__":
    main()
