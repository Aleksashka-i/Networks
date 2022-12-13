import argparse
import subprocess
import platform

def print_verbose(v_mode: bool, data: str, end = '\n'):
    if v_mode:
        print(data, end=end, flush=True)

def try_ping(host, mtu_sz, cnt: int, v_mode: bool):
    print_verbose(v_mode, f'Trying MTU: {mtu_sz}...', ' ')
    os = platform.system().lower()
    if os == 'darwin': #macos
        cmd_arr = ['ping', '-D', '-s', str(mtu_sz), '-c', str(cnt), str(host)]
    else: # other
        cmd_arr = ['ping', '-M', 'do', '-s', str(mtu_sz), '-c', str(cnt), str(host)]
    result = subprocess.run(
        cmd_arr,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0

def find_mtu(host, cnt, v_mode: bool):
    left = 1
    right = 1500 + 1 # MAX_MTU=1500
    while right - left > 1:
        m = (left + right) // 2
        if try_ping(host, m, cnt, v_mode):
            print_verbose(v_mode, 'PASS')
            left = m
        else:
            print_verbose(v_mode, 'FAIL')
            right = m
    return left

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python script to find MTU between hosts.')
    parser.add_argument('host', help='target host name')
    parser.add_argument('-v', '--verbose',
                        action='store_true', help='turn on verbose print')
    parser.add_argument('-c', '--cnt', type=int,
                        default=1, help='number of packages')

    args = parser.parse_args()

    print_verbose(args.verbose, f'OS: {platform.system().lower()}.')

    print_verbose(args.verbose, f'Checking {args.host}...')
    if not try_ping(args.host, 0, args.cnt, args.verbose):
        print('Provided host is non-existent or unavailable.')
        exit(1)
    
    print_verbose(args.verbose, '\nChecking is all done!')

    mtu = find_mtu(args.host, args.cnt, args.verbose)
    print(f'MTU for {args.host} including header: {mtu + 28}')
