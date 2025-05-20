def write_output(filename, results):
    with open(filename, "w", encoding="utf-8") as f:
        for section in results:
            if section:
                f.write(section + "\n" + "="*50 + "\n")
