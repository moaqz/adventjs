def decode_filename(filename: str) -> str:
    last_dot_index = filename.rfind(".")
    underscore_index = filename.find("_")
    return f"{filename[underscore_index+1:last_dot_index]}"


print(
    decode_filename("2023122512345678_sleighDesign.png.grinchwa"),  # sleighDesign.png
    decode_filename("42_chimney_dimensions.pdf.hack2023"),  # chimney_dimensions.pdf
    decode_filename("987654321_elf-roster.csv.tempfile"),  # elf-roster.csv
    sep="\n",
)
