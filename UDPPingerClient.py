from socket import *
import time

pings = 10
totalRtt = []
lostPacket = 0

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # Set socket timeout to 1 second

serverAddr = ('10.9.101.33', 12001)

print("\n")

for sequence_number in range(1, pings + 1): #to check if the pings 1-10
    
    Time = time.time()
    message = (f"Ping {sequence_number} {Time}").encode() 
    clientSocket.sendto(message, serverAddr) # message sent to server
    try:

        responseMessage, server = clientSocket.recvfrom(1024)
        returnTime = time.time()
        rtt = returnTime - Time #current pings's RTT time
        totalRtt.append(rtt)
        print(f"Found: {responseMessage.decode()} seconds, RTT = {rtt:.6f} seconds")

    except timeout:
        lostPacket += 1
        print(f"LOST:  PING {sequence_number} request was timed out")

clientSocket.close()


if totalRtt:
    print("\nCalculations:")
    averageRtt = sum(totalRtt) / len(totalRtt)
    print(f"\n    Minimum RTT: {min(totalRtt):.6f} seconds")
    print(f"    Maximum RTT: {max(totalRtt):.6f} seconds")
    print(f"    Average RTT: {averageRtt:.6f} seconds")
LossRate = (lostPacket / pings) * 100
print(f"    Packet Loss Rate: {LossRate:.2f}%")