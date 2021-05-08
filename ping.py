from pythonping import ping

def my_ping(ip_addr='8.8.8.8'):
    network_status = True
    response_list = ping(ip_addr)

    if response_list.packet_loss == 1.0:
        network_status = False
    return network_status

def check_network():
    ip_addr1 = '8.8.8.8'
    ip_addr2 = '223.5.5.5'
    
    result1 = my_ping(ip_addr1)
    result2 = my_ping(ip_addr2)

    Status = False

    if (result1 is True) and (result2 is True):
        Status = True

    return Status


if __name__ == '__main__':
    check_network()
