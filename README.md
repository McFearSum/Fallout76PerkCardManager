# Fallout76 Perk Card Manager

**Version:** v0.3.1  
**Status:** CLI MVP Complete

---

## Project Description

Manage your Fallout76 perk cards, builds, and decks — the Vault-Tec way!  
Easily create builds, save/load decks, colorized SPECIAL attribute handling, and future-proof expansion for legendary perks.

---

## Features

- Create and save Normal Perk Card Decks
- Create and save Builds with cards grouped under SPECIAL attributes
- Colorized SPECIAL points and associated Perk Cards
- Load existing decks and builds from `.json` files
- Easy to use Command Line Interface (CLI)
- Organized project structure (`cards/`, `builds/`, `decks/`, `utils/`, `manager/`)
- Clean JSON serialization for full portability
- Professional Git versioning and tags (`v0.2.0`, `v0.2.1`, `v0.3.1`)

---

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/McFearSum/Fallout76PerkCardManager.git
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Launch the application:
    ```bash
    python main.py
    ```

---

## Future Roadmap

- Add Legendary Perk Card deck and build support
- Implement card merging (3x 1-star → 1x 3-star)
- Scrap orphan cards into Legendary Perk Points
- Auto-fetch perk card data from online sources
- Add Colorama dynamic styling for Legendary Perk Cards
- Create a Web Version (Flask or FastAPI)
- Deploy to a public server
- Save/Load multiple player profiles
- Achievements system (Track deck/build milestones)

---

## License

MIT License (optional - add later)
