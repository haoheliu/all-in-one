#!/usr/bin/env python3

import sys
import os

def verify_local_natten():
    print("🔍 Verifying Local NATTEN Integration...")
    
    # Check if we can import the local NATTEN functions
    try:
        from allin1.natten.functional import na1d, na2d
        print("✅ Successfully imported local NATTEN functions")
        print(f"   - na1d module: {na1d.__module__}")
        print(f"   - na2d module: {na2d.__module__}")
    except ImportError as e:
        print(f"❌ Failed to import local NATTEN: {e}")
        return False
    
    # Check if the functions are from the local module
    if "allin1.natten" in na1d.__module__ and "allin1.natten" in na2d.__module__:
        print("✅ Confirmed using local NATTEN implementation")
    else:
        print("❌ Not using local NATTEN implementation")
        return False
    
    # Test basic music structure analysis
    try:
        import allin1
        print("✅ Successfully imported allin1 package")
    except ImportError as e:
        print(f"❌ Failed to import allin1: {e}")
        return False
    
    # Test that the analysis works
    try:
        result = allin1.analyze('mixture_128.mp3', out_dir='./struct')
        print("✅ Music structure analysis works with local NATTEN")
        print(f"   - BPM: {result.bpm}")
        print(f"   - Beats: {len(result.beats)}")
        print(f"   - Segments: {len(result.segments)}")
    except Exception as e:
        print(f"❌ Music structure analysis failed: {e}")
        return False
    
    print("\n🎉 All verifications passed! Local NATTEN integration is working correctly.")
    return True

if __name__ == "__main__":
    success = verify_local_natten()
    sys.exit(0 if success else 1) 