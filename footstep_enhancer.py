"""
Footstep Sound Enhancer - Main Application Module
Manages the overall application flow, connecting the GUI and audio processing.
"""

import tkinter as tk
import sys
from gui import FootstepEnhancerGUI
from audio_processor import AudioProcessor

class FootstepEnhancerApp:
    """Main application class that connects the GUI with the audio processor."""
    
    def __init__(self):
        """Initialize the application."""
        self.root = tk.Tk()
        self.root.title("Footstep Sound Enhancer")
        self.root.minsize(400, 300)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Initialize the audio processor
        self.audio_processor = AudioProcessor()
        
        # Initialize the GUI with a reference to the audio processor
        self.gui = FootstepEnhancerGUI(self.root, self.audio_processor)
        
    def run(self):
        """Start the application main loop."""
        try:
            self.root.mainloop()
        except Exception as e:
            print(f"Error in application main loop: {e}")
            self.on_close()
    
    def on_close(self):
        """Handle application closing."""
        try:
            # Stop the audio processor if it's running
            if self.audio_processor.is_running:
                self.audio_processor.stop()
            
            # Destroy the Tkinter root
            self.root.destroy()
            
            # Exit the application
            sys.exit(0)
        except Exception as e:
            print(f"Error during shutdown: {e}")
            sys.exit(1)
