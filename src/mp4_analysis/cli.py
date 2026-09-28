"""
cli.py - 命令行入口
支持: mp4-analysis input.mp4 -o output/
"""

import argparse
import sys
import os
from mp4_analysis.pipeline import DocumentExtractionPipeline

def main():
    parser = argparse.ArgumentParser(description="MP4 Video-to-Document Analysis Engine")
    parser.add_argument("video", help="Path to input MP4 screen recording")
    parser.add_argument("-o", "--output", default="output", help="Output directory (default: output/)")
    parser.add_argument("--id", default=None, help="Document ID (default: video filename)")

    args = parser.parse_args()

    if not os.path.exists(args.video):
        print(f"Error: Video file not found: {args.video}", file=sys.stderr)
        sys.exit(1)

    pipeline = DocumentExtractionPipeline(output_dir=args.output)
    pipeline.process(args.video, doc_id=args.id)

if __name__ == "__main__":
    main()
