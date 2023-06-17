# Yamaha Remote Control Protocol (RCP)

Unofficial documentation for Yamaha's mixer control protocol with an emphasis on the [TF Series of mixers](https://usa.yamaha.com/products/proaudio/mixers/tf/index.html).

> **Note:** This is a big work in progress. If you want to help out, feel free to open up a [Discussion](https://github.com/BrenekH/yamaha-rcp-docs/discussions), [Issue](https://github.com/BrenekH/yamaha-rcp-docs/issues), or [Pull Request](https://github.com/BrenekH/yamaha-rcp-docs/pulls).

## Official Sources

 * [Python Script Template](https://usa.yamaha.com/files/download/other_assets/0/1266290/Python_Script_Template_V100.zip) - Simple Python scripts and PDFs that are light on details

## Basics

Yamaha uses a simple TCP connection to transfer all of the data between the client and the mixer.
The data is split into messages that are delimited by a newline character (`\n`).
Each message starts with one of the following command keywords:

Client to Mixer:
 * `get` - Request a value from the mixer
 * `set` - Set a value on the mixer
 * `ssrecall_ex` - Recall a scene to the mixer

Mixer to Client:
 * `OK` - Indicates that the client's request was accepted
 * `OKm` - The difference between this keyword and `OK` is likely to be an indication of a modified value, but this has not yet been confirmed
 * `NOTIFY` - Unsolicited message from the mixer indicating a change was made outside of the current connection
 * `ERROR` - Indicates an error with the client's request

### Data Types

 * Strings
   * Represented by a variable length of characters surrounded by quotation marks (`"`)
 * Decibels
   * Represented by an integer where the dB value has been multiplied by 100 (`10 dB` -> `1000`)
   * Max Fader Value: 1000
   * Min Fader Value: -13800
   * Negative Infinity Value: -32768
 * Booleans
   * Represented by either a `0` or `1`, `0` for false and `1` for true

### Getting and Setting Values

Getting and setting simple values uses essentially the same syntax.
The only difference is really that a `get` command doesn't contain a value on the end while `set` does.

Here's some basic examples:
 * Channel 1 Fader Values:
   * `get MIXER:Current/InCh/Fader/Level 0 0`
   * `set MIXER:Current/InCh/Fader/Level 0 0 1000`

 * Channel 16 Fader Label:
   * `get MIXER:Current/InCh/Fader/Name 15 0`
   * `set MIXER:Current/InCh/Fader/Name 15 0 "My Label"`

## Credits

 * Yamaha - For making a great mixer. Not for properly documenting it's API.
 * [bitfocus/companion-module-yamaha-rcp](https://github.com/bitfocus/companion-module-yamaha-rcp) - For compiling a list of commands available
