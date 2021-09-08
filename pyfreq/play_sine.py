#!/usr/bin/env python3
"""Play a sine signal."""
import argparse
import numpy as np
import sounddevice as sd

start_idx = 0

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def play(frequency, amplitude):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        'frequency', nargs='?', metavar='FREQUENCY', type=float, default=frequency,
        help='frequency in Hz (default: %(default)s)')
    parser.add_argument(
        '-d', '--device', type=int_or_str,
        help='output device (numeric ID or substring)')
    parser.add_argument(
        '-a', '--amplitude', type=float, default=amplitude,
        help='amplitude (default: %(default)s)')
    args = parser.parse_args(remaining)

    try:
        samplerate = sd.query_devices(args.device, 'output')['default_samplerate']
        def callback(outdata, frames, time, status):
            global start_idx
            t = (start_idx + np.arange(frames)) / samplerate
            t = t.reshape(-1, 1)
            outdata[:] = args.amplitude * np.sin(2 * np.pi * args.frequency * t)
            start_idx += frames

        sound = sd.OutputStream(device=args.device, channels=2, callback=callback,
                            samplerate=samplerate, blocksize=1024)
        return sound
    except Exception as e:
        print(e)
