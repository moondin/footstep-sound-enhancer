# GitHub Release Guide for Footstep Sound Enhancer

This guide will walk you through the process of making the Footstep Sound Enhancer executable available for download from your GitHub repository.

## Prerequisites

1. A GitHub account
2. Git installed on your computer
3. The Footstep Sound Enhancer code repository on your computer

## Step 1: Create a GitHub Repository

1. Log in to GitHub and click on the "+" icon in the top right corner, then select "New repository"
2. Name your repository (e.g., "footstep-sound-enhancer")
3. Choose whether to make it public or private
4. Click "Create repository"

## Step 2: Push the Code to GitHub

1. Open a terminal or command prompt in your project folder
2. Initialize a Git repository (if not already done):
   ```
   git init
   ```
3. Add all files to the repository:
   ```
   git add .
   ```
4. Commit the files:
   ```
   git commit -m "Initial commit"
   ```
5. Add the GitHub repository as a remote:
   ```
   git remote add origin https://github.com/moondin/footstep-sound-enhancer.git
   ```
   (Replace moondin with your actual GitHub username)
6. Push the code to GitHub:
   ```
   git push -u origin main
   ```

## Step 3: Create a Release with Executable

### Method 1: Automatic Build and Release (Recommended)

The repository includes GitHub Actions workflows that will automatically build the executable and create a release when you create a new tag.

1. Create a tag for your release:
   ```
   git tag -a v1.0.0 -m "First release"
   ```
2. Push the tag to GitHub:
   ```
   git push origin v1.0.0
   ```
3. GitHub Actions will automatically:
   - Build the Windows executable
   - Create a new release
   - Upload the executable as an asset to the release

4. Once the workflow completes (usually within a few minutes), go to your repository on GitHub and click on "Releases" in the right sidebar. You should see your new release with the downloadable .exe file.

### Method 2: Manual Upload

If you prefer to build the executable locally and upload it manually:

1. Build the executable using one of the build scripts:
   - On Windows: `build_exe.bat` or `build_with_spec.bat`
   - On macOS/Linux: `./build_exe.sh` or `./build_with_spec.sh`

2. On GitHub, go to your repository and click on "Releases" in the right sidebar
3. Click "Create a new release"
4. Enter the tag version (e.g., "v1.0.0")
5. Add a title and description for the release
6. Upload the executable file (from the `dist` folder) by dragging it to the "Attach binaries..." section
7. Click "Publish release"

## Step 4: Share the Download Link

After creating the release, you can get a direct link to the executable:

1. Go to the release page on GitHub
2. Right-click on the executable file and select "Copy link address"
3. Share this link with users who want to download your application

The link will look something like:
`https://github.com/moondin/footstep-sound-enhancer/releases/download/v1.0.0/FootstepSoundEnhancer.exe`

## Updating the Application

When you make changes to the code and want to release a new version:

1. Update the version number in your code (if applicable)
2. Commit your changes:
   ```
   git add .
   git commit -m "Update application"
   ```
3. Push to GitHub:
   ```
   git push origin main
   ```
4. Create a new tag with an incremented version number:
   ```
   git tag -a v1.0.1 -m "Fixed bugs and improved performance"
   ```
5. Push the tag:
   ```
   git push origin v1.0.1
   ```
6. GitHub Actions will automatically build and release the new version

## Troubleshooting

### GitHub Actions Workflow Failed

If the automatic build process fails:

1. Go to your repository on GitHub
2. Click on "Actions" to see the workflow runs
3. Click on the failed workflow to see the error logs
4. Fix the issues in your code
5. Push the changes and create a new tag

### PyAudio Installation Issues in GitHub Actions

PyAudio requires PortAudio to be installed. If the GitHub Actions workflow fails with PyAudio installation errors:

1. Edit the `.github/workflows/build-release.yml` file:
   - For Windows runners, add a step to install the Windows build tools:
     ```yaml
     - name: Install Windows build tools
       run: |
         choco install visualstudio2019buildtools
         choco install visualstudio2019-workload-vctools
     ```
   - Or consider using a pre-built PyAudio wheel:
     ```yaml
     - name: Install PyAudio from wheel
       run: |
         pip install https://download.lfd.uci.edu/pythonlibs/w4tscw6k/PyAudio-0.2.11-cp39-cp39-win_amd64.whl
     ```

2. Commit and push these changes, then create a new tag to trigger the workflow again