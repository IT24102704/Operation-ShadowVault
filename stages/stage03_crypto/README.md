\# Stage 03 - Cipher Relay



\## Challenge ID

SV-03



\## Domain

Cryptography



\## Difficulty

Moderate



\## Scenario

Players receive an encoded relay export from Asteria Dynamics.



The relay content uses two layers:



1\. Base64 encoding

2\. Vigenere cipher



The Vigenere key is recovered from the previous stage.



\## Player Objective

Decode the relay message, recover the Stage 3 flag, and identify the indicator required for Stage 4.



\## Intended Investigation Path

1\. Open `cipher\_relay.txt`.

2\. Identify that the outer layer is Base64.

3\. Decode the Base64 content.

4\. Recognize that the decoded message is still encrypted.

5\. Use the key recovered from Stage 2.

6\. Apply the Vigenere cipher using the key `NIGHTFALL`.

7\. Recover the plaintext relay message.



\## Expected Plaintext

The decrypted relay message reveals:



\- Stage 3 flag

\- Stage 4 indicator



\## Flag

`SHADOW{relay\_layers\_unlocked}`



\## Stage 4 Indicator

`archive-gw.asteria.local`



\## Required Key

`NIGHTFALL`



\## Challenge Asset

`cipher\_relay.txt`



\## Skills Demonstrated

\- Identifying encoding vs encryption

\- Base64 decoding

\- Vigenere cipher decryption

\- Using information recovered from a previous challenge stage



\## Isolation

All data, hostnames, messages, and infrastructure references are synthetic and created specifically for the Operation ShadowVault training environment.

