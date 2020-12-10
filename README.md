# Network Programming

## Intro

This laboratory implements an simple echo server that uses custom communication protocol built on UDP. It has __error checking__ and __data encryption__.

## Error Checking

Error checking is implemented by sending checksum along with data and, on receiver, hashing the data and checking if it corresponds with checksum. Here can be should retransmission, because yeah, there is no many use in error checking without retransmission.

## Data Encryption

For data encryption here is used Diffie–Hellman key exchange in order to compute an public key on both participant. Then with
Vigenère cipher and computed key the whole payload is encoded and sent.
