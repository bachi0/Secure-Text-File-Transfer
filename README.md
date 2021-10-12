# Secure-Text-File-Transfer
Secure Text File Transfer using Diffie Hellman Key Exchange and AES Algorithm.

# Diffie Hellman Key Exchange

One of the simplest ways for safe transfer is for user A to encrypt the data using a key, which is then shared with user B. This technique can work to some extent, but there is always the possibility of third-party eavesdropping. We wanted a system in which two users could independently create the identical key at both ends without knowing the secret key. This key might be used to encrypt and decode the text in the future. The diffie-hellman key exchange algorithm is used.

Diffie–Hellman key exchange is a technique of securely transferring cryptographic keys over a public channel that was invented by Ralph Merkle and named after Whitfield Diffie and Martin Hellman.  DH was one of the first practical examples of public key exchange in the world of cryptography. Diffie–Hellman key exchange creates a shared secret between two parties that can be used for secret communication and data exchange over a public network. 


An analogy that uses colors instead of very big numbers to demonstrate the notion of public key exchange:

* The procedure begins with the two parties, Alice and Bob, publicly agreeing on an arbitrary beginning color that is not required to be kept secret (but should be different every time).The color used in this example is yellow.<br>
* In addition, each individual chooses a secret color that they keep to themselves — in this example, red and blue-green.<br>
* The key element of the procedure is that Alice and Bob combine their respective secret colors with their mutually shared colors, resulting in orange-tan and light-blue mixes, and then publicly exchange the two mixed colors.<br>
* Finally, they each combine the color they got from their spouse with their own personal color. As a result, the final color mixture (yellow-brown in this example) is identical to the final color mixture of the partner.<br>
* If a third party were to listen in on the conversation, it would only know the common color (yellow) and the first blended colors (orange-tan and light-blue), but determining the ultimate secret color would be tough (yellow-brown).<br>
* To return to the analogy of a real-life trade using huge numbers rather than colors, this determination is computationally costly. Even with today's supercomputers, it is difficult to calculate in a reasonable period of time.


### Pre-requisites 
```

python-flask
hashlib
pycrypto
secretsharing
tkinter
webbrowser

```

## Source Code Explanation

In this project, the private and public keys of both users are created at random from a 600-digit prime integer. The created public keys are shared to both users, and the secret key is computed. The AES Ciphering Algorithm will next be used to encrypt and decrypt the text-containing file.


**DH.py**: This file is about creating keys using diffie-hellman. It creates three keys: a private key, a public key, and a secret key (used for encryption and decryption)<br>
**ENCDEC.py**: This file is used for AES algorithm encryption and decryption.<br>
**connection.py**: This file serves as a bridge between the main application and the other code files.<br>
**main.py**: This file is concerned with the graphical user interface. It is the primary file.<br>


If you have any more questions, please contact us at **udayakiran.ns@gmail.com** or **charanreddysai234@gmail.com**
