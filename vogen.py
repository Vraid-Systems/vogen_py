def main():
    import argparse
    parser = argparse.ArgumentParser(description='generate ActionScript VOs from static code analysis')
    parser.add_argument('input_dir', metavar='input_dir', type=str, nargs=1,
                        help='directory tree containing Python source with inline static annotations')
    parser.add_argument('--output_dir', dest='output_dir', default='',
                        help='existing/new directory for VO file output relative to execution')
    args = parser.parse_args()

if __name__ == "__main__":
    main()
