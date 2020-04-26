import time
import sys
import pandas_test as pt

hora = 60*60

def main():
    while (True):
        print("\n\npython_code activo - 1 minuto\n\n", file=sys.stderr)
        print("\n\nNos quedamos en 1.53.00\n\n", file=sys.stderr)
        time.sleep(60)

if __name__ == "__main__":
    pt.main()
    main()