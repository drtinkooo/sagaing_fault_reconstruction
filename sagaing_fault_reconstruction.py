#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sagaing Fault Plate Reconstruction Animation

This script creates an animated visualization of the Sagaing Fault's
tectonic evolution from 50 Ma (before fault formation) to present day.

The Sagaing Fault is a 1,400 km right-lateral strike-slip fault in Myanmar
that formed ~22-15 Ma and accommodates India-Sunda plate motion.

Author: Tin Ko Oo
Institution: Mahidol University, Thailand
Date: December 2025

References:
- Müller et al. (2019) - Plate reconstruction model
- Zahirovic et al. (2014) - SE Asia tectonic evolution
- Socquet & Pubellier (2005) - Sagaing Fault initiation
"""

# =============================================================================
# IMPORTS
# =============================================================================
import gplately
from gplately import PlateReconstruction, PlotTopologies
import pygplates
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
import warnings
warnings.filterwarnings("ignore")

# =============================================================================
# CONFIGURATION
# =============================================================================
CONFIG = {
    # Time settings
    'time_start': 50,           # Ma - before India-Eurasia collision peak
    'time_end': 0,              # Ma - present day
    'time_step': 1,             # Ma per frame
    'fault_initiation': 22,     # Ma - when Sagaing Fault formed
    
    # Animation settings
    'fps': 10,
    'dpi': 150,
    'output_file': 'sagaing_fault_reconstruction.mp4',
    
    # Map extent [lon_min, lon_max, lat_min, lat_max]
    'extent_myanmar': [92, 102, 10, 28],      # Myanmar focus
    'extent_regional': [70, 120, -5, 35],      # Regional context
    'extent_seasia': [90, 145, -15, 30],       # SE Asia wide view
    
    # Visualization
    'figure_size': (14, 10),
    'fault_color': '#FF0000',
    'fault_width': 3.0,
}

# =============================================================================
# SAGAING FAULT TRACE DATA
# =============================================================================
# Modern Sagaing Fault trace coordinates (lon, lat)
# From Gulf of Martaban to Eastern Himalayan Syntaxis
# Data compiled from: Sloan et al. (2017), USGS, GEM Global Active Faults

SAGAING_FAULT_TRACE = [
    # Southern Section - Gulf of Martaban to Bago
    (96.30, 16.50),  # Offshore termination
    (96.35, 17.00),  # Bago segment
    (96.25, 17.50),
    
    # Central Section - Naypyidaw to Mandalay
    (96.10, 18.00),  # Pyu segment
    (96.00, 18.50),
    (95.95, 19.00),  # Naypyidaw segment
    (95.90, 19.50),
    (96.00, 20.00),  # Meiktila segment
    (96.05, 20.50),
    (96.10, 21.00),
    (96.00, 21.50),  # Sagaing segment (type locality)
    (95.95, 22.00),
    (96.00, 22.50),
    
    # Northern Section - Horsetail zone
    (96.10, 23.00),  # Tawma segment
    (96.20, 23.50),
    (96.35, 24.00),  # Ban Mauk segment
    (96.50, 24.50),
    (96.70, 25.00),
    (97.00, 25.50),  # Northern splay zone
    (97.30, 26.00),
    (97.50, 26.50),  # Approaches Eastern Syntaxis
]

# Fault segments for detailed visualization
SAGAING_SEGMENTS = {
    'Bago': {'coords': [(96.30, 16.50), (96.35, 17.00), (96.25, 17.50)], 'color': '#FF6B6B'},
    'Pyu': {'coords': [(96.25, 17.50), (96.10, 18.00), (96.00, 18.50)], 'color': '#FF8E72'},
    'Naypyidaw': {'coords': [(96.00, 18.50), (95.95, 19.00), (95.90, 19.50)], 'color': '#FFB347'},
    'Meiktila': {'coords': [(95.90, 19.50), (96.00, 20.00), (96.05, 20.50), (96.10, 21.00)], 'color': '#FFD93D'},
    'Sagaing': {'coords': [(96.00, 21.50), (95.95, 22.00), (96.00, 22.50)], 'color': '#FF0000'},
    'Tawma': {'coords': [(96.00, 22.50), (96.10, 23.00), (96.20, 23.50)], 'color': '#C70039'},
    'BanMauk': {'coords': [(96.35, 24.00), (96.50, 24.50), (96.70, 25.00)], 'color': '#900C3F'},
}

# =============================================================================
# GEOLOGICAL FEATURES
# =============================================================================
# Key geological features to overlay
GEOLOGICAL_FEATURES = {
    'Central_Myanmar_Basin': {
        'type': 'polygon',
        'coords': [(94.5, 17), (96, 17), (96, 24), (94.5, 24)],
        'color': '#D4A574',
        'label': 'Central Myanmar Basin'
    },
    'Shan_Plateau': {
        'type': 'polygon', 
        'coords': [(96.5, 19), (100, 19), (100, 24), (96.5, 24)],
        'color': '#8B7355',
        'label': 'Shan Plateau'
    },
    'Mogok_Belt': {
        'type': 'line',
        'coords': [(96.2, 21), (96.5, 22), (96.8, 23), (97.2, 24)],
        'color': '#9932CC',
        'label': 'Mogok Metamorphic Belt'
    },
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def load_plate_model(model_name="Muller2019"):
    """
    Load GPlately plate reconstruction model.
    
    Parameters
    ----------
    model_name : str
        Name of plate model (e.g., "Muller2019", "Muller2022")
    
    Returns
    -------
    tuple
        (model, gplot, rotation_model, coastlines, continents)
    """
    print(f"Loading {model_name} plate model...")
    
    gdownload = gplately.DataServer(model_name)
    rotation_model, topology_features, static_polygons = gdownload.get_plate_reconstruction_files()
    coastlines, continents, COBs = gdownload.get_topology_geometries()
    
    model = PlateReconstruction(rotation_model, topology_features, static_polygons)
    gplot = PlotTopologies(model, coastlines=coastlines, continents=continents, COBs=COBs, time=0)
    
    print("Model loaded successfully!")
    return model, gplot, rotation_model, coastlines, continents


def create_sagaing_fault_feature(coords=SAGAING_FAULT_TRACE, 
                                  plate_id=807,  # Shan/Sibumasu
                                  valid_time_start=22):
    """
    Create a pygplates feature for the Sagaing Fault.
    
    Parameters
    ----------
    coords : list
        List of (lon, lat) tuples defining fault trace
    plate_id : int
        Reconstruction plate ID (807 = Shan/Sibumasu/Sunda)
    valid_time_start : float
        Time when fault formed (Ma)
    
    Returns
    -------
    pygplates.Feature
        Fault feature for reconstruction
    """
    # Convert to pygplates format (lat, lon)
    points = [(lat, lon) for lon, lat in coords]
    
    # Create polyline geometry
    fault_polyline = pygplates.PolylineOnSphere(points)
    
    # Create feature
    fault_feature = pygplates.Feature()
    fault_feature.set_geometry(fault_polyline)
    fault_feature.set_reconstruction_plate_id(plate_id)
    fault_feature.set_valid_time(valid_time_start, 0)  # Valid from initiation to present
    fault_feature.set_name("Sagaing Fault")
    
    return fault_feature


def reconstruct_fault(fault_feature, rotation_model, reconstruction_time):
    """
    Reconstruct fault position at a given time.
    
    Returns None if time is before fault formation.
    """
    # Check if fault existed at this time
    valid_time = fault_feature.get_valid_time()
    if valid_time and reconstruction_time > valid_time[0]:
        return None  # Fault didn't exist yet
    
    reconstructed_geometries = []
    pygplates.reconstruct(
        fault_feature,
        rotation_model,
        reconstructed_geometries,
        reconstruction_time
    )
    
    if not reconstructed_geometries:
        return None
    
    # Extract coordinates
    coords = []
    for recon_geom in reconstructed_geometries:
        geom = recon_geom.get_reconstructed_geometry()
        for point in geom.get_points():
            lat, lon = point.to_lat_lon()
            coords.append((lon, lat))
    
    return coords


def calculate_cumulative_displacement(reconstruction_time, 
                                       slip_rate=18,  # mm/yr
                                       max_displacement=400,  # km
                                       initiation_time=22):  # Ma
    """
    Calculate cumulative displacement on Sagaing Fault.
    
    Parameters
    ----------
    reconstruction_time : float
        Time in Ma
    slip_rate : float
        Slip rate in mm/yr (default 18 mm/yr from GPS)
    max_displacement : float
        Maximum observed displacement in km
    initiation_time : float
        Fault initiation time in Ma
    
    Returns
    -------
    float
        Cumulative displacement in km
    """
    if reconstruction_time > initiation_time:
        return 0.0
    
    # Time since fault initiation (in years)
    duration_years = (initiation_time - reconstruction_time) * 1e6
    
    # Displacement (convert mm/yr to km)
    displacement_km = duration_years * slip_rate * 1e-6
    
    # Cap at maximum observed
    return min(displacement_km, max_displacement)


def plot_fault_on_map(ax, fault_coords, reconstruction_time, 
                      fault_initiation=22, **kwargs):
    """
    Plot Sagaing Fault on map axis.
    
    Shows fault as:
    - Solid line after initiation
    - Dashed line (precursor) before initiation
    - No line long before initiation
    """
    if fault_coords is None:
        return
    
    lons = [c[0] for c in fault_coords]
    lats = [c[1] for c in fault_coords]
    
    # Style based on time
    if reconstruction_time <= fault_initiation:
        # Fault exists - solid line
        style = '-'
        alpha = 1.0
        label = 'Sagaing Fault'
    elif reconstruction_time <= fault_initiation + 10:
        # Pre-fault / incipient - dashed line
        style = '--'
        alpha = 0.5
        label = 'Proto-Sagaing Zone'
    else:
        # Long before fault
        return
    
    ax.plot(lons, lats, 
            linestyle=style,
            color=kwargs.get('color', CONFIG['fault_color']),
            linewidth=kwargs.get('linewidth', CONFIG['fault_width']),
            alpha=alpha,
            transform=ccrs.PlateCarree(),
            label=label,
            zorder=10)


def add_tectonic_annotations(ax, reconstruction_time):
    """Add tectonic context annotations."""
    
    # India plate motion arrow (approximate)
    if reconstruction_time > 0:
        # Arrow showing India motion direction
        ax.annotate('', 
                    xy=(85, 25), xytext=(85, 20),
                    arrowprops=dict(arrowstyle='->', color='blue', lw=2),
                    transform=ccrs.PlateCarree())
        ax.text(83, 22.5, 'India\nmotion', fontsize=8, 
                transform=ccrs.PlateCarree(), ha='center')
    
    # Displacement annotation
    displacement = calculate_cumulative_displacement(reconstruction_time)
    if displacement > 0:
        ax.text(0.98, 0.02, f'Cumulative slip: ~{displacement:.0f} km',
                transform=ax.transAxes, fontsize=10,
                ha='right', va='bottom',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))


# =============================================================================
# MAIN ANIMATION FUNCTION
# =============================================================================

def create_animation(config=CONFIG):
    """
    Create the Sagaing Fault reconstruction animation.
    """
    print("=" * 60)
    print("SAGAING FAULT PLATE RECONSTRUCTION ANIMATION")
    print("=" * 60)
    
    # Load plate model
    model, gplot, rotation_model, coastlines, continents = load_plate_model()
    
    # Create fault feature
    fault_feature = create_sagaing_fault_feature()
    print(f"Sagaing Fault feature created (initiation: {config['fault_initiation']} Ma)")
    
    # Set up figure
    fig = plt.figure(figsize=config['figure_size'])
    ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
    
    # Calculate frames
    n_frames = int((config['time_start'] - config['time_end']) / config['time_step']) + 1
    print(f"Animation: {n_frames} frames from {config['time_start']} Ma to {config['time_end']} Ma")
    
    def update(frame):
        reconstruction_time = config['time_start'] - frame * config['time_step']
        if reconstruction_time < config['time_end']:
            reconstruction_time = config['time_end']
        
        # Clear axes
        ax.clear()
        ax.set_extent(config['extent_myanmar'], crs=ccrs.PlateCarree())
        
        # Add gridlines
        gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5)
        gl.top_labels = False
        gl.right_labels = False
        
        # Update PlotTopologies time
        gplot.time = reconstruction_time
        
        # Plot base layers
        try:
            gplot.plot_continents(ax, facecolor='#E8DCC4', edgecolor='none', alpha=0.7)
        except:
            pass
        
        try:
            gplot.plot_coastlines(ax, color='#4A4A4A', linewidth=0.8)
        except:
            pass
        
        # Plot plate boundaries
        try:
            gplot.plot_ridges(ax, color='blue', linewidth=1.5)
            gplot.plot_trenches(ax, color='purple', linewidth=1.5)
            gplot.plot_subduction_teeth(ax, color='purple', linewidth=1.0)
        except:
            pass
        
        # Reconstruct and plot Sagaing Fault
        fault_coords = reconstruct_fault(fault_feature, rotation_model, reconstruction_time)
        plot_fault_on_map(ax, fault_coords, reconstruction_time)
        
        # Add annotations
        add_tectonic_annotations(ax, reconstruction_time)
        
        # Title and time label
        ax.set_title('Sagaing Fault Tectonic Evolution', fontsize=14, fontweight='bold')
        
        # Time indicator
        time_str = f'{reconstruction_time:.0f} Ma'
        if reconstruction_time <= config['fault_initiation']:
            time_str += ' (Fault active)'
        ax.text(0.02, 0.98, time_str,
                transform=ax.transAxes, fontsize=14, va='top', ha='left',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))
        
        # Legend
        legend_elements = [
            Line2D([0], [0], color='#4A4A4A', linewidth=1, label='Coastlines'),
            Line2D([0], [0], color=CONFIG['fault_color'], linewidth=3, label='Sagaing Fault'),
            Line2D([0], [0], color='blue', linewidth=1.5, label='Spreading Ridge'),
            Line2D([0], [0], color='purple', linewidth=1.5, label='Subduction Zone'),
        ]
        ax.legend(handles=legend_elements, loc='lower left', fontsize=8)
        
        # Progress
        if frame % 10 == 0:
            print(f"  Frame {frame}/{n_frames}: {reconstruction_time:.0f} Ma")
        
        return []
    
    # Create animation
    print("\nCreating animation...")
    anim = FuncAnimation(fig, update, frames=n_frames, 
                         interval=1000/config['fps'], blit=False)
    
    # Save
    print(f"\nSaving to {config['output_file']}...")
    anim.save(config['output_file'], fps=config['fps'], 
              dpi=config['dpi'], writer='ffmpeg')
    
    print(f"\n✓ Animation saved as {config['output_file']}")
    plt.close()
    
    return anim


def create_time_slices(times=[50, 40, 30, 22, 15, 10, 5, 0], config=CONFIG):
    """
    Create static figures for specific time slices.
    
    Useful for publications and presentations.
    """
    print("Creating time slice figures...")
    
    # Load model
    model, gplot, rotation_model, coastlines, continents = load_plate_model()
    fault_feature = create_sagaing_fault_feature()
    
    fig, axes = plt.subplots(2, 4, figsize=(20, 10),
                             subplot_kw={'projection': ccrs.PlateCarree()})
    axes = axes.flatten()
    
    for i, time in enumerate(times):
        ax = axes[i]
        ax.set_extent(config['extent_myanmar'], crs=ccrs.PlateCarree())
        
        # Update time
        gplot.time = time
        
        # Plot layers
        try:
            gplot.plot_continents(ax, facecolor='#E8DCC4', edgecolor='none', alpha=0.7)
            gplot.plot_coastlines(ax, color='#4A4A4A', linewidth=0.8)
        except:
            pass
        
        # Plot fault
        fault_coords = reconstruct_fault(fault_feature, rotation_model, time)
        plot_fault_on_map(ax, fault_coords, time)
        
        # Add gridlines
        gl = ax.gridlines(draw_labels=True, linewidth=0.3, alpha=0.5)
        gl.top_labels = False
        gl.right_labels = False
        
        # Title
        ax.set_title(f'{time} Ma', fontsize=12, fontweight='bold')
        
        # Displacement annotation
        disp = calculate_cumulative_displacement(time)
        if disp > 0:
            ax.text(0.95, 0.05, f'{disp:.0f} km', transform=ax.transAxes,
                    fontsize=9, ha='right', va='bottom',
                    bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
    
    plt.suptitle('Sagaing Fault Evolution Through Time', fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    output_file = 'sagaing_fault_time_slices.png'
    plt.savefig(output_file, dpi=200, bbox_inches='tight')
    print(f"✓ Time slices saved as {output_file}")
    
    return fig


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("SAGAING FAULT RECONSTRUCTION PROJECT")
    print("Author: Tin Ko Oo, Mahidol University")
    print("=" * 60 + "\n")
    
    # Create main animation
    create_animation()
    
    # Create static time slices
    # create_time_slices()
    
    print("\n" + "=" * 60)
    print("COMPLETE!")
    print("=" * 60)
