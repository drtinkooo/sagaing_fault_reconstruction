# Sagaing Fault Plate Reconstruction

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GPlately](https://img.shields.io/badge/GPlately-1.0%2B-green.svg)](https://github.com/GPlates/gplately)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/sagaing-fault-reconstruction/blob/main/sagaing_fault_reconstruction.ipynb)

A Python tool for visualizing the tectonic evolution of Myanmar's **Sagaing Fault** through plate reconstruction, from 50 million years ago to present day.

![Sagaing Fault Animation Preview](docs/images/animation_preview.gif)

## 🌏 Overview

The **Sagaing Fault** is one of the world's most significant active strike-slip faults, running 1,400 km through the heart of Myanmar. This project creates animated visualizations showing:

- **Fault formation** at ~22 Ma (Middle Miocene)
- **Plate boundary evolution** between India and Sunda plates
- **Cumulative displacement** tracking (~400 km total)
- **Regional tectonic context** including subduction zones and spreading ridges

### Tectonic Significance

| Parameter | Value |
|-----------|-------|
| **Length** | ~1,400 km |
| **Type** | Right-lateral (dextral) strike-slip |
| **Formation** | ~22-15 Ma (Miocene) |
| **Current Slip Rate** | 18-24 mm/yr |
| **Total Displacement** | 330-450 km |
| **Seismic Hazard** | High (M7+ earthquakes) |

The Sagaing Fault connects the **Andaman Sea spreading center** in the south to the **Eastern Himalayan Syntaxis** in the north, accommodating the oblique convergence between the Indian and Sunda plates.

## 🗺️ Fault Segments

The fault is divided into several named segments (south to north):

```
┌─────────────────────────────────────────────────────────┐
│  EASTERN HIMALAYAN SYNTAXIS (26.5°N)                    │
│         ↑                                               │
│    Northern Horsetail Zone                              │
│         ↑                                               │
│    Ban Mauk Segment (24-25.5°N)                         │
│         ↑                                               │
│    Tawma Segment (22.5-24°N)                            │
│         ↑                                               │
│    ★ SAGAING SEGMENT (21-22.5°N) - Type locality        │
│         ↑                                               │
│    Meiktila Segment (19.5-21°N)                         │
│         ↑                                               │
│    Naypyidaw Segment (18.5-19.5°N) - Capital region     │
│         ↑                                               │
│    Pyu Segment (17.5-18.5°N)                            │
│         ↑                                               │
│    Bago Segment (16.5-17.5°N)                           │
│         ↑                                               │
│  GULF OF MARTABAN / ANDAMAN SEA (16.5°N)                │
└─────────────────────────────────────────────────────────┘
```

## 🎬 Sample Output

### Animation Timeline

| Time (Ma) | Tectonic Event | Visualization |
|-----------|----------------|---------------|
| 50-35 | India-Eurasia collision intensifies | Regional plate motion |
| 35-22 | Pre-fault deformation in Myanmar | Dashed proto-fault zone |
| **22** | **Sagaing Fault initiates** | **Fault appears (solid red)** |
| 22-10 | Fault matures, Andaman Sea opens | Growing displacement |
| 10-0 | Modern configuration established | Full fault trace |

### Key Visualizations

- **Animated MP4**: Complete 50 Ma → 0 Ma evolution
- **Time Slices**: Static figures at 50, 40, 30, 22, 15, 10, 5, 0 Ma
- **Displacement Graph**: Cumulative slip through time

## 🚀 Quick Start

### Option 1: Google Colab (Recommended)

Click the "Open in Colab" badge above, or:

1. Open [Google Colab](https://colab.research.google.com/)
2. Upload `sagaing_fault_reconstruction.py`
3. Run:

```python
# Install dependencies
!pip install gplately cartopy
!apt-get install ffmpeg -qq

# Run the script
%run sagaing_fault_reconstruction.py
```

### Option 2: Local Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/sagaing-fault-reconstruction.git
cd sagaing-fault-reconstruction

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python sagaing_fault_reconstruction.py
```

## 📋 Requirements

### Python Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| gplately | ≥1.0.0 | Plate reconstruction |
| pygplates | ≥1.0.0 | Low-level GPlates API |
| cartopy | ≥0.20.0 | Map projections |
| matplotlib | ≥3.5.0 | Plotting & animation |
| numpy | ≥1.20.0 | Numerical operations |

### System Requirements

- **Python**: 3.8 or higher
- **FFmpeg**: Required for MP4 output
- **RAM**: 8 GB minimum (16 GB recommended)
- **Storage**: ~2 GB for plate model cache

### Installing FFmpeg

```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows - Download from ffmpeg.org

# Google Colab
!apt-get install ffmpeg -qq
```

## ⚙️ Configuration

Customize the animation by modifying the `CONFIG` dictionary:

```python
CONFIG = {
    # Time range (millions of years ago)
    'time_start': 50,           # Animation start
    'time_end': 0,              # Animation end (present)
    'time_step': 1,             # Time per frame
    'fault_initiation': 22,     # When fault formed
    
    # Animation settings
    'fps': 10,                  # Frames per second
    'dpi': 150,                 # Resolution
    'output_file': 'sagaing_fault_reconstruction.mp4',
    
    # Map extent [lon_min, lon_max, lat_min, lat_max]
    'extent_myanmar': [92, 102, 10, 28],   # Myanmar focus
    'extent_regional': [70, 120, -5, 35],   # India-SE Asia
    'extent_seasia': [90, 145, -15, 30],    # SE Asia wide
    
    # Visualization
    'figure_size': (14, 10),
    'fault_color': '#FF0000',
    'fault_width': 3.0,
}
```

### Map Extent Options

| Extent | Coordinates | Best For |
|--------|-------------|----------|
| Myanmar | [92, 102, 10, 28] | Fault detail (default) |
| Regional | [70, 120, -5, 35] | India-Eurasia context |
| SE Asia | [90, 145, -15, 30] | Broad tectonic setting |

## 📁 Project Structure

```
sagaing-fault-reconstruction/
├── sagaing_fault_reconstruction.py    # Main script
├── sagaing_fault_reconstruction.ipynb # Jupyter notebook
├── README.md                          # This file
├── requirements.txt                   # Dependencies
├── LICENSE                            # MIT License
├── CITATION.cff                       # Citation info
├── .gitignore
├── data/
│   └── sagaing_fault_trace.geojson   # Fault coordinates
├── docs/
│   ├── images/
│   │   └── animation_preview.gif
│   └── references/
└── outputs/                           # Generated files
    ├── sagaing_fault_reconstruction.mp4
    └── sagaing_fault_time_slices.png
```

## 🔬 Scientific Background

### Tectonic Setting

Myanmar sits at a complex triple junction where:

1. **Indian Plate** moves NNE at ~35 mm/yr relative to Eurasia
2. **Burma Microplate** is sandwiched between India and Sunda
3. **Sunda Plate** forms the stable SE Asian block

The Sagaing Fault accommodates ~18-24 mm/yr of the India-Sunda relative motion through right-lateral strike-slip faulting.

### Geological Evolution

```
┌────────────────────────────────────────────────────────────┐
│ 50 Ma │ India-Eurasia collision ongoing                    │
│       │ Myanmar region experiencing compression            │
├───────┼────────────────────────────────────────────────────┤
│ 35 Ma │ Deformation localizing in central Myanmar          │
│       │ Proto-shear zone developing                        │
├───────┼────────────────────────────────────────────────────┤
│ 22 Ma │ ★ SAGAING FAULT INITIATES                          │
│       │ Discrete strike-slip boundary forms                │
├───────┼────────────────────────────────────────────────────┤
│ 15 Ma │ Fault becomes dominant plate boundary              │
│       │ Andaman Sea rifting begins                         │
├───────┼────────────────────────────────────────────────────┤
│ 4 Ma  │ Andaman Sea spreading established                  │
│       │ Modern fault geometry achieved                     │
├───────┼────────────────────────────────────────────────────┤
│ 0 Ma  │ Active fault, high seismic hazard                  │
│       │ ~400 km cumulative displacement                    │
└───────┴────────────────────────────────────────────────────┘
```

### Plate Model

This project uses the **Müller et al. (2019)** global plate reconstruction model via GPlately, which provides:

- Continuous plate boundary evolution
- Deforming plate regions for SE Asia
- High-resolution coastlines through time

## 🎨 Visualization Legend

| Feature | Color | Description |
|---------|-------|-------------|
| Sagaing Fault | 🔴 Red | Main strike-slip fault |
| Proto-fault Zone | 🔴 Red (dashed) | Pre-22 Ma shear zone |
| Coastlines | ⚫ Dark gray | Reconstructed shorelines |
| Continents | 🟤 Tan | Continental areas |
| Spreading Ridges | 🔵 Blue | Divergent boundaries |
| Subduction Zones | 🟣 Purple | Convergent boundaries |

## 📊 Output Products

### 1. Animation (MP4)

- **File**: `sagaing_fault_reconstruction.mp4`
- **Duration**: ~5 seconds at 10 fps
- **Frames**: 51 (50 Ma to 0 Ma at 1 Ma steps)
- **Resolution**: 2100 × 1500 pixels (150 dpi)

### 2. Time Slices (PNG)

- **File**: `sagaing_fault_time_slices.png`
- **Layout**: 2×4 grid
- **Times**: 50, 40, 30, 22, 15, 10, 5, 0 Ma

### 3. Displacement Data

The script calculates cumulative fault displacement using:

```python
displacement = slip_rate × time_since_initiation
# slip_rate = 18 mm/yr
# Maximum = 400 km (observed geological offset)
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution

- [ ] Higher resolution fault trace data
- [ ] Additional geological overlays (basins, metamorphic belts)
- [ ] Seismicity overlay for historical earthquakes
- [ ] GPS velocity vector visualization
- [ ] 3D visualization options

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## 📖 Citation

If you use this code in your research, please cite:

```bibtex
@software{kooo2025sagaing,
  author = {Ko Oo, Tin},
  title = {Sagaing Fault Plate Reconstruction},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/YOUR_USERNAME/sagaing-fault-reconstruction}
}
```

Also cite the underlying plate model:

```bibtex
@article{muller2019global,
  title={A global plate model including lithospheric deformation along 
         major rifts and orogens since the Triassic},
  author={M{\"u}ller, R Dietmar and Zahirovic, Sabin and Williams, Simon E 
          and others},
  journal={Tectonics},
  volume={38},
  pages={1884--1907},
  year={2019}
}
```

## 🙏 Acknowledgments

- **[GPlately](https://github.com/GPlates/gplately)** - Plate reconstruction library
- **[EarthByte Group](https://www.earthbyte.org/)** - Plate models and data
- **[GPlates](https://www.gplates.org/)** - Open-source reconstruction software
- **Myanmar Geosciences Society** - Regional geological expertise

## 📚 References

1. **Müller, R.D., et al. (2019)**. A global plate model including lithospheric deformation along major rifts and orogens since the Triassic. *Tectonics*, 38, 1884-1907.

2. **Zahirovic, S., et al. (2014)**. The Cretaceous and Cenozoic tectonic evolution of Southeast Asia. *Solid Earth*, 5, 227-273.

3. **Socquet, A., & Pubellier, M. (2005)**. Cenozoic deformation in western Yunnan and Indochina. *Tectonophysics*, 391, 145-158.

4. **Curray, J.R. (2005)**. Tectonics and history of the Andaman Sea region. *Journal of Asian Earth Sciences*, 25, 187-232.

5. **Sloan, R.A., et al. (2017)**. Active tectonics of Myanmar and the Andaman Sea. *Geological Society, London, Memoirs*, 48, 19-52.

6. **Wang, Y., et al. (2014)**. GPS-constrained inversion of present-day slip rates along major faults of the Sichuan-Yunnan region, China. *Science China Earth Sciences*.

## 📧 Contact

**Tin Ko Oo**  
Mahidol University, Thailand  
Email: tin.koo@mahidol.ac.th

---

<p align="center">
  <i>Advancing understanding of Myanmar's seismic hazards through open science</i>
  <br><br>
  Made with ❤️ for the geoscience community
</p>
