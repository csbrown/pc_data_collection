import csv

def byte2bits(byte):
    return bin(byte)[2:].rjust(8, "0")

def file_bytes(fname):
    with open(fname, "rb") as f:
        works = f.read()
    return works

def file_byte2ints(fname):
    return list(map(int, file_bytes(fname)))

def file_bytes_colvec(fname):
    asbytes = file_byte2ints(fname)
    col = list(map(lambda x: [x], asbytes))
    col = [["bytes"]] + col
    return col

def file_bits(fname):
    return "".join(map(byte2bits, file_bytes(fname)))

def file_bits_colvec(fname):
    bits = file_bits(fname)
    col = list(map(list, bits))
    col = [["bits"]] + col
    return col

def file_bytes_csv(infile, csv_file):
    asbytes= file_bytes_colvec(infile)
    with open(csv_file, "w") as f:
        writer = csv.writer(f)
        writer.writerows(asbytes)

def file_bits_csv(infile, csv_file):
    bits = file_bits_colvec(infile)
    with open(csv_file, "w") as f:
        writer = csv.writer(f)
        writer.writerows(bits)

def to_csv(datagen_func, csv_file=None):
    data = datagen_func()
    if csv_file is not None:
        with open(csv_file, "w") as f:
            writer = csv.writer(f)
            writer.writerows(data)
    else:
        print(data)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", help="output file", type=str)
    parser.add_argument("infile", help="the file to read in", type=str)
    parser.add_argument("outtype", help="the output style", type=str, choices=["bytes", "bits"])
    args = parser.parse_args()

    if args.outtype == "bytes":
        func = file_bytes_csv
    elif args.outtype == "bits":
        func = file_bits_csv
    func(args.infile, args.output if args.output else None)
