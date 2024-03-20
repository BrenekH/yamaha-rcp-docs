# Yamaha Remote Control Protocol (RCP)

Unofficial documentation for Yamaha's mixer control protocol with an emphasis on the [TF Series of mixers](https://usa.yamaha.com/products/proaudio/mixers/tf/index.html).
The concepts in this documentation do apply to some of Yamaha's other mixers (notably the QL, CL, Rivage, and DM3 series), but since I only have access to a TF console, that's what this documentation is most relevant to.

> **Note:** This is a big work in progress. If you want to help out, feel free to open up a [Discussion](https://github.com/BrenekH/yamaha-rcp-docs/discussions), [Issue](https://github.com/BrenekH/yamaha-rcp-docs/issues), or [Pull Request](https://github.com/BrenekH/yamaha-rcp-docs/pulls).

## Official Sources

* [Python Script Template](https://usa.yamaha.com/files/download/other_assets/0/1266290/Python_Script_Template_V100.zip) - Simple Python scripts and PDFs that are light on details
* [MTX3, MTX5-D, MRX7-D, XMV Series, EXi8, EXo8 RCP Spec V4.0.0](https://usa.yamaha.com/files/download/other_assets/5/1343735/200330_mtx_mrx_xmv_ex_rcps_v400_rev14_en.pdf) - Yamaha docs on the protocol for their multi-zone commercial mixing system (thanks [@morydd](https://github.com/BrenekH/yamaha-rcp-docs/discussions/1))
* [RIVAGE PM Series OSC Specifications V1.0.2](https://uk.yamaha.com/files/download/other_assets/5/1407565/RIVAGE_PM_osc_specs_v102_en.pdf) - Documentation for using Open Sound Control (OSC) on Rivage PM consoles (thanks [@snurrgnu](https://github.com/BrenekH/yamaha-rcp-docs/discussions/1#discussioncomment-8644878))
* [DM3 Series OSC Specifications V1.0.0](https://fr.yamaha.com/files/download/other_assets/2/2063222/DM3_osc_specs_v100_en.pdf) - Documentation for using Open Sound Control (OSC) on DM3 consoles (thanks [@hansSchall](https://github.com/BrenekH/yamaha-rcp-docs/discussions/3))

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

### List of Command Paths

* [MIXER:Current/InCh/Fader/Level](commands/current_inch_fader_level.md)

* [MIXER:Current/InCh/Fader/On](commands/current_inch_fader_on.md)

* [MIXER:Current/InCh/Label/Color](commands/current_inch_label_color.md)

* [MIXER:Current/InCh/Label/Icon](commands/current_inch_label_icon.md)

* [MIXER:Current/InCh/Label/Category](commands/current_inch_label_category.md)

* [MIXER:Current/InCh/Label/Name](commands/current_inch_label_name.md)

* [MIXER:Current/InCh/Role](commands/current_inch_role.md)

* [MIXER:Current/InCh/ToFx/Level](commands/current_inch_tofx_level.md)

* [MIXER:Current/InCh/ToFx/On](commands/current_inch_tofx_on.md)

* [MIXER:Current/InCh/ToFx/PrePost](commands/current_inch_tofx_prepost.md)

* [MIXER:Current/InCh/ToMix/Level](commands/current_inch_tomix_level.md)

* [MIXER:Current/InCh/ToMix/On](commands/current_inch_tomix_on.md)

* [MIXER:Current/InCh/ToMix/Pan](commands/current_inch_tomix_pan.md)

* [MIXER:Current/InCh/ToMix/PrePost](commands/current_inch_tomix_prepost.md)

* [MIXER:Current/InCh/ToMono/Level](commands/current_inch_tomono_level.md)

* [MIXER:Current/InCh/ToMono/On](commands/current_inch_tomono_on.md)

* [MIXER:Current/InCh/ToSt/Pan](commands/current_inch_tost_pan.md)

* [MIXER:Current/InCh/ToStereo/Pan](commands/current_inch_tostereo_pan.md)

* [MIXER:Current/StInCh/Fader/Level](commands/current_stinch_fader_level.md)

* [MIXER:Current/StInCh/Fader/On](commands/current_stinch_fader_on.md)

* [MIXER:Current/StInCh/Label/Color](commands/current_stinch_fader_color.md)

* [MIXER:Current/StInCh/Label/Icon](commands/current_stinch_label_icon.md)

* [MIXER:Current/StInCh/Label/Category](commands/current_stinch_label_category.md)

* [MIXER:Current/StInCh/Label/Name](commands/current_stinch_label_name.md)

* [MIXER:Current/StInCh/ToFx/Level](commands/current_stinch_tofx_level.md)

* [MIXER:Current/StInCh/ToFx/On](commands/current_stinch_tofx_on.md)

* [MIXER:Current/StInCh/ToFx/PrePost](commands/current_stinch_tofx_prepost.md)

* [MIXER:Current/StInCh/ToMix/Level](commands/current_stinch_tomix_level.md)

* [MIXER:Current/StInCh/ToMix/On](commands/current_stinch_tomix_on.md)

* [MIXER:Current/StInCh/ToMix/Pan](commands/current_stinch_tomix_pan.md)

* [MIXER:Current/StInCh/ToMix/PrePost](commands/current_stinch_tomix_prepost.md)

* [MIXER:Current/StInCh/ToMono/Level](commands/current_stinch_tomono_level.md)

* [MIXER:Current/StInCh/ToMono/On](commands/current_stinch_tomono_on.md)

* [MIXER:Current/StInCh/ToSt/Pan](commands/current_stinch_tost_pan.md)

* [MIXER:Current/StInCh/ToStereo/Pan](commands/current_stinch_tostereo_pan.md)

* [MIXER:Current/FxRtnCh/Fader/Level](commands/current_fxrtnch_fader_level.md)

* [MIXER:Current/FxRtnCh/Fader/On](commands/current_fxrtnch_fader_on.md)

* [MIXER:Current/FxRtnCh/Label/Color](commands/current_fxrtnch_label_color.md)

* [MIXER:Current/FxRtnCh/Label/Icon](commands/current_fxrtnch_label_icon.md)

* [MIXER:Current/FxRtnCh/Label/Name](commands/current_fxrtnch_label_name.md)

* [MIXER:Current/FxRtnCh/ToMix/Level](commands/current_fxrtnch_tomix_level.md)

* [MIXER:Current/FxRtnCh/ToMix/On](commands/current_fxrtnch_tomix_on.md)

* [MIXER:Current/FxRtnCh/ToMix/Pan](commands/current_fxrtnch_tomix_pan.md)

* [MIXER:Current/FxRtnCh/ToMix/PrePost](commands/current_fxrtnch_tomix_prepost.md)

* [MIXER:Current/FxRtnCh/ToMono/Level](commands/current_fxrtnch_tomono_level.md)

* [MIXER:Current/FxRtnCh/ToMono/On](commands/current_fxrtnch_tomono_on.md)

* [MIXER:Current/FxRtnCh/ToSt/Pan](commands/current_fxrtnch_tost_pan.md)

* [MIXER:Current/FxRtnCh/ToStereo/Pan](commands/current_fxrtnch_tostereo_pan.md)

* [MIXER:Current/DCA/Fader/Level](commands/current_dca_fader_level.md)

* [MIXER:Current/DcaCh/Fader/Level](commands/current_dcach_fader_level.md)

* [MIXER:Current/DCA/Fader/On](commands/current_dca_fader_on.md)

* [MIXER:Current/DcaCh/Fader/On](commands/current_dcach_fader_on.md)

* [MIXER:Current/DCA/Label/Color](commands/current_dca_label_color.md)

* [MIXER:Current/DcaCh/Label/Color](commands/current_dcach_label_color.md)

* [MIXER:Current/DCA/Label/Icon](commands/current_dca_label_icon.md)

* [MIXER:Current/DcaCh/Label/Icon](commands/current_dcach_label_icon.md)

* [MIXER:Current/DCA/Label/Category](commands/current_dca_label_category.md)

* [MIXER:Current/DcaCh/Label/Category](commands/current_dcach_label_category.md)

* [MIXER:Current/DCA/Label/Name](commands/current_dca_label_name.md)

* [MIXER:Current/DcaCh/Label/Name](commands/current_dcach_label_name.md)

* [MIXER:Current/Mix/Fader/Level](commands/current_mix_fader_level.md)

* [MIXER:Current/Mix/Fader/On](commands/current_mix_fader_on.md)

* [MIXER:Current/Mix/Label/Color](commands/current_mix_label_color.md)

* [MIXER:Current/Mix/Label/Icon](commands/current_mix_label_icon.md)

* [MIXER:Current/Mix/Label/Category](commands/current_mix_label_category.md)

* [MIXER:Current/Mix/Label/Name](commands/current_mix_label_name.md)

* [MIXER:Current/Mix/ToMtrx/Level](commands/current_mix_tomtrx_level.md)

* [MIXER:Current/Mix/ToMtrx/On](commands/current_mix_tomtrx_on.md)

* [MIXER:Current/Mix/Out/Balance](commands/current_mix_out_balance.md)

* [MIXER:Current/Mix/PanLink](commands/current_mix_panlink.md)

* [MIXER:Current/Mix/Role](commands/current_mix_role.md)

* [MIXER:Current/Mtrx/Fader/Level](commands/current_mtrx_fader_level.md)

* [MIXER:Current/Mtrx/Fader/On](commands/current_mtrx_fader_on.md)

* [MIXER:Current/Mtrx/Label/Color](commands/current_mtrx_label_color.md)

* [MIXER:Current/Mtrx/Label/Icon](commands/current_mtrx_label_icon.md)

* [MIXER:Current/Mtrx/Label/Category](commands/current_mtrx_label_category.md)

* [MIXER:Current/Mtrx/Label/Name](commands/current_mtrx_label_name.md)

* [MIXER:Current/Mtrx/Role](commands/current_mtrx_role.md)

* [MIXER:Current/St/Fader/Level](commands/current_st_fader_level.md)

* [MIXER:Current/St/Fader/On](commands/current_st_fader_on.md)

* [MIXER:Current/St/Label/Color](commands/current_st_label_color.md)

* [MIXER:Current/St/Label/Icon](commands/current_st_label_icon.md)

* [MIXER:Current/St/Label/Category](commands/current_st_label_category.md)

* [MIXER:Current/St/Label/Name](commands/current_st_label_name.md)

* [MIXER:Current/St/ToMtrx/Level](commands/current_st_tomtrx_level.md)

* [MIXER:Current/St/ToMtrx/On](commands/current_st_tomtrx_on.md)

* [MIXER:Current/St/Out/Balance](commands/current_st_out_balance.md)

* [MIXER:Current/Mono/Fader/Level](commands/current_mono_fader_level.md)

* [MIXER:Current/Mono/Fader/On](commands/current_mono_fader_on.md)

* [MIXER:Current/Mono/Label/Color](commands/current_mono_label_color.md)

* [MIXER:Current/Mono/Label/Icon](commands/current_mono_label_icon.md)

* [MIXER:Current/Mono/Label/Category](commands/current_mono_label_category.md)

* [MIXER:Current/Mono/Label/Name](commands/current_mono_label_name.md)

* [MIXER:Current/Mono/ToMtrx/Level](commands/current_mono_tomtrx_level.md)

* [MIXER:Current/Mono/ToMtrx/On](commands/current_mono_tomtrx_on.md)

* [MIXER:Setup/MonitorMix/Password](commands/setup_monitormix_password.md)

* [MIXER:Current/MuteMaster/On](commands/current_mutemaster_on.md)

* [MIXER:Current/Mix/BusType](commands/current_mix_bustype.md)

* [MIXER:Current/InCh/PanMode](commands/current_inch_panmode.md)

* [MIXER:Current/StInCh/PanMode](commands/current_stinch_panmode.md)

* [MIXER:Current/FxRtnCh/PanMode](commands/current_fxrtnch_panmode.md)

* [MIXER:Current/Mix/PanMode](commands/current_mix_panmode.md)

* [MIXER:Current/St/PanMode](commands/current_st_panmode.md)

* [MIXER:Current/StInCh/Role](commands/current_stinch_role.md)

* [MIXER:Current/FxRtnCh/Role](commands/current_fxrtnch_role.md)

* [MIXER:Current/St/Role](commands/current_st_role.md)

* [MIXER:Current/FxRtnCh/Label/Category](commands/current_fxrtnch_label_category.md)

* [MIXER:Current/MuteMaster/Label/Name](commands/current_mutemaster_label_name.md)

* [ssrecall_ex](commands/ssrecall_ex.md)

## Credits

* Yamaha - For making a great mixer. Not for properly documenting it's API.
* [bitfocus/companion-module-yamaha-rcp](https://github.com/bitfocus/companion-module-yamaha-rcp) - For compiling a list of commands available
