#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports():
    import lnkfile

def TestOneInput(data):
        fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
        with fdp.ConsumeMemoryStringFile(all_data=True) as f:
            lnkfile.lnk_file(f)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()