<img align="right" padding-top="100%" height="100"  src="./resources/Feather for ESSE.svg" >

# Mystiko-Minyma


## Image Steganography Service


### Steganography
Steganography is the practice of concealing a message within another message or a physical object. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video. The word steganography comes from Greek steganographia, which combines the words steganós, meaning "covered or concealed", and -graphia meaning "writing".

## what is mystiko-minyma?
The words mystiko-minyma are derived from the Greek words mystiko (meaning "secret") and minyma (meaning "message"). The word mystiko-minyma is a combination of the two words, which means "secret message".

## what is the purpose of mystiko-minyma?
The purpose of mystiko-minyma is to provide a service that allows users to hide messages within images.

## How does mystiko-minyma work?
The service is based on the idea that a message can be hidden within an image. The message is firstly encoded using a user given key. The encoded message is hidden within the image using a technique called "Least Siginificant Bit (LSB) manipulation". This encoding is done using the technique of "bitwise XOR" (exclusive or). The pixels of the image are then manipulated to hide the encoded message.

## The LSB technique
In Steganography, The most well known techniques to data hiding in images are least significant bit (LSB) substitution, and masking & filtering techniques. LSB is a simple approach to embedding information in an image. But image manipulation can destroy the hidden information in this image.
<br>
More about LSB technique: [LSB Manipulation in Steganography](https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372)

# GUI for Mystiko-Minyma
GUI for the service is provided in the form of application. This was developed using TKinter python library.

The GUI is divided into two tabs.
- The first tab is for encoding (```akoúo```)
<br>
Akoúo translates to `to tell` in Greek.
<br>

- The second tab is for decoding (`légo`) 
<br>
légo translates to `to listen` in Greek.

## How to use the GUI?
### Encoding
- Step 1: Select the image file to be encoded, using the ```Open File``` button. Supported files are PNG(*.png), JPEG(*.jpg) and JEPG(*.jpeg).
- Step 2: Enter the message to be encoded, using the ```Message``` text box(First text box).
- Step 3: Enter the key to be used for encoding, using the ```Key``` text box(Second text box).
- Step 4: Click the ```Let's Tell``` button to start encoding. This opens a new window of file explorer to save the encoded image.
<br>
*Note: The encoded image is saved can only be saved as PNG(*.png) file because of compression in other file formats at save.*
- Step 5: Click the button which has 28 character key which is used for encoding the message to copy the key to the clipboard.
<br>
_This completes the encoding process._
### Decoding
- Step 1: Select the image file to be decoded, using the ```Open File``` button. Supported files are PNG(*.png).
- Step 2: Enter the previously generated 28 Character key to be used for decoding, using the ```Gernerated Key``` text box(First text box).
- Step 3: Enter the user key to be used for decoding, using the ```User Key``` text box(Second text box).
- Step 4: Click the ```Let's Listen``` button to start decoding. If the decryption is successful, the decoded message is displayed in the ```Message``` Button. Which on click copies the message to the clipboard.
<br>
_This completes the decoding process._

# CLI for Mystiko-Minyma
The CLI for the service is provided in the form of application. This was developed using Python 3.7.

## How to use the CLI?
### Encoding
```shell
$ mystiko-minyma [-t] -i {image_file} -m {message} -b {base} -o {output_file}
```
### arguments
Flag | Description
-----|------------
`-t`  `--tell`| Encode the message in the image.
`-i`  `--input`| The image file to be encoded.
`-m` `--message`| The message to be encoded.

### Optional Arguments

Flag | Default | Description
-----------|----------------|------------
`-b`  `--base` | `GodOfMischief` | The base user key to be used for encoding.
`-o`  `--output` | `minyma.png` | The output file to be encoded.

### Example
```shell 
$ mystiko-minyma -t -i image.png -m "I Love you 3000 <3" -b IamIRONMAN -o Morgan_stark.png
 ```

### Decoding 
```shell
$ mystiko-minyma [-l] -i {image_file} -k {key} -b {base} -o {output_file}
```
### arguments
Flag | Description
-----|------------
`-l`  `--listen`| Decode the message in the image.
`-i`  `--input`| The image file to be decoded.
`-k` `--key`| The key to be used for decoding.

### Optional Argument
Flag | Default | Description
-----------|----------------|------------
`-b`  `--base` | `GodOfMischief` | The base user key to be used for decoding.

### Example
```shell
$ mystiko-minyma -l -i Morgan_stark.png -k 230th4MkUKLirC44cXQBcfSakLaH -b IamIRONMAN
```

### Other Arguments
Flag | Description
-----|------------
`-h`  `--help`| Prints the help message.
`-v`  `--version`| Prints the version of the application.


## Contact
lokeshtejavath@yahoo.com

## Authors
[Lokesh Tejavath](https://github.com/lokeshtejavath)

[Abhiram Nallama](https://github.com/Abhiram8910)

[Waseem Syed](https://github.com/sw2812)

[Indira Nandepu](https://github.com/CloverX4)
