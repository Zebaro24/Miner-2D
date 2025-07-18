# Miner-2D 🪨

[![Project Status](https://img.shields.io/badge/Status-Finished-blue)]()
[![Python](https://img.shields.io/badge/Python-3.x-%233776AB?logo=python)](https://python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.5.2-%23FF7F00?logo=pygame)](https://pygame.org)

2D resource mining simulator with procedural world generation and multiplayer support. Explore, mine, and build in dynamically generated worlds with friends!

---

## ✨ Core Features
- **World Generation**:
    - 🌍 Procedurally generated infinite worlds
    - ⛰️ Multiple block types with unique properties
- **Gameplay**:
    - ⛏️ Resource mining and collection
    - 🎒 Inventory management system
    - 🗺️ Real-time terrain modification
- **Multiplayer**:
    - 🌐 Client-server architecture
    - 👥 Real-time player synchronization
    - 🔄 Shared persistent world state

---

## 🧰 Tech Stack
- **Engine**: 
  ![Pygame](https://img.shields.io/badge/Pygame-2.5.2-FF7F00?logo=pygame)
- **Networking**: 
  ![Python Sockets](https://img.shields.io/badge/Sockets-Python_Standard_Library-1C1C1C)
- **Data Handling**: 
  ![Pickle](https://img.shields.io/badge/Pickle-Data_Serialization-1C1C1C)
- **Concurrency**: 
  ![Threading](https://img.shields.io/badge/Threading-Concurrency_Control-1C1C1C)

---

## ⚙️ Installation & Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/Zebaro24/Miner-2D.git
   cd Miner-2D
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install pygame
   ```

---

## 🚀 Launching the Game

### Starting the Server
```bash
python sockets/server.py
```
*Default address: 127.0.0.1:12345*

### Launching Clients
```bash
python runner.py
```

### Game Controls
- **Movement**: WASD keys
- **Inventory**: E key
- **Mining**: Left mouse button
- **Building**: Right mouse button
- **Camera**: Mouse wheel zoom

---

## 🌐 Multiplayer Setup
1. Start server on host machine
2. Players launch game clients
3. Connect using server IP:port format
4. All world changes sync in real-time
5. See other players mining and building

---

## 🗂️ Project Structure
```bash
blocks/
├── all_block.py        # Block type management
├── block.py            # Base block class
scenes/
├── inventory.py        # Inventory UI system
├── menu.py             # Game menus
├── miner_2d.py         # Core gameplay scene
sockets/
├── client.py           # Client networking
├── server.py           # Server backend
images/                 # Game textures
config.py               # Game settings
map_miner.py            # Procedural world generation
player.py               # Player controller
runner.py               # Main game executable
```

---

## 🎮 Gameplay Preview
| Single Player | Multiplayer |
|---------------|-------------|
| <img src="https://github.com/user-attachments/assets/1f17dbb0-1352-44f6-a949-10e20e7790b3" alt="Solo Mining" width="500" /> | <img src="https://github.com/user-attachments/assets/99586130-7fcf-4ee9-81bb-4a84234cfd10" alt="Team Play" width="500" /> |
| <img src="https://github.com/user-attachments/assets/870c44d4-f1d0-4750-a8de-0c4cd0c2260f" alt="Inventory" width="500" /> | <img src="https://github.com/user-attachments/assets/e27b6ca1-aa59-4a57-91b7-c16022abbc99" alt="Team Play" width="500" /> |


---

## 📬 Contacts
| 👨‍💻 Developer   | 📧 Email              | 💻 GitHub                                |
|-------------------|-----------------------|------------------------------------------|
| Denys Shcherbatyi | zebaro.work@gmail.com | [@Zebaro24](https://github.com/Zebaro24) |
| Dmitro Itsko      | cloud.me.fr@gmail.com | [@WhiteDh](https://github.com/WhiteDh)   |
