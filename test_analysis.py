#!/usr/bin/env python3

import allin1
import json
from pathlib import Path

def test_music_structure_analysis():
    print("Testing music structure analysis...")
    
    # Analyze the audio file
    result = allin1.analyze('mixture_128.mp3', out_dir='./struct')
    
    print("Analysis completed successfully!")
    print(f"BPM: {result.bpm}")
    print(f"Number of beats: {len(result.beats)}")
    print(f"Number of downbeats: {len(result.downbeats)}")
    print(f"Number of segments: {len(result.segments)}")
    
    # Print first few beats
    if result.beats:
        print(f"First 5 beats: {result.beats[:5]}")
    
    # Print segment information
    if result.segments:
        print("\nSegment information:")
        for i, segment in enumerate(result.segments[:5]):  # Show first 5 segments
            print(f"  Segment {i+1}: {segment.start:.2f}s - {segment.end:.2f}s ({segment.label})")
    
    # Check if results were saved
    struct_dir = Path('./struct')
    if struct_dir.exists():
        json_files = list(struct_dir.glob('*.json'))
        print(f"\nSaved results in: {[f.name for f in json_files]}")
        
        # Load and display the saved JSON
        if json_files:
            with open(json_files[0], 'r') as f:
                saved_data = json.load(f)
            print(f"Saved BPM: {saved_data.get('bpm', 'N/A')}")
            print(f"Saved beats count: {len(saved_data.get('beats', []))}")
    
    return result

if __name__ == "__main__":
    test_music_structure_analysis() 