\# SV-02 - Pixel Whisper



\## Domain

Steganography



\## Difficulty

Easy



\## Challenge File

`office\_photo.png`



\## Scenario

An Asteria Dynamics employee event photograph is suspected of containing hidden information related to Operation ShadowVault.



\## Player Task

Inspect the PNG metadata and file structure, identify the hidden payload, and recover:



\- the Stage 2 flag

\- the keyword required for Stage 3



\## Intended Technique

The PNG contains trailing text data after the normal PNG `IEND` chunk.



The intended investigation path is:



1\. Inspect the image with ExifTool or an equivalent metadata tool.

2\. Notice that trailer data exists after the PNG end marker.

3\. Inspect or extract the trailing content using tools such as ExifTool, strings, binwalk, or equivalent utilities.

4\. Recover the internal note.



\## Recovered Evidence

The hidden note contains:



\- Stage 2 flag

\- next stage name

\- Stage 3 keyword hint



\## Validation

CTFd validates the Stage 2 flag using exact-match validation.



\## Reset / Recovery

This is a static evidence file. Restore `office\_photo.png` from the clean master copy if the challenge file is modified.



\## Notes

`office\_photo\_original.png` is the clean source image used to rebuild the challenge file.

