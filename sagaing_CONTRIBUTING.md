# Contributing to Sagaing Fault Plate Reconstruction

Thank you for your interest in contributing! This project aims to advance understanding of Myanmar's tectonic hazards through open science.

## 🤝 Ways to Contribute

### 1. Report Issues

Found a bug or have a suggestion? Please [open an issue](https://github.com/YOUR_USERNAME/sagaing-fault-reconstruction/issues) with:

- Clear, descriptive title
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Your environment (OS, Python version, package versions)
- Screenshots or error messages if applicable

### 2. Improve Documentation

- Fix typos or clarify explanations
- Add examples or tutorials
- Translate documentation
- Improve code comments

### 3. Enhance Visualizations

- Better color schemes
- Additional map overlays
- Interactive visualizations
- 3D rendering options

### 4. Add Scientific Data

- Higher resolution fault traces
- Historical earthquake locations
- GPS velocity data
- Geological unit boundaries

### 5. Code Improvements

- Performance optimizations
- New features
- Better error handling
- Unit tests

## 🔧 Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/sagaing-fault-reconstruction.git
cd sagaing-fault-reconstruction

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (optional)
pip install pytest black flake8
```

## 📝 Code Style

- Follow [PEP 8](https://pep8.org/) guidelines
- Use meaningful variable names
- Add docstrings for all functions
- Comment complex logic
- Keep functions focused and modular

### Example Function Style

```python
def calculate_displacement(reconstruction_time, slip_rate=18, max_displacement=400):
    """
    Calculate cumulative fault displacement at a given time.
    
    Parameters
    ----------
    reconstruction_time : float
        Time in millions of years ago (Ma)
    slip_rate : float, optional
        Slip rate in mm/yr (default: 18)
    max_displacement : float, optional
        Maximum displacement in km (default: 400)
    
    Returns
    -------
    float
        Cumulative displacement in km
    
    Examples
    --------
    >>> calculate_displacement(10)
    216.0
    >>> calculate_displacement(30)  # Before fault initiation
    0.0
    """
    # Implementation here
    pass
```

## 🔀 Pull Request Process

1. **Fork** the repository
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make changes** and commit with clear messages:
   ```bash
   git commit -m "Add: description of new feature"
   git commit -m "Fix: description of bug fix"
   git commit -m "Docs: update README with new section"
   ```
4. **Test** your changes thoroughly
5. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots if applicable

## 🧪 Testing

Before submitting:

```bash
# Run the main script
python sagaing_fault_reconstruction.py

# Check code style (if installed)
flake8 sagaing_fault_reconstruction.py
black --check sagaing_fault_reconstruction.py
```

## 📊 Data Contributions

If contributing geological data:

- Provide source/reference
- Use standard formats (GeoJSON, Shapefile)
- Include metadata (coordinate system, accuracy, date)
- Ensure data is openly licensed or properly attributed

### Fault Trace Data Format

```json
{
  "type": "Feature",
  "properties": {
    "name": "Sagaing Fault - Segment Name",
    "source": "Reference citation",
    "accuracy_km": 1.0
  },
  "geometry": {
    "type": "LineString",
    "coordinates": [[lon1, lat1], [lon2, lat2], ...]
  }
}
```

## 🌏 Scientific Guidelines

When contributing scientific content:

1. **Cite sources** for all geological interpretations
2. **Use consistent units** (Ma for time, km for distance, mm/yr for rates)
3. **Note uncertainties** where applicable
4. **Follow established models** (Müller et al. 2019) unless proposing alternatives with justification

## 📜 Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Credit others' contributions

## ❓ Questions?

- Open a [Discussion](https://github.com/YOUR_USERNAME/sagaing-fault-reconstruction/discussions)
- Contact the maintainer: tin.koo@mahidol.ac.th

---

Thank you for helping improve our understanding of Myanmar's seismic hazards! 🙏
