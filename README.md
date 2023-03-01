# Yamaha Remote Control Protocol (RCP)

Unofficial documentation for Yamaha's mixer control protocol with an emphasis on the [TF Series of mixers](https://usa.yamaha.com/products/proaudio/mixers/tf/index.html).

## Basics

Yamaha uses a simple TCP connection to transfer all of the data between the client and the mixer.
The data is split into messages that are delimited by a newline (`\n`).
Each message starts with one of the following command keywords:

Client to Mixer:
 * `get` - Request a value from the mixer
 * `set` - Set a value on the mixer

Mixer to Client:
 * `OK` - Indicates that the client's request was accepted
 * `OKm` - The difference between this keyword and `OK` is theorized as an indicator of a modified value, but that hasn't been confirmed yet
 * `NOTIFY` - Unsolicited message from the mixer indicating a change was made outside of the current connection
 * `ERROR` - Indicates an error with the client's request
