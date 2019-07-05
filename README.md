# HackPrinter

This project can hack into old version network printer which uses 9100 port.

## Usage

`python hackprinter.py`

It will lead you to a cmd loop iff we successfully hacked into target.

`print_text "text_message"`

This cmd can make the target print text message.

`print_file file_name`

This cmd can make the target print specific file, the file format can be .txt, .pdf, or most of the format used by image, such as .jpg, .png ...

`buffer_explosion`

This cmd will overwhelm target's buffer, which is really dangerous.

You can also use `./hack.sh` to autalmatically hacked into more than one printer.
