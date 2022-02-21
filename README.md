
# VSCode Intellisense For Your Mbed Projects

`mbed-vscode-tools` is made for software engineers who want to develop their mbed projects in vscode instead of mbed studio.
The tool offers a commandline interface to generate and update your c_cpp_properties.json for correct vscode intellisense.

## Notes

* This tool works in conjunction with the official cli tool (`mbed-tools`) provided by the mbed team.
* We assume that the reader knows how to use mbed-tools and its workflow; otherwise see [the official docs](https://os.mbed.com/docs/mbed-os/v6.15/build-tools/use.html). 

## Dependencies

Python interpreter:

* python >= 3.6.0 (f strings are used in the source)

Python packages:

* click >= 8.0.0

Other softwares:

* mbed-tools >= 7.0.0
* arm-none-eabi-gcc >= 9.0.0 or armcc >= 6.0.0
* cmake >= 3.19.0
* ninja >= 1.0.0

## Installation

```bash
$ pip install mbed-vscode-tools
```

Run `$ pip uninstall mbed-vscode-tools` to uninstall mbed-vscode-tools.

## Quick Start

## Usage

The mbed-vscode-tools the following three commands: `configure`, `generate`, and `update`.

See the documantion below for details of each command.

### `configure`

Configure the build settings.

```
$ mbed-vscode-tools configure MBED_TOOLCHAIN MBED_TARGET VSCODE_CONF_FILE [--mbed-profile [debug|develop|release]] [--mbed-program-dir directory] [--help]
```

**Positional Arguments**

* `MBED_TOOL_CHAIN`  
  Select \"GCC_ARM\" or "ARM". Set \"GCC_ARM\" if you use the gnu arm embedded toolchain (arm-none-eabi-gcc). Set \"ARM\" if you use the arm compiler (armcc). Note that armcc is a paid compiler.
* `MBED_TARGET`  
  Set a target mbed-enabled board identifier.
  You can find it by `$ mbed-tools detect` command.
* `VSCODE_CONF_FILE`  
  Path to your c_cpp_properties.json.
  The file must have \"Mbed\" configuration entry,
  which will be inherited by \"MbedAuto\" entry
  automatically generated by this tool.
  You can generate a template of your c_cpp_properties.json
  by `generate` command for quick start.

**Options**

* `--mbed-profile`  
  Select a build profile from \"debug\", \"develop\", and \"release\". See [here](https://os.mbed.com/docs/mbed-os/v6.15/program-setup/build-profiles-and-rules.html) for the specification of each profile. [default: develop]
* `--mbed-program-dir`  
  Path to an mbed program directory. [default: current working directory]

### `configure`

Generate a template of your c_cpp_properties.json for quick start. 

### `update`

Update your c_cpp_properties.json.

## Trouble Shooting
