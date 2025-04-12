"""
GUI Module for Footstep Sound Enhancer
Provides the user interface for controlling the footstep sound enhancement.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

# Import to check if we're in fallback mode
from audio_processor import PYAUDIO_AVAILABLE

class FootstepEnhancerGUI:
    """GUI class for the Footstep Sound Enhancer application."""
    
    def __init__(self, master, audio_processor):
        """
        Initialize the GUI.
        
        Args:
            master: Tkinter root window
            audio_processor: AudioProcessor instance
        """
        self.master = master
        self.audio_processor = audio_processor
        
        # Register callbacks for audio processor events
        self.audio_processor.on_level_change = self.update_level_meter
        self.audio_processor.on_status_change = self.update_status
        self.audio_processor.on_footstep_detected = self.update_footstep_indicator
        
        # Apply a modern style
        self._configure_style()
        
        # Create the GUI elements
        self._create_widgets()
        
        # Show warning if PyAudio is not available
        if not PYAUDIO_AVAILABLE:
            messagebox.showwarning(
                "Limited Functionality Mode",
                "PyAudio module could not be loaded. Application will run in limited functionality mode "
                "without actual audio processing capabilities.\n\n"
                "To fix this issue, please make sure PyAudio is properly installed. "
                "You can use pip to install it: 'pip install pyaudio'\n\n"
                "If running the executable, please use one of the updated build scripts "
                "with proper PyAudio dependencies included."
            )
        
        # Set up periodic UI updates
        self.update_interval_ms = 50  # UI refresh rate in milliseconds
        self._schedule_updates()
    
    def _configure_style(self):
        """Configure the application style."""
        self.style = ttk.Style()
        
        # Configure colors and styles
        self.bg_color = "#f0f0f0"
        accent_color = "#4a7eff"
        
        self.master.configure(bg=self.bg_color)
        
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TButton", background=accent_color, foreground="white", font=("Arial", 10, "bold"))
        self.style.configure("TLabel", background=self.bg_color, font=("Arial", 10))
        self.style.configure("Title.TLabel", background=self.bg_color, font=("Arial", 14, "bold"))
        self.style.configure("Status.TLabel", background=self.bg_color, font=("Arial", 10, "bold"))
        
    def _create_widgets(self):
        """Create all the GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Footstep Sound Enhancer", 
            style="Title.TLabel"
        )
        title_label.pack(pady=(0, 10))
        
        # Status section
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(status_frame, text="Status:").pack(side=tk.LEFT, padx=5)
        self.status_label = ttk.Label(status_frame, text="Stopped", style="Status.TLabel")
        self.status_label.pack(side=tk.LEFT, padx=5)
        
        # Create a frame for the footstep indicator
        footstep_frame = ttk.Frame(main_frame)
        footstep_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(footstep_frame, text="Footstep Detection:").pack(side=tk.LEFT, padx=5)
        self.footstep_indicator = tk.Canvas(
            footstep_frame, 
            width=20, 
            height=20, 
            bg=self.bg_color,
            highlightthickness=0
        )
        self.footstep_indicator.pack(side=tk.LEFT, padx=5)
        self.footstep_indicator.create_oval(2, 2, 18, 18, fill="gray", tags="indicator")
        
        # Level meter
        meter_frame = ttk.Frame(main_frame)
        meter_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(meter_frame, text="Audio Level:").pack(side=tk.LEFT, padx=5)
        self.level_meter = tk.Canvas(
            meter_frame, 
            width=200, 
            height=20, 
            bg="black",
            highlightthickness=1,
            highlightbackground="gray"
        )
        self.level_meter.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Enhancement controls
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(control_frame, text="Enhancement Factor:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.enhancement_scale = tk.Scale(
            control_frame, 
            from_=1.0, 
            to=5.0, 
            resolution=0.1, 
            orient=tk.HORIZONTAL,
            command=self.on_enhancement_change
        )
        self.enhancement_scale.set(2.0)  # Default enhancement
        self.enhancement_scale.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Threshold control
        ttk.Label(control_frame, text="Detection Threshold:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.threshold_scale = tk.Scale(
            control_frame, 
            from_=0.01, 
            to=0.2, 
            resolution=0.01, 
            orient=tk.HORIZONTAL,
            command=self.on_threshold_change
        )
        self.threshold_scale.set(0.05)  # Default threshold
        self.threshold_scale.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Make column 1 expandable
        control_frame.columnconfigure(1, weight=1)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        self.start_button = ttk.Button(
            button_frame, 
            text="Start Enhancement", 
            command=self.start_enhancement
        )
        self.start_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.stop_button = ttk.Button(
            button_frame, 
            text="Stop Enhancement", 
            command=self.stop_enhancement, 
            state=tk.DISABLED
        )
        self.stop_button.pack(side=tk.RIGHT, padx=5, expand=True, fill=tk.X)
        
        # Information text
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=10)
        
        info_text = (
            "This application enhances footstep sounds in games by analyzing audio in real-time.\n"
            "Adjust the Enhancement Factor to control how much footstep sounds are amplified.\n"
            "Adjust the Detection Threshold to fine-tune footstep detection sensitivity."
        )
        ttk.Label(info_frame, text=info_text, wraplength=380, justify=tk.LEFT).pack(fill=tk.X)
    
    def start_enhancement(self):
        """Start the audio enhancement process."""
        if self.audio_processor.start():
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
    
    def stop_enhancement(self):
        """Stop the audio enhancement process."""
        if self.audio_processor.stop():
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            
            # Reset the level meter and footstep indicator
            self.update_level_meter(0.0)
            self.update_footstep_indicator(False)
    
    def on_enhancement_change(self, value):
        """Handle changes to the enhancement factor slider."""
        self.audio_processor.set_enhancement_factor(value)
    
    def on_threshold_change(self, value):
        """Handle changes to the threshold slider."""
        self.audio_processor.set_detection_threshold(value)
    
    def update_status(self, status):
        """Update the status label."""
        self.status_label.config(text=status)
    
    def update_level_meter(self, level):
        """Update the audio level meter."""
        try:
            # Clear the meter
            self.level_meter.delete("bar")
            
            # Calculate width based on level (logarithmic)
            if level > 0:
                # Convert to dB scale (logarithmic)
                db_level = 20 * math.log10(level / 0.0002)  # Reference 0.0002 as approximate silence
                # Normalize to 0-1 range
                normalized_level = max(0, min(1, (db_level + 90) / 90))
            else:
                normalized_level = 0
                
            # Calculate width and draw the bar
            width = int(normalized_level * self.level_meter.winfo_width())
            
            # Color gradient from green to red
            if normalized_level < 0.5:
                # Green to yellow
                r = int(255 * normalized_level * 2)
                g = 255
            else:
                # Yellow to red
                r = 255
                g = int(255 * (1 - (normalized_level - 0.5) * 2))
            
            color = f"#{r:02x}{g:02x}00"
            
            self.level_meter.create_rectangle(
                0, 0, width, self.level_meter.winfo_height(), 
                fill=color, 
                outline="", 
                tags="bar"
            )
        except Exception as e:
            print(f"Error updating level meter: {e}")
    
    def update_footstep_indicator(self, detected):
        """Update the footstep detection indicator."""
        color = "#00ff00" if detected else "gray"
        self.footstep_indicator.itemconfig("indicator", fill=color)
    
    def _schedule_updates(self):
        """Schedule periodic UI updates."""
        # Update the UI based on the current state
        self.master.after(self.update_interval_ms, self._schedule_updates)
