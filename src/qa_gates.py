#!/usr/bin/env python3
"""Measured QA gates for a built Short (Phase 1 seed).

Usage: python3 src/qa_gates.py <video.mp4>
Checks (via ffprobe/ffmpeg): dimensions, duration, integrated loudness + true peak
(loudnorm analysis), and longest silence gap (silencedetect at -45 dB).
Thresholds are read from config/gates.yaml by eye — this script reports measured
values; the audit step compares them against the gates.
"""
import json, re, subprocess, sys

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout + subprocess.run(cmd, capture_output=True, text=True).stderr

def probe(path):
    out = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json",
                          "-show_format", "-show_streams", path],
                         capture_output=True, text=True).stdout
    return json.loads(out)

def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    path = sys.argv[1]
    info = probe(path)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    dur = float(info["format"]["duration"])
    print(f"file: {path}")
    print(f"dimensions: {v['width']}x{v['height']}  (gate: 1080x1920)")
    print(f"duration: {dur:.2f}s  (gate: 35-55s)")
    # loudnorm analysis pass
    r = subprocess.run(["ffmpeg", "-i", path, "-af",
                        "loudnorm=I=-14:TP=-1:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.search(r"\[Parsed_loudnorm[^{]*(\{[^}]*\})", r.stderr, re.S)
    if m:
        ln = json.loads(m.group(1))
        print(f"loudness: {ln['input_i']} LUFS (gate: -14 +/-0.5), true peak {ln['input_tp']} dB (gate: <= -1)")
    else:
        print("loudness: could not parse loudnorm output")
    # silence gaps
    r = subprocess.run(["ffmpeg", "-i", path, "-af", "silencedetect=noise=-45dB:d=0.3",
                        "-f", "null", "-"], capture_output=True, text=True)
    gaps = [float(x) for x in re.findall(r"silence_duration: ([0-9.]+)", r.stderr)]
    longest = max(gaps) if gaps else 0.0
    print(f"silence gaps >=0.3s at -45dB: {len(gaps)}, longest {longest:.2f}s  (gate: < 0.4s)")

if __name__ == "__main__":
    main()
