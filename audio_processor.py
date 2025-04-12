"""
Audio Processor Module for Footstep Sound Enhancer
Handles real-time audio capture, analysis, and enhancement.
"""

import pyaudio
import numpy as np
import threading
import time
from scipy import signal

class AudioProcessor:
    """Handles the audio capture, processing, and playback for footstep enhancement."""
    
    def __init__(self):
        """Initialize the audio processor."""
        self.is_running = False
        self.audio_stream = None
        self.sample_rate = 44100  # Standard audio sample rate
        self.chunk_size = 1024    # Process audio in chunks
        self.channels = 2         # Stereo audio (most common)
        self.audio_format = pyaudio.paInt16  # 16-bit integer audio
        
        # Audio enhancement parameters
        self.enhancement_factor = 2.0
        self.footstep_freq_low = 200   # Lower frequency bound for footsteps (Hz)
        self.footstep_freq_high = 800  # Upper frequency bound for footsteps (Hz)
        self.detection_threshold = 0.05  # Threshold for footstep detection
        self.processing_thread = None
        
        # Initialize PyAudio
        self.p = pyaudio.PyAudio()
        
        # Create butterworth bandpass filter for footstep frequency range
        self.b, self.a = self._create_bandpass_filter()
        
        # Stats for UI updates
        self.current_level = 0.0
        self.footstep_detected = False
        self.current_enhancement = 1.0
        
        # Callbacks to be registered
        self.on_level_change = None
        self.on_status_change = None
        self.on_footstep_detected = None
        
    def _create_bandpass_filter(self):
        """Create a bandpass filter for the footstep frequency range."""
        nyquist = 0.5 * self.sample_rate
        low = self.footstep_freq_low / nyquist
        high = self.footstep_freq_high / nyquist
        b, a = signal.butter(4, [low, high], btype='band')
        return b, a
    
    def set_enhancement_factor(self, value):
        """Update the enhancement factor."""
        self.enhancement_factor = float(value)
    
    def set_detection_threshold(self, value):
        """Update the detection threshold."""
        self.detection_threshold = float(value)
    
    def start(self):
        """Start audio processing in a separate thread."""
        if not self.is_running:
            self.is_running = True
            if self.on_status_change:
                self.on_status_change("Running")
            
            self.processing_thread = threading.Thread(target=self._process_audio)
            self.processing_thread.daemon = True
            self.processing_thread.start()
            return True
        return False
    
    def stop(self):
        """Stop audio processing."""
        if self.is_running:
            self.is_running = False
            if self.on_status_change:
                self.on_status_change("Stopped")
            
            # Wait for processing thread to finish
            if self.processing_thread and self.processing_thread.is_alive():
                self.processing_thread.join(timeout=1.0)
            
            # Close audio stream
            if self.audio_stream:
                try:
                    if self.audio_stream.is_active():
                        self.audio_stream.stop_stream()
                    self.audio_stream.close()
                except Exception as e:
                    print(f"Error closing audio stream: {e}")
            
            # Terminate PyAudio
            try:
                self.p.terminate()
                self.p = pyaudio.PyAudio()  # Reinitialize for next start
            except Exception as e:
                print(f"Error terminating PyAudio: {e}")
                
            return True
        return False
    
    def _detect_footstep(self, audio_data):
        """
        Analyze audio to detect potential footstep sounds.
        
        Uses a combination of bandpass filtering to isolate frequencies typical
        of footsteps, and energy detection to identify transient sounds.
        """
        # Apply bandpass filter to isolate potential footstep frequencies
        filtered_audio = signal.lfilter(self.b, self.a, audio_data)
        
        # Calculate RMS of the filtered audio
        rms = np.sqrt(np.mean(filtered_audio**2))
        self.current_level = rms
        
        # Update UI with current level
        if self.on_level_change:
            self.on_level_change(rms)
        
        # Check if the energy exceeds our threshold
        is_footstep = rms > self.detection_threshold
        
        # Only notify UI if footstep state has changed
        if is_footstep != self.footstep_detected:
            self.footstep_detected = is_footstep
            if self.on_footstep_detected:
                self.on_footstep_detected(is_footstep)
        
        return is_footstep
    
    def _process_audio(self):
        """Process the audio stream in real-time."""
        try:
            # Open audio stream
            self.audio_stream = self.p.open(
                format=self.audio_format,
                channels=self.channels,
                rate=self.sample_rate,
                input=True,
                output=True,
                frames_per_buffer=self.chunk_size
            )
            
            print("Audio stream started.")
            
            # Main processing loop
            while self.is_running:
                try:
                    # Read audio chunk
                    audio_data = self.audio_stream.read(self.chunk_size, exception_on_overflow=False)
                    
                    # Convert to numpy array for processing
                    audio_array = np.frombuffer(audio_data, dtype=np.int16)
                    
                    # Normalize to float (-1.0 to 1.0)
                    audio_float = audio_array.astype(np.float32) / 32767.0
                    
                    # Detect footstep in audio
                    footstep_detected = self._detect_footstep(audio_float)
                    
                    if footstep_detected:
                        # Enhance the footstep sound
                        enhanced_audio = audio_float * self.enhancement_factor
                        
                        # Apply soft clipping to avoid harsh distortion
                        enhanced_audio = np.tanh(enhanced_audio)
                        
                        # Convert back to int16 format
                        output_audio = (enhanced_audio * 32767.0).astype(np.int16).tobytes()
                        
                        # Update current enhancement level for UI
                        self.current_enhancement = self.enhancement_factor
                    else:
                        # Pass through original audio
                        output_audio = audio_data
                        self.current_enhancement = 1.0
                    
                    # Output the processed audio
                    self.audio_stream.write(output_audio)
                    
                except Exception as e:
                    print(f"Error during audio processing: {e}")
                    # Short delay to prevent tight error loop
                    time.sleep(0.1)
        
        except Exception as e:
            print(f"Error opening audio stream: {e}")
            self.is_running = False
            if self.on_status_change:
                self.on_status_change("Error")
        
        print("Audio stream stopped.")
