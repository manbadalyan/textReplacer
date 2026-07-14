# textReplacer

Replaces substrings in a text file based on key=value pairs from a configuration file, then outputs lines sorted by the total number of characters replaced (most changed lines first).

## Requirements

* Python 3.8+

## Usage

```bash
python3 replace.py <config_file> <text_file>
```

Example:

```bash
python3 replace.py config.txt text.txt
```

## Configuration file format

The configuration file contains one replacement pair per line in the following format:

```text
old_value=new_value
```

Example:

```text
a=z
bb=y
c=x
```

Notes:

* Each key in the configuration file is unique.
* Each value in the configuration file is unique.
* Replacements are applied in the order they appear in the configuration file.

## Example

### config.txt

```text
a=z
bb=y
c=x
```

### text.txt

```text
jgrebbk6hnae
cnhjrfyjvth3nxr
b#sjcf_ansbbbbbvo!
dajf#aemfaocfna%
```

### Output

```text
b#sjxf_znsyybvo!
dzjf#zemfzoxfnz%
jgreyk6hnze
xnhjrfyjvth3nxr
```

## Behavior

* Replacements are performed using non-overlapping matches.
* Lines are sorted by the total number of replaced characters in descending order.
* Lines with the same number of replacements preserve their original order.
* The resulting text is printed to standard output (`stdout`).
