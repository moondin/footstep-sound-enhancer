"""
Footstep Sound Enhancer for Games - Main Entry Point
Selectively enhances footstep sounds in games to improve audio cues.
"""

import sys
from footstep_enhancer import FootstepEnhancerApp

def main():
    """Main entry point for the application."""
    app = FootstepEnhancerApp()
    app.run()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Application error: {e}")
        sys.exit(1)
