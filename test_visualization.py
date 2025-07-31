#!/usr/bin/env python3

import allin1
import json
from pathlib import Path

def test_visualization_and_sonification():
    print("Testing visualization and sonification features...")
    
    # Analyze the audio file with visualization and sonification
    result = allin1.analyze(
        'mixture_128.mp3', 
        out_dir='./struct',
        visualize='./viz',
        sonify='./sonif',
        keep_byproducts=True
    )
    
    print("Analysis with visualization and sonification completed!")
    
    # Check if visualization files were created
    viz_dir = Path('./viz')
    if viz_dir.exists():
        viz_files = list(viz_dir.glob('*'))
        print(f"Visualization files created: {[f.name for f in viz_files]}")
    
    # Check if sonification files were created
    sonif_dir = Path('./sonif')
    if sonif_dir.exists():
        sonif_files = list(sonif_dir.glob('*'))
        print(f"Sonification files created: {[f.name for f in sonif_files]}")
    
    # Test manual visualization
    print("\nTesting manual visualization...")
    allin1.visualize(result, out_dir='./manual_viz')
    
    # Test manual sonification
    print("Testing manual sonification...")
    allin1.sonify(result, out_dir='./manual_sonif')
    
    print("All tests completed successfully!")

if __name__ == "__main__":
    test_visualization_and_sonification() 