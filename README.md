# PixelHue Color Palette Generator 🎨

PixelHue is a simple Streamlit web app that extracts a color palette from any uploaded image using K-Means clustering.  
It helps designers, developers, and anyone interested in color to quickly generate a set of colors from their images.

## Features

- Upload images in various formats (JPG, PNG, JPEG, BMP, GIF, WEBP).
- Extract a customizable number of colors.
- Visualize the palette as color swatches with hex codes.
- Uses K-Means clustering for accurate color extraction.

## Demo

![PixelHue Demo Screenshot](/sample/screenshot.png)

## Getting Started

### Try it here: [PixelHue](https://pixelhue.streamlit.app/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/j-ncel/PixelHue.git
   cd pixel-hue
   ```

2. **Install dependencies:**

   ```bash
   pip install requirements.txt
   ```

   or

   ```bash
   pip install streamlit pillow scikit-learn numpy
   ```

### Running the App

```bash
streamlit run main.py
```

Open the provided local URL in your browser to use PixelHue.

## Usage

1. Click Browse files or drag a picture to select an image file.
2. View the extracted palette and copy the hex codes as needed.
3. Adjust the "Number of Colors" if you want to set how many colors you want in your palette.

## Project Structure

```
pixel-hue/
├── main.py
├── palette_extractor.py
├── koala.png
├── requirements.txt
├── README.md
```

- `main.py` — Streamlit app UI and logic.
- `palette_extractor.py` — Color extraction logic.
- `koala.png` — Default image

## Credits

- Koala sample picture (Image by <a href="https://pixabay.com/users/souandresantana-61090/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7322174">André Santana Design André Santana</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=7322174">Pixabay</a>)
- Built with [Streamlit](https://streamlit.io/).
