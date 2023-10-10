# UDP-Pinger

* Sends one ping message per second using UDP to Server
* message contains The ping number and the time at which it was sent
* Server generates a random number from 1-10.
* if the number is < 4 then the message is returned from server and the time is calculated
* the diff b\w packet sent and recived back to client is one Round-Trip-Time (RTT)
* else packet is lost
* Minimum, Maximum and Average RTT is calculated along with the pakcet loss rate in %

<br>

![Image](/UDP-Pinger/Output.jpg)