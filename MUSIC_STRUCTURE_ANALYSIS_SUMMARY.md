# Music Structure Analysis - All-in-One Codebase

## Setup Summary

The music structure analysis system is now fully functional in the `madmom` conda environment with the following components:

### ✅ Dependencies Installed
- **PyTorch 2.7.1** with CUDA support
- **NATTEN 0.21.0** (Neighborhood Attention) - updated to work with new API
- **madmom 0.17.dev0** - for audio processing
- **allin1 1.1.0** - the main music structure analysis package
- **Additional libraries**: librosa, matplotlib, scipy, soundfile, etc.

### ✅ Fixed Issues
1. **NATTEN API Compatibility**: Updated `src/allin1/models/dinat.py` to use the new NATTEN API:
   - Changed from `na1d_av`, `na1d_qk`, `na2d_av`, `na2d_qk` to `na1d`, `na2d`
   - Updated function calls to use the unified attention API
   - Fixed import statements

2. **Audio Processing**: Fixed visualization and sonification modules:
   - Updated `src/allin1/visualize.py` to use librosa instead of demucs
   - Updated `src/allin1/sonify.py` to use scipy.io.wavfile for WAV output
   - Fixed audio format and shape issues

3. **Analysis Pipeline**: Fixed `src/allin1/analyze.py` to handle empty demix_paths

## ✅ Test Results

### Music Structure Analysis
- **BPM Detection**: ✅ 100 BPM detected
- **Beat Tracking**: ✅ 324 beats detected
- **Downbeat Detection**: ✅ 81 downbeats detected
- **Segment Analysis**: ✅ 11 segments identified
  - Start: 0.00s - 6.87s
  - Verse: 6.87s - 36.00s
  - Chorus: 36.00s - 64.63s
  - Verse: 64.63s - 88.79s
  - Chorus: 88.79s - 110.39s

### Visualization
- **PDF Generation**: ✅ `mixture_128.pdf` created (66KB)
- **Segment Visualization**: ✅ Shows RMS waveform with segment boundaries
- **Color-coded Segments**: ✅ Different colors for different segment types

### Sonification
- **WAV Generation**: ✅ `mixture_128.sonif.wav` created (41MB)
- **Audio Features**: ✅ Includes metronome clicks and boundary sounds
- **Playable Output**: ✅ Can be played to hear the analysis

### CLI Interface
- **Command Line**: ✅ `python -m allin1.cli mixture_128.mp3 --visualize --sonify`
- **Output Directories**: ✅ Results saved to `./struct`, `./viz`, `./sonif`

## Usage Examples

### Basic Analysis
```bash
python test_analysis.py
```

### With Visualization and Sonification
```bash
python test_visualization.py
```

### Command Line Interface
```bash
python -m allin1.cli mixture_128.mp3 --visualize --sonify
```

### Python API
```python
import allin1
result = allin1.analyze('mixture_128.mp3', out_dir='./struct')
print(f"BPM: {result.bpm}")
print(f"Beats: {len(result.beats)}")
print(f"Segments: {len(result.segments)}")
```

## Output Files

### Analysis Results
- `struct/mixture_128.json` - Complete analysis data in JSON format

### Visualizations
- `viz/mixture_128.pdf` - PDF visualization with waveform and segments

### Sonifications
- `sonif/mixture_128.sonif.wav` - Audio file with analysis sonification

## Environment
- **Conda Environment**: `madmom`
- **Python Version**: 3.10
- **CUDA Support**: ✅ Available
- **GPU**: RTX 3090

The music structure analysis system is now fully operational and ready for use! 